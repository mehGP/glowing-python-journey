# # # # # Check for duplicates
# # # # some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# # # # # print(some_list)

# # # # duplicate = []
# # # # for value in some_list:
# # # #     if some_list.count(value) > 1:
# # # #         if value not in duplicate:
# # # #             duplicate.append(value)
# # # # print(f'The duplicate values are {duplicate}')


# # # # # picture = [
# # # # #     [0, 0, 0, 1, 0, 0, 0],
# # # # #     [0, 0, 1, 1, 1, 0, 0],
# # # # #     [0, 1, 1, 1, 1, 1, 0],
# # # # #     [1, 1, 1, 1, 1, 1, 1],
# # # # #     [0, 0, 0, 1, 0, 0, 0],
# # # # #     [0, 0, 0, 1, 0, 0, 0]
# # # # # ]
# # # # # for image in picture:
# # # # #     for pixel in image:
# # # # #         if (pixel == 1):
# # # # #             print('*', end='')
# # # # #         else:
# # # # #             print(' ', end='')
# # # # #     print(' ')

# # # # # x = 1
# # # # # y = 0
# # # # # while y < 5:
# # # # #     y = x+x
# # # # #     z = x+y
# # # # #     print(f'Current number {y} previous number {x} sum: {z}')
# # # # #     y = x+x
# # # # #     # print(f'Current number {y} previous number {x} sum: {x+y}')
# # # # #     continue

# # # # # # # # i = 0
# # # # # # # # while i < 50:
# # # # # # # #     print(i)
# # # # # # # #     i = i + 1
# # # # # # # # else:
# # # # # # # #     print('I am done')

# # # # # # # i = 1
# # # # # # # while i < 4:
# # # # # # #     print(i)
# # # # # # #     i += 1


# # # # # # x = 200
# # # # # # y = 30

# # # # # # if (x*y) <= 1000:
# # # # # #     print(x*y)
# # # # # # elif (x*y) > 1000:
# # # # # #     print(x+y)

# # # # def say_hello(name='meh', emoji=':P'):
# # # #     print(f'helloooooo {name}, {emoji}')


# # # # say_hello('Gopi', ':P')
# # # # say_hello('Nyra', ':P')

# # # # say_hello()


# # # # def add(num1, num2):
# # # #     def another_func(n1,n2)
# # # #     return num1 + num2


# # # # print(add(20, 5))


# # # # def checkDriverAge(age=0):
# # # #     # age = input("What is your age?:")
# # # #     if int(age) < 18:
# # # #         print("Sorry, you are too young to drive this car. Powering off")
# # # #     elif int(age) > 18:
# # # #         print("Powering On. Enjoy the ride!")
# # # #     elif int(age) == 18:
# # # #         print("Congratulations on your first year of driving. Enjoy the ride")


# # # # (checkDriverAge(12))

# # # # even = 0


# # # def highest_even(list):
# # #     evens = []
# # #     for item in list:
# # #         if item % 2 == 0:
# # #             evens.append(item)
# # #     print(evens)
# # #     return max(evens)
# # #     # print()


# # # print(highest_even([10, 1, 2, 3, 4, 5, 56, 6, 7]))

# # # # print(evens)

# # # #     # for item in list:
# # # #     #     if list % 2 == 0:
# # # #     #         return list
# # # #     #         print(highest_even)


# # # # highest_even([10, 1, 2, 3, 4, 5, 56, 6, 7])


# # print('My name is Gopinath Padmanaban')
# # long_string = '''
# # Hello?
# # Is there anybody in there?
# # Just nod if you can hear me
# # Is there anyone home?

# # Come on now
# # I hear you're feeling down
# # Well, I can ease your pain
# # And get you on your feet again

# # Relax
# # I'll need some information first
# # Just the basic facts
# # Can you show me where it hurts?

# # There is no pain, you are receding
# # A distant ship, smoke on the horizon
# # You are only coming through in waves
# # Your lips move, but I can't hear what you're saying
# # When I was a child, I had a fever
# # My hands felt just like two balloons
# # Now I've got that feeling once again
# # I can't explain, you would not understand
# # This is not how I am

# # I have become comfortably numb

# # I have become comfortably numb

# # Okay
# # Just a little pinprick
# # There'll be no more
# # But you may feel a little sick

# # Can you stand up?
# # I do believe it's working, good
# # That'll keep you going through the show
# # Come on, it's time to go

# # There is no pain, you are receding
# # A distant ship, smoke on the horizon
# # You are only coming through in waves
# # Your lips move, but I can't hear what you're saying
# # When I was a child, I caught a fleeting glimpse
# # Out of the corner of my eye
# # I turned to look, but it was gone
# # I cannot put my finger on it now
# # The child is grown, the dream is gone

# # I have become comfortably numb'''
# # print(long_string)


# def sum(num1, num2):
#     sum_of_two_numbers = num1 + num2
#     return sum_of_two_numbers

# # print(sum(64, 32))


# def ex1(num1, num2):
#     multi = num1 * num2
#     # return multi
#     print(multi)
#     if multi > 1000:
#         sum = num1 + num2
#         return sum
#         print(sum)
#     else:
#         print(multi)


# # print(ex1(1000, 2))

#

# fname = 'gopinath'
# lname = 'padmanaban'
# full_name = f'{fname} {lname}'
# message = f'Hello, {full_name.title()}'
# print(message)
# # print(f'Hello, {full_name.title()}')


# new_variable = ' python '
# print(new_variable.rstrip())
# print(new_variable.lstrip())
# print(new_variable.strip())

# simple_message = 'Hi, how are you.'
# print(simple_message)
# simple_message = 'Meh, what the hell.'
# print(simple_message.upper())

# person_name = 'gopinath padmanaban'
# print(f'Hi {person_name}, would you like to learn some Python today?? ')
# print(f'Hi {person_name.lower()}, would you like to learn some Python today?? ')
# print(f'Hi {person_name.upper()}, would you like to learn some Python today?? ')
# print(f'Hi {person_name.title()}, would you like to learn some Python today?? ')
# print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")

# famous_person = "Albert Einstein"
# quote = '\"A person who never made a mistake never tried anything new.\"'
# message = f'{famous_person} once said, {quote}'
# print(message)

# first_name = 'Nyra'
# last_name = 'Gopinath'
# full_name = f' {first_name} {last_name} '
# print(full_name)
# print(f'The users full name is: {full_name.lstrip()}')
# print(f'The users full name is: {full_name.rstrip()}')
# print(f'The users full name is: {full_name.strip()}')

# weird_number = 10_00_000_000
# print(weird_number)

# print(6+2)
# print(11-3)
# print(4*2)
# print(16/2)

# fav_number = 2
# message = f'My favourite number is: {fav_number}'
# print(message)


# import this
