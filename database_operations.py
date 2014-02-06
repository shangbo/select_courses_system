#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
import sys


def login(id_=None,password=None):
    conn = ''
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user=id_,passwd=password,db='school',charset='utf8')
    except MySQLdb.OperationalError:
        conn = ''
    finally:
        return conn

def get_login_info(id_,status,conn):
    username = ''
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
    cur = conn.cursor()
    try:
        cur.execute("set password = password('%s')" % password)
        return True
    except MySQLdb.OperationalError:
        return False
    finally:
        cur.close()

def logout(conn):
    try:
        conn.close()
    except AttributeError:
        pass

def get_student_info(id_, conn):
    cur = conn.cursor()
    info = ''
    try:
        cur.execute("select stuName,stuId,stuGender,stuBirthday,stuNativePlace,"
                    "stuPhoneNum,departName "
                    "from Students,Departments "
                    "where Students.stuId = '%s' and Students.departId = Departments.departId " % id_)
        info = cur.fetchall()
    except MySQLdb.OperationalError:
        print sys.exc_value[1]
        info = ''
    finally:
        cur.close()
        return info







