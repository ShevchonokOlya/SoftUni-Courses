# #exam8_1
#
# price_strawberry = float(input()) #ягоди
#
# weight_bananas = float(input())
# weight_oranges = float(input())
# weight_raspberry = float(input()) # малини
# weight_strawberry = float(input())
#
#
# price_raspberry = price_strawberry /2
# price_oranges = price_raspberry * 0.6
# price_bananas = price_raspberry * 0.2
#
# total_sum = (price_strawberry * weight_strawberry + price_oranges * weight_oranges
#              + price_bananas * weight_bananas + price_raspberry * weight_raspberry)
#
# print(format(total_sum, '.2f'))
import sys
from functools import total_ordering
from tkinter.font import names
from unittest import case

# #exam8_2
# budget = float(input()) #0.0 ... 10_000.0
# fuel_l = float(input()) #1..50
# day_of_week =  input() # "Saturday" и "Sunday"
#
# fuel_price  = 2.1
# excursion_price = 100.0
#
#
# sale = 0.9 if day_of_week == 'Saturday' else 0.8
#
# money = budget - (fuel_l * fuel_price + excursion_price) * sale
# if money < 0:
#     print(f"Not enough money! Money needed: {abs(money):.2f} lv.")
# else:
#     print(f"Safari time! Money left: {money:.2f} lv. ")

# #exam8_3


# price_table  = {
#     "Small": {
#             "one": 9.98,
#             "two": 8.58
#     },
#     "Middle":
#         {
#             "one": 18.99,
#             "two": 17.09
#     },
#     "Large":
#         {
#             "one": 25.98,
#             "two": 23.59
#     },
#     "ExtraLarge":
#             {
#                 "one": 35.99,
#                 "two": 31.79
#         }
# }
# #dictionary[key1][key2]
# term = input() # one, two
# type_of_contract = input() #"Small",  "Middle", "Large"или "ExtraLarge"
# mobile_int_adition = input() #yes no
# month_number = int(input()) #1-24
#
# price = price_table[type_of_contract][term]
#
# if  mobile_int_adition == "yes":
#     if price <= 10.0:
#         price += 5.5
#     elif 10<price<=30:
#         price += 4.35
#     else:
#         price += 3.85
#
# if term == "two":
#     price *= 0.9625
#
# print(f"{price*month_number:.2f} lv.")


# #exam8_4
#
# budget = float(input())
# total_product_number = 0
# total_cost = 0.0
# money_stay = budget
# product_counter = 0
# ran_out_of_money = False
# needed_money = 0
#
# while True:
#     product_name = input()
#
#     if product_name == 'Stop':
#         break
#
#     product_counter += 1 #one more product
#     product_price = float(input())
#
#     if product_counter == 3:
#         product_price *= 0.5
#
#     if money_stay >= product_price:
#         total_product_number += 1
#         total_cost += product_price
#         money_stay -= product_price
#         if product_counter == 3:
#             product_counter = 0
#     else:
#         ran_out_of_money = True
#         needed_money = product_price - money_stay
#
#         break
#
#
# if ran_out_of_money:
#     print(f"You don't have enough money!\nYou need {abs(needed_money):.2f} leva!")
# else:
#     print(f"You bought {total_product_number} products for {total_cost:.2f} leva.")
#

# #exam8_6
#
# number_of_days = int(input()) #1-5
# number_of_hours = int(input()) #1-24
# total_price = 0.0
#
# for day in range(1, number_of_days + 1):
#     daily_price = 0.0
#     for hour in range(1, number_of_hours + 1):
#         if day % 2 == 0:
#             if hour % 2 != 0:
#                 daily_price += 2.5
#             else:
#                 daily_price += 1.0
#         else:
#             if hour % 2 != 0:
#                 daily_price += 1.0
#             else:
#                 daily_price += 1.25
#
#     print(f"Day: {day} - {daily_price:.2f} leva")
#     total_price += daily_price
#
# print(f"Total: {total_price:.2f} leva")

#exam2_5
# import sys
#
# number_of_films = int(input())
# lowest_rating = sys.maxsize
# bad_film_option = ""
# highest_rating = -sys.maxsize
# good_film_option = ""
# total_rating = 0.0
#
# for i in range(number_of_films):
#
#     name = input()
#     rating = float(input())
#
#     if rating < lowest_rating:
#         lowest_rating = rating
#         bad_film_option = name
#
#     if rating > highest_rating:
#         highest_rating = rating
#         good_film_option = name
#
#     total_rating += rating
#
# print(f"{good_film_option} is with highest rating: {highest_rating:.1f}")
# print(f"{bad_film_option} is with lowest rating: {lowest_rating:.1f}")
# print(f"Average rating: {(total_rating/number_of_films):.1f}")

#exam 1-1_basketball

# year_tax = int(input())
# shoes = 0.6 * year_tax
# clothes = 0.8 * shoes
# ball =  0.25 * clothes
# accessorises = 0.2 * ball
#
# price = year_tax + shoes + clothes + ball + accessorises
# print(format(price, '.2f'))


#exam 1-1 Tennis
# from math import floor, ceil
#
# racket_price = float(input())
# number_of_rackets = int(input())
# number_of_shoes = int(input())
#
# shoe_price = racket_price / 6
# tax_clothes = 1.2
#
# final_price =  (shoe_price * number_of_shoes + racket_price * number_of_rackets) * tax_clothes
#
# print(f"Price to be paid by Djokovic {floor(1/8 * final_price)}")
# print(f"Price to be paid by sponsors {ceil(7/8 * final_price)}")

# #exam 1-02. football
# drawn, won, lost = 0, 0, 0
# for number_of_the_match in range(1, 4):
#     match_result = input() #"2:0", "0:1", "1:1"
#     if match_result[0] == match_result[2]:
#         drawn += 1
#     elif int(match_result[0]) >= int(match_result[2]):
#         won += 1
#     else:
#         lost += 1
#
#
# print(f"Team won {won} games.\nTeam lost {lost} games.")
# print(f" Drawn games: {drawn}")
#
# # exam 1-02. Skeleton
#
# control_min = int(input()) # 0-59
# control_sec = int(input()) # 0-59
# length = float(input())
# speed_for_100m = int(input())
#
# sec_control_point = control_min * 60 + control_sec
# time_changing = length / 120
# time = time_changing * 2.5
#
# result = length / 100 * speed_for_100m - time
#
# if result > sec_control_point:
#     print(f"No, Marin failed! He was {(result - sec_control_point):.3f} second slower.")
# else:
#     print(f"Marin Bangiev won an Olympic quota!\nHis time is {result:.3f}.")

# # exam 1-03. Gymnastics
# country = input() # ("Russia", "Bulgaria" или "Italy")
# type = input() # ("ribbon", "hoop" или "rope")
# difficulty = 0.0
# perfomance = 0.0
#
# '''Difficulty: 9.100
# Performance: 9.400'''
#
# if country == 'Russia':
#     if type == 'ribbon':
#         difficulty = 9.1
#         perfomance = 9.4
#     elif type == 'hoop':
#         difficulty = 9.3
#         perfomance = 9.8
#     else:
#         difficulty = 9.6
#         perfomance = 9.0
# elif country == 'Bulgaria':
#     if type == 'ribbon':
#         difficulty = 9.6
#         perfomance = 9.4
#     elif type == 'hoop':
#         difficulty = 9.55
#         perfomance = 9.75
#     else:
#         difficulty = 9.5
#         perfomance = 9.4
# elif country == 'Italy':
#     if type == 'ribbon':
#         difficulty = 9.2
#         perfomance = 9.5
#     elif type == 'hoop':
#         difficulty = 9.45
#         perfomance = 9.35
#     else:
#         difficulty = 9.7
#         perfomance = 9.15
# else:
#    print("wrong country")
#
# total_mark = difficulty + perfomance
#
# print(f"The team of {country} get {total_mark:.3f} on {type}.")
# print(f"{((20-total_mark)/20):.2%}")

#
# # exam 1-03. Snooker
#
# price_table  = {
#     "Quarter final":
#         {
#         "Standard": 55.5,
#         "Premium": 105.2,
#         "VIP": 118.9
#     },
#     "Semi final":
#         {
#         "Standard": 75.88,
#         "Premium": 125.22,
#         "VIP": 300.4
#     },
#     "Final":
#         {
#             "Standard": 110.1,
#             "Premium": 160.66,
#             "VIP": 400
#     }
# }
#
# etap = input().strip() #“Quarter final ”, “Semi final” или “Final”
# type_of_ticket = input() #“Standard”, “Premium” или “VIP”
# number_of_tickets = int(input()) # 1..30
# photo = input() # Y N
# sale = 1
# photo_price = 40.0 if photo == 'Y' else 0.0
#
#
# total_price = price_table[etap][type_of_ticket]* number_of_tickets
#
# if total_price > 4_000:
#     sale = 0.75
#     photo_price = 0.0
# elif total_price > 2_500:
#     sale = 0.9
#
# total_price = total_price  * sale + photo_price * number_of_tickets
#
# print(f"{total_price:.2f}")

# exam 1-04. Game Number Wars
# first_player = input()
# second_player = input()
# points_first = 0
# points_second = 0
# number_wars_situation = False
#
# while True:
#     card1 = input()
#     if card1 == 'End of game':
#         print(f"{first_player} has {points_first} points")
#         print(f"{second_player} has {points_second} points")
#         break
#     first_player_card = int(card1)
#     second_player_card = int(input())
#
#     if first_player_card == second_player_card:
#         print("Number wars!")
#         number_wars_situation = True
#         continue
#
#     else:
#         if number_wars_situation:
#             if first_player_card > second_player_card:
#                 print(f"{first_player} is winner with {points_first} points")
#             else:
#                 print(f"{second_player} is winner with {points_second} points")
#             break
#         else:
#             if first_player_card > second_player_card:
#                 points_first = points_first + first_player_card - second_player_card
#             else:
#                 points_second = points_second + second_player_card - first_player_card

#
# # exam 1 - 04. Darts
#
# START = 301
# name = input()
# total_points = START
# count_of_unsuccessful_shots = 0
# count_of_successful_shots = 0
#
# while True:
#     try_word = input()
#     if try_word == 'Retire':
#         print(f"{name} retired after {count_of_unsuccessful_shots} unsuccessful shots.")
#         break
#     field = try_word #"Single", "Double" или "Triple"
#     points = int(input())
#
#     if  field == 'Double':
#         points *= 2
#     elif field == 'Triple':
#         points *= 3
#
#     if points > total_points:
#         unsuccessful = True
#         count_of_unsuccessful_shots += 1
#         continue
#     else:
#         count_of_successful_shots += 1
#         total_points -= points
#         if total_points == 0:
#             print(f"{name} won the leg with {count_of_successful_shots} shots.")
#             break



#
# # exam 1 - 05. Fitness Center
#
# '''
# На първия ред – броят на посетителите [1...1000]
# За всеки един посетител  ("Back", "Chest", "Legs", "Abs", "Protein shake" или "Protein bar")
# '''
#
# number_of_clients = int(input())
# work_out_counter = 0
# protein_counter = 0
# back_counter = 0
# chest_counter = 0
# legs_counter = 0
# abs_counter = 0
# protein_shake_counter = 0
# protein_bar_counter = 0
#
# for i in range(number_of_clients):
#     type_of_gym = input()
#
#     if  type_of_gym == "Back":
#         back_counter += 1
#         work_out_counter += 1
#     elif type_of_gym == "Chest":
#         chest_counter += 1
#         work_out_counter += 1
#     elif type_of_gym == "Legs":
#         legs_counter += 1
#         work_out_counter += 1
#     elif type_of_gym == "Abs":
#         abs_counter += 1
#         work_out_counter += 1
#     elif type_of_gym == "Protein shake":
#         protein_shake_counter += 1
#         protein_counter += 1
#     elif type_of_gym == "Protein bar":
#         protein_bar_counter += 1
#         protein_counter += 1
#
# print(f"{back_counter} - back")
# print(f"{chest_counter} - chest")
# print(f"{legs_counter} - legs")
# print(f"{abs_counter} - abs")
# print(f"{protein_shake_counter} - protein shake")
# print(f"{protein_bar_counter} - protein bar")
# print(f"{(work_out_counter/number_of_clients):.2%} - work out")
# print(f"{(protein_counter/number_of_clients):.2%} - protein")
#
#

#
# # exam 1 - 06. High Jump
#
# target = int(input())
# current_high = target - 30
#
# it_is_failed = False
# number_of_jumps = 0
# unsucsess_at_this_high = 0
#
# while current_high <= target:
#
#     high_of_jump = int(input())
#     number_of_jumps += 1
#
#     if high_of_jump > current_high:
#         current_high += 5
#         unsucsess_at_this_high = 0
#     else:
#         unsucsess_at_this_high += 1
#
#         if unsucsess_at_this_high == 3:
#             it_is_failed = True
#             break
#
# if  it_is_failed:
#     print(f"Tihomir failed at {current_high}cm after {number_of_jumps} jumps.")
# else:
#     print(f"Tihomir succeeded, he jumped over {target}cm after {number_of_jumps} jumps.")

# # exam 1 - 06. Basketball Tournament
#
# win = 0
# total_matches = 0
#
# while True:
#     name_of_tourney = input()
#     if name_of_tourney == 'End of tournaments':
#         break
#
#
#     matches_number = int(input()) #1..15
#     total_matches += matches_number
#
#     for current_match in range(1, matches_number + 1):
#         desi_team_points = int(input())
#         varior_team_points = int(input())
#
#         if  desi_team_points > varior_team_points:
#             print(f"Game {current_match} of tournament {name_of_tourney}: "
#                   f"win with {desi_team_points - varior_team_points} points.")
#             win += 1
#         else:
#             print(f"Game {current_match} of tournament {name_of_tourney}: "
#                   f"lost with {varior_team_points - desi_team_points} points.")
#
# print(f"{(win/total_matches):.2%} matches win")
# print(f"{((total_matches - win)/total_matches):.2%} matches lost")


# #Exam 7-06. Barcode Generator
# start_number =  input()
# end_number =  input()
#
# for number0 in range(int(start_number[0]), int(end_number[0]) + 1):
#     if number0 % 2 == 1:
#         for number1 in range(int(start_number[1]), int(end_number[1]) + 1):
#             if number1 % 2 == 1:
#                 for number2 in range(int(start_number[2]), int(end_number[2]) + 1):
#                     if number2 % 2 == 1:
#                         for number3 in range(int(start_number[3]), int(end_number[3]) + 1):
#                             if number3 % 2 == 1: #НЕчетно
#                                 print(f"{number0}{number1}{number2}{number3}", end=' ')

# #exam 05. Best Player
# import sys
# max_goal = -sys.maxsize
# best_player = ""
# hat_trick = False
#
# while True:
#     name = input()
#     if name == 'END':
#         break
#     goals = int(input())
#
#     if goals > max_goal:
#         max_goal = goals
#         best_player = name
#         hat_trick = True if goals >= 3 else False
#
#     if goals >= 10:
#         break
#
# print(f"{best_player} is the best player!")
# if hat_trick:
#     print(f"He has scored {max_goal} goals and made a hat-trick !!!")
# else:
#     print(f"He has scored {max_goal} goals.")

# #pre-Exam 5 02. Family Trip
#
# budget = float(input()) #[1.00 … 10000.00]
# number_nights = int(input())
# price_per_night = float(input())
# extra = int(input())/100 # 1..100
#
# if number_nights > 7:
#     price_per_night *=0.95
#
# diff = budget - price_per_night * number_nights - budget * (extra)
# if diff >= 0 :
#    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
# else:
#     print(f"{abs(diff):.2f} leva needed.")

# #pre-Exam 5 01. Pool Day
#
# from math import ceil
# number_of_clients = int(input())
# price_for_person = float(input())
# shezlong_price = float(input()) #[1.00 … 50.00]
# umbrella_price = float(input())
#
# umbrella_number = ceil(number_of_clients / 2)
# shezlong_number = ceil(number_of_clients * 0.75)
#
#
# price = (number_of_clients * price_for_person +
#          umbrella_number * umbrella_price + shezlong_price*shezlong_number)
#
# print(f"{price:.2f} lv." )

# #pre-Exam 4 03. Movie Destination
#
# budget = float(input())
# destination =  input() #"Dubai", "Sofia" и "London"
# season =  input() # "Summer" и "Winter"
# day_amount = int(input())
#
# sofia_tax = 1.25
# dubai_sale = 0.7
# price = 0.0
#
# match season:
#     case "Winter":
#         if destination == "Dubai":
#             price = 45000 * dubai_sale
#         elif destination == "Sofia":
#             price = 17000 * sofia_tax
#         elif destination == "London":
#             price = 24000
#     case "Summer":
#         if destination == "Dubai":
#             price = 40000 * dubai_sale
#         elif destination == "Sofia":
#             price = 12500 * sofia_tax
#         elif destination == "London":
#             price = 20250
#
# diff = budget - price * day_amount
# if (diff) >= 0:
#     print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
# else:
#     print(f"The director needs {abs(diff):.2f} leva more!")

#
# #pre-Exam 5 03. Coffee Machine
# type_of_drink = input()
# sugar = input()
# number_of_cups = int(input())
#
#
# drink_price = {
#     "Espresso": {
#         "Without": 0.90,
#         "Normal": 1.0,
#         "Extra": 1.2
#     },
#     "Cappuccino": {
#         "Without": 1.0,
#         "Normal": 1.20,
#         "Extra": 1.60
#     },
#     "Tea": {
#         "Without": 0.50,
#         "Normal": 0.6,
#         "Extra": 0.7
#     }
# }
#
# price = drink_price[type_of_drink][sugar]*number_of_cups
# if sugar == "Without":
#     price *= 0.65
# if number_of_cups >= 5 and type_of_drink == "Espresso":
#     price *= 0.75
# if price > 15:
#     price *= 0.8
#
# print(f"You bought {number_of_cups} cups of {type_of_drink} for {price:.2f} lv.")
#
# # #pre-Exam 5 03. Travel Agency
#
#
# city = input() #("Bansko",  "Borovets", "Varna" или "Burgas")
# type = input() # ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# vip = input() #"yes" или "no"
# days = int(input())
#
# valid_cities = ["Bansko",  "Borovets", "Varna" , "Burgas"]
# price_per_day = 0.0
# vip_sale = 1.0
#
# if city == "Bansko" or city == "Borovets":
#     if type == "withEquipment":
#         price_per_day = 100
#         vip_sale = 0.9 if vip == "yes" else 1
#     elif type == "noEquipment":
#         price_per_day = 80
#         vip_sale = 0.95 if vip == "yes" else 1
# elif city == "Varna" or city == "Burgas":
#     if type == "withBreakfast":
#         price_per_day = 130
#         vip_sale = 0.88 if vip == "yes" else 1
#     elif type == "noBreakfast":
#         price_per_day = 100
#         vip_sale = 0.93 if vip == "yes" else 1
#
# days = (days- 1) if days > 7 else days
#
# price = price_per_day * vip_sale * days
#
# if city not in valid_cities or price_per_day == 0.0:
#     print("Invalid input!")
# elif days < 1:
#     print("Days must be positive number!")
# else:
#     print(f"The price is {price:.2f}lv! Have a nice time!")



# # #pre-Exam 5 04. Club
# target_profit = float(input())
# club_profit = 0.0
#
# while True:
#     entared_name = input()
#     if entared_name == "Party!" :
#         print(f"We need {(target_profit - club_profit):.2f} leva more.")
#         break
#
#     coctale_name = entared_name
#     coctale_price = len(coctale_name)
#     coctale_count = int(input())
#
#     price = coctale_price * coctale_count
#     if  price % 2 == 1:
#         price *= 0.75
#
#     club_profit += price
#
#     if club_profit >= target_profit:
#         print(f"Target acquired.")
#         break
#
# print(f"Club income - {club_profit:.2f} leva.")
#
# #pre-exam 5 - 04. Renovation
# from math import ceil
# high = int(input())
# width = int(input())
# persent_of_windows = int(input())
# total_painted = 0
#
# total_area = high * width * 4
# percent_to_remove = total_area * (persent_of_windows / 100)
# squers = ceil(total_area - percent_to_remove)
#
# while  total_painted < squers :
#     litres = input()
#     if litres == "Tired!":
#         print(f"{abs(squers - total_painted)} quadratic m left.")
#         break
#     l = int(litres)
#     total_painted += l
# else:
#     if total_painted - squers > 0:
#         print(f"All walls are painted and you have {total_painted - squers} l paint left!")
#     elif total_painted == squers:
#        print("All walls are painted! Great job, Pesho!")


##option 2
# import math
#
# height = int(input())
# width = int(input())
# percent_not_painted = int(input())
#
# total_area = (height * width) * 4
# area_to_paint = total_area * (1 - percent_not_painted / 100)
#
# total_area_needed = math.ceil(area_to_paint)
#
# while True:
#     command = input()
#
#     if command == "Tired!":
#         print(f"{total_area_needed} quadratic m left.")
#         break
#     liters_paint = int(command)
#
#     total_area_needed -= liters_paint
#
#     if total_area_needed < 0:
#         paint_left = abs(total_area_needed)
#         print(f"All walls are painted and you have {paint_left} l paint left!")
#         break
#
#     elif total_area_needed == 0:
#
#         print("All walls are painted! Great job, Pesho!")
#         break

    #
#
# #pre-exam 5 - 05. PC Game Shop
#
# number_of_games = int(input())
# number_of_Hearthstone = 0
# number_of_Fornite = 0
# number_of_Overwatch = 0
# number_of_Others = 0
#
# for i in range(number_of_games):
#     name = input()
#
#     match name:
#         case "Hearthstone":
#             number_of_Hearthstone += 1
#         case "Fornite":
#             number_of_Fornite += 1
#         case "Overwatch":
#             number_of_Overwatch += 1
#         case _:
#             number_of_Others += 1
#
#
# total_ordering= number_of_Hearthstone + number_of_Fornite + number_of_Overwatch + number_of_Others
#
# print(f"Hearthstone - {(number_of_Hearthstone/total_ordering):.2%}")
# print(f"Fornite - {(number_of_Fornite/total_ordering):.2%}")
# print(f"Overwatch - {(number_of_Overwatch/total_ordering):.2%}")
# print(f"Others - {(number_of_Others/total_ordering):.2%}")
#
# # pre-exam 5 - 05. PC Game Shop
# name_of_team = input()
# number_of_games = int(input())
# points, winner, equal, lost = 0, 0, 0, 0
#
# if number_of_games == 0:
#     print (f"{name_of_team} hasn't played any games during this season.")
# else:
#     for i in range(number_of_games):
#         result = input()  #'W' +3, 'D'+1 и 'L' 0
#         if result == "W":
#             points += 3
#             winner += 1
#         elif result == "D":
#             equal += 1
#             points += 1
#         else:
#             lost += 1
#
#     print (f"{name_of_team} has won {points} points during this season.")
#
#     print (f"Total stats:")
#     print (f"## W: {winner}")
#     print (f"## D: {equal}")
#     print (f"## L: {lost}")
#     print (f"Win rate: {(winner/number_of_games):.2%}")
#
# # # pre-exam 5 - 06. Name Game
# import sys
# max_points = -sys.maxsize
# name_of_player = ""
#
# while True:
#     string_inp = input()
#     if string_inp == "Stop":
#         break
#
#     points_of_gamer = 0
#     name = string_inp
#     number_of_tourney = len(name)
#     for index_of_char in range(number_of_tourney):
#
#         code_number = int(input())
#         if ord(name[index_of_char]) == code_number:
#             points_of_gamer += 10
#         else:
#             points_of_gamer += 2
#
#     if points_of_gamer >= max_points:
#         max_points = points_of_gamer
#         name_of_player = name
# print(f"The winner is {name_of_player} with {max_points} points!")

# #pre-exam 5 - 06. The Most Powerful Word
# import sys
# from math import floor
# strongest_word = ""
#
# max_points = -sys.maxsize
#
# while True:
#     word_points = 0
#     string_inp = input()
#     if string_inp == "End of words":
#         break
#
#
#     for char in string_inp:
#         word_points += ord(char)
#
#     if string_inp[0].lower() in 'aeiouy':
#         word_points *= len(string_inp)
#     else:
#         word_points = floor(word_points /len(string_inp))
#
#     if word_points > max_points:
#         max_points = word_points
#         strongest_word = string_inp
#
# print(f"The most powerful word is {strongest_word} - {max_points}")


# # #pre-exam 4 - 01. Series Calculator
# from math import floor
# name = input()
# seasons = int(input())
# episodes = int(input())
# time_for_episode = float(input())
#
# total_time = floor(seasons * 10 + seasons * episodes * time_for_episode * 1.2)
# print( f"Total time needed to watch the {name} series is {total_time} minutes.")



# # # #pre-exam 4 - 01. Movie Profit
# film_name = input()
# number_days = int(input())
# number_of_tickets = int(input())
# ticket_price = float(input())
# studio_part = 1 - int(input()) / 100
#
# total_order = ticket_price * number_of_tickets * number_days * studio_part
# print(f"The profit from the movie {film_name} is {total_order:.2f} lv.")

# #pre-exam 4 - 02. Movie Day
# time_for_shooting = int(input())
# teren = time_for_shooting * 0.15
# number_of_scene = int(input())
# scene_time = int(input())
#
# total_time = scene_time * number_of_scene + teren
#
# diff = total_time - time_for_shooting
#
# if diff < 0 :
#     print(f"You managed to finish the movie on time! You have {round(abs(diff))} minutes left!")
# else:
#     print(f"Time is up! To complete the movie you need {round((diff))} minutes.")
#
# # pre-exam 4 - 03. Film Premiere
# price_per_item = 0
# movie_name = input()
# package_type = input()
# ticket_number = int(input())
#
# match movie_name:
#
#     case "John Wick":
#         match package_type:
#             case "Drink":
#                 price_per_item = 12
#             case "Popcorn":
#                 price_per_item = 15
#             case "Menu":
#                 price_per_item = 19
#
#     case "Star Wars":
#         match package_type:
#             case "Drink":
#                 price_per_item = 18
#             case "Popcorn":
#                 price_per_item = 25
#             case "Menu":
#                 price_per_item = 30
#
#     case "Jumanji":
#         match package_type:
#             case "Drink":
#                 price_per_item = 9
#             case "Popcorn":
#                 price_per_item = 11
#             case "Menu":
#                 price_per_item = 14
#
# sale = 1
# if movie_name == "Star Wars"  and ticket_number >= 4:
#     sale = 0.7
# elif movie_name == "Jumanji" and ticket_number == 2:
#     sale = 0.85
#
# total_price = price_per_item * ticket_number * sale
# print(f"Your bill is {total_price:.2f} leva.")

# # pre-exam 4 - 04. Cinema
# places_in_hall = int(input())
# number_of_people_in_hall = 0
# total_profit = 0.0
#
# while True:
#     people_entered =  input()
#     if people_entered ==  "Movie time!":
#         print(f"There are {places_in_hall - number_of_people_in_hall} seats left in the cinema.")
#         break
#     num_people = int(people_entered)
#     number_of_people_in_hall += num_people
#
#     if number_of_people_in_hall > places_in_hall:
#         print(f"The cinema is full.")
#         break
#     total_profit += num_people * 5
#     if num_people % 3 == 0:
#         total_profit -= 5
#
# print(f"Cinema income - {total_profit:.0f} lv.")

# # pre-exam 4 - 04. Movie Stars
# budget = float(input())
# while True:
#     name = input()
#     if name == 'ACTION':
#         break
#
#     if len(name) > 15:
#         bonus  = 0.2*budget
#     else:
#         bonus = float(input())
#
#     budget -= bonus
#     if   budget<=0:
#         break
#
# if budget >= 0:
#     print(f'We are left with {budget:.2f} leva.')
# else:
#     print(f'We need {abs(budget):.2f} leva for our actors.')

# # pre-exam 4 -05. Series
#
# budget = float(input())
# number_of_films  = int(input())
# koef_Thrones , koef_Lucifer , koef_Protector , koef_TotalDrama, koef_Area = 0.5, 0.6, 0.7, 0.8, 0.9
# '''On a SALE : Thrones – 50% Lucifer – 40%	 Protector – 30%
# TotalDrama – 20% Area – 10%'''
#
# price_of_all_films = 0.0
# for _ in range(number_of_films):
#     name = input()
#
#     match name:
#         case "Thrones":
#             koef = koef_Thrones
#         case "Lucifer":
#             koef = koef_Lucifer
#         case "Protector":
#             koef = koef_Protector
#         case "TotalDrama":
#             koef = koef_TotalDrama
#         case "Area":
#             koef = koef_Area
#         case _:
#             koef = 1
#
#     price_of_all_films += float(input()) * koef
#
# diff = budget - price_of_all_films
# if diff >= 0:
#     print(f"You bought all the series and left with {diff:.2f} lv.")
# else:
#     print(f"You need {abs(diff):.2f} lv. more to buy the series!")

# # pre-exam 4 - 06. Favorite Movie
# import sys
# max_points = -sys.maxsize
# best_film = ""
# for _ in range(7):
#     film_name = input()
#     if film_name == 'STOP':
#         break
#     points = 0
#     length = len(film_name)
#
#     for letter in film_name:
#         points += ord(letter)
#         if letter.isupper():
#             points -= length
#         elif letter.islower():
#             points -= 2*length
#
#     if points > max_points:
#         best_film = film_name
#         max_points = points
#
# else:
#     print("The limit is reached.")
# print(f"The best movie for you is {best_film} with {max_points} ASCII sum.")
#
# # pre-exam 4 - 06. Movie Tickets
#
# a1 = int(input())
# a2 = int(input())
# n = int(input())
# for number_of_letter in range(a1, a2):
#     if number_of_letter % 2 != 0:
#         letter = chr(number_of_letter)
#
#         for number in range(1, n):
#             for number2 in range(1, int(n/2)):
#
#                 if (number + number2 + number_of_letter) % 2 != 0:
#                     print(f'{letter}-{number}{number2}{number_of_letter}')

# # pre-exam 6 -01. Change Bureau
# BIT_LEV = 1168
# CHIN_USD = 0.15
# USD_LEV = 1.76
# EUR_LEV = 1.95
#
# bit_amount = int(input())
# chin_amount = float(input())
# comission = 1 - float(input()) / 100
#
# result_sum = (bit_amount * BIT_LEV + chin_amount * CHIN_USD * USD_LEV) / EUR_LEV * comission
# print(f'{result_sum:.2f}')


# # # pre-exam 6 -01. Birthday Party
# hall_rent  = float(input())
# cake_price = 0.2 * hall_rent
# drinks_price = 0.55 * cake_price
# animator = hall_rent / 3
#
# total_price = hall_rent + cake_price + drinks_price + animator
#
# print(total_price)

# # pre - exam 06 - 02. Mountain Run
# from math import floor
#
# record_in_sec = float(input())
# distance_m = float(input())
# time_s_per_1m = float(input())
#
# slowing = floor(distance_m / 50) * 30
# if time_s_per_1m > 0:
#     final_time = distance_m * time_s_per_1m + slowing
#     diff = final_time - record_in_sec
#     if diff >= 0:
#         print(f"No! He was {diff:.2f} seconds slower.")
#     else:
#         print(f" Yes! The new record is {final_time:.2f} seconds.")


# pre - exam 06 - 02. Cat Walking

#
# min = int(input())
# walking_number = int(input())
# callories = int(input()) * 0.5
#
# burned = min * walking_number * 5
# if callories <= burned:
#         print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned:.0f}.")
# else:
#         print(f"No, the walk for your cat is not enough. Burned calories per day: {burned:.0f}.")

# pre - exam 06 - 03. Energy Booster


# fruit = input()
# type_of_set = input()
# set_number = int(input())
# price = 0.0
#
# if fruit == "Watermelon":
#     if type_of_set == "small":
#         price = 56.00 * 2
#     elif type_of_set == "big":
#         price = 28.70 * 5
# elif fruit == "Mango":
#     if type_of_set == "small":
#         price = 36.66 * 2
#     elif type_of_set == "big":
#         price = 19.60 * 5
# elif fruit == "Pineapple":
#     if type_of_set == "small":
#         price = 42.10 * 2
#     elif type_of_set == "big":
#         price = 24.80 * 5
# elif fruit == "Raspberry":
#     if type_of_set == "small":
#         price = 20.00 * 2
#     elif type_of_set == "big":
#         price = 15.2 * 5
#
# total_price = price * set_number
# if 400 <= total_price <= 1_000:
#     total_price *= 0.85
# elif 1_000 < total_price:
#     total_price *= 0.5
#
# print(f'{total_price:.2f} lv.')
#
# # pre - exam 06 - 03. Fitness Card
# budget = float(input())
# gender = input()  # "Мъж" or "жена"
# age = int(input())
# sport = input()   # "Gym", "Boxing", ...
#
# price = 0
#
# if gender == "m":
#
#     if sport == "Gym":
#         price = 42
#     elif sport == "Boxing":
#         price = 41
#     elif sport == "Yoga":
#         price = 45
#     elif sport == "Zumba":
#         price = 34
#     elif sport == "Dances":
#         price = 51
#     elif sport == "Pilates":
#         price = 39
#
# elif gender == "f":
#
#     if sport == "Gym":
#         price = 35
#     elif sport == "Boxing":
#         price = 37
#     elif sport == "Yoga":
#         price = 42
#     elif sport == "Zumba":
#         price = 31
#     elif sport == "Dances":
#         price = 53
#     elif sport == "Pilates":
#         price = 37
#
# sale = 0.8 if age <= 19 else 1
#
# total_price = price * sale
#
# difference = total_price - budget
# if difference >= 0:
#     print(f"You don't have enough money! You need ${difference:.2f} more.")
# else:
#     print(f"You purchased a 1 month pass for {sport}.")
#
# # pre - exam 06 - 04. Trekking Mania
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


# # pre - exam 06 - 04. Food for Pets
# day_amount = int(input())
# food_stays_for_pets = float( input()) # [0.00…10_000.00]
# total_coockies = 0
# total_dog = 0
# total_cat = 0
#
# for day in range(1, day_amount+1):
#     dog_food_per_day = int(input())
#     cat_food_per_day = int(input())
#    # total_food_per_day = dog_food_per_day + cat_food_per_day
#
#     coockies = (dog_food_per_day + cat_food_per_day) * 0.1  if day % 3 == 0 else  0
#     total_coockies += coockies
#    # total_food_per_day += coockies
#     total_dog += dog_food_per_day
#     total_cat += cat_food_per_day
#
# if food_stays_for_pets == 0:
#     percent_eaten = 0.0
# else:
#     percent_eaten = (total_dog + total_cat) / food_stays_for_pets
#
# print(f"Total eaten biscuits: {round(total_coockies)}gr.")
# print(f"{percent_eaten:.2%} of the food has been eaten.")
# print(f"{(total_dog/(total_dog + total_cat)):.2%} eaten from the dog.")
# print(f"{(total_cat/(total_dog + total_cat)):.2%} eaten from the cat.")



# # pre - exam 06 - 05. Care of Puppy
#
# food_bought = int(input()) * 1000
# while True:
#     need_food_per_day = input()
#     if need_food_per_day == "Adopted":
#
#         break
#     food_bought -= int(need_food_per_day)
#
# if food_bought < 0:
#     print(f"Food is not enough. You need {abs(food_bought)} grams more.")
# else:
#     print(f"Food is enough! Leftovers: {food_bought} grams.")


#
# # pre - exam 06 - 05. Suitcases Load
#
# total_volume = float(input())
# counter = 0
# volume_stays = total_volume
#
# while True:
#     luggage = input()
#     if luggage == 'End':
#         print("Congratulations! All suitcases are loaded!")
#         break
#
#     volume_of_luggage = float(luggage)
#     #do we need to increase the volume?
#     if (counter + 1) % 3 == 0:
#           volume_of_luggage *= 1.1
#
#     # can we put it inside ? is it enough space
#     volume_stays -= volume_of_luggage
#     if volume_stays < 0:
#         #if we can't
#         print("No more space!")
#         break
#     # if we can
#     counter += 1
#
#
# print(f"Statistic: {counter} suitcases loaded.")
#
# # pre - exam 06 - 06. Tournament of Christmas
# days = int(input())
# money = 0.0
# total_win = 0
# total_lose = 0
#
# for day in range(days):
#     daily_money = 0.0
#     daily_wins = 0
#     daily_losses = 0
#
#     while True:
#         type_of_sport = input()
#         if type_of_sport == "Finish":
#             break
#
#         result = input() #"win" или "lose"
#         if result == "win":
#             daily_wins += 1
#             daily_money += 20.0
#         else:
#             daily_losses += 1
#
#     if daily_wins > daily_losses:
#         daily_money *= 1.1
#
#     total_win += daily_wins
#     total_lose += daily_losses
#     money += daily_money
#
# if total_win > total_lose:
#     money *= 1.2
#     print(f"You won the tournament! Total raised money: {money:.2f}")
# else:
#     print(f"You lost the tournament! Total raised money: {money:.2f}")


# # pre - exam 03 - 01. Easter Lunch
# easter_bread = int(input())
# eggs = int(input())
# coockies = int(input())
#
# total = easter_bread *3.2 + eggs * 4.35 + coockies * 5.4 + 0.15 * 12 * eggs
# print(f"{total:.2f}")

# # pre - exam 03 - 01. Easter Bakery
#
# price_flour = float(input())
# killogram_flour = float(input())
# price_sugar = price_flour * 0.75
# killogram_sugar = float(input())
# price_eggs = price_flour * 1.1
# eggs  = int(input())
# price_yeast = 0.2 * price_sugar
# yeast = int(input())
#
# total = (yeast * price_yeast + eggs * price_eggs
#          + killogram_sugar * price_sugar + killogram_flour * price_flour)
# print(format(total ,'.2f'))

# # pre - exam 03 - 02. Easter Party
# number_of_guests = int(input())
# price_per_guest = float(input())
# budget = float(input())
#
# if 10 <= number_of_guests <= 15:
#     price_per_guest = price_per_guest * 0.85
# elif 15 < number_of_guests <= 20:
#     price_per_guest = price_per_guest * 0.8
# elif 20 < number_of_guests:
#     price_per_guest = price_per_guest * 0.75
#
# cake = 0.1 * budget
#
# total_spend = cake + price_per_guest*number_of_guests
# difference = total_spend - budget
#
# if difference <= 0:
#     print(f"It is party time! {abs(difference):.2f} leva left.")
# else:
#     print(f"No party! {difference:.2f} leva needed.")


# pre - exam 03 - 02. Easter Guests
# from math import ceil
#
# number_of_guests = int(input())
# budget = int(input())
#
# easter_bread = ceil(number_of_guests / 3)
# eggs = number_of_guests * 2
#
# total_cost = easter_bread * 4 + eggs * 0.45
# diff = budget - total_cost
#
# if diff < 0:
#     print(f"Lyubo doesn't have enough money.\nHe needs {abs(diff):.2f} lv. more.")
# else:
#     print(f"Lyubo bought {easter_bread} "
#           f"Easter bread and {eggs} eggs."
#           f"\nHe has {diff:.2f} lv. left.")

# pre - exam 03 - 03. Easter Trip



#
# # pre - exam 03 - 03. Painting Eggs
# #
# destination = input()
# dates = input()
# nights = int(input())
#
# price_per_night = 0
#
# if destination == "France":
#
#     if dates == "21-23":
#         price_per_night = 30
#     elif dates == "24-27":
#         price_per_night = 35
#     elif dates == "28-31":
#         price_per_night = 40
#
# elif destination == "Italy":
#
#     if dates == "21-23":
#         price_per_night = 28
#     elif dates == "24-27":
#         price_per_night = 32
#     elif dates == "28-31":
#         price_per_night = 39
#
# elif destination == "Germany":
#
#     if dates == "21-23":
#         price_per_night = 32
#     elif dates == "24-27":
#         price_per_night = 37
#     elif dates == "28-31":
#         price_per_night = 43
#
# total_price = price_per_night * nights
# print(f"Easter trip to {destination} : {total_price:.2f} leva.")

#
# # pre - exam 03 -04. Easter Eggs Battle
#
# price_per_batch = 0
# size = input()
# color = input()
# count = int(input())
#
# if size == "Large":
#     if color == "Red":
#         price_per_batch = 16
#     elif color == "Green":
#         price_per_batch = 12
#     elif color == "Yellow":
#         price_per_batch = 9
#
# elif size == "Medium":
#     if color == "Red":
#         price_per_batch = 13
#     elif color == "Green":
#         price_per_batch = 9
#     elif color == "Yellow":
#         price_per_batch = 7
#
# elif size == "Small":
#     if color == "Red":
#         price_per_batch = 9
#     elif color == "Green":
#         price_per_batch = 8
#     elif color == "Yellow":
#         price_per_batch = 5
#
# total_revenue = price_per_batch * count*0.65
# print(f"{total_revenue:.2f} leva.")
#
# #pre - exam 03 -04. Easter Shop
# player1 = int(input())
# player2 = int(input())
#
# while player1 != 0 and player2 != 0:
#     winner = input()
#     if winner == "End":
#         print(f"Player one has {player1} eggs left.")
#         print(f"Player two has {player2} eggs left.")
#         break
#     elif winner == "one":
#         player2 -= 1
#     elif winner == "two":
#         player1 -= 1
# else:
#     if player1 == 0:
#         print(f"Player one is out of eggs. Player two has {player2} eggs left.")
#     elif  player2 == 0:
#         print(f"Player two is out of eggs. Player one has {player1} eggs left.")
#
#
# #pre - exam 03 -05. Easter Eggs
#
# started_count = int(input())
# eggs_now = started_count
# while True:
#     command = input()
#     if command == "Close":
#         print(f"Store is closed!")
#         sold_eggs = started_count - eggs_now
#         print(f"{sold_eggs} eggs sold.")
#
#         break
#
#     eggs = int(input())
#
#     if command == "Buy":
#         if eggs_now >= eggs:
#             eggs_now -= eggs
#         else:
#             print(f"Not enough eggs in store!")
#             print(f"You can buy only {eggs_now}.")
#             break
#     elif command == "Fill":
#         started_count += eggs
#         eggs_now += eggs
#
#

# #pre - exam 03 -05. Easter Eggs
#
# import sys
# total_eggs = int(input())
# red, orange, blue, green = 0,0,0,0
# max = - sys.maxsize
# winner_name = ""
#
# for _ in range(total_eggs):
#     color = input().strip()
#
#     match color:
#         case 'red':
#             red += 1
#         case 'orange':
#             orange += 1
#         case 'blue':
#             blue += 1
#         case 'green':
#             green += 1
#
#
# if red > max:
#     winner_name = "red"
#     max = red
# if orange > max:
#     winner_name = "orange"
#     max = orange
# if green > max:
#     winner_name = "green"
#     max = green
# if blue > max:
#     winner_name = "blue"
#     max = blue
#
#
# print(f"Red eggs: {red}")
# print(f"Orange eggs: {orange}")
# print(f"Blue eggs: {blue}")
# print(f"Green eggs: {green}")
# print(f"Max eggs: {max} -> {winner_name}")

#
# #pre - exam 03 -05. Easter Bake
# import sys
# from math import ceil
# max_sugar = - sys.maxsize
# max_flour = - sys.maxsize
#
# breads = int(input())
# total_sugar = 0
# total_flour = 0
#
# for _ in range(breads):
#     sugar = int(input())
#     flour = int(input())
#     total_sugar += sugar
#     total_flour += flour
#     if sugar > max_sugar:
#         max_sugar = sugar
#     if flour > max_flour:
#         max_flour = flour
#
# sugar_packages = ceil(total_sugar / 950)
# flour_packages = ceil(total_flour / 750)
#
# print(f"Sugar: {sugar_packages}")
# print(f"Flour: {flour_packages}")
# print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
#
# #pre - exam 03 -06. Easter Competition
# import sys
# max_points = -sys.maxsize
# winner_name = ""
# bread_count = int(input())
#
# for _ in range(bread_count):
#     name = input()
#     total_points_of_backery = 0
#
#     while True:
#         number = input()
#
#         if number == 'Stop':
#             print(f"{name} has {total_points_of_backery} points.")
#             break
#
#         total_points_of_backery += int(number)
#
#     if total_points_of_backery > max_points:
#         print(f"{name} is the new number 1!")
#
#         winner_name = name
#         max_points = total_points_of_backery
#
# print(f"{winner_name} won competition with {max_points} points!")


#
# #pre - exam 03 -06. Easter Decoration
#
# BASKET_PRICE = 1.5
# WREATH_PRICE = 3.8
# BUNNY_PRICE = 7
#
# client_number = int(input())
# profit = 0.0
#
#
# for client in range(client_number):
#     client_check = 0.0
#     client_purchasing = 0
#     while True:
#         shopping = input().strip()
#
#         if shopping == "Finish":
#             if client_purchasing % 2 == 0:
#                 client_check *= 0.8
#             print(f"You purchased {client_purchasing} items for {client_check:.2f} leva.")
#             break
#
#         client_purchasing += 1
#
#         if shopping == "basket":
#             client_check += BASKET_PRICE
#         elif shopping == "wreath":
#             client_check += WREATH_PRICE
#         elif shopping == "chocolate bunny":
#             client_check += BUNNY_PRICE
#
#
#
#     profit += client_check
#
# print(f"Average bill per client is: {(profit/client_number):.2f} leva.")

