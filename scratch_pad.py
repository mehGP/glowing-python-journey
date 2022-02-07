# # # Title: Python program to add two numbers
# # # Task: Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers.

# # # a = input('Please provide a number to add: ')
# # # b = input('Please provide another number to add to a: ')
# # # sum = int(a) + int(b)
# # # print(f'The sum of the {a} and {b} is {sum}')

# # Title: Maximum of two numbers in Python
# # Task: Given two numbers, write a Python code to find the Maximum of these two numbers.

# # num1 = int(input('Please provide a number to compare: '))
# # num2 = int(input('Please provide another number to compare against: '))

# # if num1 > num2:
# #     print(f'The max of both the numbers is {num1}')
# # elif num2 > num1:
# #     print(f'The max of both the numbers is {num2}')

# # Title: Python Program for factorial of a number
# # Task: Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.

# num = int(input('Please provide the number for which you want its factorial value: '))


# def factorial(num):
#     if num < 0:
#         print('Please enter a non-negative or value greater than 0')
#     elif num == 0 or num == 1:
#         print(f'The factorial value is {num}')
#     else:
#         fact = 1
#         while(num > 1):
#             fact *= num
#             num -= 1
#         return fact


# print(f'The factorial value for {num} is {factorial(num)}')

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Nyra', 2)
player2 = PlayerCharacter('Sandhya',  3)

print(player1)
