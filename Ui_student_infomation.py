# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_infomation.ui'
#
# Created: Thu Feb  6 18:25:26 2014
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

class Ui_stu_info(object):
    def setupUi(self, stu_info):
        stu_info.setObjectName(_fromUtf8("stu_info"))
        stu_info.resize(563, 462)
        self.textBrowser = QtGui.QTextBrowser(stu_info)
        self.textBrowser.setGeometry(QtCore.QRect(60, 30, 431, 351))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(stu_info)
        QtCore.QMetaObject.connectSlotsByName(stu_info)

    def retranslateUi(self, stu_info):
        stu_info.setWindowTitle(_translate("stu_info", u"学生信息", None))

