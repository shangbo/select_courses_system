
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in.ui'
#
# Created: Wed Feb  5 13:44:25 2014
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

class Ui_login_dlg(object):
    def setupUi(self, login_dlg):
        login_dlg.setObjectName(_fromUtf8("login_dlg"))
        login_dlg.resize(347, 343)

        regx = QtCore.QRegExp("[0-9]+$") # add
        validator = QtGui.QRegExpValidator(regx) # add

        self.horizontalLayoutWidget = QtGui.QWidget(login_dlg)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 261, 81))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.user_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.user_layout.setMargin(0)
        self.user_layout.setObjectName(_fromUtf8("user_layout"))
        self.label_user = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_user.setObjectName(_fromUtf8("label_user"))
        self.user_layout.addWidget(self.label_user)
        self.lineedit_user = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineedit_user.setObjectName(_fromUtf8("lineedit_user"))
        self.lineedit_user.setValidator(validator)   # add
        self.lineedit_user.setMaxLength(4) # add
        self.user_layout.addWidget(self.lineedit_user)


        self.horizontalLayoutWidget_3 = QtGui.QWidget(login_dlg)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 100, 261, 91))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.pass_layout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.pass_layout.setMargin(0)
        self.pass_layout.setObjectName(_fromUtf8("pass_layout"))
        self.label_pass = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_pass.setObjectName(_fromUtf8("label_pass"))
        self.pass_layout.addWidget(self.label_pass)
        self.lineedit_pass = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineedit_pass.setObjectName(_fromUtf8("lineedit_pass"))
        self.lineedit_pass.setEchoMode(QtGui.QLineEdit.Password) # add
        self.pass_layout.addWidget(self.lineedit_pass)

        self.horizontalLayoutWidget_2 = QtGui.QWidget(login_dlg)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 190, 161, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radio_teacher = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radio_teacher.setObjectName(_fromUtf8("teacher_radio"))

        self.horizontalLayout.addWidget(self.radio_teacher)
        self.radio_student = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.radio_student.setObjectName(_fromUtf8("student_radio"))
        self.horizontalLayout.addWidget(self.radio_student)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(login_dlg)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(60, 230, 241, 71))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.login_button = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.login_button.setObjectName(_fromUtf8("login"))
        self.horizontalLayout_2.addWidget(self.login_button)

        self.exit_button = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.exit_button.setObjectName(_fromUtf8("exit"))
        self.horizontalLayout_2.addWidget(self.exit_button)

        self.retranslateUi(login_dlg)
        QtCore.QObject.connect(self.exit_button, QtCore.SIGNAL(_fromUtf8("clicked()")), login_dlg.close)
        # QtCore.QMetaObject.connectSlotsByName(login_dlg)

    def retranslateUi(self, login_dlg):
        login_dlg.setWindowTitle(_translate("login_dlg", "Dialog", None))
        self.label_pass.setText(_translate("login_dlg", "     密码      ", None))
        self.label_user.setText(_translate("login_dlg", "学号(工号)", None))
        self.radio_teacher.setText(_translate("login_dlg", "教师", None))
        self.radio_student.setText(_translate("login_dlg", "学生", None))
        self.login_button.setText(_translate("login_dlg", "登录", None))
        self.exit_button.setText(_translate("login_dlg", "退出", None))

