# https://github.com/ithobbies/ExpenseTracker/tree/main
# https://www.youtube.com/watch?v=G8x0hWLqC5M&list=PLmzEsfSiDGPN6H-bF_iOVNfbClBrvM2zc&ab_channel=%D0%9C%D0%B8%D1%85%D0%B0%D0%B8%D0%BB%D0%9A%D0%B0%D1%82%D0%B0%D1%88%D0%B5%D0%B2%D1%86%D0%B5%D0%B2

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from ui_main import Ui_MainWindow

from connection import Data


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.ui.pushButtonPerson.clicked.connect(self.add_new_person)
        self.ui.pushButtonContractor.clicked.connect(self.add_new_contractor)
        self.ui.pushButtonCash.clicked.connect(self.add_new_cash)

    def view_data(self):
        self.modelPerson = QSqlTableModel(self)
        self.modelPerson.setTable('person')
        self.modelPerson.select()
        self.ui.tablePerson.setModel(self.modelPerson)

        self.modelContractor = QSqlTableModel(self)
        self.modelContractor.setTable('contractor')
        self.modelContractor.select()
        self.ui.tableContractor.setModel(self.modelContractor)

        self.modelCash = QSqlTableModel(self)
        self.modelCash.setTable('cash')
        self.modelCash.select()
        self.ui.tableCash.setModel(self.modelCash)

        # обновляем comboBox
        self.ui.comboBoxCashGiver.addItem('Илья', 1)
        self.ui.comboBoxCashGiver.addItem('Дима репаблика', 2)
        self.ui.comboBoxCashGiver.addItem('нева', 3)



    def reload_data(self):
        print('Расчет баланса')


    def add_new_person(self):
        person_name = self.ui.textEditPersonName.toPlainText()
        person_description = self.ui.textEditPersonDescription.toPlainText()
        self.conn.add_new_person_query(person_name, person_description)
        self.view_data()
        self.reload_data()

    def add_new_contractor(self):
        contractor_name = self.ui.textEditContractorName.toPlainText()
        contractor_description = self.ui.textEditContractorDescription.toPlainText()
        self.conn.add_new_contractor_query(contractor_name, contractor_description)
        self.view_data()
        self.reload_data()

    def add_new_cash(self):
        # cash_giver_id, cash_receiver_id, cash_date, cash_sum, cash_description
        cash_giver_id = 1
        cash_receiver_id = 1
        cash_date = self.ui.textEditCashDate.toPlainText()
        cash_sum = self.ui.textEditCashSum.toPlainText()
        cash_description = self.ui.textEditCashDescription.toPlainText()
        self.conn.add_new_cash_query(cash_giver_id, cash_receiver_id, cash_date, cash_sum, cash_description)
        self.view_data()
        self.reload_data()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    # Вызов exec() запускает цикл событий и блокируется до тех пор, пока приложение не закроется.
    sys.exit(app.exec()) # == app.exec()
