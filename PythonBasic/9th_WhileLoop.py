#1
#
# while True:
#     city = input()
#     if city == 'Stop':
#         break
#     print(city)
from functools import total_ordering
from platform import mac_ver

# #2
#
# name = input()
#
# password = input()
#
# while True:
#     passW = input()
#     if password == passW:
#         print(f"Welcome {name}!")
#         break

#3

# input_number = int(input())
# sum_of_numbers = 0
#
# while True:
#     if sum_of_numbers >= input_number:
#         break
#     else:
#         new_number = int(input())
#         sum_of_numbers += new_number
#
# print(sum_of_numbers)

# #4
# number = int(input())
# current_number = 1
#
# while current_number <= number:
#     print(current_number)
#     current_number = current_number * 2 + 1
#
# #5
#
# total_sum = 0.00
# while True:
#     inputed_word = input()
#     try:
#         number = float(inputed_word)
#         if number < 0:
#             print("Invalid operation!")
#             break
#         else:
#             total_sum += number
#             print(f'Increase: {number:.2f}')
#     except ValueError:
#         word = inputed_word
#         if word == "NoMoreMoney":
#             break
#         else:
#             print("Please enter a number")
#             continue
#
# print(f"Total: {total_sum:.2f}")

# #6
# import sys
# max_number = -sys.maxsize
# while True:
#     input_word = input()
#     if input_word == 'Stop':
#         break
#     else:
#         try:
#             number = int(input_word)
#             if number > max_number:
#                 max_number = number
#         except ValueError:
#             print('Please enter an integer')
#
# print(max_number)
#
# #7
# import sys
# min_number = sys.maxsize
# while True:
#     input_word = input()
#     if input_word == 'Stop':
#         break
#     else:
#         try:
#             number = int(input_word)
#             if number < min_number:
#                 min_number = number
#         except ValueError:
#             print('Please enter an integer')
#
# print(min_number)

# #8
#
# student_name = input()
# class_counter = 1
# total_score = 0.0
# max_tries = 0
#
# while class_counter <= 12:
#     new_score = float(input())
#     if new_score >= 4.0:
#         class_counter += 1
#         total_score += new_score
#     else:
#         max_tries += 1
#         if max_tries > 1:
#             print(f'{student_name} has been excluded at {class_counter} grade')
#             break
# else:
#     print(f'{student_name} graduated. Average grade: {total_score/12:.2f}')



########################



########################

#WHILE Loop - Exercise

########################



########################

# # # exercise1
# looking_for_book = input()
# NO_MORE_BOOK = "No More Books"
# number_of_books_we_checked = 0
#
# while True:
#     next_book =  input()
#
#     if next_book != looking_for_book:
#         if next_book == NO_MORE_BOOK:
#             print(f"The book you search is not here!\nYou checked {number_of_books_we_checked} books.")
#             break
#         number_of_books_we_checked += 1  # book
#
#     else:
#         print(f"You checked {number_of_books_we_checked} books and found it.")
#         break

# #2
# max_number_of_negative_marks = int(input())
#
# LECTOR_APROVED = "Enough"
# NEGATIVE_MARK = 4
# taked_negative_mark = 0
# number_of_tasks_resolved = 0
#
# sum_of_score = 0.0
# last_task = ""
#
# while True:
#     lector_say = input()
#
#     if lector_say == LECTOR_APROVED:
#         print(f"Average score: {sum_of_score/number_of_tasks_resolved:.2f}")
#         print(f"Number of problems: {number_of_tasks_resolved}")
#         print(f"Last problem: {last_task}")
#         break # Излизаме
#     else:
#         next_mark = int(input())
#         if  next_mark <= NEGATIVE_MARK:
#             taked_negative_mark += 1
#
#         if taked_negative_mark >= max_number_of_negative_marks:
#             print(f"You need a break, {taked_negative_mark} poor grades.")
#             break
#         else:
#             sum_of_score += next_mark
#             number_of_tasks_resolved += 1
#             last_task = lector_say

# #3
# excursion_price = float(input().replace(',', '.'))
# cash = float(input().replace(',', '.'))
# money_stay = cash
# shopping_days = 0
# days = 0
#
# while True:
#     days += 1
#     type_of_action = input() # spend save
#     price_of_action = float(input().replace(',', '.'))
#
#     if type_of_action == 'spend':
#         money_stay = money_stay - price_of_action
#         shopping_days += 1
#
#         if money_stay < 0:
#             money_stay = 0
#
#         if shopping_days >= 5:
#             print(f"You can't save the money.\n{days}")
#             break
#     elif type_of_action == 'save':
#         shopping_days = 0
#         money_stay = money_stay + price_of_action
#         if money_stay >= excursion_price:
#             print(f"You saved the money for {days} days.")
#             break
#     else:
#         print(f"Wrong action")

# #4
#
# steps = 0
# while steps < 10000:
#      enterance = input()
#
#      if enterance == 'Going home':
#          steps += int(input())
#          break
#      else:
#          steps += int(enterance)
#
#
# if steps < 10000:
#     print(f"{10000- steps} more steps to reach goal.")
# else:
#     print(f"Goal reached! Good job!\n{steps-10000} steps over the goal!")

# #5
#
#
# list_of_coins = [200, 100, 50, 20, 10, 5, 2, 1]
# resto = float(input())
#
# money_stay = int(resto*100)
# coins_counter = 0
#
# for coin_price in list_of_coins:
#     amount_of_1type_coin = money_stay // coin_price
#     coins_counter += amount_of_1type_coin
#     money_stay -= amount_of_1type_coin * coin_price
#
#     if money_stay == 0:
#         break
#
# print(coins_counter)

# #6
# int1 = int(input())
# int2 = int(input())
# pieceOfCake = int1*int2
#
# while pieceOfCake > 0:
#     inputWord = input()
#     if inputWord == 'STOP':
#         break
#     pieceOfCake -= int(inputWord)
#
# if pieceOfCake < 0:
#     print(f"No more cake left! You need {abs(pieceOfCake)} pieces more.")
# else:
#     print(f"{pieceOfCake} pieces are left.")


# lengh = int(input())
# width = int(input())
# height = int(input())
# total_volume = lengh * width * height
#
# while total_volume > 0:
#     inputWord = input()
#     if inputWord == 'Done':
#         break
#     total_volume -= int(inputWord)
#
# if total_volume < 0:
#     print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
# else:
#     print(f"{total_volume} Cubic meters left.")

