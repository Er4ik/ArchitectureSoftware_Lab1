from curses.ascii import isdigit
import math

is_adv_digit = lambda x: x.isdigit() if x[:1]!='-' else x[1:].isdigit()

def checkTypeCoefficient(coef):
    if(is_adv_digit(coef)): 
        return float(coef)
    else: 
        return checkTypeCoefficient(input("Error. Expected a valid real number, got invalid instead: "))

def inputCoefficient():
    a = checkTypeCoefficient(input("a = "))
    b = checkTypeCoefficient(input("b = "))
    c = checkTypeCoefficient(input("c = "))
    print(f'Equation is: ({a}) x^2 + ({b}) x + {c} = 0')
    return a, b, c

def calculateFunction (a, b, c):
    discr = b ** 2 - 4 * a * c
    
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("There are 2 roots: \nx1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("There are 1 root: \nx = %.2f" % x)
    else:
        print("no roots")

a, b, c = inputCoefficient()
calculateFunction(a, b, c)