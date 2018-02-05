num1, operator, num2 = input("Enter Calculation: ").split()

num1 = int(num1)
num2 = int(num2)

if operator == '+':
    sum = num1 + num2
    print('{} + {} = {}'.format(num1, num2, sum))
elif operator == '-':
    difference = num1 - num2
    print('{} - {} = {}'.format(num1, num2, difference))
elif operator == '*':
    product = num1 * num2
    print('{} * {} = {}'.format(num1, num2, product))
elif operator == '/':
    quotient = num1 / num2
    print('{} / {} = {}'.format(num1, num2, quotient))
elif operator == '%':
    remainder = num1 % num2
    print('{} % {} = {}'.format(num1, num2, remainder))
else:
    print("Operation not supported, please use '+','-','*','/','%' only")