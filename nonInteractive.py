from common.helpers.quadraticEquation import calculateFunction, is_adv_digit

def readFile(path): 
    fileWithCoefficients = open(path, 'r')
    lineCoeffs = fileWithCoefficients.readline()
    return lineCoeffs

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

coeffs = readFile('./common/files/coeffs.txt')

flagValig, validCoeffs = checkValidCoeffs(coeffs)

if flagValig:
    print(f'Equation is: ({validCoeffs[0]}) x^2 + ({validCoeffs[1]}) x + {validCoeffs[2]} = 0')
    calculateFunction(*validCoeffs)
