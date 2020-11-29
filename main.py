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
            sql_request = f"SELECT sorts.title FROM coffee LEFT JOIN sorts ON " \
                          f"sorts.id = coffee.sort_id WHERE sorts.id = {data[i][1]}"
            sort = str(*[str(*i) for i in cursor.execute(sql_request)])
            sql_request = f"SELECT degrees.title FROM coffee LEFT JOIN degrees ON " \
                          f"degrees.id = coffee.degree_roasting_id WHERE degrees.id = " \
                          f"{data[i][2]}"
            degree = str(*[str(*i) for i in cursor.execute(sql_request)])
            sql_request = f"SELECT types.title FROM coffee LEFT JOIN types ON " \
                          f"types.id = coffee.type_id WHERE types.id = {data[i][3]}"
            type_coffee = str(*[str(*i) for i in cursor.execute(sql_request)])
            self.coffee_table.setItem(i, 1, QTableWidgetItem(sort))
            self.coffee_table.setItem(i, 2, QTableWidgetItem(degree))
            self.coffee_table.setItem(i, 3, QTableWidgetItem(type_coffee))
            self.coffee_table.setItem(i, 4, QTableWidgetItem(str(data[i][4])))
            self.coffee_table.setItem(i, 5, QTableWidgetItem(f"{data[i][5]}₽"))
            self.coffee_table.setItem(i, 6, QTableWidgetItem(f"{data[i][6]}ml"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CafeCoffee()
    ex.show()
    sys.exit(app.exec())
