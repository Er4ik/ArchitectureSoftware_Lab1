from nonInteractive import checkValidCoeffs, readFile
from interactive import inputCoefficient
from common.helpers.quadraticEquation import calculateFunction, is_adv_digit

def main():
    programType = input('Select program type Intercactive - i or Noninteractive - ni: ')
    if(programType == 'i'):
        a, b, c = inputCoefficient()
        calculateFunction(a, b, c)
    elif(programType == 'ni'):
        coeffs = readFile(input('input path to file: '))
        flagValid, validCoeffs = checkValidCoeffs(coeffs)

        if flagValid:
            print(f'Equation is: ({validCoeffs[0]}) x^2 + ({validCoeffs[1]}) x + {validCoeffs[2]} = 0')
            calculateFunction(*validCoeffs)
    else:
        print('Wrong progpar type!')
        main()

main()
