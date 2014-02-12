# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_courses.ui'
#
# Created: Sat Feb  8 11:40:22 2014
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

class Ui_search_courses(object):
    def setupUi(self, search_courses):
        search_courses.setObjectName(_fromUtf8("search_courses"))
        search_courses.resize(816, 499)
        self.layoutWidget = QtGui.QWidget(search_courses)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 701, 421))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.main_layout = QtGui.QGridLayout(self.layoutWidget)
        self.main_layout.setMargin(0)
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.search_layout = QtGui.QGridLayout()
        self.search_layout.setObjectName(_fromUtf8("search_layout"))
        self.search_button = QtGui.QPushButton(self.layoutWidget)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.search_layout.addWidget(self.search_button, 1, 0, 1, 1)
        self.reset_button = QtGui.QPushButton(self.layoutWidget)
        self.reset_button.setObjectName(_fromUtf8("reset_button"))
        self.search_layout.addWidget(self.reset_button, 1, 1, 1, 1)
        self.lineedit_layout = QtGui.QGridLayout()
        self.lineedit_layout.setObjectName(_fromUtf8("lineedit_layout"))
        self.courses_id_label = QtGui.QLabel(self.layoutWidget)
        self.courses_id_label.setObjectName(_fromUtf8("courses_id_label"))
        self.lineedit_layout.addWidget(self.courses_id_label, 0, 0, 1, 1)
        self.courses_name_lineedit = QtGui.QLineEdit(self.layoutWidget)
        self.courses_name_lineedit.setObjectName(_fromUtf8("courses_name_lineedit"))
        self.lineedit_layout.addWidget(self.courses_name_lineedit, 0, 3, 1, 1)
        self.tea_name_label = QtGui.QLabel(self.layoutWidget)
        self.tea_name_label.setObjectName(_fromUtf8("tea_name_label"))
        self.lineedit_layout.addWidget(self.tea_name_label, 1, 2, 1, 1)
        self.courses_id_lineedit = QtGui.QLineEdit(self.layoutWidget)
        self.courses_id_lineedit.setObjectName(_fromUtf8("courses_id_lineedit"))
        self.lineedit_layout.addWidget(self.courses_id_lineedit, 0, 1, 1, 1)
        self.courses_name_label = QtGui.QLabel(self.layoutWidget)
        self.courses_name_label.setObjectName(_fromUtf8("courses_name_label"))
        self.lineedit_layout.addWidget(self.courses_name_label, 0, 2, 1, 1)
        self.tea_id_label = QtGui.QLabel(self.layoutWidget)
        self.tea_id_label.setObjectName(_fromUtf8("tea_id_label"))
        self.lineedit_layout.addWidget(self.tea_id_label, 1, 0, 1, 1)
        self.tea_id_lineedit = QtGui.QLineEdit(self.layoutWidget)
        self.tea_id_lineedit.setObjectName(_fromUtf8("tea_id_lineedit"))
        self.lineedit_layout.addWidget(self.tea_id_lineedit, 1, 1, 1, 1)
        self.work_time_lineedit = QtGui.QLineEdit(self.layoutWidget)
        self.work_time_lineedit.setObjectName(_fromUtf8("work_time_lineedit"))
        self.lineedit_layout.addWidget(self.work_time_lineedit, 0, 5, 1, 1)
        self.work_time_label = QtGui.QLabel(self.layoutWidget)
        self.work_time_label.setObjectName(_fromUtf8("work_time_label"))
        self.lineedit_layout.addWidget(self.work_time_label, 0, 4, 1, 1)
        self.tea_name_lineedit = QtGui.QLineEdit(self.layoutWidget)
        self.tea_name_lineedit.setObjectName(_fromUtf8("tea_name_lineedit"))
        self.lineedit_layout.addWidget(self.tea_name_lineedit, 1, 3, 1, 1)
        self.credit_label = QtGui.QLabel(self.layoutWidget)
        self.credit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.credit_label.setObjectName(_fromUtf8("credit_label"))
        self.lineedit_layout.addWidget(self.credit_label, 1, 4, 1, 1)
        self.credit_lineedit = QtGui.QLineEdit(self.layoutWidget)
        self.credit_lineedit.setObjectName(_fromUtf8("credit_lineedit"))
        self.lineedit_layout.addWidget(self.credit_lineedit, 1, 5, 1, 1)
        self.search_layout.addLayout(self.lineedit_layout, 0, 0, 1, 2)
        self.main_layout.addLayout(self.search_layout, 0, 0, 1, 1)
        self.display_table_widget = QtGui.QTableWidget(self.layoutWidget)
        self.display_table_widget.setObjectName(_fromUtf8("display_table_widget"))
        self.display_table_widget.setColumnCount(7)
        self.display_table_widget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.display_table_widget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.display_table_widget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.display_table_widget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.display_table_widget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.display_table_widget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.display_table_widget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.display_table_widget.setHorizontalHeaderItem(6, item)
        self.main_layout.addWidget(self.display_table_widget, 1, 0, 1, 1)

        self.retranslateUi(search_courses)
        # QtCore.QMetaObject.connectSlotsByName(search_courses)

    def retranslateUi(self, search_courses):
        search_courses.setWindowTitle(_translate("search_courses", "查询课程", None))
        self.search_button.setText(_translate("search_courses", "查询", None))
        self.reset_button.setText(_translate("search_courses", "重置", None))
        self.courses_id_label.setText(_translate("search_courses", "课程号", None))
        self.tea_name_label.setText(_translate("search_courses", "教师姓名", None))
        self.courses_name_label.setText(_translate("search_courses", "课程名称", None))
        self.tea_id_label.setText(_translate("search_courses", "教师号", None))
        self.work_time_label.setText(_translate("search_courses", "上课时间", None))
        self.credit_label.setText(_translate("search_courses", "学分", None))
        item = self.display_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("search_courses", "课程号", None))
        item = self.display_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("search_courses", "课程名", None))
        item = self.display_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("search_courses", "学分", None))
        item = self.display_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("search_courses", "教师号", None))
        item = self.display_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("search_courses", "教师名", None))
        item = self.display_table_widget.horizontalHeaderItem(5)
        item.setText(_translate("search_courses", "学期", None))
        item = self.display_table_widget.horizontalHeaderItem(6)
        item.setText(_translate("search_courses", "上课时间 ", None))

