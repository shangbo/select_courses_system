#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt4.QtGui import QWidget,QApplication, QMessageBox
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from Ui_student_main_window import Ui_student_main
from change_pass import change_pass_dlg
from student_infomation import stu_info
class student_main_window(QWidget, Ui_student_main):
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
        self.pass_dialog = change_pass_dlg()
        self.stu_info_dlg = stu_info()
        self.set_signal_slot()
    @pyqtSlot()
    def on_select_courses_button_clicked(self):
        pass

    @pyqtSlot()
    def on_stu_info_button_clicked(self):
        self.stu_info_dlg.set_html(self.conn,self.id_)
        self.stu_info_dlg.exec_()
    @pyqtSlot()
    def on_search_courses_button_clicked(self):
        pass

    @pyqtSlot()
    def on_view_grade_button_clicked(self):
        pass

    @pyqtSlot()
    def on_change_pass_button_clicked(self):
        self.pass_dialog.set_info(self.password, self.conn)
        self.pass_dialog.exec_()

    def set_info(self, name, id_, status, password, conn):
        self.username = name
        self.id_ = id_
        self.status = status
        self.password = password
        self.conn = conn
        self.name2_label.setText(self.username)
        self.id2_label.setText(self.id_)

    def set_signal_slot(self):
        QtCore.QObject.connect(self.change_pass_button, QtCore.SIGNAL("clicked()"), self.on_change_pass_button_clicked)
        QtCore.QObject.connect(self.stu_info_button, QtCore.SIGNAL("clicked()"), self.on_stu_info_button_clicked)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = student_main_window()
    window.show()

    sys.exit(app.exec_())

