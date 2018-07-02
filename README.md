# sinaCrawlerV
easy program to backup posts and comments of specify user in sina
简易爬虫抓取指定用户的微博和微博文章

## Requirement：
- python 3.6
	+ extension:
		* bs4
		* lxml
		* pymysql

- mysql 5.6

## Function:
- database.py 封装了各种mysql操作
- post.py 抓取微博，每次抓取到上次抓取的时间为止
- article.py 抓取文章，同上
- gadget.py 用到的各种小工具
- config.py 需要用到的参数

## Usage：
- 创建数据表：运行sina.sql创建数据表
- 完善config.py的参数，抓取微博使用移动端的请求链接；抓取文章需要登录，这里手动登录后，查看移动端的异步请求，复制Request Header里面的cookie出来使用
- 命令行终端cd到py文件所在目录，运行pyhton.py和article.py，或修改auto.bat文件的cd路径，双击改文件开始抓取

## Todo：
- OOP改写
- 自动登录

