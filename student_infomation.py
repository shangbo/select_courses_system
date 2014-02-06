#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from PyQt4.QtGui import QDialog, QApplication, QMessageBox
from Ui_student_infomation import Ui_stu_info
from database_operations import get_student_info
# gobal
HTML = u"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
    <meta name="qrichtext" content="1" />
    <style type="text/css">
        p, li { white-space: pre-wrap; }
    </style>
</head>
<body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">姓名:  </span><span style=" font-size:14pt; font-weight:600;"></span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;"> </span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">学号:  </span><span style=" font-size:14pt; font-weight:600;"></span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">性别:  </span><span style=" font-size:14pt; font-weight:600;"></span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">生日:  </span><span style=" font-size:14pt; font-weight:600;"></span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">籍贯:  </span><span style=" font-size:14pt; font-weight:600;"></span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">电话:  </span><span style=" font-size:14pt; font-weight:600;"></span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">学院:  </span><span style=" font-size:14pt; font-weight:600;"></span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;"><br /></p></body></html>"""

class stu_info(QDialog, Ui_stu_info):
    """

    """
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
    def set_html(self, id_, conn):
        info = get_student_info(conn,id_)
        position = 0
        i = 0
        while position != -1:
            try:
                position = HTML.find(u"""</span><span style=" font-size:14pt; font-weight:600;"></span></p>""")
                global HTML
                HTML = HTML[:position+55] + unicode(info[0][i]) + HTML[position+55:]
                # QMessageBox.information(self, u"dsa", str(type(info)), QMessageBox.Ok, QMessageBox.Ok)
                i += 1
            except IndexError:
                position = -1
        self.textBrowser.setHtml(HTML)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    s = stu_info()
    s.show()
    sys.exit(app.exec_())
