#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb


def get_database_connection():
    conn = MySQLdb.connect(user='root', passwd='shangbo123', host='127.0.0.1', charset='utf8', db='school')
    return conn


def get_stu_id(conn):
    cur = conn.cursor()
    cur.execute("select stuId from Students")
    id_ = cur.fetchall()
    cur.close()
    return id_


def get_tea_id(conn):
    cur = conn.cursor()
    cur.execute("select teaId from Teachers")
    id_ = cur.fetchall()
    cur.close()
    return id_


def create_stu_add_priv(id_tup,conn):
    cur = conn.cursor()
    for i in id_tup:
        cur.execute("grant usage,select on school.* to '%s'@'%%' identified by '%s' " % (i[0], i[0]))
        cur.execute("grant insert,delete on school.SelectCourses to '%s'@'%%' identified by '%s' " % (i[0],i[0]))
    cur.close()


def create_tea_add_priv(id_tup,conn):
    cur = conn.cursor()
    for i in id_tup:
        cur.execute("grant usage,select on school.* to '%s'@'%%' identified by '%s' " % (i[0], i[0]))
        cur.execute("grant update on school.SelectCourses to '%s'@'%%' identified by '%s' " % (i[0],i[0]))
    cur.close()


def modified_student_info(id_, conn, column, value):
    pass


def main():
    conn = get_database_connection()
    stu_id_tup = get_stu_id(conn)
    tea_id_tup = get_tea_id(conn)
    create_stu_add_priv(stu_id_tup, conn)
    create_tea_add_priv(tea_id_tup, conn)
    conn.close()
if __name__ == '__main__':
    main()

