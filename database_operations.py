#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
#global

def login(username=None,password=None):
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user=username,passwd=password,db='school',charset='utf8')
    except MySQLdb.OperationalError:
        conn = ''
    return conn

def get_login_info(conn):
    cur = conn.cursor()
    #TODO 替换掉stuId
    cur.execute("select stuName from Students where stuId=1101;")
    username = cur.fetchall()
    return username


