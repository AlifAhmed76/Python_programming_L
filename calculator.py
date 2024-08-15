operator = input('Enter any Operator-(+,-,*,/,%): ')
number1=float(input('Enter first number: '))
number2=float(input('Enter second number: '))

if operator=='+':
    print('Addition of ',number2,"and ",number2,"is : ",number1+number2)
elif operator=='-':
    print('Substraction of ',number2,"and ",number2,"is : ",number1-number2)
elif operator=='*':
    print('Multiplication ',number2,"and ",number2,"is : ",number1*number2)
elif operator=='/':
    print('division of ',number2,"and ",number2,"is : ",number1/number2)
elif operator=='%':
    print('Modulus of ',number2,"and ",number2,"is : ",number1%number2)
else:
    print('Invalid Input Entered!!!')