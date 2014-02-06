#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
#global

def login(id_=None,password=None):
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user=id_,passwd=password,db='school',charset='utf8')
    except MySQLdb.OperationalError:
        conn = ''
    finally:
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
    finally:
        cur.close()
        return username

def change_password(password, conn):
    try:
        cur = conn.cursor()
        cur.execute("set password = password('%s')" % password)
        return True
    except MySQLdb.OperationalError:
        return False
    finally:
        cur.close()

def logout(conn):
    conn.close()






