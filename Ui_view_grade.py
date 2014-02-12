# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_grade.ui'
#
# Created: Tue Feb 11 12:26:25 2014
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

class Ui_view_grade(object):
    def setupUi(self, view_grade):
        view_grade.setObjectName(_fromUtf8("view_grade"))
        view_grade.resize(612, 412)
        self.grade_widget = QtGui.QTableWidget(view_grade)
        self.grade_widget.setGeometry(QtCore.QRect(50, 20, 501, 261))
        self.grade_widget.setObjectName(_fromUtf8("grade_widget"))
        self.grade_widget.setColumnCount(5)
        self.grade_widget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.grade_widget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.grade_widget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.grade_widget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.grade_widget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.grade_widget.setHorizontalHeaderItem(4, item)
        self.widget = QtGui.QWidget(view_grade)
        self.widget.setGeometry(QtCore.QRect(150, 330, 261, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.grade_label = QtGui.QLabel(self.widget)
        self.grade_label.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_label.setObjectName(_fromUtf8("grade_label"))
        self.horizontalLayout.addWidget(self.grade_label)
        self.avg_grade_label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.avg_grade_label.setFont(font)
        self.avg_grade_label.setAlignment(QtCore.Qt.AlignCenter)
        self.avg_grade_label.setObjectName(_fromUtf8("avg_grade_label"))
        self.horizontalLayout.addWidget(self.avg_grade_label)

        self.retranslateUi(view_grade)
        # QtCore.QMetaObject.connectSlotsByName(view_grade)

    def retranslateUi(self, view_grade):
        view_grade.setWindowTitle(_translate("view_grade", "Dialog", None))
        item = self.grade_widget.horizontalHeaderItem(0)
        item.setText(_translate("view_grade", "课程号", None))
        item = self.grade_widget.horizontalHeaderItem(1)
        item.setText(_translate("view_grade", "课程名", None))
        item = self.grade_widget.horizontalHeaderItem(2)
        item.setText(_translate("view_grade", "新建列", None))
        item = self.grade_widget.horizontalHeaderItem(3)
        item.setText(_translate("view_grade", "学分", None))
        item = self.grade_widget.horizontalHeaderItem(4)
        item.setText(_translate("view_grade", "总成绩", None))
        self.grade_label.setText(_translate("view_grade", "平均成绩:", None))
        self.avg_grade_label.setText(_translate("view_grade", "Default", None))

