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


def courses_query(search_condition, conn):
    cur = conn.cursor()
    sql = "select Courses.courId,Courses.courName,Courses.courCredit," \
          "Teachers.teaId,Teachers.teaName,OpenClasses.semester,OpenClasses.workTime " \
          "from Courses,OpenClasses,Teachers " \
          "where Courses.courId=OpenClasses.courId and Teachers.teaId=OpenClasses.teaId"
    for key, value in search_condition.items():
        sql += " and %s='%s'" % (key, value)
    sql += ';'
    try:
        cur.execute(sql)
        courses_info = cur.fetchall()
    except MySQLdb.OperationalError:
        courses_info = ''
    finally:
        cur.close()
        return courses_info


def get_studied_courses_info(id_, conn):
    cur = conn.cursor()
    try:
        cur.execute(" select Courses.courId,Courses.courName,SelectCourses.semester,Courses.courCredit,"
                    "SelectCourses.totalGrade from Courses,SelectCourses "
                    "where SelectCourses.stuId = '%s' and SelectCourses.courId = Courses.courId "
                    "and not SelectCourses.totalGrade is NULL;" % id_)
        studied_info = cur.fetchall()
    except MySQLdb.OperationalError:
        studied_info = ''
    finally:
        cur.close()
    return studied_info


def get_selected_courses_info(id_,conn):
    cur = conn.cursor()
    try:
        cur.execute("select Courses.courId,Courses.courName,Teachers.teaId,Teachers.teaName,OpenClasses.semester,"
                    "OpenClasses.workTime from SelectCourses,Courses,Teachers,OpenClasses "
                    "where SelectCourses.stuId = '%s' and SelectCourses.totalGrade is NULL "
                    "and Teachers.teaId = OpenClasses.teaId AND Courses.courId = SelectCourses.courId "
                    "and Teachers.teaId = SelectCourses.teaId and Courses.courId = OpenClasses.courId;" % id_)
        selected_info = cur.fetchall()
    except MySQLdb.OperationalError:
        selected_info = ''
    finally:
        cur.close()
        return selected_info


def get_could_select_info(id_, conn):
    cur = conn.cursor()
    try:
        cur.execute("select Courses.courId,Courses.courName,Teachers.teaId,Teachers.teaName,"
                    "OpenClasses.semester,OpenClasses.workTime,Courses.courCredit,Departments.departName"
                    " from OpenClasses,Courses,Teachers,Departments "
                    "where OpenClasses.courId  not in (select courId from SelectCourses where stuId='%s')"
                    " and Courses.courId=OpenClasses.courId and OpenClasses.teaId=Teachers.teaId "
                    "and Courses.departId=Departments.departId;" % id_)
        could_select_info = cur.fetchall()
    except MySQLdb.OperationalError:
        could_select_info = ''
    finally:
        cur.close()
        return could_select_info


def select_courses_operation(id_, cour_id, tea_id, conn):
    cur = conn.cursor()
    try:
        cur.execute("select semester from OpenClasses where courId='%s' and teaId='%s'" % (cour_id, tea_id))
        semester = cur.fetchall()
        if len(semester) == 1:
            cur.execute(u"insert into SelectCourses(stuId,semester,courId,teaId,regularGrade,examGrade,totalGrade) values('%s','%s','%s','%s',NULL,NULL,NULL)" % (id_, semester[0][0], cour_id, tea_id))
            conn.commit()
            return True
        else:
            return False
    except MySQLdb.OperationalError, MySQLdb.ProgrammingError:
        return False
    finally:
        cur.close()


def drop_courses_operation(id_, cour_id, tea_id, conn):
    cur = conn.cursor()
    try:
        cur.execute("delete from SelectCourses where stuId= '%s' and courId = '%s' and teaId = '%s' " % (id_, cour_id, tea_id))
        conn.commit()
        return True
    except MySQLdb.OperationalError, MySQLdb.ProgrammingError:
        return False






