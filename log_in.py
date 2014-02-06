#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Module implementing login_dlg.
"""
from PyQt4.QtGui import QDialog, QMessageBox, QApplication
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from Ui_log_in import Ui_login_dlg
from student_main_window import student_main_window
from database_operations import login, get_login_info

class login_dlg(QDialog, Ui_login_dlg):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.id_ = 0
        self.username = ''
        self.status = ''
        self.password = ''
        self.conn = ''
        self.setupUi(self)
        self.connect_signal_slot()
    @pyqtSlot()
    def on_login_button_clicked(self):
        """
        Slot documentation goes here.
        """
        self.password = self.lineedit_pass.text().toUtf8()
        self.id_ = self.lineedit_user.text()
        tea_status = self.radio_teacher.isChecked()
        stu_status = self.radio_student.isChecked()
        self.conn = login(str(self.id_), str(self.password))
        if not self.id_:
            QMessageBox.information(self, u'登录失败', u'请输入学号(工号)\n', QMessageBox.Ok, QMessageBox.Ok)
        elif not self.password:
            QMessageBox.information(self, u'登录失败', u'请输入密码\n', QMessageBox.Ok, QMessageBox.Ok)
        elif not (tea_status or stu_status):
            QMessageBox.information(self, u'登录失败', u'请选择身份\n', QMessageBox.Ok, QMessageBox.Ok)
        elif not self.conn:
            QMessageBox.information(self, u'登录失败', u'请检查你的学号(工号)和密码或者身份是否正确!\n', QMessageBox.Ok, QMessageBox.Ok)
        else:
            username = get_login_info( self.id_, stu_status, self.conn)
            if len(username) == 1:
                self.username = username[0][0]
                if tea_status:
                    self.status = '老师'
                    QMessageBox.information(self, u'登录成功', u'欢迎你!\n'+unicode(username[0][0])+u' 老师', QMessageBox.Ok, QMessageBox.Ok)
                    self.accept()
                else:
                    self.status = '学生'
                    QMessageBox.information(self, u'登录成功', u'欢迎你!\n'+unicode(username[0][0])+u' 同学', QMessageBox.Ok, QMessageBox.Ok)
                    self.accept()
            elif len(username) == 0:
                QMessageBox.information(self, u'登录失败', u'请检查你的学号(工号)和密码或者身份是否正确!\n', QMessageBox.Ok, QMessageBox.Ok)

    def connect_signal_slot(self):
        QtCore.QObject.connect(self.login_button, QtCore.SIGNAL("clicked()"), self.on_login_button_clicked)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    x = login_dlg()
    stu_window = student_main_window()
    if x.exec_():
        stu_window.set_info(x.username, x.id_, x.status, x.password, x.conn)
        stu_window.show()
        sys.exit(app.exec_())