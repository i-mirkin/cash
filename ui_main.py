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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTableView, QTextBrowser, QTextEdit,
    QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(732, 613)
        MainWindow.setStyleSheet(u"background-color: #eee;\n"
"\n"
"QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  33px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"    background-color:  red;\n"
"    color:  red;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  red;\n"
"}\n"
"\n"
"QTabWidget {\n"
"    color: red;\n"
"	background-color: red;\n"
"}\n"
"QHeaderView {\n"
"    color: blue;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"	color: black;\n"
"	background: white;\n"
"}\n"
"QTabBar::tab:selected{\n"
"	color: white;\n"
"	background: gray;\n"
"}\n"
"\n"
"QTableView{\n"
"	color: blue;\n"
"}\n"
"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 311, 36))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(13, 10, 285, 16))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 50, 713, 381))
        font = QFont()
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"color: black;")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tab_start = QWidget()
        self.tab_start.setObjectName(u"tab_start")
        self.tab_start.setStyleSheet(u"")
        self.textEdit = QTextEdit(self.tab_start)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 690, 260))
        self.tabWidget.addTab(self.tab_start, "")
        self.tab_persons = QWidget()
        self.tab_persons.setObjectName(u"tab_persons")
        self.tablePerson = QTableView(self.tab_persons)
        self.tablePerson.setObjectName(u"tablePerson")
        self.tablePerson.setGeometry(QRect(10, 10, 690, 260))
        self.tablePerson.setAutoFillBackground(True)
        self.tablePerson.setStyleSheet(u"background-color: white;")
        self.frame_add_person = QFrame(self.tab_persons)
        self.frame_add_person.setObjectName(u"frame_add_person")
        self.frame_add_person.setGeometry(QRect(10, 290, 691, 51))
        self.frame_add_person.setStyleSheet(u"background-color: white;")
        self.frame_add_person.setFrameShape(QFrame.StyledPanel)
        self.frame_add_person.setFrameShadow(QFrame.Raised)
        self.textEditPersonId = QTextEdit(self.frame_add_person)
        self.textEditPersonId.setObjectName(u"textEditPersonId")
        self.textEditPersonId.setEnabled(False)
        self.textEditPersonId.setGeometry(QRect(8, 10, 81, 32))
        self.textEditPersonName = QTextEdit(self.frame_add_person)
        self.textEditPersonName.setObjectName(u"textEditPersonName")
        self.textEditPersonName.setGeometry(QRect(95, 10, 100, 32))
        self.textEditPersonDescription = QTextEdit(self.frame_add_person)
        self.textEditPersonDescription.setObjectName(u"textEditPersonDescription")
        self.textEditPersonDescription.setGeometry(QRect(201, 10, 100, 32))
        self.textEditPersonDescription.setStyleSheet(u"border-bottom: 1px solid #888;")
        self.textEditPersonActive = QTextEdit(self.frame_add_person)
        self.textEditPersonActive.setObjectName(u"textEditPersonActive")
        self.textEditPersonActive.setEnabled(False)
        self.textEditPersonActive.setGeometry(QRect(306, 10, 100, 32))
        self.textEditPersonCreatedAt = QTextEdit(self.frame_add_person)
        self.textEditPersonCreatedAt.setObjectName(u"textEditPersonCreatedAt")
        self.textEditPersonCreatedAt.setEnabled(False)
        self.textEditPersonCreatedAt.setGeometry(QRect(412, 10, 100, 32))
        self.textEditPersonUpdatedAt = QTextEdit(self.frame_add_person)
        self.textEditPersonUpdatedAt.setObjectName(u"textEditPersonUpdatedAt")
        self.textEditPersonUpdatedAt.setEnabled(False)
        self.textEditPersonUpdatedAt.setGeometry(QRect(517, 10, 100, 32))
        self.pushButtonPerson = QPushButton(self.frame_add_person)
        self.pushButtonPerson.setObjectName(u"pushButtonPerson")
        self.pushButtonPerson.setGeometry(QRect(630, 10, 51, 32))
        self.tabWidget.addTab(self.tab_persons, "")
        self.tab_contractors = QWidget()
        self.tab_contractors.setObjectName(u"tab_contractors")
        self.tableContractor = QTableView(self.tab_contractors)
        self.tableContractor.setObjectName(u"tableContractor")
        self.tableContractor.setGeometry(QRect(10, 10, 690, 260))
        self.tableContractor.setStyleSheet(u"background-color: white;")
        self.frame_add_contractor = QFrame(self.tab_contractors)
        self.frame_add_contractor.setObjectName(u"frame_add_contractor")
        self.frame_add_contractor.setGeometry(QRect(10, 290, 691, 51))
        self.frame_add_contractor.setStyleSheet(u"background-color: white;")
        self.frame_add_contractor.setFrameShape(QFrame.StyledPanel)
        self.frame_add_contractor.setFrameShadow(QFrame.Raised)
        self.textEditContractorId = QTextEdit(self.frame_add_contractor)
        self.textEditContractorId.setObjectName(u"textEditContractorId")
        self.textEditContractorId.setEnabled(False)
        self.textEditContractorId.setGeometry(QRect(8, 10, 81, 32))
        self.textEditContractorName = QTextEdit(self.frame_add_contractor)
        self.textEditContractorName.setObjectName(u"textEditContractorName")
        self.textEditContractorName.setGeometry(QRect(95, 10, 100, 32))
        self.textEditContractorDescription = QTextEdit(self.frame_add_contractor)
        self.textEditContractorDescription.setObjectName(u"textEditContractorDescription")
        self.textEditContractorDescription.setGeometry(QRect(201, 10, 100, 32))
        self.textEditContractorDescription.setStyleSheet(u"border-bottom: 1px solid #888;")
        self.textEditContractorActive = QTextEdit(self.frame_add_contractor)
        self.textEditContractorActive.setObjectName(u"textEditContractorActive")
        self.textEditContractorActive.setEnabled(False)
        self.textEditContractorActive.setGeometry(QRect(306, 10, 100, 32))
        self.textEditContractorCreatedAt = QTextEdit(self.frame_add_contractor)
        self.textEditContractorCreatedAt.setObjectName(u"textEditContractorCreatedAt")
        self.textEditContractorCreatedAt.setEnabled(False)
        self.textEditContractorCreatedAt.setGeometry(QRect(412, 10, 100, 32))
        self.textEditContractorUpdatedAt = QTextEdit(self.frame_add_contractor)
        self.textEditContractorUpdatedAt.setObjectName(u"textEditContractorUpdatedAt")
        self.textEditContractorUpdatedAt.setEnabled(False)
        self.textEditContractorUpdatedAt.setGeometry(QRect(517, 10, 100, 32))
        self.pushButtonContractor = QPushButton(self.frame_add_contractor)
        self.pushButtonContractor.setObjectName(u"pushButtonContractor")
        self.pushButtonContractor.setGeometry(QRect(630, 10, 51, 32))
        self.tabWidget.addTab(self.tab_contractors, "")
        self.tab_cash = QWidget()
        self.tab_cash.setObjectName(u"tab_cash")
        self.tableCash = QTableView(self.tab_cash)
        self.tableCash.setObjectName(u"tableCash")
        self.tableCash.setGeometry(QRect(10, 10, 690, 260))
        self.tableCash.setStyleSheet(u"background-color: white;")
        self.frame_add_contractor_2 = QFrame(self.tab_cash)
        self.frame_add_contractor_2.setObjectName(u"frame_add_contractor_2")
        self.frame_add_contractor_2.setGeometry(QRect(10, 280, 691, 51))
        self.frame_add_contractor_2.setStyleSheet(u"background-color: white;")
        self.frame_add_contractor_2.setFrameShape(QFrame.StyledPanel)
        self.frame_add_contractor_2.setFrameShadow(QFrame.Raised)
        self.textEditCashDate = QTextEdit(self.frame_add_contractor_2)
        self.textEditCashDate.setObjectName(u"textEditCashDate")
        self.textEditCashDate.setGeometry(QRect(201, 10, 100, 32))
        self.textEditCashDate.setStyleSheet(u"border-bottom: 1px solid #888;")
        self.textEditCashSum = QTextEdit(self.frame_add_contractor_2)
        self.textEditCashSum.setObjectName(u"textEditCashSum")
        self.textEditCashSum.setEnabled(False)
        self.textEditCashSum.setGeometry(QRect(306, 10, 100, 32))
        self.textEditCashDescription = QTextEdit(self.frame_add_contractor_2)
        self.textEditCashDescription.setObjectName(u"textEditCashDescription")
        self.textEditCashDescription.setEnabled(False)
        self.textEditCashDescription.setGeometry(QRect(412, 10, 100, 32))
        self.pushButtonCash = QPushButton(self.frame_add_contractor_2)
        self.pushButtonCash.setObjectName(u"pushButtonCash")
        self.pushButtonCash.setGeometry(QRect(630, 10, 51, 32))
        self.comboBoxCashGiver = QComboBox(self.frame_add_contractor_2)
        self.comboBoxCashGiver.setObjectName(u"comboBoxCashGiver")
        self.comboBoxCashGiver.setGeometry(QRect(10, 10, 90, 32))
        self.comboBoxCashReceiver = QComboBox(self.frame_add_contractor_2)
        self.comboBoxCashReceiver.setObjectName(u"comboBoxCashReceiver")
        self.comboBoxCashReceiver.setGeometry(QRect(106, 10, 90, 32))
        self.tabWidget.addTab(self.tab_cash, "")
        self.tab_swap = QWidget()
        self.tab_swap.setObjectName(u"tab_swap")
        self.tableSwap = QTableView(self.tab_swap)
        self.tableSwap.setObjectName(u"tableSwap")
        self.tableSwap.setGeometry(QRect(10, 10, 690, 260))
        self.tableSwap.setStyleSheet(u"background-color: white;")
        self.tabWidget.addTab(self.tab_swap, "")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 450, 711, 151))
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.textBrowser.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0443\u0447\u0435\u0442\u0430 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u0441\u0440\u0435\u0434\u0441\u0442\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_start), QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u0438", None))
        self.textEditPersonId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"person_id", None))
        self.textEditPersonName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"person_name", None))
        self.textEditPersonDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"person_description", None))
        self.textEditPersonActive.setPlaceholderText(QCoreApplication.translate("MainWindow", u"person_active", None))
        self.textEditPersonCreatedAt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"created_at", None))
        self.textEditPersonUpdatedAt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"updated_at", None))
        self.pushButtonPerson.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_persons), QCoreApplication.translate("MainWindow", u"\u0424\u0438\u0437. \u043b\u0438\u0446\u0430", None))
        self.textEditContractorId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contractor_id", None))
        self.textEditContractorName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contractor_name", None))
        self.textEditContractorDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contractor_description", None))
        self.textEditContractorActive.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contractor_active", None))
        self.textEditContractorCreatedAt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"created_at", None))
        self.textEditContractorUpdatedAt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"updated_at", None))
        self.pushButtonContractor.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contractors), QCoreApplication.translate("MainWindow", u"\u042e\u0440. \u043b\u0438\u0446\u0430", None))
        self.textEditCashDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cash_date", None))
        self.textEditCashSum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cash_sum", None))
        self.textEditCashDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cash_description", None))
        self.pushButtonCash.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cash), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_swap), QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0435\u043b\u043a\u0438", None))
    # retranslateUi

