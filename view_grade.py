#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PyQt4.QtGui import QDialog, QMessageBox, QApplication, QTableWidgetItem, QAbstractItemView
from Ui_view_grade import Ui_view_grade
from database_operations import get_studied_courses_info


class view_grade(QDialog, Ui_view_grade):
    """

    """
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.id_ = ''
        self.conn = ''
        self.total_grade = 0
        self.avg_grade = 0
        self.setupUi(self)
        self.grade_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def set_view(self):
        studied_info = get_studied_courses_info(self.id_, self.conn)
        self.grade_widget.setRowCount(len(studied_info))
        for i, item_tuple in enumerate(studied_info):
            for j, item in enumerate(item_tuple):
                if j == 4:
                    self.total_grade = self.total_grade + item
                new_item = QTableWidgetItem(unicode(item))
                self.grade_widget.setItem(i, j, new_item)
        self.avg_grade = self.total_grade/len(studied_info)
        self.avg_grade_label.setText(str(self.avg_grade))

    def get_info(self, id_, conn):
        self.id_ = id_
        self.conn = conn

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    v = view_grade()
    v.show()
    sys.exit(app.exec_())
