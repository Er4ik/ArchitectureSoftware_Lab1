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
        else: return 'Invalid coefficients in file!'
    return resArray

coeffs = readFile('./common/files/coeffs.txt')
validCoeffs = checkValidCoeffs(coeffs)
calculateFunction(*validCoeffs)
print(*validCoeffs)
