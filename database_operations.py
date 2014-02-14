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


def get_teacher_courses(id_, conn):
    cur = conn.cursor()
    try:
        cur.execute("select courName,Courses.courId from OpenClasses,Courses "
                    "where OpenClasses.courId=Courses.courId "
                    "and OpenClasses.teaId = '%s';" % id_)
        cour_name_tuple = cur.fetchall()
    except MySQLdb.OperationalError, MySQLdb.ProgrammingError:
        cour_name_tuple = ""
    finally:
        cur.close()
        return cour_name_tuple


def get_studied_the_courses_stu_info(tea_id, cour_id, conn):
    cur = conn.cursor()
    try:
        cur.execute("select Students.stuId,Students.stuName,SelectCourses.totalGrade from SelectCourses,Students "
                    "where SelectCourses.teaId = '%s' and SelectCourses.courId='%s' "
                    "and SelectCourses.stuId=Students.stuId and not totalGrade is NULL" % (tea_id, cour_id))
        stu_info = cur.fetchall()
    except MySQLdb.OperationalError, MySQLdb.ProgrammingError:
        stu_info = ''
    finally:
        cur.close()
        return stu_info


def get_studied_the_courses_stu_info_2(tea_id, cour_id, conn):
    cur = conn.cursor()
    try:
        cur.execute("select Students.stuId,Students.stuName,SelectCourses.regularGrade,"
                    "SelectCourses.examGrade,SelectCourses.totalGrade from SelectCourses,Students "
                    "where SelectCourses.teaId = '%s' and SelectCourses.courId='%s' "
                    "and SelectCourses.stuId=Students.stuId and not totalGrade is NULL" % (tea_id, cour_id))
        stu_info = cur.fetchall()
    except MySQLdb.OperationalError, MySQLdb.ProgrammingError:
        stu_info = ''
    finally:
        cur.close()
        return stu_info


def get_no_grade_stu_info(tea_id, cour_id, conn):
    cur = conn.cursor()
    try:
        cur.execute("select Students.stuId,Students.stuName,SelectCourses.totalGrade from SelectCourses,Students "
                    "where SelectCourses.teaId = '%s' and SelectCourses.courId='%s' "
                    "and SelectCourses.stuId=Students.stuId and totalGrade is NULL" % (tea_id, cour_id))
        stu_info = cur.fetchall()
    except MySQLdb.OperationalError,MySQLdb.ProgrammingError:
        stu_info = ''
    finally:
        cur.close()
        return stu_info


def update_grade(regular_grade, exam_grade, cour_name, stu_name, total_grade, conn):
    cur = conn.cursor()
    cur.execute("select courId from Courses where courName = '%s'" % cour_name)
    cour_id = cur.fetchall()[0][0]
    cur.execute("select stuId from Students where stuName = '%s'" % stu_name)
    stu_id = cur.fetchall()[0][0]
    cur.execute("update SelectCourses set regularGrade = '%s' where courId='%s' "
                "and stuId='%s';" % (regular_grade, cour_id, stu_id))
    conn.commit()
    cur.execute("update SelectCourses set examGrade = '%s' where courId='%s' "
                "and stuId='%s';" % (exam_grade, cour_id, stu_id))
    conn.commit()
    cur.execute("update SelectCourses set totalGrade = '%s' where courId='%s' "
                "and stuId='%s';" % (total_grade, cour_id, stu_id))
    conn.commit()


def get_the_courses_stu_name(tea_id, cour_id, conn):
    cur = conn.cursor()
    cur.execute("select Students.stuId,Students.stuName,SelectCourses.totalGrade from SelectCourses,Students "
                    "where SelectCourses.teaId = '%s' and SelectCourses.courId='%s' "
                    "and SelectCourses.stuId=Students.stuId" % (tea_id, cour_id))
    stu_info = cur.fetchall()
    return stu_info

