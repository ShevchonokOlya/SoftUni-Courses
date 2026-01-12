# #1
# numberOfTheDay = int(input())
# if numberOfTheDay == 1:
#     print("Monday")
# elif numberOfTheDay == 2:
#     print("Tuesday")
# elif numberOfTheDay == 3:
#     print("Wednesday")
# elif numberOfTheDay == 4:
#     print("Thursday")
# elif numberOfTheDay == 5:
#     print("Friday")
# elif numberOfTheDay == 6:
#     print("Saturday")
# elif numberOfTheDay == 7:
#     print("Sunday")
# else:
#     print("Error")
#
# #1
# nameOfTheDay =  input()
# weekends = ["Saturday", "Sunday"]
# working = ["Monday", "Tuesday", "Wednesday" ,"Friday", "Thursday"]
#
# if nameOfTheDay in weekends:
#     print("Weekend")
# elif nameOfTheDay in working:
#     print("Working day")
# else:
#     print("Error")
from idlelib.configdialog import is_int

# # 1
# nameOfTheAnimal= input().lower()
#
# if nameOfTheAnimal == "dog":
#     print("mammal")
# elif nameOfTheAnimal == "crocodile" or nameOfTheAnimal == "tortoise" or nameOfTheAnimal == "snake":
#     print("reptile")
# else:
#     print("unknown")

#4
# age = float(input())
# gender = input().lower()
# if gender == "m":
#     if age >= 16:
#         print("Mr.")
#     else:
#         print("Master")
# elif gender == "f":
#     if age >= 16:
#         print("Ms.")
#     else:
#         print("Miss")

# #shop
# product = input().lower()
# city = input().lower()
# quantity = float(input())
#
# if city == "sofia":
#     # 3. Внутренний блок: Проверяем Продукт для Софии
#     if product == "coffee":
#         price = 0.50
#     elif product == "water":
#         price = 0.80
#     elif product == "beer":
#         price = 1.20
#     elif product == "sweets":
#         price = 1.45
#     elif product == "peanuts":
#         price = 1.60
#
# elif city == "plovdiv":
#     # 3. Внутренний блок: Проверяем Продукт для Пловдива
#     if product == "coffee":
#         price = 0.40
#     elif product == "water":
#         price = 0.70
#     elif product == "beer":
#         price = 1.15
#     elif product == "sweets":
#         price = 1.30
#     elif product == "peanuts":
#         price = 1.50
#
# elif city == "varna":
#     # 3. Внутренний блок: Проверяем Продукт для Варны
#     if product == "coffee":
#         price = 0.45
#     elif product == "water":
#         price = 0.70
#     elif product == "beer":
#         price = 1.10
#     elif product == "sweets":
#         price = 1.35
#     elif product == "peanuts":
#         price = 1.55
#
# # 4. Рассчитываем и выводим результат
# total_cost = price * quantity
# print(total_cost)


# #7
#
# number = int(input())
# a = -100 <= number
# b  = number <= 100
# if -100 <= number <= 100 and number != 0:
#     print("Yes")
# else:
#     print("No")
#
# #6
#
# number = int(input())
# day = input().lower()
#
# if 10 <= number <= 18 and day != 'sunday':
#     print("open")
# else:
#     print("closed")


# #8
#
# day = input().lower()
# if day == 'monday' or day == 'tuesday' or day == 'friday':
#     print('12')
# elif day == 'saturday' or day == 'sunday':
#     print('16')
# elif day == 'wednesday' or day == 'thursday':
#     print('14')
# else:
#     print('You did misprint')


# #9
#
# product = input().lower()
# fruits = ["banana", "apple", "kiwi", "cherry", "lemon" , "grapes"]
# vegetables = ["tomato", "cucumber", "pepper", "carrot"]
#
# if product in fruits:
#     print("fruit")
# elif product in vegetables:
#     print("vegetable")
# else:
#     print("unknown")

# #10
#
# number = int(input())
#
# if 100 <= number <= 200 or number == 0:
#     pass
# else:
#      print("invalid")

# #11
# fruit = input().lower()
# day = input().lower()
# number = float(input())
#
# price = 0.0
#
# if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
#
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#     else:
#         print("error")
#
# elif day == "saturday" or day == "sunday":
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#     else:
#         print("error")
# else:
#     print("error")
#
# if price !=0 :
#     print(f"{price*number:.2f}")

# #12
# city = input().lower()
# money = float(input())
# taxes = 0.0
#
# if  money < 0:
#     print("error")
# elif city == "sofia":
#     if 0 <= money <= 500 :
#         taxes = 0.05
#     elif 500 < money <= 1000 :
#         taxes = 0.07
#     elif 1000 < money <= 10000 :
#         taxes = 0.08
#     elif money >= 10000:
#         taxes = 0.12
#
#
# elif city == "varna":
#     if 0 <= money <= 500:
#         taxes = 0.045
#     elif 500 < money <= 1000:
#         taxes = 0.075
#     elif 1000 < money <= 10000:
#         taxes = 0.10
#     elif money >= 10000:
#         taxes = 0.13
#
# elif city == "plovdiv":
#     if 0 <= money <= 500:
#         taxes = 0.055
#     elif 500 < money <= 1000:
#         taxes = 0.08
#     elif 1000 < money <= 10000:
#         taxes = 0.12
#     elif money >= 10000:
#         taxes = 0.145
#
# else:
#     print("error")
#
# if taxes > 0:
#     print(f"{taxes*money:.2f}")

#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1



#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1




#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1



#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1




#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1#8-1

#
# #8-1
# PREMIERE = 12
# NORMAL = 7.5
# DISCOUNT = 5.0
#
#
#
# screening_type = input().lower()
# row = int(input())
# column = int(input())
#
# sizeOfHall = row*column
#
# if screening_type == "normal":
#     print(f"{sizeOfHall*NORMAL:.2f} leva")
# elif screening_type == "discount":
#     print(f"{sizeOfHall*DISCOUNT:.2f} leva")
# elif screening_type == "premiere":
#     print(f"{sizeOfHall * PREMIERE:.2f} leva")
# else:
#     print("Wrong Input")


#
# #8-2
# degrees = int(input())
# time_of_day = input().lower()
#
# clothes = ""
# shoes = ""
#
#
#
# if 10 <= degrees <= 18:
#     if time_of_day == "morning":
#         clothes = "Sweatshirt"
#         shoes = "Sneakers"
#     elif time_of_day == "afternoon":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#     elif time_of_day == "evening":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#
# elif 18 < degrees <= 24:
#     if time_of_day == "morning":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#     elif time_of_day == "afternoon":
#         clothes = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_day == "evening":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#
# elif degrees >= 25:
#     if time_of_day == "morning":
#         clothes = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_day == "afternoon":
#         clothes = "Swim Suit"
#         shoes = "Barefoot"
#     elif time_of_day == "evening":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#
# #
# #
# # if time_of_day == "evening":
# #     clothes = "Shirt"
# #     shoes = "Moccasins"
# #
# # elif time_of_day == "afternoon":
# #     if 10 <= degrees <= 18:
# #         clothes = "Shirt"
# #         shoes = "Moccasins"
# #     elif 18 < degrees <= 24:
# #         clothes = "T-Shirt"
# #         shoes = "Sandals"
# #     elif degrees >= 25:
# #         clothes = "Swim Suit"
# #         shoes = "Barefoot"
# #
# # if time_of_day == "morning":
# #     if 10 <= degrees <= 18:
# #         clothes = "Sweatshirt"
# #         shoes = "Sneakers"
# #     elif 18 < degrees <= 24:
# #         clothes = "Shirt"
# #         shoes = "Moccasins"
# #     elif degrees >= 25:
# #         clothes = "T-Shirt"
# #         shoes = "Sandals"
#
#
# print(f"It's {degrees} degrees, get your {clothes} and {shoes}.")
#
# #8-2-2
# degrees = int(input())
# time_of_day = input().lower()
#
# clothes = ""
# shoes = ""
#
#
#
# if 10 <= degrees <= 18:
#     if time_of_day == "morning":
#         clothes = "Sweatshirt"
#         shoes = "Sneakers"
#     elif time_of_day == "afternoon":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#     elif time_of_day == "evening":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#
# elif 18 < degrees <= 24:
#     if time_of_day == "morning":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#     elif time_of_day == "afternoon":
#         clothes = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_day == "evening":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#
# elif degrees >= 25:
#     if time_of_day == "morning":
#         clothes = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_day == "afternoon":
#         clothes = "Swim Suit"
#         shoes = "Barefoot"
#     elif time_of_day == "evening":
#         clothes = "Shirt"
#         shoes = "Moccasins"
#
#
# print(f"It's {degrees} degrees, get your {clothes} and {shoes}.")
#
#
# # 8-3
# type_of_flowers= input()
# count_of_flowers = int(input())
# budget = int(input())
#
# ROSES = 5
# Dahlias = 3.8
# Tulips = 2.8
# Narcissus = 3
# Gladiolus = 2.5
# price = 0.0
#
# if type_of_flowers == "Roses":
#     price = ROSES
# elif type_of_flowers == "Dahlias":
#     price = Dahlias
# elif type_of_flowers == "Tulips":
#     price = Tulips
# elif type_of_flowers == "Narcissus":
#     price = Narcissus
# elif type_of_flowers == "Gladiolus":
#     price = Gladiolus
#
# discount = 1
#
#
# if type_of_flowers == "Roses" and count_of_flowers > 80:
#     discount = 0.9
# elif type_of_flowers == "Dahlias" and count_of_flowers > 90:
#     discount = 0.85
# elif type_of_flowers == "Tulips" and count_of_flowers > 80:
#     discount = 0.85
# elif type_of_flowers  == "Narcissus" and count_of_flowers < 120:
#     discount = 1.15
# elif type_of_flowers == "Gladiolus" and count_of_flowers < 80:
#     discount = 1.2
#
# money = budget - count_of_flowers*discount*price
# if money >= 0:
#     print(f"Hey, you have a great garden with {count_of_flowers} {type_of_flowers} and {money:.2f} leva left.")
# else:
#     print(f"Not enough money, you need {abs(money):.2f} leva more.")

#
#
# # 8-4
# budget = int(input())
# season = input() #"Spring", "Summer", "Autumn" или "Winter"
# count_of_fishmen = int(input())
#
# rent = 0
# discount = 1
#
# if season == "Spring":
#     rent = 3000
# elif season == "Summer" or season == "Autumn":
#     rent = 4200
# elif season == "Winter":
#     rent = 2600
#
# if count_of_fishmen <= 6:
#     discount = 0.9
# elif 7 <= count_of_fishmen <= 11:
#     discount = 0.85
# elif 12 <= count_of_fishmen:
#     discount = 0.75
#
# if count_of_fishmen % 2 == 0 and season != "Autumn":
#     discount *= 0.95
#
# money = budget - rent * discount
#
# if money >= 0:
#     print(f"Yes! You have {money:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {abs(money):.2f} leva.")

# # 8-5
# budget = float(input())
# season = input() # "summer", "winter"
#
#
# rent = 0
# destination = ""
# type_of_hotel = ""
# price = 0.00
#
# if budget <= 100:
#     destination = "Bulgaria"
#     if  season == "summer":
#         type_of_hotel = "Camp"
#         price = 0.3 * budget
#     elif season == "winter":
#         type_of_hotel = "Hotel"
#         price = 0.7 * budget
# elif budget <= 1000:
#     destination = "Balkans"
#     if  season == "summer":
#         type_of_hotel = "Camp"
#         price = 0.4 * budget
#     elif season == "winter":
#         type_of_hotel = "Hotel"
#         price = 0.8 * budget
# else:
#     destination = "Europe"
#     type_of_hotel = "Hotel"
#     price = 0.9 * budget
#
#
#
# print(f"Somewhere in {destination}")
# print(f"{type_of_hotel} - {price:.2f}")

# #8-6
#
# number1 = int(input())
# number2 = int(input())
# operator_str = input()
#
# if operator_str == "+" or operator_str == "-" or operator_str == "*":
#     if operator_str == "+":
#         result = number1 + number2
#     elif operator_str == "-":
#         result = number1 - number2
#     elif operator_str == "*":
#         result = number1 * number2
#     string = "even" if result % 2 == 0 else "odd"
#     print(f"{number1} {operator_str} {number2} = {result} - {string}")
#
# elif operator_str == "/" or operator_str == "%":
#     if number2 != 0:
#         if operator_str == "/":
#             result = format((number1 / number2),'.2f')
#         elif operator_str == "%":
#             result = number1 % number2
#
#         print(f"{number1} {operator_str} {number2} = {result}")
#     else:
#         print(f"Cannot divide {number1} by zero")
#
# else:
#     print("Error")



# #8-7
#
# month = input() #May, June, July, August, September или October;
# nights = int(input())
#
# studio_night = 0.0
# apartment_night = 0.0
#
# if month == "May" or month == "October":
#     studio_night = 50.0
#     apartment_night = 65.0
# elif month == "June" or month == "September":
#     studio_night = 75.2
#     apartment_night = 68.7
# elif month == "July" or month == "August":
#     studio_night = 76.0
#     apartment_night = 77.0
#
# if month == "May" or month == "October":
#     if 7 < nights <= 14:
#         studio_night *= 0.95
#     elif nights > 14:
#         studio_night *= 0.7
# elif month == "June" or month == "September":
#     if nights > 14:
#         studio_night *= 0.8
#
# if nights > 14:
#     apartment_night *= 0.9
#
# print(f"Apartment: {format(apartment_night*nights, '.2f')} lv.")
#
# print(f"Studio: {format(studio_night*nights,'.2f')} lv.")


#
# days_to_stay = int(input())
# room_type = input().lower()
# feedback = input().lower()
#
# nights = days_to_stay - 1
#
# price_per_night = 0.0
# total_cost = 0.0
#
# if room_type == "room for one person":
#     price_per_night = 18.00
#     total_cost = nights * price_per_night
#
# elif room_type == "apartment":
#     price_per_night = 25.00
#     total_cost = nights * price_per_night
#
#
#     if nights < 10:
#         total_cost = total_cost * 0.70
#     elif 10 <= nights <= 15:
#         total_cost = total_cost * 0.65
#     else:  # 'повече от 15'
#         total_cost = total_cost * 0.50
#
# elif room_type == "president apartment":
#     price_per_night = 35.00
#     total_cost = nights * price_per_night
#
#     if nights < 10:
#         total_cost = total_cost * 0.90
#     elif 10 <= nights <= 15:
#         total_cost = total_cost * 0.85
#     else:  # 'повече от 15'
#         total_cost = total_cost * 0.80
#
# if feedback == "positive":
#     total_cost = total_cost * 1.25
# elif feedback == "negative":
#     total_cost = total_cost * 0.90
#
# print(f"{total_cost:.2f}")
#
# #8.8
# exam_hour = int(input( )) #0-23
# exam_minute = int(input()) #0-59
# enterance_hour = int(input())
# enterance_minute = int(input())
#
# total_exam_time = exam_hour * 60 + exam_minute
# total_enterance_time = enterance_hour * 60 + enterance_minute
# diff = total_exam_time - total_enterance_time
#
# if diff == 0 or 0 < diff <= 30:
#     print("On time")
#     if 0 < diff <= 30:
#         minute_diff = diff % 60
#         print(f"{minute_diff} minutes before the start")
#
# else:
#     if diff < 0: #Late
#         print("Late")
#         diff = abs(diff)
#         if diff < 60:
#             minute_diff = diff % 60
#             print(f"{minute_diff} minutes after the start")
#         else:
#             hour_diff = diff // 60
#             minute_diff = diff % 60
#             print(f"{hour_diff}:{format(minute_diff, '02d')} hours after the start")
#     else:
#         print("Early")
#         if diff < 60:
#             minute_diff = diff % 60
#             print(f"{minute_diff} minutes before the start")
#         else:
#             hour_diff = diff // 60
#             minute_diff = diff % 60
#             print(f"{hour_diff}:{format(minute_diff, '02d')} hours before the start")


# #3exam
# film_name = input() #"A Star Is Born", "Bohemian Rhapsody","Green Book" или "The Favourite"
# hall_type = input() #"normal", "luxury" или "ultra luxury"
# count_of_tickets = int(input())
#
# price_per_1_ticket = 0.0
#
# if film_name == "A Star Is Born":
#     if hall_type == "normal":
#         price_per_1_ticket = 7.5
#     elif hall_type == "luxury":
#         price_per_1_ticket = 10.5
#     elif hall_type == "ultra luxury":
#         price_per_1_ticket = 13.5
# elif film_name == "Bohemian Rhapsody":
#     if hall_type == "normal":
#         price_per_1_ticket = 7.35
#     elif hall_type == "luxury":
#         price_per_1_ticket = 9.45
#     elif hall_type == "ultra luxury":
#         price_per_1_ticket = 12.75
# elif film_name == "Green Book":
#     if hall_type == "normal":
#         price_per_1_ticket = 8.15
#     elif hall_type == "luxury":
#         price_per_1_ticket = 10.25
#     elif hall_type == "ultra luxury":
#         price_per_1_ticket = 13.25
# elif film_name == "The Favourite":
#     if hall_type == "normal":
#         price_per_1_ticket = 8.75
#     elif hall_type == "luxury":
#         price_per_1_ticket = 11.55
#     elif hall_type == "ultra luxury":
#         price_per_1_ticket = 13.95
#
# profit = format(price_per_1_ticket * count_of_tickets, '.2f')

#print(f"{film_name} -> {profit} lv.")

#
#  #4exam
#
# vaucher_price = int(input())
#
# name = input()
# film_price = 0
# ticket1_counter = 0
# ticket2_counter = 0
# is_it_film = False
#
# while name != "End":
#     if len(name) > 8:
#         film_price = ord(name[0]) + ord(name[1])
#         is_it_film = True
#     elif len(name) <= 8:
#         is_it_film = True
#         film_price = ord(name[0])
#
#
#     if film_price > vaucher_price:
#         break
#     else:
#        if is_it_film == True:
#            ticket1_counter += 1
#        else:
#            ticket2_counter += 1
#     vaucher_price -= film_price
#     name = input()
#     is_it_film = False

print(ticket1_counter)
print(ticket2_counter)