#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
#global

def login(id_=None,password=None):
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user=id_,passwd=password,db='school',charset='utf8')
    except MySQLdb.OperationalError:
        conn = ''
    return conn

def get_login_info(conn,id_,status):
    cur = conn.cursor()
    try:
        if status:
            cur.execute("select stuName from Students where stuId='%s';" % id_)
        else:
            cur.execute("select teaName from Teachers where teaId='%s';" % id_)
        username = cur.fetchall()
    except MySQLdb.OperationalError:
        username = ''
    return username


