# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extracting_information.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog_Extracting(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(698, 449)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(4,2,65,1), stop: 0.427447 rgba(3,22,100,1), stop: 1 rgba(0, 0, 0, 255));\n"
"font-family: LPM PuffPuff;")
        self.l_title = QLabel(Dialog)
        self.l_title.setObjectName(u"l_title")
        self.l_title.setGeometry(QRect(40, 10, 621, 41))
        self.l_title.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 21px;\n"
"\n"
"")
        self.b_extract_data = QPushButton(Dialog)
        self.b_extract_data.setObjectName(u"b_extract_data")
        self.b_extract_data.setGeometry(QRect(250, 210, 201, 31))
        self.b_extract_data.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 12px;")
        self.b_add_img = QPushButton(Dialog)
        self.b_add_img.setObjectName(u"b_add_img")
        self.b_add_img.setGeometry(QRect(30, 60, 201, 31))
        self.b_add_img.setCursor(QCursor(Qt.ArrowCursor))
        self.b_add_img.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 12px;")
        self.l_name_stego = QLabel(Dialog)
        self.l_name_stego.setObjectName(u"l_name_stego")
        self.l_name_stego.setGeometry(QRect(50, 410, 161, 20))
        self.l_name_stego.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 12px;")
        self.l_name_text = QLabel(Dialog)
        self.l_name_text.setObjectName(u"l_name_text")
        self.l_name_text.setGeometry(QRect(490, 410, 161, 20))
        self.l_name_text.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 12px;")
        self.l_data_extract = QLabel(Dialog)
        self.l_data_extract.setObjectName(u"l_data_extract")
        self.l_data_extract.setGeometry(QRect(470, 100, 201, 301))
        self.l_data_extract.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 2px solid rgba(255,255,255,60);")
        self.l_image_add = QLabel(Dialog)
        self.l_image_add.setObjectName(u"l_image_add")
        self.l_image_add.setGeometry(QRect(30, 100, 201, 301))
        self.l_image_add.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 2px solid rgba(255,255,255,60);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.l_title.setText(QCoreApplication.translate("Dialog", u"\u0418\u0417\u0412\u041b\u0415\u0427\u0415\u041d\u0418\u0415 \u0418\u041d\u0424\u041e\u0420\u041c\u0410\u0426\u0418\u0418 \u0418\u0417 \u0418\u0417\u041e\u0411\u0420\u0410\u0416\u0415\u041d\u0418\u042f", None))
        self.b_extract_data.setText(QCoreApplication.translate("Dialog", u"\u0418\u0417\u0412\u041b\u0415\u0427\u042c", None))
        self.b_add_img.setText(QCoreApplication.translate("Dialog", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u0418\u0417\u041e\u0411\u0420\u0410\u0416\u0415\u041d\u0418\u0415", None))
        self.l_name_stego.setText(QCoreApplication.translate("Dialog", u"\u0441\u0442\u0435\u0433\u043e-\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.l_name_text.setText(QCoreApplication.translate("Dialog", u"\u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.l_data_extract.setText("")
        self.l_image_add.setText("")
    # retranslateUi

