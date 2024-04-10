from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QMessageBox, QHBoxLayout, QGroupBox, QButtonGroup
from random import*

#Главное меню
#Здесь будет  меню с кнопкой "Играть", названием и управление
app = QApplication([])
main_win = QWidget()
#кнопка
pbutton = QPushButton('Играть')
#шашлык
vline = QVBoxLayout()

vline.addWidget(pbutton)


main_win.setLayout(vline)

main_win.show()
app.exec_()
