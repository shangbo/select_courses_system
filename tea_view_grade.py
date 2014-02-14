#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt4.QtGui import QDialog, QApplication, QMessageBox, QAbstractItemView, QTableWidgetItem
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from database_operations import get_teacher_courses, get_studied_the_courses_stu_info
from Ui_tea_view_grade import Ui_tea_view_grade


class TeaViewGrade(QDialog, Ui_tea_view_grade):
    """

    """
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.id_ = ""
        self.conn = ""
        self.username = ""
        self.cour_id = []
        self.grade_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.conn_signal_slot()

    def set_init_view(self):
        self.tea_name_show_label.setText(self.username)
        self.courses_show_label.setText("")
        courses_tuple = get_teacher_courses(self.id_, self.conn)
        # QMessageBox.information(self,"e",unicode(courses_tuple),QMessageBox.Ok)
        for item in courses_tuple:
            self.courses_name_show_combobox.addItem(item[0])
            self.cour_id.append(item[1])

    @pyqtSlot()
    def on_view_button_clicked(self):
        cour_id = self.courses_name_show_combobox.currentIndex()
        stu_info = get_studied_the_courses_stu_info(self.id_, self.cour_id[cour_id], self.conn)
        # QMessageBox.information(self, "s", unicode(stu_info), QMessageBox.Ok)
        self.grade_tableWidget.setRowCount(len(stu_info))
        for i, item_tuple in enumerate(stu_info):
            for j, item in enumerate(item_tuple):
                new_item = QTableWidgetItem(unicode(item))
                self.grade_tableWidget.setItem(i, j, new_item)

    def get_info(self, id_, username, conn):
        self.id_ = id_
        self.username = username
        self.conn = conn

    def conn_signal_slot(self):
        QtCore.QObject.connect(self.courses_name_show_combobox, QtCore.SIGNAL("currentIndexChanged(QString)"),
                               self.courses_show_label.setText)
        QtCore.QObject.connect(self.view_button,QtCore.SIGNAL("clicked()"),
                               self.on_view_button_clicked)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    t = TeaViewGrade()
    t.show()
    sys.exit(app.exec_())
