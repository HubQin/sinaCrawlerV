#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
post.py
~~~~~~~~~~~~~~~~~
Crawl post content
"""
import requests  
import json
from bs4 import BeautifulSoup
from config import *
from database import *
from gadget import *

def getContent(page,latestTimestamp,conn):
	'''get post content and save in database'''


	timeLocal = getDate(latestTimestamp)
	print("=====开始抓取时间[%s]之后的微博=====" % timeLocal)
	print("=====开始抓取第%s页之后的微博=====" % page)

	url = listUrlFormat.format(page)

	data = requests.get(url, headers = headers)
	data.encoding = 'utf-8'
	data = json.loads(data.text)
	
	breakCount = 0
	# Process all post items
	for content in data['data']['cards']:
		if('mblog' in content.keys()):
			addTime = getTimestamp(content['mblog']['created_at'])
			print('添加时间%s' % addTime)

			#only save which havn't been crawled
			if addTime > latestTimestamp:
				print('POST ID: %s 开始抓取\n' % content['mblog']['id'])
				kwPost = {}
				kwPost['add_time'] = addTime
				kwPost['post_id'] = content['mblog']['id'] 
				kwPost['attitudes_count'] = content['mblog']['attitudes_count'] 
				kwPost['comments_count'] = content['mblog']['comments_count']

				# if there is no long text, use the current text
				if content['mblog']['isLongText'] == False:
					kwPost['content'] = content['mblog']['text']
				else:
					kwPost['content'] = getLongTextContent(content['mblog']['id'])
				# if fail to get long text, just use the short one 
				if kwPost['content'] == False:
						kwPost['content'] = content['mblog']['text']
				# if has retweeted content, get it in the same way
				if 'retweeted_status' in content['mblog']:
					kwPost['retweet_id'] = content['mblog']['retweeted_status']['id']
					if content['mblog']['retweeted_status']['isLongText'] == False:
						kwPost['retweet_content'] = content['mblog']['retweeted_status']['text']
					else:
						kwPost['retweet_content'] = getLongTextContent(content['mblog']['retweeted_status']['id'])
					if kwPost['retweet_content'] == False:
						kwPost['retweet_content'] = content['mblog']['retweeted_status']['text']

				# Insert post data into database
				insert_data('wb_mzm_post',conn,**kwPost)
				print('POST ID: %s 写入成功\n' % kwPost['post_id'])

				# Start getting comments of post
				for data in getComment(kwPost['post_id'], 0):
					if data:
						kwComment = {}
						kwComment['post_id'] = kwPost['post_id']
						kwComment['comment_id'] = data[0]
						kwComment['like_count'] = data[1]
						kwComment['add_time'] = data[2]
						kwComment['comment_user_id'] = data[3]
						kwComment['comment_user_name'] = data[4]
						kwComment['user_photo'] = data[5]
						kwComment['user_profile'] = data[6]
						kwComment['text'] = data[7]
						kwComment['reply_text'] = data[8]
						insert_data('wb_mzm_comment', conn, **kwComment)
				print('POST ID:%s 的评论写入完毕\n' % kwPost['post_id'])
			else:
				print('时间小于最新时间，不写入')
				breakCount = breakCount + 1
				if breakCount == 5:
					print('已经抓取完毕，程序结束...')
					exit()

	print('=====第%s页抓取完毕=====\n' % page)

def getLongTextContent(id):
	url = postUrlFormat.format(id)
	data = requests.get(url, headers = headers)
	if data and '打开微博客户端' not in data.text:
		data.encoding = 'utf-8'
		data = json.loads(data.text)
		return data['data']['longTextContent']
	else:
		return False

def getComment(id, page):
	'''get all comments of a post page by page recursively and return a generator'''

	url = commentUrlFormat.format(id = id, page = page)
	data = requests.get(url, headers = headers) 
	data.encoding = 'utf-8'
	data = json.loads(data.text)
	while data['ok'] == 1 and 'data' in data.keys() and page < data['data']['max']:
		for content in data['data']['data']:
			addTime = getTimestamp(content['created_at'])
			if 'reply_text' in content.keys() and 'text' in content.keys():
				yield [content['id'], content['like_counts'], addTime, content['user']['id'], content['user']['screen_name'], content['user']['profile_image_url'], content['user']['profile_url'], content['text'], content['reply_text']]
			elif 'reply_text' in content.keys() and 'text' not in content.keys():
				yield [content['id'], content['like_counts'], addTime, content['user']['id'], content['user']['screen_name'], content['user']['profile_image_url'], content['user']['profile_url'], '', content['reply_text']]
			elif 'reply_text' not in content.keys() and 'text' in content.keys():
				yield [content['id'], content['like_counts'], addTime, content['user']['id'], content['user']['screen_name'], content['user']['profile_image_url'], content['user']['profile_url'], content['text'], '']
		print('抓取评论第%s页\n' % page)
		page = page + 1
		getComment(id,page)
	else:
		yield []

if __name__ == '__main__':
	conn = db_connector()
	latestTimestamp = selectData(conn,'wb_mzm_post1',3)
	if latestTimestamp == None:
		latestTimestamp = 0
	print(latestTimestamp)
	ppage = 1

	# the program would extis while all latest posts are crawled
	while ppage < 100:
		getContent(ppage,latestTimestamp,conn)
		ppage = ppage + 1
		sleepTimes(1)
