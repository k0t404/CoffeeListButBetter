import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication
from change_ui import Ui_MainWindow

con = sqlite3.connect('coffee_list.sqlite')
cur = con.cursor()
result = cur.execute("""SELECT name FROM coffee_name""").fetchall()
COFFEE_NAMES = []
for elem in result:
    COFFEE_NAMES.append(elem[0])
con.close()
WHICH_THING = ['name', 'fried', 'ground_grains', 'description', 'price', 'volume']


class Example2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems(COFFEE_NAMES)
        self.comboBox_2.addItems(WHICH_THING)
        self.pushButton.clicked.connect(self.change)
        self.pushButton_2.clicked.connect(self.add)

    def check(self):
        if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text() and \
                self.lineEdit_5.text() and self.lineEdit_6.text():
            return True
        return False

    def check1(self):
        if self.lineEdit_7.text():
            return True
        return False

    def change(self):
        self.label_11.setText('')
        if self.check1():
            change = self.lineEdit_7.text()
            con1 = sqlite3.connect('coffee_list.sqlite')
            cur1 = con1.cursor()
            seek_for = self.comboBox.currentText()
            what = self.comboBox_2.currentText()
            total = (change, seek_for,)
            if what == 'name':
                cur1.execute("""UPDATE coffee_info
                            SET name = ?
                            WHERE name = ?""", total)
                con1.commit()
                con1.close()
            if what == 'fried':
                cur1.execute("""UPDATE coffee_info
                            SET fried = ?
                            WHERE name = ?""", total)
                con1.commit()
                con1.close()
            if what == 'ground_grains':
                cur1.execute("""UPDATE coffee_info
                            SET ground_grains = ?
                            WHERE name = ?""", total)
                con1.commit()
                con1.close()
            if what == 'description':
                cur1.execute("""UPDATE coffee_info
                            SET description = ?
                            WHERE name = ?""", total)
                con1.commit()
                con1.close()
            if what == 'price':
                cur1.execute("""UPDATE coffee_info
                            SET price = ?
                            WHERE name = ?""", total)
                con1.commit()
                con1.close()
            if what == 'volume':
                cur1.execute("""UPDATE coffee_info
                            SET volume = ?
                            WHERE name = ?""", total)
                con1.commit()
                con1.close()
        else:
            self.label_11.setText('Заполните все')

    def add(self):
        if self.check():
            con2 = sqlite3.connect('coffee_list.sqlite')
            cur2 = con2.cursor()
            name = self.lineEdit.text()
            fried = self.lineEdit_2.text()
            ground_grains = self.lineEdit_3.text()
            description = self.lineEdit_4.text()
            price = self.lineEdit_5.text()
            volume = self.lineEdit_6.text()
            total = (name, fried, ground_grains, description, price, volume,)
            name1 = (name,)
            cur2.execute("""INSERT INTO coffee_info(name, fried, ground_grains, description, price, volume) 
                        VALUES(?, ?, ?, ?, ?, ?)""", total)
            cur2.execute("""INSERT INTO coffee_name(name) 
                                    VALUES(?)""", name1)
            con2.commit()
            con2.close()
        else:
            self.label_7.setText('Заполните все')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
