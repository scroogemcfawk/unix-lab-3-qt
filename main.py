import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

n = 1
output_label = None
fizz_input = None
buzz_input = None


def on_click():
    global n
    global output_label
    global fizz_input
    global buzz_input
    print()
    out = ""
    if n % int(fizz_input.toPlainText()) == 0 and n % int(buzz_input.toPlainText()) == 0:
        out = "Fizz Buzz"
    elif n % int(fizz_input.toPlainText()) == 0:
        out = "Fizz"
    elif n % int(buzz_input.toPlainText()) == 0:
        out = "Buzz"
    else:
        out = str(n)
    output_label.setText(out)
    n += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    n = 1

    window = QWidget()

    fizz_label = QLabel(window)
    fizz_label.setText("Fizz: ")
    fizz_label.setFont(QFont("Arial", 10))
    fizz_label.move(10, 10)

    fizz_input = QTextEdit(window)
    fizz_input.move(40, 10)
    fizz_input.resize(60, 25)
    fizz_input.setText("3")

    buzz_label = QLabel(window)
    buzz_label.setText("Buzz: ")
    buzz_label.setFont(QFont("Arial", 10))
    buzz_label.move(110, 10)

    buzz_input = QTextEdit(window)
    buzz_input.move(150, 10)
    buzz_input.resize(60, 25)
    buzz_input.setText("5")

    button = QPushButton(window)
    button.move(230, 10)
    button.setText("Print Next")
    button.clicked.connect(on_click)

    output_label = QLabel(window)
    output_label.move(150, 50)
    output_label.resize(150, 50)
    output_label.setText("...")

    window.resize(320, 240)
    window.setWindowTitle("Fizz Buzz")
    window.show()

    sys.exit(app.exec_())
