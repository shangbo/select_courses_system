#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt4.QtGui import QDialog, QMessageBox, QApplication, QTableWidgetItem, QAbstractItemView
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from Ui_select_courses import Ui_select_courses
from database_operations import get_could_select_info, get_selected_courses_info, get_studied_courses_info
from database_operations import select_courses_operation, drop_courses_operation


class select_courses(QDialog, Ui_select_courses):
    """

    """
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.conn = ''
        self.id_ = ''
        self.conn_signal_slot()
        self.studied_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.could_select_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selected_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def set_view(self):
        self.set_could_select_view()
        self.set_selected_view()
        self.set_studied_view()

    def set_studied_view(self):
        studied_info = get_studied_courses_info(self.id_, self.conn)
        self.studied_table_widget.setRowCount(len(studied_info))
        for i, item_tuple in enumerate(studied_info):
            for j, item in enumerate(item_tuple):
                new_item = QTableWidgetItem(unicode(item))
                self.studied_table_widget.setItem(i, j, new_item)

    def set_selected_view(self):
        selected_info = get_selected_courses_info(self.id_, self.conn)
        self.selected_table_widget.setRowCount(len(selected_info))
        for i, item_tuple in enumerate(selected_info):
            for j, item in enumerate(item_tuple):
                new_item = QTableWidgetItem(unicode(item))
                self.selected_table_widget.setItem(i, j, new_item)

    def set_could_select_view(self):
        could_select_info = get_could_select_info(self.id_, self.conn)
        self.could_select_table_widget.setRowCount(len(could_select_info))
        for i, item_tuple in enumerate(could_select_info):
            for j, item in enumerate(item_tuple):
                new_item = QTableWidgetItem(unicode(item))
                self.could_select_table_widget.setItem(i, j, new_item)

    @pyqtSlot()
    def on_select_courses_button_clicked(self):
        cour_id = self.courses_id_lineedit.text()
        tea_id = self.tea_id_lineedit.text()
        if not cour_id:
            QMessageBox.information(self, u"错误", u"请输入课程号!", QMessageBox.Ok)
        elif not tea_id:
            QMessageBox.information(self, u"错误", u"请输入教师号!", QMessageBox.Ok)
        else:
            judge = select_courses_operation(self.id_, cour_id, tea_id, self.conn)
            if not judge:
                QMessageBox.information(self, u"错误", u"请检查课程号与教师号", QMessageBox.Ok)
            else:
                self.set_selected_view()
                self.set_could_select_view()
        # QMessageBox.information(self,"sd","dsa",QMessageBox.Ok)

    @pyqtSlot()
    def on_drop_courses_button_clicked(self):
        cour_id = self.courses_id_lineedit.text()
        tea_id = self.tea_id_lineedit.text()
        if not cour_id:
            QMessageBox.information(self, u"错误", u"请输入课程号!", QMessageBox.Ok)
        elif not tea_id:
            QMessageBox.information(self, u"错误", u"请输入教师号!", QMessageBox.Ok)
        else:
            judge = drop_courses_operation(self.id_, cour_id, tea_id, self.conn)
            if not judge:
                QMessageBox.information(self, u"错误", u"请检查课程号与教师号", QMessageBox.Ok)
            else:
                self.set_selected_view()
                self.set_could_select_view()

    @pyqtSlot()
    def on_refresh_button_clicked(self):
        self.set_view()

    def get_conn(self, id_, conn):
        self.conn = conn
        self.id_ = id_

    def conn_signal_slot(self):
        QtCore.QObject.connect(self.select_courses_button, QtCore.SIGNAL("clicked()"),
                               self.on_select_courses_button_clicked)
        QtCore.QObject.connect(self.drop_courses_button, QtCore.SIGNAL("clicked()"),
                               self.on_drop_courses_button_clicked)
        QtCore.QObject.connect(self.refresh_button,QtCore.SIGNAL("clicked()"),
                               self.on_refresh_button_clicked)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    s = select_courses()
    s.show()

    sys.exit(app.exec_())
