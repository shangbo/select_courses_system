#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt4.QtGui import QWidget, QApplication, QMessageBox
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from Ui_teacher_main_window import Ui_TeacherDialog
from change_pass import change_pass_dlg
from database_operations import logout
from tea_view_grade import TeaViewGrade
from update_grade import UpdateGrade


class TeacherMainWindow(Ui_TeacherDialog, QWidget):
    """

    """
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.username = ''
        self.status = ''
        self.id_ = ''
        self.password = ''
        self.conn = ''
        self.conn_signal_slot()
        self.pass_dialog = change_pass_dlg()
        self.view_grade_dlg = TeaViewGrade()
        self.update_grade_dlg = UpdateGrade()

    @pyqtSlot()
    def on_logout_button_clicked(self):
        logout(self.conn)
        QMessageBox.information(self, u"信息", u"已注销,请重新登录!", QMessageBox.Ok)
        QtCore.QCoreApplication.instance().quit()

    @pyqtSlot()
    def on_change_pass_button_clicked(self):
        self.pass_dialog.set_info(self.password, self.conn)
        self.pass_dialog.exec_()

    @pyqtSlot()
    def on_view_grade_button_clicked(self):
        self.view_grade_dlg.get_info(self.id_, self.username, self.conn)
        self.view_grade_dlg.set_init_view()
        self.view_grade_dlg.exec_()

    @pyqtSlot()
    def on_update_grade_button_clicked(self):
        self.update_grade_dlg.get_info(self.id_, self.conn)
        self.update_grade_dlg.set_init_view()
        self.update_grade_dlg.exec_()

    def set_info(self, name, id_, status, password, conn):
        self.username = name
        self.id_ = id_
        self.status = status
        self.password = password
        self.conn = conn
        self.name_show_label.setText(self.username)
        self.id_show_label.setText(self.id_)

    def conn_signal_slot(self):
        QtCore.QObject.connect(self.change_pass_button, QtCore.SIGNAL("clicked()"),
                               self.on_change_pass_button_clicked)
        QtCore.QObject.connect(self.log_out_button, QtCore.SIGNAL("clicked()"),
                               self.on_logout_button_clicked)
        QtCore.QObject.connect(self.view_stu_grade, QtCore.SIGNAL("clicked()"),
                               self.on_view_grade_button_clicked)
        QtCore.QObject.connect(self.update_stu_grade, QtCore.SIGNAL("clicked()"),
                               self.on_update_grade_button_clicked)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    t = TeacherMainWindow()
    t.show()
    sys.exit(app.exec_())