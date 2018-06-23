#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
aritcle.py
~~~~~~~~~~~~~~~~~
Crawl aritcle content
"""
import requests  
import json
from bs4 import BeautifulSoup
import re
from config import *
from database import *
from gadget import *

def getArticle(page, latestTimestamp, conn):
	'''Get Article Content: Get article id and then get content with it'''

	# convert timestamp to date format
	timeLocal = getDate(latestTimestamp)
	print("=====开始抓取时间[%s]之后的微博文章=====" % timeLocal)
	print('开始抓取文章列表第%s页' % page)

	url = articleListUrlFormat.format(page)
	data = requests.get(url, headers = headers)
	data.encoding = 'utf-8'
	data = json.loads(data.text)

	for content in data['data']['cards'][0]['card_group']:
		# if 'card_type' is 9
		if content['card_type'] == 9:
			kwArticle = {}
			kwArticle['add_time'] = getTimestamp(content['mblog']['created_at'])
			kwArticle['title'] = content['mblog']['page_info']['page_title']

			object_id = content['mblog']['page_info']['object_id']
			kwArticle['article_id'] = object_id.split(":")[1]
			articleTuple = getArticleContent(kwArticle['article_id'],1)
			if articleTuple[0] == '':
				saveFailId(kwArticle['article_id'],kwArticle['title'])
				continue
			kwArticle['content'] = articleTuple[0]
		# sometimes the return 'card_type' not equal to 9,get content in different way
		elif content['card_type'] == 8:
			regex = re.compile('id=.*?&')
			result = regex.findall(content['scheme'])
			kwArticle = {}
			kwArticle['article_id'] = result[0].rstrip("&").split("=")[1]
			kwArticle['title'] = content['title_sub']

			urlFormat = r'http://card.weibo.com/article/aj/articleshow?cid={}'
			urlArticle = urlFormat.format(kwArticle['article_id'])
			articleTuple = getArticleContent(kwArticle['article_id'], 2)
			if articleTuple[0] == '':
				saveFailId(kwArticle['article_id'],kwArticle['title'])
				continue
			
			kwArticle['add_time'] = getTimestamp(articleTuple[1])
			kwArticle['content'] = articleTuple[0]
		print('保存文章：%s' % kwArticle['title'])
		insert_data('wb_mzm_article', conn, **kwArticle)
		print("保存成功！\n")

def getArticleContent(id,card_type):
	'''Get content by id'''

	object_id = '1022:' + id
	url = articleUrlFormat.format(object_id = object_id, id = id)
	response = requests.get(url, headers = articleHeaders)
	response.encoding = 'utf-8';
	soup = BeautifulSoup(response.text,'lxml')

	# if article content contains in script tag, parse content in it
	if len(soup.findAll("script")) > 1 and card_type == 1:
		jsText = soup.findAll("script")[1].text

		# Extract value of content,add brackets in regex to make it only return the brackets part
		regex = re.compile('\"content\":(.*)')
		result = regex.findall(jsText)

		# Get rid of html tag
		resultSoup = BeautifulSoup(result[0], 'lxml')
		return resultSoup.body.get_text().strip(',').strip('"'), ''

	# if article content return from api 
	else:
		urlFormat = r'http://card.weibo.com/article/aj/articleshow?cid={}'
		url = urlFormat.format(id)
		response = requests.get(url, headers = articleHeaders)
		if response:
			response.encoding = 'utf-8'
			content = json.loads(response.text)
			parseContent = json.dumps(content).encode('utf-8').decode('unicode_escape')
			
			if type(content) == str or '原文章已被删除' in parseContent or '正在加载内容' in parseContent:
				return '',''

			articleHTML = content['data']['article']
			articleSoup = BeautifulSoup(articleHTML,'lxml')
			articleContent = articleSoup.find('div', class_='WBA_content').text
			articleTime = articleSoup.find('span', class_='time').text
			return articleContent.strip(',').strip('"'), articleTime
		else:
			return '',''

if __name__ == '__main__':
	conn = db_connector()
	latestTimestamp = selectData(conn,'wb_mzm_article',4)
	
	if latestTimestamp == None:
		latestTimestamp = 0

	saveLastTimestamp(latestTimestamp,'last_article_timestamp.txt')
	print('上次更新到：%s' % getDate(latestTimestamp))
	articlePage = 24

	while True:
		getArticle(articlePage,latestTimestamp,conn)
		articlePage = articlePage + 1
		sleepTimes(3)

