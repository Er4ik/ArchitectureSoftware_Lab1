from msilib.schema import Error
from common.helpers.quadraticEquation import calculateFunction, is_adv_digit

def readFile(path): 
    try:
        red  = '\033[31m'
        white  = '\033[0m' 
        fileWithCoefficients = open(path, 'r')
        lineCoeffs = fileWithCoefficients.readline()
        return lineCoeffs
    except FileNotFoundError:
        print(red + f"Error ---> can't read file by path - {path}" + white)

def checkValidCoeffs(coeffs): 
    resArray = []
    values = coeffs.strip().split(' ')
    if(len(values) > 3): return 'Invalid coefficients in file!'
    for value in values:
        if(is_adv_digit(value)): resArray.append(float(value))
        else: 
            print('Invalid coefficients in file!')
            return False, resArray
    return True, resArray