# -*- coding: utf-8 -*-

"""
Module implementing login_dlg.
"""
import  sys
from PyQt4.QtGui import QDialog, QMessageBox, QApplication
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtCore
from Ui_log_in import Ui_login_dlg

from database_operations import login, get_login_info

class login_dlg(QDialog, Ui_login_dlg):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.connect_signal_slot()
    @pyqtSlot()
    def on_login_button_clicked(self):
        """
        Slot documentation goes here.
        """
        password = self.lineedit_pass.text().toUtf8()
        id_ = self.lineedit_user.text()
        tea_status = self.radio_teacher.isChecked()
        stu_status = self.radio_student.isChecked()
        conn = login(str(id_), str(password))
        if not id_:
            QMessageBox.information(self, u'登录失败', u'请输入学号(工号)\n', QMessageBox.Ok, QMessageBox.Ok)
        elif not password:
            QMessageBox.information(self, u'登录失败', u'请输入密码\n', QMessageBox.Ok, QMessageBox.Ok)
        elif not (tea_status or stu_status):
            QMessageBox.information(self, u'登录失败', u'请选择身份\n', QMessageBox.Ok, QMessageBox.Ok)
        elif not conn:
            QMessageBox.information(self, u'登录失败', u'请检查你的学号(工号)和密码或者身份是否正确!\n', QMessageBox.Ok, QMessageBox.Ok)
        else:
            username = get_login_info(conn, id_,stu_status)
            if len(username) == 1:
                if tea_status:
                    QMessageBox.information(self, u'登录成功', u'欢迎你!\n'+unicode(username[0][0])+u' 老师', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.information(self, u'登录成功', u'欢迎你!\n'+unicode(username[0][0])+u' 同学', QMessageBox.Ok, QMessageBox.Ok)
            elif len(username) == 0:
                QMessageBox.information(self, u'登录失败', u'请检查你的学号(工号)和密码或者身份是否正确!\n', QMessageBox.Ok, QMessageBox.Ok)
    def connect_signal_slot(self):
        QtCore.QObject.connect(self.login_button, QtCore.SIGNAL("clicked()"), self.on_login_button_clicked)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    x = login_dlg()
    x.show()
    sys.exit(app.exec_())