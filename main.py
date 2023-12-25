# https://github.com/ithobbies/ExpenseTracker/tree/main
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow

from connection import Data



class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    # Вызов exec() запускает цикл событий и блокируется до тех пор, пока приложение не закроется.
    sys.exit(app.exec()) # == app.exec()
