#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
database.py
~~~~~~~~~~~~~~~~~
Encapsule some database operations in pymysql
"""

import pymysql

def db_connector():
	'''Create a database connector with your database config'''

	conn = pymysql.connect("localhost","root","root","weibo", use_unicode = True, charset="utf8mb4")
	return conn

def insert_data(table_name,conn, **kw):
	'''Insert data into table'''

	# Concat SQL string which format like:"INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
	sql = "INSERT INTO %s" % table_name
	sql += " ("
	tail_part = "VALUES ("
	value_list = []

	for key,value in kw.items():
		sql += "`" + key +"`,"
		tail_part += "%s,"
		value_list.append(value)

	sql = sql[:-1]
	sql += ") "

	tail_part = tail_part[:-1]
	tail_part += ")"

	# Need a tuple as parameter
	value_tuple = tuple(value_list)
	sql = sql + tail_part

	#Insert data into table
	conn.cursor().execute(sql,value_tuple)
	conn.commit()

def selectData(conn,table,fieldnum):
	'''Select one record from table and return specify field value
	:fieldnum:the index of the field,start from zero
	'''
	sql =  "SELECT * FROM `%s` order by add_time desc limit 1" % table
	cur = conn.cursor()
	cur.execute(sql)
	for r in cur:
		return r[fieldnum]

def closeConn(conn):
	'''close the connection'''
	conn.close()

