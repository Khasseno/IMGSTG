# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adding_information.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_Adding(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(680, 449)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(4,2,65,1), stop: 0.427447 rgba(3,22,100,1), stop: 1 rgba(0, 0, 0, 255));\n"
"font-family: LPM PuffPuff;")
        self.l_title = QLabel(Dialog)
        self.l_title.setObjectName(u"l_title")
        self.l_title.setGeometry(QRect(40, 10, 611, 41))
        self.l_title.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 21px;\n"
"\n"
"")
        self.b_add_img = QPushButton(Dialog)
        self.b_add_img.setObjectName(u"b_add_img")
        self.b_add_img.setGeometry(QRect(20, 60, 201, 31))
        self.b_add_img.setCursor(QCursor(Qt.ArrowCursor))
        self.b_add_img.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 12px;")
        self.l_image_add = QLabel(Dialog)
        self.l_image_add.setObjectName(u"l_image_add")
        self.l_image_add.setGeometry(QRect(20, 100, 201, 301))
        self.l_image_add.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 2px solid rgba(255,255,255,60);")
        self.text = QPlainTextEdit(Dialog)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(240, 100, 201, 261))
        self.text.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 2px solid rgba(255,255,255,60);\n"
"font-family: Times New Roman;\n"
"color: white;\n"
"font-size: 14px;")
        self.text.setFrameShadow(QFrame.Sunken)
        self.b_add_data = QPushButton(Dialog)
        self.b_add_data.setObjectName(u"b_add_data")
        self.b_add_data.setGeometry(QRect(240, 370, 201, 31))
        self.b_add_data.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 12px;")
        self.b_save = QPushButton(Dialog)
        self.b_save.setObjectName(u"b_save")
        self.b_save.setGeometry(QRect(460, 370, 201, 31))
        self.b_save.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 12px;")
        self.l_image_save = QLabel(Dialog)
        self.l_image_save.setObjectName(u"l_image_save")
        self.l_image_save.setGeometry(QRect(460, 60, 201, 301))
        self.l_image_save.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 2px solid rgba(255,255,255,60);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.l_title.setText(QCoreApplication.translate("Dialog", u"\u0412\u041d\u0415\u0414\u0420\u0415\u041d\u0418\u0415 \u0418\u041d\u0424\u041e\u0420\u041c\u0410\u0426\u0418\u0418 \u0412 \u0418\u0417\u041e\u0411\u0420\u0410\u0416\u0415\u041d\u0418\u0415", None))
        self.b_add_img.setText(QCoreApplication.translate("Dialog", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u0418\u0417\u041e\u0411\u0420\u0410\u0416\u0415\u041d\u0418\u0415", None))
        self.l_image_add.setText("")
        self.text.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f ", None))
        self.b_add_data.setText(QCoreApplication.translate("Dialog", u"\u0412\u041d\u0415\u0414\u0420\u0418\u0422\u042c", None))
        self.b_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
        self.l_image_save.setText("")
    # retranslateUi

