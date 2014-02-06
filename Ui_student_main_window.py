
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_main_window.ui'
#
# Created: Thu Feb  6 12:22:36 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_student_main(object):
    def setupUi(self, student_main):
        student_main.setObjectName(_fromUtf8("student_main"))
        student_main.resize(815, 479)
        self.select_courses_button = QtGui.QToolButton(student_main)
        self.select_courses_button.setGeometry(QtCore.QRect(30, 250, 121, 161))
        self.select_courses_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_courses_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.select_courses_button.setObjectName(_fromUtf8("select_courses_button"))
        self.stu_info_button = QtGui.QToolButton(student_main)
        self.stu_info_button.setGeometry(QtCore.QRect(30, 80, 121, 161))
        self.stu_info_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stu_info_button.setCheckable(False)
        self.stu_info_button.setAutoRepeat(False)
        self.stu_info_button.setArrowType(QtCore.Qt.NoArrow)
        self.stu_info_button.setObjectName(_fromUtf8("stu_info_button"))
        self.search_courses_button = QtGui.QToolButton(student_main)
        self.search_courses_button.setGeometry(QtCore.QRect(170, 80, 121, 161))
        self.search_courses_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_courses_button.setObjectName(_fromUtf8("search_courses_button"))
        self.view_grade_button = QtGui.QToolButton(student_main)
        self.view_grade_button.setGeometry(QtCore.QRect(170, 250, 121, 161))
        self.view_grade_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.view_grade_button.setObjectName(_fromUtf8("view_grade_button"))
        self.calendar = QtGui.QCalendarWidget(student_main)
        self.calendar.setGeometry(QtCore.QRect(340, 90, 451, 321))
        self.calendar.setObjectName(_fromUtf8("calendar"))
        self.change_pass_button = QtGui.QPushButton(student_main)
        self.change_pass_button.setGeometry(QtCore.QRect(670, 30, 98, 27))
        self.change_pass_button.setObjectName(_fromUtf8("change_pass_button"))
        self.horizontalLayoutWidget = QtGui.QWidget(student_main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 161, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.name_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.name_layout.setMargin(0)
        self.name_layout.setObjectName(_fromUtf8("name_layout"))
        self.name_label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.name_layout.addWidget(self.name_label)
        self.name2_label = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name2_label.setFont(font)
        self.name2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name2_label.setObjectName(_fromUtf8("name2_label"))
        self.name_layout.addWidget(self.name2_label)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(student_main)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(210, 10, 161, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.id_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.id_layout.setMargin(0)
        self.id_layout.setObjectName(_fromUtf8("id_layout"))
        self.id_label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label.setObjectName(_fromUtf8("id_label"))
        self.id_layout.addWidget(self.id_label)
        self.id2_label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.id2_label.setFont(font)
        self.id2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.id2_label.setObjectName(_fromUtf8("id2_label"))
        self.id_layout.addWidget(self.id2_label)

        self.retranslateUi(student_main)
        # QtCore.QMetaObject.connectSlotsByName(student_main)

    def retranslateUi(self, student_main):
        student_main.setWindowTitle(_translate("student_main", "student main window", None))
        self.select_courses_button.setText(_translate("student_main", "选课", None))
        self.stu_info_button.setText(_translate("student_main", "个人信息", None))
        self.search_courses_button.setText(_translate("student_main", "查询课程", None))
        self.view_grade_button.setText(_translate("student_main", "查看成绩", None))
        self.change_pass_button.setText(_translate("student_main", "更改密码", None))
        self.name_label.setText(_translate("student_main", "姓名:", None))
        self.name2_label.setText(_translate("student_main", "default", None))
        self.id_label.setText(_translate("student_main", "学号:", None))
        self.id2_label.setText(_translate("student_main", "default", None))

