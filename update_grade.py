#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt4.QtGui import QDialog, QMessageBox, QApplication, QTableWidgetItem, QAbstractItemView
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from Ui_update_grade import Ui_update_dialog
from database_operations import get_teacher_courses, get_studied_the_courses_stu_info_2, get_no_grade_stu_info
from database_operations import update_grade, get_the_courses_stu_name


class UpdateGrade(QDialog, Ui_update_dialog):
    """

    """
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.conn = ''
        self.id_ = ''
        self.cour_id = []
        self.conn_signal_slot()
        self.studied_stu_info = ''
        self.no_grade_stu_info = ''
        self.cour_name = []
        self.has_grade_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.no_grade_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.conn_signal_slot()

    def set_init_view(self):
        courses_tuple = get_teacher_courses(self.id_, self.conn)
        for item in courses_tuple:
            self.choose_courses_combo.addItem(item[0])
            self.cour_id.append(item[1])
            self.cour_name.append(item[0])
        self.set_table_widget_view(0)
        stu_tuple = get_the_courses_stu_name(self.id_, self.cour_id[0], self.conn)
        self.stu_name_combo.clear()
        for item in stu_tuple:
            self.stu_name_combo.addItem(item[1])

    def set_table_widget_view(self, cour):
            cour_id = self.set_stu_combo_view(cour)
            stu_tuple = get_the_courses_stu_name(self.id_, cour_id, self.conn)
            self.stu_name_combo.clear()
            for item in stu_tuple:
                self.stu_name_combo.addItem(item[1])

    def set_stu_combo_view(self, cour):
        if len(self.cour_id) != 0:
            cour_id = self.cour_id[cour]
            self.studied_stu_info = get_studied_the_courses_stu_info_2(self.id_, cour_id, self.conn)
            self.has_grade_tableWidget.setRowCount(len(self.studied_stu_info))
            for i, item_tuple in enumerate(self.studied_stu_info):
                for j, item in enumerate(item_tuple):
                    new_item = QTableWidgetItem(unicode(item))
                    self.has_grade_tableWidget.setItem(i, j, new_item)

            self.no_grade_stu_info = get_no_grade_stu_info(self.id_, cour_id, self.conn)
            self.no_grade_tableWidget.setRowCount(len(self.no_grade_stu_info))
            for i, item_tuple in enumerate(self.no_grade_stu_info):
                for j, item in enumerate(item_tuple):
                    new_item = QTableWidgetItem(unicode(item))
                    self.no_grade_tableWidget.setItem(i, j, new_item)
            return cour_id

    def get_info(self, id_, conn):
        self.id_ = id_
        self.conn = conn

    @pyqtSlot()
    def on_update_button_clicked(self):
        regular_grade = self.regular_grade_lineedit.text().toUtf8()
        exam_grade = self.exam_grade_lineedit.text().toUtf8()
        cour_name = self.choose_courses_combo.currentText().toUtf8()
        stu_name = self.stu_name_combo.currentText().toUtf8()
        total_grade = (int(regular_grade) + int(exam_grade)) / 2
        if regular_grade:
            if exam_grade:
                update_grade(regular_grade, exam_grade, cour_name, stu_name, total_grade, self.conn)
                index = self.choose_courses_combo.currentIndex()
                self.set_stu_combo_view(index)
            else:
                QMessageBox.information(self, u"错误", u"请输入考试成绩",QMessageBox.Ok)
        else:
            QMessageBox.information(self, u"错误", u"请输入平时成绩",QMessageBox.Ok)


    def conn_signal_slot(self):
            QtCore.QObject.connect(self.update_grade_button, QtCore.SIGNAL("clicked()"),
                                   self.on_update_button_clicked)
            QtCore.QObject.connect(self.choose_courses_combo, QtCore.SIGNAL("currentIndexChanged(int)"),
                                   self.set_table_widget_view)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    u = UpdateGrade()
    u.show()

    sys.exit(app.exec_())
