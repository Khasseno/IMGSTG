# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IMGSTG_WELCOME.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(669, 464)
        font = QFont()
        font.setFamilies([u"LPM PuffPuff"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(4,2,65,1), stop: 0.427447 rgba(3,22,100,1), stop: 1 rgba(0, 0, 0, 255));\n"
"font-family: LPM PuffPuff;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.b_vnedrenie = QPushButton(self.centralwidget)
        self.b_vnedrenie.setObjectName(u"b_vnedrenie")
        self.b_vnedrenie.setGeometry(QRect(80, 200, 241, 71))
        self.b_vnedrenie.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 17px;")
        self.b_izvlechenie = QPushButton(self.centralwidget)
        self.b_izvlechenie.setObjectName(u"b_izvlechenie")
        self.b_izvlechenie.setGeometry(QRect(350, 200, 241, 71))
        self.b_izvlechenie.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 17px;")
        self.l_welcome = QLabel(self.centralwidget)
        self.l_welcome.setObjectName(u"l_welcome")
        self.l_welcome.setGeometry(QRect(70, 60, 511, 51))
        self.l_welcome.setFont(font)
        self.l_welcome.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 25px;\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IMGSTG", None))
        self.b_vnedrenie.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041d\u0415\u0414\u0420\u0415\u041d\u0418\u0415", None))
        self.b_izvlechenie.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0417\u0412\u041b\u0415\u0427\u0415\u041d\u0418\u0415", None))
        self.l_welcome.setText(QCoreApplication.translate("MainWindow", u"  \u0414\u041e\u0411\u0420\u041e \u041f\u041e\u0416\u0410\u041b\u041e\u0412\u0410\u0422\u042c \u0412 IMGSTG!", None))
    # retranslateUi

