from math import *
from common.helpers.quadraticEquation import calculateFunction, is_adv_digit

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



a, b, c = inputCoefficient()
calculateFunction(a, b, c)