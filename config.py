#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
config.py
~~~~~~~~~~~~~~~~~
Constants need in crawler
"""
# Header
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# Header for crawl article
# articleHeaders = {
# 	'Cookie':r'_T_WM=0b13657a0903c215891afe5a7a4012cd; ALF=1532181429; WEIBOCN_FROM=1110005030; SCF=Att_NsRwCo9sMXbYndJPt4Sl30epTVZCzDk3yaiNUg2GefeRMdqshooy58qaUZpwaWpYpaHzKl4SOntfxkgzstM.; SUB=_2A252L96_DeRhGedO6lcV8yvLzziIHXVV0-L3rDV6PUJbktANLXTVkW1NIy84ODGyaWMsczoLwB7knUvQ3qWd91vF; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5dDAfB1DujZzmLzymi6i1K5JpX5K-hUgL.Fo27eK-Xe0-NShB2dJLoIpjLxKnLB.qL1-zLxKqLB-BLBK-LxKnLB--LBo5t; SUHB=0au2DNPXsvoq0w; SSOLoginState=1529589487; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D2310181496913734_-_longbloglist_original%26oid%3D3787648436993966%26uicode%3D10000370',
# 	'User-Agent':"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Mobile Safari/537.36"
# }
articleHeaders = {
	'Cookie':r'ALF=1532785263; _T_WM=bde86559938e533e578d8172691246fa; WEIBOCN_FROM=1110006030; SCF=AmmfF3qnIlzy94enIcFLjnaUnAQUiWWCEQgCmuJzaXlJiVBgfHUTepPbBkfhKrqGdGjpWPzM1oS9SRejKYpfjdc.; SUB=_2A252MJZ8DeRhGedO6lcV8yvLzziIHXVV2jo0rDV6PUJbktAKLUHAkW1NIy84OBcSc-aylpH9jvVW08FGwxm9gt09; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5dDAfB1DujZzmLzymi6i1K5JpX5K-hUgL.Fo27eK-Xe0-NShB2dJLoIpjLxKnLB.qL1-zLxKqLB-BLBK-LxKnLB--LBo5t; SUHB=0G0YSAIUb0Z7ru; SSOLoginState=1530193452; MLOGIN=1; M_WEIBOCN_PARAMS=fid%3D1005051496913734%26uicode%3D10000011',
	'User-Agent':"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Mobile Safari/537.36"
}
# URL format of Post list 
listUrlFormat = r'https://m.weibo.cn/api/container/getIndex?type=uid&value=1496913734&containerid=1076031496913734&page={}'

# URL format of Post
postUrlFormat = r'https://m.weibo.cn/statuses/extend?id={}'

# URL format of Post comment 
commentUrlFormat = r'https://m.weibo.cn/api/comments/show?id={id}&page={page}'

# URL format of Article list 
# articleListUrlFormat = r'https://m.weibo.cn/api/container/getIndex?containerid=2303190002_445_1496913734_WEIBO_ARTICLE_LIST_DETAIL&count=20&luicode=10000011&lfid=1005051496913734&type=uid&value=1496913734&page={}'
articleListUrlFormat = r'https://m.weibo.cn/api/container/getIndex?containerid=2310181496913734_-_longbloglist_original&luicode=10000011&lfid=1005051496913734&page={}'

# URL format of Article 
articleUrlFormat = r'https://media.weibo.cn/article?object_id={object_id}&id={id}'