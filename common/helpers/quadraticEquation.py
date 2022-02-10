import math

def checkType(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_adv_digit(x): 
    if(x.isdigit()): 
        return x[:1]!='-' 
    else:
        return (checkType(x))

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