# ask the user its name and say hello

name = input("what is your name? ")

print('Hello', name)

'''
def hello():
    var = "hello world"
    print(var)

hello()
'''

num1, num2 = input('Enter two numbers:').split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2

difference = num1 - num2

product = num1 * num2

quotient = num1 / num2

Remainder = num1 % num2

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, Remainder))


