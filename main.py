import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class CafeCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_flag = True
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Кафе «Кофе»')
        self.initialization()

    def initialization(self):
        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        data = [list(i) for i in cursor.execute("SELECT * FROM coffee")]
        length = len(data)
        self.coffee_table.setRowCount(length)
        for i in range(length):
            self.coffee_table.setItem(i, 0, QTableWidgetItem(str(data[i][0])))
            self.coffee_table.setItem(i, 1, QTableWidgetItem(str(data[i][1])))
            self.coffee_table.setItem(i, 2, QTableWidgetItem(str(data[i][2])))
            self.coffee_table.setItem(i, 3, QTableWidgetItem(str(data[i][3])))
            self.coffee_table.setItem(i, 4, QTableWidgetItem(str(data[i][4])))
            self.coffee_table.setItem(i, 5, QTableWidgetItem(str(data[i][5])))
            self.coffee_table.setItem(i, 6, QTableWidgetItem(str(data[i][6])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CafeCoffee()
    ex.show()
    sys.exit(app.exec())
