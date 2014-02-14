# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_main_window.ui'
#
# Created: Wed Feb 12 19:46:50 2014
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

class Ui_TeacherDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(714, 504)
        self.calendarWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(240, 120, 451, 351))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.view_stu_grade = QtGui.QToolButton(Dialog)
        self.view_stu_grade.setGeometry(QtCore.QRect(50, 120, 131, 141))
        self.view_stu_grade.setObjectName(_fromUtf8("view_stu_grade"))
        self.update_stu_grade = QtGui.QToolButton(Dialog)
        self.update_stu_grade.setGeometry(QtCore.QRect(50, 300, 131, 141))
        self.update_stu_grade.setObjectName(_fromUtf8("update_stu_grade"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.id_label_layout = QtGui.QHBoxLayout(self.widget)
        self.id_label_layout.setMargin(0)
        self.id_label_layout.setObjectName(_fromUtf8("id_label_layout"))
        self.id_label = QtGui.QLabel(self.widget)
        self.id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label.setObjectName(_fromUtf8("id_label"))
        self.id_label_layout.addWidget(self.id_label)
        self.id_show_label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.id_show_label.setFont(font)
        self.id_show_label.setObjectName(_fromUtf8("id_show_label"))
        self.id_label_layout.addWidget(self.id_show_label)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(190, 30, 161, 31))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.name_label_layout = QtGui.QHBoxLayout(self.widget1)
        self.name_label_layout.setMargin(0)
        self.name_label_layout.setObjectName(_fromUtf8("name_label_layout"))
        self.name_label = QtGui.QLabel(self.widget1)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.name_label_layout.addWidget(self.name_label)
        self.name_show_label = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_show_label.setFont(font)
        self.name_show_label.setObjectName(_fromUtf8("name_show_label"))
        self.name_label_layout.addWidget(self.name_show_label)
        self.widget2 = QtGui.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(480, 30, 204, 32))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.push_button_layout = QtGui.QHBoxLayout(self.widget2)
        self.push_button_layout.setMargin(0)
        self.push_button_layout.setObjectName(_fromUtf8("push_button_layout"))
        self.log_out_button = QtGui.QPushButton(self.widget2)
        self.log_out_button.setObjectName(_fromUtf8("log_out_button"))
        self.push_button_layout.addWidget(self.log_out_button)
        self.change_pass_button = QtGui.QPushButton(self.widget2)
        self.change_pass_button.setObjectName(_fromUtf8("change_pass_button"))
        self.push_button_layout.addWidget(self.change_pass_button)

        self.retranslateUi(Dialog)
        # QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "教师主窗口", None))
        self.view_stu_grade.setText(_translate("Dialog", "查看学生成绩", None))
        self.update_stu_grade.setText(_translate("Dialog", "登记/修改学生成绩", None))
        self.id_label.setText(_translate("Dialog", "工号:", None))
        self.id_show_label.setText(_translate("Dialog", "default", None))
        self.name_label.setText(_translate("Dialog", "姓名:", None))
        self.name_show_label.setText(_translate("Dialog", "default", None))
        self.log_out_button.setText(_translate("Dialog", "注销", None))
        self.change_pass_button.setText(_translate("Dialog", "修改密码", None))

