# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(351, 618)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(242, 178, 55, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(25, 42, 50, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit_1 = QTextEdit(self.centralwidget)
        self.textEdit_1.setObjectName(u"textEdit_1")
        font = QFont()
        font.setFamilies([u"SG Kara SemiBold"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.textEdit_1.setFont(font)
        self.textEdit_1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"SG Kara SemiBold\";")

        self.gridLayout.addWidget(self.textEdit_1, 0, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(111)
        sizePolicy1.setVerticalStretch(111)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setMinimumSize(QSize(111, 111))
        self.btn_1.setMaximumSize(QSize(333, 333))
        font1 = QFont()
        font1.setFamilies([u"Segoe Script"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_1.setFont(font1)
        self.btn_1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"font: 700 12pt \"Segoe Script\";\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_1, 4, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"SG Kara SemiBold\";")

        self.gridLayout.addWidget(self.textEdit_2, 1, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setMinimumSize(QSize(111, 111))
        self.btn_2.setMaximumSize(QSize(333, 333))
        self.btn_2.setFont(font1)
        self.btn_2.setStyleSheet(u"QPushButton{\n"
"	font: 700 12pt \"Segoe Script\";\n"
"	background-color: rgb(255, 170, 255)\n"
"}")

        self.gridLayout.addWidget(self.btn_2, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main Window", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"new session", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"line break removal Now", None))
    # retranslateUi

