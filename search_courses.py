#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialog, QMessageBox, QApplication, QAbstractItemView ,QTableWidgetItem
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from PyQt4 import QtGui
from Ui_search_courses import Ui_search_courses
from database_operations import courses_query

class search_courses(Ui_search_courses, QDialog):
    """

    """
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.display_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.courses_name = ''
        self.courses_id = ''
        self.credit = ''
        self.tea_id = ''
        self.tea_name = ''
        self.work_time = ''
        self.conn = ''

        regx = QtCore.QRegExp("[0-9]+$") # add
        validator = QtGui.QRegExpValidator(regx) # add

        self.courses_id_lineedit.setValidator(validator)
        self.credit_lineedit.setValidator(validator)
        self.tea_id_lineedit.setValidator(validator)
        self.courses_id_lineedit.setMaxLength(7)
        self.credit_lineedit.setMaxLength(2)
        self.tea_id_lineedit.setMaxLength(3)
        self.conn_signal_slot()

    @pyqtSlot()
    def on_search_button_clicked(self):
        self.courses_id = self.courses_id_lineedit.text()
        self.courses_name = self.courses_name_lineedit.text()
        self.credit = self.credit_lineedit.text()
        self.tea_id = self.tea_id_lineedit.text()
        self.tea_name = self.tea_name_lineedit.text()
        self.work_time = self.work_time_lineedit.text()

        condition_dict = {}
        black = not (self.courses_id or self.courses_name or self.credit or self.tea_id or self.tea_name or
                     self.work_time)
        if black:
            QMessageBox.information(self, u"错误", u"请填入查询条件", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.courses_id:
                condition_dict['Courses.courId'] = self.courses_id
            if self.courses_name:
                condition_dict['Courses.courName'] = self.courses_name
            if self.credit:
                condition_dict['Courses.courCredit'] = self.credit
            if self.tea_id:
                condition_dict['Teachers.teaId'] = self.tea_id
            if self.tea_name:
                condition_dict['Teachers.teaName'] = self.tea_name
            if self.work_time:
                condition_dict['OpenClasses.workTime'] = self.work_time

            courses_info = courses_query(condition_dict, self.conn)

            self.display_table_widget.setRowCount(len(courses_info))
            if courses_info:
                for i, item_tuple in enumerate(courses_info):
                    for j, item in enumerate(item_tuple):
                        new_item = QTableWidgetItem(unicode(item))
                        self.display_table_widget.setItem(i, j, new_item)
            else:
                QMessageBox.information(self, u"信息", u"没有符合条件的课程", QMessageBox.Ok)

    @pyqtSlot()
    def on_reset_button_clicked(self):
        self.courses_id_lineedit.setText("")
        self.credit_lineedit.setText("")
        self.tea_id_lineedit.setText("")
        self.courses_name_lineedit.setText("")
        self.tea_name_lineedit.setText("")
        self.work_time_lineedit.setText("")

    def get_conn(self, conn):
        self.conn = conn

    def conn_signal_slot(self):
        QtCore.QObject.connect(self.search_button, QtCore.SIGNAL("clicked()"), self.on_search_button_clicked)
        QtCore.QObject.connect(self.reset_button, QtCore.SIGNAL("clicked()"), self.on_reset_button_clicked)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    s = search_courses()
    s.show()

    sys.exit(app.exec_())
