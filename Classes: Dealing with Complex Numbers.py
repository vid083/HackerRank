"""
Concept:
Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here. 

Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality. 
__add__-> Can be overloaded for + operation

__sub__ -> Can be overloaded for - operation

__mul__ -> Can be overloaded for * operation

input Format:
One line of input: The real and imaginary part of a number separated by a space.

Output Format:
For two complex numbers  and , the output should be in the following sequence on separate lines:

Sample Input:
2 1
5 6

Sample Output:
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
"""

import math

class Complex(object):
    def __init__(self, real, imaginary):
        
    def __add__(self, no):
        
    def __sub__(self, no):
        
    def __mul__(self, no):

    def __truediv__(self, no):

    def mod(self):

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    import math

class Complex(object):
    def __init__(self, real, imaginary):
        
    def __add__(self, no):
        
    def __sub__(self, no):
        
    def __mul__(self, no):

    def __truediv__(self, no):

    def mod(self):

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__'
c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

