import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
from math import *

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_dell = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_fith = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_dell)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_fith)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_dell = QPushButton('Отчистить', self)
        self.hbox_dell.addWidget(self.b_dell)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)

        self.b_multiplication = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_multiplication)

        self.b_division = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_division)

        self.b_EXP = QPushButton("EXP", self)
        self.hbox_first.addWidget(self.b_EXP)

        self.b_square = QPushButton("√", self)
        self.hbox_first.addWidget(self.b_square)

        self.b_1 = QPushButton("1", self)
        self.hbox_second.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_second.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_second.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_third.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_third.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_third.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_fourth.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_fourth.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_fourth.addWidget(self.b_9)

        self.b_0 = QPushButton("0", self)
        self.hbox_fith.addWidget(self.b_0)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)


        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiplication.clicked.connect(lambda: self._operation("*"))
        self.b_division.clicked.connect(lambda: self._operation("/"))
        self.b_EXP.clicked.connect(lambda: self._exp("EXP"))
        self.b_square.clicked.connect(lambda: self._square("√"))
        self.b_dell.clicked.connect(lambda: self._dell())


        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))


    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)
    
    def _operation(self, op):
        self.op = op
        line = self.input.text()
        self.num_1 = int(line)
        self.input.setText(line + op)

    def _exp(self, op):
        self.op = 'EXP'
        self.input.setText(op + "(")

    def _square(self, op):
        self.op = '√'
        self.input.setText(op)

    def _dell(self):
        self.input.setText('')
    
    def _result(self):
        if self.op == "EXP":
            self.num_2 = int(self.input.text().rsplit('(')[1])
            self.input.setText(str(round(exp(self.num_2), 5)))

        if self.op == "√":
            self.num_2 = int(self.input.text().rsplit('√')[1])
            self.input.setText(str(sqrt(self.num_2)))
            
        if self.op == "+":
            self.num_2 = int(self.input.text().rsplit(self.op)[1])
            self.input.setText(str(self.num_1 + self.num_2))

        if self.op == "-":
            self.num_2 = int(self.input.text().rsplit(self.op)[1])
            self.input.setText(str(self.num_1 - self.num_2))

        if self.op == "*":
            self.num_2 = int(self.input.text().rsplit(self.op)[1])
            self.input.setText(str(self.num_1 * self.num_2))

        if self.op == "/":
            self.num_2 = int(self.input.text().rsplit(self.op)[1])
            if self.num_2 != 0:
                self.input.setText(str(self.num_1 / self.num_2))
            else: self.input.setText('')

        
app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())