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

def getArticle(page, conn):
	'''Get Article Content: Get article id and then get content with it'''

	print('开始抓取文章列表第%s页\n' % page)
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
			kwArticle['content'] = getArticleContent(kwArticle['article_id'])
			if kwArticle['content'] == '':
				saveFailId(kwArticle['article_id'])
				continue
		# sometimes the return 'card_type' not equal to 9,get content in different way
		else:
			regex = re.compile('id=.*?&')
			result = regex.findall(content['scheme'])
			kwArticle = {}
			kwArticle['article_id'] = result[0].rstrip("&").split("=")[1]

			urlFormat = r'http://card.weibo.com/article/aj/articleshow?cid={}'
			urlArticle = urlFormat.format(kwArticle['article_id'])

			response = requests.get(urlArticle, headers = articleHeaders)
			subContent = json.loads(response.text)
			if type(subContent) == str or '原文章已被删除' in json.dumps(subContent).encode('utf-8').decode('unicode_escape') or '正在加载内容' in json.dumps(subContent).encode('utf-8').decode('unicode_escape'):
				saveFailId(kwArticle['article_id'])
				continue
			kwArticle['add_time'] = 0
			kwArticle['title'] = subContent['data']['title'] 
			kwArticle['content'] = subContent['data']['article']
		print('保存文章：%s\n' % kwArticle['title'])
		insert_data('wb_mzm_article', conn, **kwArticle)
		print("保存成功！")

def getArticleContent(id):
	'''Get content by id'''

	object_id = '1022:' + id
	url = articleUrlFormat.format(object_id = object_id, id = id)
	response = requests.get(url, headers = articleHeaders)
	response.encoding = 'utf-8';
	soup = BeautifulSoup(response.text,'lxml')
	# if article content contains in script tag, parse content in it
	if len(soup.findAll("script")) > 1:
		jsText = soup.findAll("script")[1].text
		regex = re.compile('\"content\":(.*)')
		result = regex.findall(jsText)
		return result[0]
	# if article content return from api 
	else:
		urlFormat = r'http://card.weibo.com/article/aj/articleshow?cid={}'
		url = urlFormat.format(id)
		response = requests.get(url, headers = articleHeaders)
		response.encoding = 'utf-8'
		content = subContent['data']
		if content:
			content = json.dumps(content).encode('utf-8').decode('unicode_escape')
			content = content.split('<div class="WBA_content clearfix">')[1].split('<div class="link">')[0]
			return content
		else:
			return ''

def saveFailId(id):
	with open('weibofailid.txt','a') as f:
		f.write(str(id)+'\n')
		f.close()

if __name__ == '__main__':
	conn = db_connector()
	latestTimestamp = selectData(conn,'wb_mzm_article',4)
	if latestTimestamp == None:
		latestTimestamp = 0
	print(latestTimestamp)
	ppage = 1

	# the program would extis while all latest posts are crawled
	while ppage < 100:
		getContent(ppage,latestTimestamp,conn)
		ppage = ppage + 1
		sleepTimes(1)
