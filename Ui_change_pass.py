# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_pass.ui'
#
# Created: Thu Feb  6 13:45:32 2014
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

class Ui_change_pass_dialog(object):
    def setupUi(self, change_pass_dialog):
        change_pass_dialog.setObjectName(_fromUtf8("change_pass_dialog"))
        change_pass_dialog.resize(340, 260)
        self.old_pass_label = QtGui.QLabel(change_pass_dialog)
        self.old_pass_label.setGeometry(QtCore.QRect(30, 30, 91, 41))
        self.old_pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.old_pass_label.setObjectName(_fromUtf8("old_pass_label"))
        self.new_pass_label = QtGui.QLabel(change_pass_dialog)
        self.new_pass_label.setGeometry(QtCore.QRect(30, 90, 91, 41))
        self.new_pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_pass_label.setObjectName(_fromUtf8("new_pass_label"))
        self.repeat_label = QtGui.QLabel(change_pass_dialog)
        self.repeat_label.setGeometry(QtCore.QRect(30, 160, 91, 41))
        self.repeat_label.setAlignment(QtCore.Qt.AlignCenter)
        self.repeat_label.setObjectName(_fromUtf8("repeat_label"))

        self.old_pass_lineedit = QtGui.QLineEdit(change_pass_dialog)
        self.old_pass_lineedit.setGeometry(QtCore.QRect(130, 40, 151, 31))
        self.old_pass_lineedit.setObjectName(_fromUtf8("old_pass_lineedit"))
        self.old_pass_lineedit.setEchoMode(QtGui.QLineEdit.Password)

        self.new_pass_lineedit = QtGui.QLineEdit(change_pass_dialog)
        self.new_pass_lineedit.setEchoMode(QtGui.QLineEdit.Password)
        self.new_pass_lineedit.setGeometry(QtCore.QRect(130, 100, 151, 31))
        self.new_pass_lineedit.setObjectName(_fromUtf8("new_pass_lineedit"))

        self.repeat_lineedit = QtGui.QLineEdit(change_pass_dialog)
        self.repeat_lineedit.setGeometry(QtCore.QRect(130, 160, 151, 31))
        self.repeat_lineedit.setObjectName(_fromUtf8("repeat_lineedit"))
        self.repeat_lineedit.setEchoMode(QtGui.QLineEdit.Password)

        self.change_button = QtGui.QPushButton(change_pass_dialog)
        self.change_button.setGeometry(QtCore.QRect(50, 220, 98, 27))
        self.change_button.setObjectName(_fromUtf8("pushButton"))

        self.caceled_button = QtGui.QPushButton(change_pass_dialog)
        self.caceled_button.setGeometry(QtCore.QRect(190, 220, 98, 27))
        self.caceled_button.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(change_pass_dialog)
        QtCore.QObject.connect(self.caceled_button, QtCore.SIGNAL(_fromUtf8("clicked()")), change_pass_dialog.close)
        QtCore.QMetaObject.connectSlotsByName(change_pass_dialog)

    def retranslateUi(self, change_pass_dialog):
        change_pass_dialog.setWindowTitle(_translate("change_pass_dialog", "更改密码", None))
        self.old_pass_label.setText(_translate("change_pass_dialog", "旧密码", None))
        self.new_pass_label.setText(_translate("change_pass_dialog", "新密码", None))
        self.repeat_label.setText(_translate("change_pass_dialog", "重复新密码", None))
        self.change_button.setText(_translate("change_pass_dialog", "更改", None))
        self.caceled_button.setText(_translate("change_pass_dialog", "取消", None))

