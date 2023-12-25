# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(702, 600)
        MainWindow.setStyleSheet(u"background-color: gray;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.left = QFrame(self.frame)
        self.left.setObjectName(u"left")
        self.left.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);")
        self.verticalLayout = QVBoxLayout(self.left)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.left)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: white;\n"
"padding: 5px 10px;\n"
"text-align: center;")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.left)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: white;\n"
"padding: 5px 10px;\n"
"text-align: center;")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.left)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: white;\n"
"padding: 5px 10px;\n"
"text-align: center;")
        self.label_3.setPixmap(QPixmap(u":/icons/icons/grade_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.left)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: white;\n"
"padding: 5px 10px;\n"
"text-align: center;")

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(self.left)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: white;\n"
"padding: 5px 10px;\n"
"text-align: center;")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.left)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: white;\n"
"padding: 5px 10px;\n"
"text-align: center;")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_6 = QLabel(self.left)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: white;\n"
"padding: 5px 10px;\n"
"text-align: center;")

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_8 = QLabel(self.left)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: white;\n"
"padding: 5px 10px;\n"
"text-align: center;")

        self.verticalLayout.addWidget(self.label_8)


        self.horizontalLayout_7.addWidget(self.left)

        self.right = QFrame(self.frame)
        self.right.setObjectName(u"right")
        self.right.setStyleSheet(u"background-color: red;")
        self.verticalLayout_2 = QVBoxLayout(self.right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(self.right)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.right)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_11 = QLabel(self.right)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_12 = QLabel(self.right)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_13 = QLabel(self.right)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.label_14 = QLabel(self.right)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.label_15 = QLabel(self.right)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_16 = QLabel(self.right)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_5.addWidget(self.label_16)

        self.label_17 = QLabel(self.right)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_5.addWidget(self.label_17)

        self.label_18 = QLabel(self.right)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_5.addWidget(self.label_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_19 = QLabel(self.right)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_6.addWidget(self.label_19)

        self.label_20 = QLabel(self.right)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.label_21 = QLabel(self.right)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_6.addWidget(self.label_21)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addWidget(self.right)


        self.verticalLayout_3.addWidget(self.frame)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons/check_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/radio_button_partial_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/restart_alt_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: white;")

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Balance", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1200 \u0440\u0443\u0431.", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u0445\u043e\u0434", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"12 000 \u0440\u0443\u0431.", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0441\u0445\u043e\u0434", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"12 000 \u0440\u0443\u0431.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f 1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"20 000 \u0440\u0443\u0431.", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f 2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"20 000 \u0440\u0443\u0431.", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f 3", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"20 000 \u0440\u0443\u0431.", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f 4", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"20 000 \u0440\u0443\u0431.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

