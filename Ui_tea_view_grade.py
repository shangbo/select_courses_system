# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tea_view_grade.ui'
#
# Created: Thu Feb 13 13:22:45 2014
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

class Ui_tea_view_grade(object):
    def setupUi(self, tea_view_grade):
        tea_view_grade.setObjectName(_fromUtf8("tea_view_grade"))
        tea_view_grade.resize(505, 439)
        self.courses_name_show_combobox = QtGui.QComboBox(tea_view_grade)
        self.courses_name_show_combobox.setGeometry(QtCore.QRect(20, 140, 161, 31))
        self.courses_name_show_combobox.setObjectName(_fromUtf8("courses_name_show_combobox"))
        self.grade_tableWidget = QtGui.QTableWidget(tea_view_grade)
        self.grade_tableWidget.setGeometry(QtCore.QRect(190, 140, 301, 281))
        self.grade_tableWidget.setObjectName(_fromUtf8("grade_tableWidget"))
        self.grade_tableWidget.setColumnCount(3)
        self.grade_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.grade_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.grade_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.grade_tableWidget.setHorizontalHeaderItem(2, item)
        self.view_button = QtGui.QPushButton(tea_view_grade)
        self.view_button.setGeometry(QtCore.QRect(50, 330, 98, 27))
        self.view_button.setObjectName(_fromUtf8("view_button"))
        self.view_distributed_button = QtGui.QPushButton(tea_view_grade)
        self.view_distributed_button.setGeometry(QtCore.QRect(50, 370, 98, 27))
        self.view_distributed_button.setObjectName(_fromUtf8("view_distributed_button"))
        self.courses_choose_label = QtGui.QLabel(tea_view_grade)
        self.courses_choose_label.setGeometry(QtCore.QRect(30, 110, 101, 21))
        self.courses_choose_label.setObjectName(_fromUtf8("courses_choose_label"))
        self.grade_show_label = QtGui.QLabel(tea_view_grade)
        self.grade_show_label.setGeometry(QtCore.QRect(200, 110, 111, 21))
        self.grade_show_label.setObjectName(_fromUtf8("grade_show_label"))
        self.layoutWidget = QtGui.QWidget(tea_view_grade)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 171, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.courses_label_layout = QtGui.QHBoxLayout(self.layoutWidget)
        self.courses_label_layout.setMargin(0)
        self.courses_label_layout.setObjectName(_fromUtf8("courses_label_layout"))
        self.courses_label = QtGui.QLabel(self.layoutWidget)
        self.courses_label.setObjectName(_fromUtf8("courses_label"))
        self.courses_label_layout.addWidget(self.courses_label)
        self.courses_show_label = QtGui.QLabel(self.layoutWidget)
        self.courses_show_label.setObjectName(_fromUtf8("courses_show_label"))
        self.courses_label_layout.addWidget(self.courses_show_label)
        self.layoutWidget1 = QtGui.QWidget(tea_view_grade)
        self.layoutWidget1.setGeometry(QtCore.QRect(280, 40, 181, 31))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.teacher_name_label_layout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.teacher_name_label_layout.setMargin(0)
        self.teacher_name_label_layout.setObjectName(_fromUtf8("teacher_name_label_layout"))
        self.tea_name_label = QtGui.QLabel(self.layoutWidget1)
        self.tea_name_label.setObjectName(_fromUtf8("tea_name_label"))
        self.teacher_name_label_layout.addWidget(self.tea_name_label)
        self.tea_name_show_label = QtGui.QLabel(self.layoutWidget1)
        self.tea_name_show_label.setObjectName(_fromUtf8("tea_name_show_label"))
        self.teacher_name_label_layout.addWidget(self.tea_name_show_label)

        self.retranslateUi(tea_view_grade)

        # QtCore.QMetaObject.connectSlotsByName(tea_view_grade)

    def retranslateUi(self, tea_view_grade):
        tea_view_grade.setWindowTitle(_translate("tea_view_grade", "查看课程成绩", None))
        item = self.grade_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tea_view_grade", "学号", None))
        item = self.grade_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("tea_view_grade", "姓名", None))
        item = self.grade_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("tea_view_grade", "总成绩", None))
        self.view_button.setText(_translate("tea_view_grade", "查询", None))
        self.view_distributed_button.setText(_translate("tea_view_grade", "查看成绩分布", None))
        self.courses_choose_label.setText(_translate("tea_view_grade", "请选择课程名:", None))
        self.grade_show_label.setText(_translate("tea_view_grade", "已修学生成绩:", None))
        self.courses_label.setText(_translate("tea_view_grade", "课程:", None))
        self.courses_show_label.setText(_translate("tea_view_grade", "default", None))
        self.tea_name_label.setText(_translate("tea_view_grade", "任课老师:", None))
        self.tea_name_show_label.setText(_translate("tea_view_grade", "default", None))

