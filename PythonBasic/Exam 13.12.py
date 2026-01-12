# #catFood
#
# FAT = 9
# PROTEIN = 4
# CARBONATE = 4
#
# percent_Fat = int(input())/100
# percent_Protein = int(input())/100
# percent_Carbonate = int(input())/100
# total_callories = int(input())
# percent_water = int(input())/100
#
# fat_weigh = total_callories * percent_Fat / FAT
# protein_weigh = total_callories * percent_Protein / PROTEIN
# carbonate_weight = total_callories * percent_Carbonate / CARBONATE
#
# total_weigh = fat_weigh + protein_weigh + carbonate_weight
# call_per_gr = (total_callories / total_weigh) * (1 - percent_water)
#
# print(f"{call_per_gr:.4f}")

# #Deer of Santa
# from math import ceil, floor
#
# days = int(input())
# food_stay = int(input())
# food_per_day_FIRST = float(input())
# food_per_day_SECOND = float(input())
# food_per_day_THIRD = float(input())
#
# total_food_eaten = days * (food_per_day_THIRD + food_per_day_FIRST + food_per_day_SECOND)
# diff = food_stay - total_food_eaten
# if diff >= 0:
#     print(f"{floor(diff)} kilos of food left.")
# else:
#
#     print(f"{ceil(abs(diff))} more kilos of food are needed.")
#
# #Excursion Calculator
#
# people = int(input())
# season = input().lower()
#
# SUMMER_SALE = 0.85
# WINTER_SALE = 1.08
# price = 0.0
#
# match season:
#     case "spring":
#         if people <= 5:
#             price = 50.00 * people
#         else:
#             price = 48.00 * people
#
#
#     case "summer":
#         if people <= 5:
#             price = 48.50 * people
#         else:
#             price = 45.00 * people
#         price *= SUMMER_SALE
#
#     case "autumn":
#         if people <=  5:
#             price = 60.00 * people
#         else:
#             price = 49.50 * people
#
#     case "winter":
#         if people <=  5:
#             price = 86.00 * people
#         else:
#             price = 85.00 * people
#
#         price *= WINTER_SALE
#
# print(f"{price:.2f} leva.")
#
# #04. Computer Firm
#
# model_count = int(input())
# total_sales = 0
# total_rating = 0
#
# for _ in range(model_count):
#     sales_rating = int(input()) #32..306
#
#     rating = sales_rating % 10
#     sales = sales_rating // 10
#
#     if rating == 2:
#         real_sales = 0.0
#     elif rating == 3:
#         real_sales = 0.5
#     elif rating == 4:
#         real_sales = 0.7
#     elif rating == 5:
#         real_sales = 0.85
#     elif rating == 6:
#         real_sales = 1.0
#
#     sales  =  sales * real_sales
#     total_sales += sales
#     total_rating += rating
#
# middle_rating = total_rating / model_count
#
# print(f'{total_sales:.2f}\n{middle_rating:.2f}')

# #05. Everest
#
# START = 5364
# FINISH = 8848
#
# sucsess = False
# night_sleep = False
# current_day = 1
# current_high = START
#
# while True:
#     first_word = input()
#     if first_word == "END":
#         break
#     night_sleep = True if first_word == "Yes" else False
#
#     if night_sleep:
#         current_day += 1
#
#     metres = int(input())
#
#     if current_day > 5:
#         break
#
#     current_high += metres
#
#     if current_high >= FINISH:
#         sucsess = True
#         break
#
# if sucsess:
#     print(f"Goal reached for {current_day} days!")
# else:
#     print(f"Failed!\n{current_high}")

# 06. Substitute

k = int(input())
l = int(input())
m = int(input())
n = int(input())
count_of_change = 0


for first_number1 in range(k, 9):
    for first_number2 in range(9, l - 1 , -1):
            for second_number1 in range(m, 9):
                    for second_number2 in range(9, n - 1, -1):

                        if count_of_change >= 6:
                            break

                        if (first_number1 % 2 == 0 and first_number2 % 2 == 1) and (second_number1 % 2 == 0 and second_number2 % 2 == 1):

                            first = first_number1*10 + first_number2
                            second = second_number1*10 + second_number2

                            if first == second:
                                print("Cannot change the same player.")
                            else:
                                print(f"{first_number1}{first_number2} - {second_number1}{second_number2}")
                                count_of_change += 1
