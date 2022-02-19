from math import *
from common.helpers.quadraticEquation import calculateFunction, is_adv_digit

def checkTypeCoefficient(coef):
    red  = '\033[31m'
    green  = '\033[32m'
    if(is_adv_digit(coef)): 
        return float(coef)
    else: 
        print(f'Bad coefficient = {coef}' + red)
        return checkTypeCoefficient(input("Error. Expected a valid real number, got invalid instead: " + green))

def inputCoefficient():
    white  = '\033[0m' 
    green  = '\033[32m'
    bold = '\033[1m'
    a = checkTypeCoefficient(input(white + "a = " + bold + green))
    b = checkTypeCoefficient(input(white + "b = " + bold + green))
    c = checkTypeCoefficient(input(white + "c = " + bold + green))
    print(white + 'Equation is: ({a}) x^2 + ({b}) x + {c} = 0')
    return a, b, c