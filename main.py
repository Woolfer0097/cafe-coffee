import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QWidget
from PyQt5.QtWidgets import QMessageBox


class CafeCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.id = 1
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Кафе «Кофе»')
        self.add_btn.clicked.connect(lambda: self.widget_show(1))
        self.edit_btn.clicked.connect(lambda: self.widget_show(0) if
        self.coffee_table.selectedItems()
        else QMessageBox.critical(self,
                                  "Ошибка ", "Выберите элемент", QMessageBox.Ok))
        self.update_btn.clicked.connect(self.initialization)
        self.initialization()

    def initialization(self):
        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        self.data = [list(i) for i in cursor.execute("SELECT * FROM coffee")]
        length = len(self.data)
        self.coffee_table.setRowCount(length)
        for i in range(length):
            self.coffee_table.setItem(i, 0, QTableWidgetItem(str(self.data[i][0])))
            sql_request = f"SELECT DISTINCT sorts.title FROM coffee LEFT JOIN sorts ON " \
                          f"sorts.id = coffee.sort_id WHERE sorts.id = {self.data[i][1]}"
            sort = str(*[str(*i) for i in cursor.execute(sql_request)])
            sql_request = f"SELECT DISTINCT degrees.title FROM coffee LEFT JOIN degrees ON " \
                          f"degrees.id = coffee.degree_roasting_id WHERE degrees.id = " \
                          f"{int(self.data[i][2])}"
            degree = str(*[str(*i) for i in cursor.execute(sql_request)])
            sql_request = f"SELECT DISTINCT types.title FROM coffee LEFT JOIN types ON " \
                          f"types.id = coffee.type_id WHERE types.id = {self.data[i][3]}"
            type_coffee = str(*[str(*i) for i in cursor.execute(sql_request)])
            self.coffee_table.setItem(i, 1, QTableWidgetItem(sort))
            self.coffee_table.setItem(i, 2, QTableWidgetItem(degree))
            self.coffee_table.setItem(i, 3, QTableWidgetItem(type_coffee))
            self.coffee_table.setItem(i, 4, QTableWidgetItem(str(self.data[i][4])))
            self.coffee_table.setItem(i, 5, QTableWidgetItem(f"{self.data[i][5]}₽"))
            self.coffee_table.setItem(i, 6, QTableWidgetItem(f"{self.data[i][6]}ml"))

    def widget_show(self, t):
        if t == 0:
            self.id = self.data[self.coffee_table.currentRow()][0]
        self.widget = AddEditCoffee(t, self.id)
        self.widget.show()


class AddEditCoffee(QWidget):
    def __init__(self, type_, id_):
        super().__init__()
        self.type = type_
        self.id = id_
        self.connection = sqlite3.connect("coffee.sqlite")
        self.cursor = self.connection.cursor()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Виджет добавления/изменения кофе')
        self.add_btn.clicked.connect(self.check_info)
        self.edit_btn.clicked.connect(self.edit_coffee)
        self.hide_tabs()

    def check_info(self):
        if self.description_line.text() and self.price_line.text() and self.volume_line.text():
            if self.price_line.text().isdigit() and self.volume_line.text().isdigit():
                self.add_coffee()
            else:
                QMessageBox.critical(self, "Ошибка ", "Цена и объём указываются числами",
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Ошибка ", "Неверные данные", QMessageBox.Ok)

    def hide_tabs(self):
        if self.type == 0:
            self.tab_widget.removeTab(0)
            self.edit_tab_init()
        else:
            self.tab_widget.removeTab(1)
            self.add_tab_init()

    def add_tab_init(self):
        sorts = [str(*i) for i in self.cursor.execute("SELECT title FROM sorts")]
        for item in sorts:
            self.sort_box.addItem(item)
        degrees = [str(*i) for i in self.cursor.execute("SELECT title FROM degrees")]
        for item in degrees:
            self.degree_box.addItem(item)
        types = [str(*i) for i in self.cursor.execute("SELECT title FROM types")]
        for item in types:
            self.type_box.addItem(item)

    def edit_tab_init(self):
        sorts = [str(*i) for i in self.cursor.execute("SELECT title FROM sorts")]
        cur_index = int(*[str(*i) for i in self.cursor.execute("SELECT sorts.id FROM "
                                                               "coffee LEFT JOIN sorts ON "
                                                               "sorts.id = coffee.sort_id "
                                                               f"WHERE coffee.id = {self.id}")])
        for item in sorts:
            self.sort_box_edit.addItem(item)
        self.sort_box_edit.setCurrentIndex(cur_index - 1)
        degrees = [str(*i) for i in self.cursor.execute("SELECT title FROM degrees")]
        cur_index = int(*[str(*i) for i in self.cursor.execute("SELECT degrees.id FROM "
                                                               "coffee LEFT JOIN degrees ON "
                                                               "degrees.id = "
                                                               "coffee.degree_roasting_id "
                                                               f"WHERE coffee.id = {self.id}")])
        for item in degrees:
            self.degree_box_edit.addItem(item)
        self.degree_box_edit.setCurrentIndex(cur_index - 1)
        types = [str(*i) for i in self.cursor.execute("SELECT title FROM types")]
        cur_index = int(*[str(*i) for i in self.cursor.execute("SELECT types.id FROM "
                                                               "coffee LEFT JOIN types ON "
                                                               "types.id = coffee.type_id "
                                                               f"WHERE coffee.id = {self.id}")])
        for item in types:
            self.type_box_edit.addItem(item)
        self.type_box_edit.setCurrentIndex(cur_index - 1)
        description = str(*[str(*i) for i in self.cursor.execute("SELECT flavor_description "
                                                                 f"FROM coffee WHERE id = "
                                                                 f"{self.id}")])
        self.description_line_edit.setText(description)
        price = str(*[str(*i) for i in self.cursor.execute("SELECT price "
                                                           f"FROM coffee WHERE id = "
                                                           f"{self.id}")])
        self.price_line_edit.setText(price)
        volume = str(*[str(*i) for i in self.cursor.execute("SELECT volume "
                                                            f"FROM coffee WHERE id = "
                                                            f"{self.id}")])
        self.volume_line_edit.setText(volume)

    def add_coffee(self):
        sql_request = "SELECT id FROM coffee WHERE ID = (SELECT MAX(id) FROM coffee)"
        id_ = int(*[str(*i) for i in self.cursor.execute(sql_request)]) + 1
        sort = self.sort_box.currentIndex()
        degree = self.degree_box.currentIndex()
        type = self.type_box.currentIndex()
        description = self.description_line.text()
        price = self.price_line.text()
        volume = self.volume_line.text()
        sql_request = "INSERT INTO coffee(id,sort_id,degree_roasting_id,type_id,"\
                      f"flavor_description,price,volume) VALUES("\
                      f"{id_},{sort},{degree},{type},'{description}',{price},{volume})"
        self.cursor.execute(sql_request)
        self.connection.commit()
        AddEditCoffee.close(self)

    def edit_coffee(self):
        sort = self.sort_box_edit.currentIndex()
        sql_request = f"UPDATE coffee SET sort_id = {sort + 1} WHERE id = {self.id}"
        self.cursor.execute(sql_request)
        degree = self.degree_box_edit.currentIndex()
        sql_request = f"UPDATE coffee SET degree_roasting_id = {degree + 1} WHERE id = {self.id}"
        self.cursor.execute(sql_request)
        type = self.type_box_edit.currentIndex()
        sql_request = f"UPDATE coffee SET type_id = {type + 1} WHERE id = {self.id}"
        self.cursor.execute(sql_request)
        description = self.description_line_edit.text()
        sql_request = f"UPDATE coffee SET flavor_description = '{description}' WHERE id = " \
                      f"{self.id}"
        self.cursor.execute(sql_request)
        price = self.price_line_edit.text()
        sql_request = f"UPDATE coffee SET price = {price} WHERE id = {self.id}"
        self.cursor.execute(sql_request)
        volume = self.volume_line_edit.text()
        sql_request = f"UPDATE coffee SET volume = {volume} WHERE id = {self.id}"
        self.cursor.execute(sql_request)
        self.connection.commit()
        AddEditCoffee.close(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CafeCoffee()
    ex.show()
    sys.exit(app.exec())
