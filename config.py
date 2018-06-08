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
articleHeaders = {
		'Cookie':r'SINAGLOBAL=5271158416965.729.1526652878220; un=13660060546; UM_distinctid=163791d3d851ba-0237912ea94dac-72236637-cf30-163791d3d864c9; CNZZDATA1271720685=601938555-1526742339-%7C1526742339; CNZZDATA1273321676=1426356873-1526750926-%7C1526750926; _s_tentry=login.sina.com.cn; Apache=8747829202412.636.1526779725159; ULV=1526779725260:4:4:1:8747829202412.636.1526779725159:1526735261582; login_sid_t=8e2c09825d51914d85f6b98a87af278f; cross_origin_proto=SSL; CARD-ARTICLE-VIDEO=f6cb8c7fc551a8e8b396bc0a9f0f2f3d; CARD-MAIN=241a99d1f18ecf4860168aacdcddcc0a; UOR=,,login.sina.com.cn; SCF=AmmfF3qnIlzy94enIcFLjnaUnAQUiWWCEQgCmuJzaXlJubMC03imkqiLl_Xrfh20NmUcoVJBD5Q1DxgzeJLPX6M.; SUB=_2A252BRs0DeRhGedO6lcV8yvLzziIHXVVcwv8rDV8PUNbmtBeLVb_kW9NIy84OIwO4l_g3UYItnbBAggddX3fzt7V; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5dDAfB1DujZzmLzymi6i1K5JpX5K2hUgL.Fo27eK-Xe0-NShB2dJLoIpjLxKnLB.qL1-zLxKqLB-BLBK-LxKnLB--LBo5t; SUHB=0cSR7n_Uqo9cwx; ALF=1527424484; SSOLoginState=1526819685',
		'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
}
# URL format of Post list 
listUrlFormat = r'https://m.weibo.cn/api/container/getIndex?type=uid&value=1496913734&containerid=1076031496913734&page={}'

# URL format of Post
postUrlFormat = r'https://m.weibo.cn/statuses/extend?id={}'

# URL format of Post comment 
commentUrlFormat = r'https://m.weibo.cn/api/comments/show?id={id}&page={page}'

# URL format of Article list 
articleListUrlFormat = r'https://m.weibo.cn/api/container/getIndex?containerid=2303190002_445_1496913734_WEIBO_ARTICLE_LIST_DETAIL&count=20&luicode=10000011&lfid=1005051496913734&type=uid&value=1496913734&page={}'

# URL format of Article 
articleUrlFormat = r'https://media.weibo.cn/article?object_id={object_id}&id={id}'