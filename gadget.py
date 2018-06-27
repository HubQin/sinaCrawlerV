#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
gadget.py
~~~~~~~~~~~~~~~~~
Some small tools
"""

import time
import datetime
import os

def getTimestamp(text):
	'''Get timestamp from giving text'''

	if '刚刚' in text:
		return int(time.time())
	elif '小时' in text:
		text = text.replace('小时前', '').strip()
		seconds = int(text)*3600
		return int(time.time()) - seconds
	elif '分钟' in text:
		text = text.replace('分钟前', '').strip()
		seconds = int(text)*60
		return int(time.time()) - seconds
	elif '昨天' in text:
		text = text.replace('昨天','').strip()
		timeArray = text.split(':')
		today = datetime.date.today()
		yesterday = today - datetime.timedelta(days = 1)
		timeStruct = time.strptime(str(yesterday),'%Y-%m-%d')
		timestamp = int(time.mktime(timeStruct))
		timestamp = timestamp + int(timeArray[0]) * 3600 + int(timeArray[1]) * 60
		return timestamp
	else:
		if text.count('-') == 1:
			text = '2018-' + text
		if ':' in text and ' ' in text:
			timeStruct = time.strptime(text,'%Y-%m-%d %H:%M')
		else:
			timeStruct = time.strptime(text,'%Y-%m-%d')
		timestamp = int(time.mktime(timeStruct))
		return timestamp

def getDate(timestamp):
	'''Transform timestamp to date'''
	
	timeLocal = time.localtime(timestamp)
	dt = time.strftime("%Y-%m-%d %H:%M:%S",timeLocal)
	return dt

def sleepTimes(num):
	time.sleep(num)

def saveLastTimestamp(timestamp,filename):
	if not os.path.exists('log'):
		os.mkdir('log')
	with open('log/'+filename,'a',encoding='utf-8') as f:
		f.write('保存时间：'+str(datetime.datetime.now())+'\t开始时间戳：'+str(timestamp)+'\n')
		f.close()

def saveFailId(id,title):
	if not os.path.exists('log'):
		os.mkdir('log')
	with open('log/weibo_article_fail_id2.txt','a',encoding='utf-8') as f:
		f.write(title+'\t'+str(id)+'\n')
		f.close()
