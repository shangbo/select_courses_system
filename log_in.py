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
        conn = login(str(id_), str(password))
        if not conn:
            QMessageBox.information(self, u'登录失败', u'请检查你的学号和密码是否正确!\n', QMessageBox.Ok, QMessageBox.Ok)
        else:
            username = get_login_info(conn)
            if len(username) == 1:
                QMessageBox.information(self, u'登录成功', u'欢迎你!\n'+unicode(username[0][0]), QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, u'错误', u'数据库内部错误', QMessageBox.Ok, QMessageBox.Ok)

    def connect_signal_slot(self):
        QtCore.QObject.connect(self.login_button, QtCore.SIGNAL("clicked()"), self.on_login_button_clicked)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    x = login_dlg()
    x.show()
    sys.exit(app.exec_())