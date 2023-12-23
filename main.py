from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
window = QWidget()
window.resize(250,250)
window.move(560,225)

button = QPushButton('Кнопка')
text1 = QLabel('Натисни')
text2 = QLabel('?')

v = QVBoxLayout()
v.addWidget(text1, alignment=Qt.AlignCenter)
v.addWidget(text2, alignment=Qt.AlignCenter)
v.addWidget(button, alignment=Qt.AlignCenter)
window.setLayout(v)

def random_number():
    n = randint(0,101)
    text2.setText(str(n))

button.clicked.connect(random_number)

button.setStyleSheet("""
    background-color: #03f7ff;
    border-radius: 10px;
    font-size: 16px;
    border: none;
    padding: 15px 25px;
""")

window.setStyleSheet("""
    background-color: #ffc403;
    border-radius: 10px;
    font-size: 16px;
    border: none;
    padding: 15px 25px;
""")
text2.setStyleSheet("""
    background-color: #03f7ff;
    border-radius: 10px;
    font-size: 16px;
    border: none;
    padding: 15px 25px;
""")
window.show()
app.exec_()


