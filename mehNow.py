# # #
# # # # Make a Python program that prints your name.
# # # name = 'Gopinath'
# # # print(f'Hi my name is {name}')
# # #
# # # # Make a program that displays the lyrics of a song.
# # # lyrics = '''
# # # Hello?
# # # Is there anybody in there?
# # # Just nod if you can hear me
# # # Is there anyone home?
# # #
# # # Come on now
# # # I hear you're feeling down
# # # Well, I can ease your pain
# # # And get you on your feet again
# # #
# # # Relax
# # # I'll need some information first
# # # Just the basic facts
# # # Can you show me where it hurts?
# # #
# # # There is no pain, you are receding
# # # A distant ship, smoke on the horizon
# # # You are only coming through in waves
# # # Your lips move, but I can't hear what you're saying
# # # When I was a child, I had a fever
# # # My hands felt just like two balloons
# # # Now I've got that feeling once again
# # # I can't explain, you would not understand
# # # This is not how I am
# # #
# # # I have become comfortably numb
# # #
# # # I have become comfortably numb
# # #
# # # Okay
# # # Just a little pinprick
# # # There'll be no more
# # # But you may feel a little sick
# # #
# # # '''
# # # print(lyrics)
# #
# # # # Make a program that displays several numbers.
# # # a,b,c,d = 1,2,3,4
# # # print(f'Here are a few random numbers {a}, {b}, {c}, {d}')
# #
# # # # Make a program that solves and shows the summation of 64 + 32.
# # # num1 = 64
# # # num2 = 32
# # # sum_of_num1_num2 = num1 + num2
# # # print(f'The sum of the numbers 64 and 32 is {sum_of_num1_num2}')
# #
# # # Try to print the day, month, year in the form “Today is 2/2/2016”.
# #
# # # # Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum
# # # num1 = 10
# # # num2 = 1000
# # # product_num1_num2 = num1 * num2
# # # sum_num1_num2 = num1 + num2
# # # if product_num1_num2 <= 1000:
# # #     print(f'The result is {sum_num1_num2}')
# # # else:
# # #     print(f'The result is {product_num1_num2}')
# #
# # # Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number
# #
# # # i = 0;
# # # previous_number = i
# # # for i in range(0, 10):
# # #     current_number = i
# # #     sum_numb = i + previous_number
# # #     print(f'Current number is {current_number}, the previous number {previous_number} and their sum = {sum_numb}')
# # #     previous_number = i
# # # current_number = i
# # # from datetime import datetime
# #
# # # birth_year = input("What year were you born: ")
# # # # print(birth_year)
# # # age = 2021 - int(birth_year)
# # # print(f'Your age is: {age}')
# #
# # # username = input('Please enter your username: ')
# # # password = input('Please enter your password: ')
# # # length_of_password = len(password)
# # # masked_password = '*' * length_of_password
# # # print(f'Hi {username}, your password {masked_password} is {length_of_password} letters long')
# #
# # #
# # # strt = "pynative"
# # # print(f'Original String is {strt}')
# # # print(f'Printing only even index chars')
# # # for i in range(0, len(strt) - 1, 2):
# # #     print(strt(i))
# # # print(strt)
# #
# #
# # # cart = ['Whiskey', 'Brandy', 'Rum', 'Gin', 'Beer']
# # # new_cart = cart[:]
# # # print(cart[0:: 3])
# # # new_cart[0] = 'Tequila'
# # # print(cart)
# # # print(new_cart)
# #
# #
# # # basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # # basket.remove("Banana")
# # # basket.pop(2)
# # # basket.append("Kiwi")
# # # basket.insert(0, "Apples")
# # # basket.count("Apples")
# # # basket.clear()
# # # print(basket)
# #
# #
# # # print(list(range(100)))
# # # friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
# # # new_friend = ['Stanley']
# # # print(sorted(friends) + new_friend)
# #
# # # friends_list = ['Joey', 'Chandler', 'Ross', 'Racheal', 'Monica', 'Pheobe']
# # # print(friends_list[0])
# # # print(friends_list[1])
# # # print(friends_list[2])
# # # print(friends_list[3])
# # # print(friends_list[4])
# # # print(friends_list[5])
# # #
# # # print(f'Hey {friends_list[0]}, How are you?')
# # # print(f'Hey {friends_list[1]}, How are you?')
# # # print(f'Hey {friends_list[2]}, How are you?')
# # # print(f'Hey {friends_list[3]}, How are you?')
# # # print(f'Hey {friends_list[4]}, How are you?')
# # # print(f'Hey {friends_list[5]}, How are you?')
# #
# # # mode_of_transport = ['Bicycle', 'Bike', 'Scooter', 'Car', 'Bus', 'Train']
# # # print(f'My favourite mode of transportation is {mode_of_transport[3]}')
# # # print(f'Have not ridden a {mode_of_transport[0]} in ages')
# # # print(f'My wife own a {mode_of_transport[2]}')
# # # print(f'Need to get my {mode_of_transport[1]} back from the mechanic')
# # # print(f'Have not travelled in a {mode_of_transport[-2]} in like a really really long time')
# # # print(f"The last time I travelled in a {mode_of_transport[-1]} was for my wedding")
# #
# # guest_list = ['Rajnikanth', 'Kamal Hassan', 'Vikram']
# #
# # print(f'We would like to invite you Mr.{guest_list[0]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[1]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[2]} for dinner to my place')
# # print(f'Unfortunately Mr.{guest_list[0]} cannot make it for dinner')
# # guest_list.pop(0)
# # guest_list.insert(0, 'Narendra Modi')
# # guest_list.append('Amit Shah')
# # print(f'We would like to invite you Mr.{guest_list[0]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[1]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[2]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[3]} for dinner to my place')
# # print(f"Hi Mr.{guest_list[0]}, Mr.{guest_list[1]}, Mr.{guest_list[2]}, Mr.{guest_list[3]}, we found a bigger table so going to invite more people")
# # guest_list.insert(0, 'Alex Black')
# # guest_list.insert(2, 'Romaneek Pantal')
# # guest_list.append('Anveshi Jain')
# # print(len(guest_list))
# # print(f'We would like to invite you Mr.{guest_list[0]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[1]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[2]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[3]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[4]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[5]} for dinner to my place')
# # print(f'We would like to invite you Mr.{guest_list[6]} for dinner to my place')
# # print(f'Sorry the table became unavailable Mr.{guest_list[0]}, Mr.{guest_list[1]}, Mr.{guest_list[2]}, Mr.{guest_list[3]}, Mr.{guest_list[4]}, Mr.{guest_list[5]}, Mr.{guest_list[6]}, we might have to cancel some of the invites')
# # guest_list.pop()
# # guest_list.pop()
# # guest_list.pop()
# # guest_list.pop()
# # guest_list.pop()
# # print(guest_list)
# # print(len(guest_list))
#
# vacation_list = ["South Korea", "Japan", "Zimbabwe", "Netherlands", "Hawaii", "Italy"]
# # print(vacation_list)
# print(sorted(vacation_list))
# print(vacation_list)
# print(sorted(vacation_list, reverse=True))
# print(vacation_list)
# vacation_list.reverse()
# print(vacation_list)
# vacation_list.sort()
# print(vacation_list)
# vacation_list.sort(reverse=True)
# print(vacation_list)

print('Hello world')
