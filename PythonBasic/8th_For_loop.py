# #1
# for count in range(1,101):
#     print(count)
#
# # 2
# number = int(input())
#
# for counter in range(1, number + 1, 3):
#     print(counter)
import sys

# #3
# number = int(input())
#
# for counter in range(0, number + 1, 2):
#     if counter % 2 == 0:
#         num = pow(2, counter)
#         print(num)

# #4
# number = int(input())
#
# for counter in range( number, 0, -1):
#     print(counter)

# #5
# word = input()
#
# for char in word:
#     print(char)

# #6
# word = input()
# word_sum = 0
#
#
# for char in word:
#     counter = 0
#     if char == 'a':
#         counter = 1
#     elif char == 'e':
#         counter = 2
#     elif char == 'i':
#         counter = 3
#     elif char == 'o':
#         counter = 4
#     elif char == 'u':
#         counter = 5
#     word_sum += counter
#
# print(word_sum)

# #7
# amount_of_numbers = int(input())
# counter = 0
#
# for nex_number in range( 0, amount_of_numbers):
#     number= int(input())
#     counter += number
# print(counter)

# #8
# import sys
# amount_of_numbers = int(input())
# min_number = sys.maxsize
# max_number = -sys.maxsize
#
# for number in range(amount_of_numbers):
#     number_from_sequence = int(input())
#
#     if number_from_sequence > max_number:
#         max_number = number_from_sequence
#
#     if number_from_sequence < min_number:
#         min_number = number_from_sequence
#
#
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")

# # 9
#
# amount_of_numbers = int(input())
# left_sum = 0
# right_sum = 0
#
# for index in range(amount_of_numbers * 2):
#     number_from_sequence = int(input())
#
#     if index < amount_of_numbers:
#         left_sum += number_from_sequence
#     else:
#         right_sum += number_from_sequence
#
# if left_sum == right_sum:
#      print(f"Yes, sum = {left_sum}")
# else:
#     print(f"No, diff = {abs(left_sum - right_sum)}")

# # 9
#
# amount_of_numbers = int(input()) # 4 [0,1,2,3]
# odd_sum = 0 #четно
# even_sum = 0 #
#
# for index in range(amount_of_numbers): # 4 [0,1,2,3]
#     new_number = int(input())
#
#     if index % 2 == 0: # четна позиция - 2ра, 4та [_,1,_,3]
#         even_sum += new_number
#     else:
#         odd_sum += new_number
#
# if even_sum == odd_sum:
#      print(f"Yes\nSum = {even_sum}")
# else:
#     print(f"No\nDiff = {abs(even_sum - odd_sum)}")


########################



########################

#For Loop - Exercise

########################



########################

# # exercise1
#
# import sys
#
# amount_of_numbers = int(input())
# max_number = - sys.maxsize
# sum_of_numbers = 0
#
#
# for i in range(0, amount_of_numbers):
#     number = int(input())
#
#     if number > max_number:
#         max_number = number
#     sum_of_numbers += number
#
# if max_number == sum_of_numbers - max_number:
#     print(f"Yes\nSum = {max_number}")
# else :
#     difference = abs( max_number - (sum_of_numbers - max_number))
#     print(f"No\nDiff = {difference}")

#
# # exercise 3
#
# amount_of_numbers = int(input()) # (1 ≤ n ≤ 1000)
#
# p1,p2,p3,p4,p5 = 0, 0, 0, 0, 0
#
#
# for i in range(0, amount_of_numbers):
#      number = int(input())
#      if number < 200:
#          p1 += 1
#      elif 200<= number <= 399:
#          p2 += 1
#      elif 400 <= number <= 599:
#          p3 += 1
#      elif 600 <= number <= 799:
#          p4 += 1
#      else:
#          p5 += 1
#
# print(f"{p1/amount_of_numbers*100:.2f}%\n{p2/amount_of_numbers*100:.2f}%\n{p3/amount_of_numbers*100:.2f}%\n{p4/amount_of_numbers*100:.2f}%\n{p5/amount_of_numbers*100:.2f}%")


# # exercise 4
#
# how_old_Lily = int(input()) # (1 ≤ n ≤ 77)
# price_washing_machine = float(input())
# toy_price = int(input())
#
# total_money = 0.0
# toy_count = 0
# current_money = 10.0
#
#
# for current_age in range(1, how_old_Lily + 1):
#     if current_age % 2 == 0:
#         total_money += current_money - 1.00
#         current_money += 10.00
#     else:
#         toy_count += 1
#
# total_money += toy_count * toy_price
# diff = total_money - price_washing_machine
# if diff >= 0:
#     print(f"Yes! {diff:.2f}")
# else:
#     print(f"No! {abs(diff):.2f}")
#
# # exercise 5
# amount_of_tabs = int(input()) # (1 ≤ n ≤ 10)
# salary = int(input()) # [500...1500]
#
#
#
# for i in range(amount_of_tabs):
#     webSite_name = input()
#     if webSite_name == "Facebook":
#         salary -= 150
#     elif webSite_name == "Instagram":
#         salary -= 100
#     elif webSite_name == "Reddit":
#         salary -= 50
#
#     if salary <= 0:
#         break
#
# if salary <= 0:
#     print("You have lost your salary.")
# else:
#     print(salary)
#
# #6 Oskar
#
# name_of_talant = input()
# points= float(input()) # [2.0 ... 450.5]
# amount_of_judges =int(input())
# anought_points = 1250.5
#
# for i in range(amount_of_judges):
#     name_of_judge = input()
#     points_from_judge = float(input())
#
#     points += (points_from_judge * len(name_of_judge)/2)
#
#     if points > anought_points:
#         break
#
# if points > anought_points:
#     print(f"Congratulations, {name_of_talant} got a nominee for leading role with {points:.1f}!")
# else:
#     diff = anought_points - points
#     print(f"Sorry, {name_of_talant} you need {diff:.1f} more!")

# #7
#
# count_of_groups = int(input())
# paticipants_Musala = 0
# paticipants_Monblan = 0
# paticipants_Kilimandgaro = 0
# paticipants_K2 = 0
# paticipants_Everest = 0
#
# for i in range(count_of_groups):
#     number_of_participants = int(input())
#     if number_of_participants <= 5:
#         paticipants_Musala += number_of_participants
#     elif 6 <= number_of_participants <= 12:
#         paticipants_Monblan += number_of_participants
#     elif 13 <= number_of_participants <= 25:
#         paticipants_Kilimandgaro += number_of_participants
#     elif 26 <= number_of_participants <= 40:
#         paticipants_K2 += number_of_participants
#     else:
#         paticipants_Everest +=number_of_participants
#
# total_number = (paticipants_Kilimandgaro + paticipants_Monblan
#                                 + paticipants_Everest + paticipants_Musala + paticipants_K2)
#
# print(f"{paticipants_Musala/total_number*100:.2f}%")
# print(f"{paticipants_Monblan/total_number*100:.2f}%")
# print(f"{paticipants_Kilimandgaro/total_number*100:.2f}%")
# print(f"{paticipants_K2/total_number:.2%}")
# print(f"{paticipants_Everest/total_number*100:.2f}%")

# #8
#
# from math import floor, ceil
# number_of_tourney = int(input())
# start_amount_of_points = int(input())
# numbers_of_win = 0
# amount_of_points = 0
#
# for i in range(number_of_tourney):
#     tourney_result = input() # W, F, SF
#     if tourney_result == 'W':
#         numbers_of_win += 1
#         amount_of_points += 2000
#     elif tourney_result == 'F':
#         amount_of_points += 1200
#     elif tourney_result == 'SF':
#         amount_of_points += 720
#
# middle_point = floor(amount_of_points / number_of_tourney)
# total_points = amount_of_points + start_amount_of_points
#
# print(f"Final points: {total_points}\nAverage points: {middle_point}")
# print(f"{numbers_of_win/number_of_tourney:.2%}")
# #
#
# #PRE_exam 7-1 Agency Profit
# name = input()
# number_adult_tickets = int(input())
# number_child_tickets = int(input())
# pure_price_adult = float(input())
# taxes = float(input())
#
# pure_price_child = pure_price_adult*0.3
#
# royal_fi = ((pure_price_child + taxes)*number_child_tickets
#                + (pure_price_adult + taxes)*number_adult_tickets)*0.2
# print(f"The profit of your agency from {name} tickets is {royal_fi:.2f} lv.")



# #PRE_exam 7-2 Add Bags
# price = float(input())
# kilograms = float(input())
# days_before_flight= int(input())
# number_luggage = int(input())
#
#
# if kilograms <= 10:
#     price *=  0.2
# elif kilograms <= 20:
#     price *=  0.5
#
#
# if days_before_flight > 30:
#     price *= 1.10
# elif 7 <= days_before_flight <= 30:
#     price *= 1.15
# else:
#     price *= 1.40
#
# print(f" The total price of bags is: {(price * number_luggage):.2f} lv. ")

# # #PRE_exam 7-03. Aluminum Joinery
# number = int(input())
# type_joinery = input()
# delivery = input()
#
# if number < 10:
#     print("Invalid order")
# else:
#     match type_joinery:
#         case "90X130":
#             price = 110
#             if number > 60:
#                 price *= 0.92
#             elif number > 30:
#                 price *= 0.95
#
#         case "100X150":
#             price = 140
#             if number > 80:
#                 price *= 0.90
#             elif number > 40:
#                 price *= 0.94
#
#         case "130X180":
#             price = 190
#             if number > 50:
#                 price *= 0.88
#             elif number > 20:
#                 price *= 0.93
#
#         case "200X300":
#             price = 250
#             if number > 50:
#                 price *= 0.86
#             elif number > 25:
#                 price *= 0.91
#
#         case _:
#             price = 0
#
#     delivery_price = 60.0 if delivery == "With delivery" else 0.0
#     sale = 0.96 if number > 99 else 1.0
#
#     price = (number * price + delivery_price)*sale
#     print(f"{price:.2f} BGN")

# # PRE_exam 7-04. Balls
# from math import floor
#
# number_of_balls = int(input())
# points = 0
# black_ball, red_ball , orange_ball, yellow_ball , white_ball , other_colors = 0, 0,0,0, 0, 0
#
# for _ in range(number_of_balls):
#
#     color = input()
#     if color == "red":
#         points += 5
#         red_ball += 1
#     elif color == "orange":
#         points += 10
#         orange_ball += 1
#     elif color == "yellow":
#         points += 15
#         yellow_ball += 1
#     elif color == "white":
#         points += 20
#         white_ball += 1
#     elif color == "black":
#         black_ball += 1
#         points = floor(points / 2)
#     else:
#         other_colors += 1
#
# points = floor(points)
#
# print(f"Total points: {points}")
# print(f"Red balls: {red_ball}")
# print(f"Orange balls: {orange_ball}")
# print(f"Yellow balls: {yellow_ball}")
# print(f"White balls: {white_ball}")
# print(f"Other colors picked: {other_colors}")
# print(f"Divides from black balls: {black_ball}")

# #  While-Loop - More Exercises 01. Dishwasher
#
# numbers_of_bottles = int(input())
# current_level_liquid = numbers_of_bottles * 750
# finished = False
# clean_plates = 0
# clean_pans = 0
# counter = 1
#
# while True:
#
#     enter_word = input()
#     if enter_word == "End":
#         finished = True
#         break
#     number_of_props = int(enter_word)
#
#     if counter % 3 == 0: # pans
#         weigh_for_washing = number_of_props * 15
#         pans = True
#         plates = False
#
#     else: #plates
#         weigh_for_washing = number_of_props * 5
#         pans = False
#         plates = True
#
#     #try to wash - is it enough liquid for wash it
#     if current_level_liquid >= weigh_for_washing:
#         current_level_liquid -= weigh_for_washing
#         counter += 1
#
#         if pans:
#             clean_pans += number_of_props
#         else:
#             clean_plates += number_of_props
#     else:
#         print(f"Not enough detergent, {weigh_for_washing - current_level_liquid} ml. more necessary!")
#
#         break
#
# if finished:
#     print(f"Detergent was enough!")
#     print(f"{clean_plates} dishes and {clean_pans} pots were washed.")
#     print(f"Leftover detergent {current_level_liquid} ml.")


# #  While-Loop - More Exercises 02. Report System
# money_target = int(input()) #1... 10_000
# cash = True # 1 =cash 2 = card
# current_money = 0
# cash_money = 0
# number_of_cash_paiments = 0
# card_money = 0
# number_of_card_paiments = 0
#
# while True:
#     bought = input()
#     if bought == 'End':
#         print(f"Failed to collect required money for charity.")
#         break
#     product_price = int(bought)
#
#     if (product_price > 100 and cash) or (product_price < 10 and not cash):
#         print(f"Error in transaction!")
#     else:
#         current_money += product_price #getting money
#         print(f"Product sold!")
#         if cash:
#             cash_money += product_price
#             number_of_cash_paiments += 1
#         else:
#             card_money += product_price
#             number_of_card_paiments += 1
#
#         if current_money >= money_target:
#             #enought money
#             print(f"Average CS: {(cash_money / number_of_cash_paiments):.2f}")
#             print(f"Average CC: {(card_money / number_of_card_paiments):.2f}")
#             break
#
#     cash = not cash

#While-Loop - More Exercises 03. Stream Of Letters
# c_seen = False
# o_seen = False
# n_seen = False
# result = ''
# while True:
#     char = input()
#
#     if char == 'End':
#         break
#     if not char.isalpha():
#         continue
#
#     if char == 'c' and not c_seen:
#         c_seen  = True
#     elif char == 'o' and not o_seen:
#         o_seen += True
#     elif char == 'n' and not n_seen:
#         n_seen += 1
#     else:
#         result += char
#
#     if c_seen and o_seen and n_seen:
#         print(result, end=" ")
#
#         result = ""
#         c_seen = False
#         o_seen = False
#         n_seen = False

#
# #While-Loop - 05. Average Number
#
# count = int(input())
# number = 0
# for _ in range(count):
#     number += int(input())
# print(format(float(number/count), '.2f'))
#
# #While-Loop - 04. Numbers Divided by 3 Without Reminder
# for number in range(1,100):
#     if number % 3 == 0:
#         print(number)
