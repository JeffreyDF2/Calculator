import math

class calculator():
    def __init__(self, originalNum, operation, otherNum = 0):
        self.originalNum = float(originalNum)
        self.operation = operation
        self.otherNum = float(otherNum) if otherNum != '' else 0
    
    def calculate(self):
        """ Calls the correct method  depending on the operaiton given.
        >>> x = calculator(5, '+', 8)
        >>> x.calculate()
        13
        >>> x = calculator(-5.1, '-', 8)
        >>> x.calculate()
        -13.1
        >>> x = calculator(64, 'x', 8)
        >>> x.calculate()
        512
        >>> x = calculator(64, '÷', -8.987)
        >>> x.calculate()
        -7.12139757
        >>> x = calculator(64, '%')
        >>> x.calculate()
        0.64
        >>> x = calculator(64, '√')
        >>> x.calculate()
        8
        >>> x = calculator(2, 'x^',2)
        >>> x.calculate()
        4
        """
        if self.operation == '+':
            return self.intOrFloat(self.addition())
        if self.operation == '-':
            return self.intOrFloat(self.subtraction())
        if self.operation == 'x':
            return self.intOrFloat(self.multiplication())
        if self.operation == '÷':
            return self.intOrFloat(self.division())
        if self.operation == '%':
            return self.intOrFloat(self.percent())
        if self.operation == '√':
             return self.intOrFloat(self.squareRoot())
        if self.operation == 'x^':
            return self.intOrFloat(self.exponent())

    def addition(self):
        """ Adds originalNum and otherNum
        >>> x = calculator(64, '-', 8)
        >>> x.addition()
        72.0
        >>> x = calculator(0, '-', -8)
        >>> x.addition()
        -8.0
        """
        return self.originalNum + self.otherNum

    def subtraction(self):
        """ Subtracts originalNum and otherNum
        >>> x = calculator(0, '-', 8)
        >>> x.subtraction()
        -8.0
        >>> x = calculator(9, '-', -8)
        >>> x.subtraction()
        17.0
        """
        return self.originalNum - self.otherNum

    def multiplication(self):
        """ Multiplies originalNum and otherNum
        >>> x = calculator(0, '-', 8)
        >>> x.multiplication()
        0.0
        >>> x = calculator(9, '-', -2)
        >>> x.multiplication()
        -18.0
        """
        return self.originalNum * self.otherNum
   
    def division(self):
        """ Divides originalNum and otherNum
        >>> x = calculator(8, '-', 0)
        >>> x.division()
        'Error'
        >>> x = calculator(18, '-', -2)
        >>> x.division()
        -9.0
        """
        return self.originalNum / self.otherNum if self.otherNum != 0 else 'Error'

    def percent(self):
        """ Takes the percentage of the originalNum
        >>> x = calculator(81, '-')
        >>> x.percent()
        0.81
        >>> x = calculator(-0.91, '-')
        >>> x.percent()
        -0.0091
        """
        return self.originalNum / 100
    
    def squareRoot(self):
        """ Takes the squareRoot of the originalNum
        >>> x = calculator(81, '-')
        >>> x.squareRoot()
        9.0
        >>> x = calculator(-81, '-')
        >>> x.squareRoot()
        'Error'
        >>> x = calculator(3, '-')
        >>> x.squareRoot()
        1.7320508075688772
        >>> x = calculator(0.23, '-')
        >>> x.squareRoot()
        0.47958315233127197
        """
        return math.sqrt(self.originalNum) if self.originalNum > 0 else 'Error'
    
    def exponent(self):
        """ Raises original number by the otherNum power
        >>> x = calculator(4, '-', 4)
        >>> x.exponent()
        256.0
        >>> x = calculator(-0.23, '-', 3)
        >>> x.exponent()
        -0.012167
        >>> x = calculator(9, '-', -1)
        >>> x.exponent()
        0.1111111111111111
        """
        return math.pow(self.originalNum, self.otherNum)

    def intOrFloat(self, number):
        """Removes unneeded decimal points or rounds the number to 8 digits
        >>> x = calculator(4, '-', 4)
        >>> x.intOrFloat(0.0)
        0
        >>> x = calculator(4, '-', 4)
        >>> x.intOrFloat(6.34567)
        6.34567
        >>> x = calculator(4, '-', 4)
        >>> x.intOrFloat(6.000000786)
        6.00000079
        >>> x = calculator(4, '-', 4)
        >>> x.intOrFloat(6.000000784)
        6.00000078
        """
        if type(number) == str:
            return number
        if number % 1 == 0:
            return int(number)
        else:
            return round(number, 8)

if __name__ in "__main__":
    import doctest
    doctest.testmod()