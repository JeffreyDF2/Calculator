# CPTR 215 Final Project
# Jeffrey Filiberto II
# Sources:
# https://www.geeksforgeeks.org/pyqt5-create-circular-push-button/
# Zybooks
# Pyside6 Documention
# GitHub
# Stackoverflow
# My phone calculator
# History:
# 11/29/22 Created calculatorGui and made basic numbered buttons
# 12/6/22 Created the calculator class and have it mostly working
# 12/7/22 Made resizeable buttons, added more math functions and made lists
# 12/8/22 Created basic cacluator functionality
# 12/11/22 Adding Ans, +/- button and function, and fixed square root and percent
# 12/12/22 Added tests to calculator, rounding answer to 8, and removed unneeded .0 and general bug fixes
# 12/13/22 Seperating the two classes into two files, and I think im done.

from calculatorClassFinal import calculator
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QSizePolicy

number1, function, number2 = '','',''
answer = '0'

class calculatorGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.calcLayout = QGridLayout()
        self.setMinimumSize(QSize(400, 600))
            
        self.answerLabel = QLabel('')
        self.answerLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.answerLabel.setFont(QFont('Arial', 50))
        self.answerLabel.setStyleSheet("border: 3px solid grey;")
        self.calcLayout.addWidget(self.answerLabel, 0,1,1,4)

        self.buttonList = []
        self.functionList = []
        self.allButtons = []

        num = 9
        for row in range(2,5):
            for button in range(3):
                self.numberButton = QPushButton(f'{num}')
                self.calcLayout.addWidget(self.numberButton, row, 3-button)
                self.buttonList.append(self.numberButton)
                num -= 1
        
        self.zeroButton = QPushButton('0')
        self.calcLayout.addWidget(self.zeroButton, 5,1)
        self.buttonList.append(self.zeroButton)

        self.periodButton = QPushButton('.')
        self.calcLayout.addWidget(self.periodButton, 5,2)
        self.allButtons.append(self.periodButton)
        self.periodButton.pressed.connect(self.decimalClick)

        self.percentButton = QPushButton('%')
        self.calcLayout.addWidget(self.percentButton, 1,1)
        self.allButtons.append(self.percentButton)

        self.squareRoot = QPushButton('√')
        self.calcLayout.addWidget(self.squareRoot, 1, 2)
        self.allButtons.append(self.squareRoot)

        self.exponentButton = QPushButton('x^')
        self.calcLayout.addWidget(self.exponentButton, 1,3)
        self.functionList.append(self.exponentButton)

        self.clearButton = QPushButton('AC')
        self.calcLayout.addWidget(self.clearButton, 1,4)
        self.allButtons.append(self.clearButton)
        self.clearButton.pressed.connect(self.clearClick)

        self.divisionButton = QPushButton('÷')
        self.calcLayout.addWidget(self.divisionButton, 2,4)
        self.functionList.append(self.divisionButton)

        self.multiplicationButton = QPushButton('x')
        self.calcLayout.addWidget(self.multiplicationButton, 3,4)
        self.functionList.append(self.multiplicationButton)

        self.subtractionButton = QPushButton('-')
        self.calcLayout.addWidget(self.subtractionButton, 4,4)
        self.functionList.append(self.subtractionButton)

        self.additionButton = QPushButton('+')
        self.calcLayout.addWidget(self.additionButton, 5,4)
        self.functionList.append(self.additionButton)

        self.deleteButton = QPushButton('Del')
        self.calcLayout.addWidget(self.deleteButton, 6,2)
        self.allButtons.append(self.deleteButton)
        self.deleteButton.pressed.connect(self.deleteClick)

        self.answerButton = QPushButton('Ans')
        self.calcLayout.addWidget(self.answerButton, 6,3)
        self.allButtons.append(self.answerButton)
        self.answerButton.pressed.connect(self.ansClick)

        self.equalButton = QPushButton('=')
        self.calcLayout.addWidget(self.equalButton, 6,4)
        self.allButtons.append(self.equalButton)
        self.equalButton.pressed.connect(self.equalClick)

        self.negativeButton = QPushButton('+/-')
        self.calcLayout.addWidget(self.negativeButton, 5,3)
        self.allButtons.append(self.negativeButton)
        self.negativeButton.pressed.connect(self.negativeClick)

        for button in self.functionList:
            def callFunctionClicked(btn = button):
                self.functionClicked(btn)
            button.pressed.connect(callFunctionClicked)

        for button in self.buttonList:
            def callClick(btn = button):
                self.clicked(btn)
            button.pressed.connect(callClick)

        self.allButtons = self.allButtons + self.buttonList + self.functionList

        for button in self.allButtons:
            if button.text() == '√' or button.text() == '%':
                def callPercentRoot(btn = button):
                    self.percentOrSquareRoot(btn)
                button.pressed.connect(callPercentRoot)

            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setFont(QFont('Arial', 35))

        widget = QWidget()
        widget.setLayout(self.calcLayout)
        self.setCentralWidget(widget)

    def clicked(self, btn: QPushButton):
        global number1, function, number2
        if function == '':
            number1 += btn.text()
            self.answerLabel.setText(number1)
        else:
            number2 += btn.text()
            self.answerLabel.setText(number2)

        self.varStatus()

    def functionClicked(self, btn: QPushButton):
        global number1, function, number2, answer
        if number1 == '':
            number1 = answer        
        for i in self.functionList:
            i.setFlat(False) 
        btn.setFlat(True)
        function = btn.text()

        self.varStatus()
    
    def decimalClick(self):
        global number1, function, number2
        if function == '' and number1.find('.') == -1:
            number1 += '.'
            self.answerLabel.setText(number1)
        elif function != '' and number2.find('.') == -1:
            number2 += '.'
            self.answerLabel.setText(number2)

        self.varStatus()
    
    def clearClick(self):
        global number1, function, number2, answer
        for i in self.functionList:
            i.setFlat(False)
        number1, function, number2 = '','',''
        self.answerLabel.setText('')

        self.varStatus()

    def deleteClick(self):
        global number1, function, number2
        if number1 != '':
            if function == '':
                number1 = number1[:-1]
                self.answerLabel.setText(number1)
            else:
                number2 = number2[:-1]
                self.answerLabel.setText(number2)

        self.varStatus()

    def equalClick(self):
        global number1, function, number2, answer
        if function != '' and number2 != '':
            for i in self.functionList:
                i.setFlat(False)
            x = calculator(number1, function, number2)
            answer = x.calculate()
            self.answerLabel.setText(str(answer))
            number1, function, number2 = '','',''

        self.varStatus()

    def ansClick(self):
        global number1, function, number2, answer
        if function == '':
            number1 = str(answer)
            self.answerLabel.setText(number1)
        else:
            number2 = str(answer)
            self.answerLabel.setText(number2)

        self.varStatus()
           
    def negativeClick(self):
        global number1, function, number2
        switch = True
        if function == '':
            changeNum = number1
        else:
            changeNum = number2
            switch = False
        changeNum = changeNum[1:] if changeNum[0] == '-' else ('-' + changeNum)
        if switch:
            number1 = changeNum
            self.answerLabel.setText(number1)
        else:
            number2 = changeNum
            self.answerLabel.setText(number2)
        
        self.varStatus()

    def percentOrSquareRoot(self, btn: QPushButton):
        global number1, number2
        if number2 == '':
            x = calculator(number1, btn.text())
            answer = x.calculate()
            number1 = str(answer)
            self.answerLabel.setText(number1)
        else:
            x = calculator(number2, btn.text())
            answer = x.calculate()
            number2 = str(answer)
            self.answerLabel.setText(number2)

        self.varStatus()

    def varStatus(self):
        print('-----------')
        print(f'number1: {number1}')
        print(f'funciton: {function}')
        print(f'number2: {number2}')
        print(f'Answer: {answer}')    

if __name__ in "__main__":
    app = QApplication()
    window = calculatorGui()
    window.show()
    app.exec()