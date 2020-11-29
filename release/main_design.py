# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coffee_table = QtWidgets.QTableWidget(self.centralwidget)
        self.coffee_table.setGeometry(QtCore.QRect(10, 40, 911, 521))
        self.coffee_table.setObjectName("coffee_table")
        self.coffee_table.setColumnCount(7)
        self.coffee_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.coffee_table.setHorizontalHeaderItem(6, item)
        self.coffee_table.horizontalHeader().setDefaultSectionSize(128)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(730, 10, 75, 23))
        self.add_btn.setObjectName("add_btn")
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(814, 10, 101, 23))
        self.edit_btn.setObjectName("edit_btn")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.update_btn.setObjectName("update_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.coffee_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.coffee_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Сорт"))
        item = self.coffee_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Степень прожарки"))
        item = self.coffee_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.coffee_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание вкуса"))
        item = self.coffee_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.coffee_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Объём"))
        self.add_btn.setText(_translate("MainWindow", "Добавить"))
        self.edit_btn.setText(_translate("MainWindow", "Редактировать"))
        self.update_btn.setText(_translate("MainWindow", "Обновить"))
