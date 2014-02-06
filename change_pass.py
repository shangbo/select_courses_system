#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from PyQt4.QtGui import QDialog, QApplication, QMessageBox
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from Ui_change_pass import Ui_change_pass_dialog
from database_operations import change_password, logout
class change_pass_dlg(QDialog, Ui_change_pass_dialog):
    """

    """

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.old_pass = ""
        self.conn = ''
        self.setupUi(self)
        self.set_signal_slot()
    @pyqtSlot()
    def on_change_pass_button_clicked(self):
        old_pass = self.old_pass_lineedit.text()
        new_pass = self.new_pass_lineedit.text()
        repeat_new_pass = self.repeat_lineedit.text()

        if not old_pass:
            QMessageBox.information(self, u"错误", u"请输入旧密码", QMessageBox.Ok, QMessageBox.Ok)
        elif not new_pass:
            QMessageBox.information(self, u"错误", u"请输入新密码", QMessageBox.Ok, QMessageBox.Ok)
        elif not repeat_new_pass:
            QMessageBox.information(self, u"错误", u"请输入重复密码", QMessageBox.Ok, QMessageBox.Ok)
        elif repeat_new_pass != new_pass:
            QMessageBox.information(self, u"错误", u"重复输入密码不一致", QMessageBox.Ok, QMessageBox.Ok)
        elif old_pass != self.old_pass:
            QMessageBox.information(self, u"错误", u"旧密码不正确,请重新输入", QMessageBox.Ok, QMessageBox.Ok)
        else:
            change_password(new_pass, self.conn)
            reply = QMessageBox.information(self, u"成功",u"密码修改成功\n点击ok重新登录", QMessageBox.Ok, QMessageBox.Ok )
            if reply == QMessageBox.Ok:
                QtCore.QCoreApplication.instance().quit()
                logout(self.conn)
    def set_info(self, password, conn):
        self.old_pass = password
        self.conn = conn
    def set_signal_slot(self):
        QtCore.QObject.connect(self.change_button, QtCore.SIGNAL("clicked()"), self.on_change_pass_button_clicked)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    dlg = change_pass_dlg()
    dlg.show()

    sys.exit(app.exec_())
