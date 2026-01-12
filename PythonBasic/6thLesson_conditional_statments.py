# #1
#
# time_first = int(input().replace(' ', ''))
# time_second = int(input().replace(' ', ''))
# time_third = int(input().replace(' ', ''))
#
# sum_time = time_first + time_second + time_third
# min = sum_time // 60
# sec = sum_time % 60
#
# text_sec = "0" + str(sec) if sec < 10 else str(sec)
#
# print(f"{min}:{text_sec}")
import math
import sys
from functools import total_ordering

# #2
# startNumber = int(input().replace(' ', ''))
#
# extraBonus = 0
# if startNumber <= 100:
#     extraBonus = float(5)
# elif startNumber <= 1000:
#     extraBonus = 0.2 * startNumber
# elif startNumber > 1000:
#     extraBonus = 0.1 * startNumber
#
# if startNumber % 2 == 0:
#     extraBonus += 1
# elif startNumber % 10 == 5:
#     extraBonus += 2
#
# print(extraBonus)
# print(extraBonus+startNumber)


# #3
#
# time_hour = int(input().replace(' ', ''))
# time_min = int(input().replace(' ', ''))
#
#
# new_min_time = time_min + 15
#
# if new_min_time < 60:
#     print(f"{time_hour}:{new_min_time}")
# else:
#     time_hour += 1
#     new_min_time -= 60
#
#     if new_min_time < 10:
#         text_min = "0" + str(new_min_time)
#     else:
#         text_min = str(new_min_time)
#
#     if time_hour > 23:
#         time_hour = time_hour - 24
#
#     print(f"{time_hour}:{text_min}")

# #4
# PAZZLE_PRICE = 2.6
# TALKIN_DALL_PRICE = 3
# BEAR_PRICE = 4.1
# MINION_PRICE = 8.2
# TRACK_PRICE = 2
#
# excurtion_price = float(input().replace(',', '.'))
# countOfPazzle = int(input().replace(' ', ''))
# countOfDall = int(input().replace(' ', ''))
# countOfBear= int(input().replace(' ', ''))
# countOfMinion = int(input().replace(' ', ''))
# countOfTrack = int(input().replace(' ', ''))
#
# total_ordering = (countOfPazzle * PAZZLE_PRICE + countOfDall * TALKIN_DALL_PRICE +
#                   countOfBear * BEAR_PRICE + countOfMinion * MINION_PRICE +
#                   countOfTrack * TRACK_PRICE)
# countOfToys = countOfPazzle + countOfDall + countOfBear + countOfMinion + countOfTrack
# if countOfToys >= 50:
#     total_ordering *= 0.75
#
# final_price = total_ordering *0.9
# money = final_price - excurtion_price
# if money >= 0:
#     print(f"Yes! {format(money, '.2f')} lv left.")
# else:
#     print(f"Not enough money! {format(money.__abs__(), '.2f')} lv needed.")

# #5
# budget = float(input().replace(',', '.'))
# statistsAmount = int(input().replace(',', '.'))
# priceForClothes = float(input().replace(',', '.'))
#
# decoration = 0.1*budget
# if (statistsAmount >= 150):
#     clothesDiscount = 0.9
# else:
#     clothesDiscount = 1
#
# total_price = decoration + priceForClothes * statistsAmount * clothesDiscount
#
#
# if total_price > budget:
#     needMoney = total_price - budget
#     print("Not enough money!")
#     print(f"Wingard needs {format(needMoney, '.2f')} leva more.")
# else:
#     leftMoney = budget - total_price
#     print("Action!")
#     print(f"Wingard starts filming with {format(leftMoney, '.2f')} leva left.")

# #6
# DISTANCE_SPEED_DOWN = 15
# TIME_SPEED_DOWN = 12.5
#
# recordInSeconds = float(input().replace(',', '.'))
# distanceInMeters = float(input().replace(',', '.'))
# timeFor1Meter = float(input().replace(',', '.'))
#
# need_time = distanceInMeters*timeFor1Meter
# extra_time = ((distanceInMeters/DISTANCE_SPEED_DOWN).__floor__())*TIME_SPEED_DOWN
# time = need_time + extra_time
# if time < recordInSeconds:
#     result = recordInSeconds - time
#     print(f" Yes, he succeeded! The new world record is {format(time, '.2f')} seconds.")
# else:
#     result = time - recordInSeconds
#     print(f"No, he failed! He was {format(result, '.2f')} seconds slower.")


# #7
#
# budget = float(input().replace(',', '.'))
# count_VC = int(input().replace(' ', ''))
# count_Proc = int(input().replace(' ', ''))
# count_RAM = int(input().replace(' ', ''))
#
#
# VIDEO_CARD= 250
# vc_price = VIDEO_CARD*count_VC
# proc_price = 0.35*vc_price*count_Proc
# ram_price = 0.1*vc_price*count_RAM
#
# total_price =  vc_price + proc_price + ram_price
# if count_VC > count_Proc:
#     total_price *= 0.85
#
#
# money = budget-total_price
#
# if money >= 0:
#     print(f"You have {format(money, '.2f')} leva left!")
# else:
#     print(f"Not enough money! You need {format(money.__abs__(), '.2f')} leva more!")

# #8
# import math
# film_name =  input()
# episode_time = int(input().replace(' ', ''))
# totalTime = int(input().replace(' ', ''))
#
# timeForLunch = totalTime/8
# timeToRelax = 0.25 * totalTime
# timeStays =  totalTime - timeForLunch - timeToRelax
# time = timeStays - episode_time
#
# if time >= 0:
#     free_time = math.ceil(time)
#     print(f"You have enough time to watch {film_name} and left with {free_time} minutes free time.")
#
# else:
#     needed_time = math.ceil(abs(time))
#     print(f"You don't have enough time to watch {film_name}, you need {needed_time} more minutes.")


# #Extra1
# import math
# inheritance = float(input().replace(',', '.'))
# targetYear = int(input())
#
# YEAR_SPEND_MONEY = 12000
# EXTRA_MONEY_IN_EVEN_YEAR = 50
#
# current_age = 18
#
# for i in range(1800, targetYear + 1, 1):
#     if i % 2 == 1: #odd year (NEchetny)
#         inheritance -= current_age*EXTRA_MONEY_IN_EVEN_YEAR
#     inheritance -= YEAR_SPEND_MONEY
#     current_age += 1
#
# if inheritance >= 0:
#     print(f"Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.")
# else:
#     money_need = math.fabs(inheritance)
#     print(f"He will need {money_need:.2f} dollars to survive.")

# #Extra2
#
# current_doctor_amount = 7
#
# days_amount = int(input())
# treated_patients = 0
# untreated_patients = 0
#
# for day in range(1, days_amount + 1, 1):
#     patients_today = int(input())
#
#     if day % 3 == 0 and treated_patients < untreated_patients:
#         current_doctor_amount += 1
#     if patients_today >= current_doctor_amount:
#         dayli_threated_patients = current_doctor_amount
#         dayli_untreated_patients = patients_today - current_doctor_amount
#     else:
#         dayli_threated_patients = patients_today
#         dayli_untreated_patients = 0
#
#     treated_patients += dayli_threated_patients
#     untreated_patients += dayli_untreated_patients
#
# print(f"Treated patients: {treated_patients}.")
# print(f"Untreated patients: {untreated_patients}.")

# #Extra11
#
# amount_of_numbers = int(input())
#
# list_of_numbers = []
# for  number in range(amount_of_numbers):
#     list_of_numbers.append(float(input()))
#
# #нечетная позиция
# odd_list = list_of_numbers[::2]
#
# #четная позиция
# even_list = list_of_numbers[1::2]
#
# # odd_position_list = []
# #
# # for index, odd_position in enumerate(list_of_numbers):
# #     if index % 2 == 0:
# #         odd_position_list.append(list_of_numbers.index(odd_position))
#
# print(f"OddSum={sum(odd_list):.2f},")
#
# if not odd_list:
#     print("OddMin=No,")
#     print("OddMax=No,")
# else:
#     print(f"OddMin={min(odd_list):.2f},")
#     print(f"OddMax={max(odd_list):.2f},")
#
# print(f"EvenSum={sum(even_list):.2f},")
# if not even_list:
#     print("EvenMin=No,")
#     print("EvenMax=No")
# else:
#     print(f"EvenMin={min(even_list):.2f},")
#     print(f"EvenMax={max(even_list):.2f}")

# # #Extra3
#
# amount_of_product = int(input())
# list_of_product_weight = []
#
# minibus_tons = 0
# truck_tons = 0
# train_tons = 0
# total_cost = 0
#
# for products in range(amount_of_product):
#     current_load = int(input())
#     if current_load <= 3:
#         # Микробус
#         total_cost += current_load * 200
#         minibus_tons += current_load
#
#     elif current_load <= 11:
#         # Камион
#         total_cost += current_load * 175
#         truck_tons += current_load
#
#     else:
#         # Влак
#         total_cost += current_load * 120
#         train_tons += current_load
#
# total_weight = truck_tons + minibus_tons + train_tons
# middle_transp_price = total_cost / total_weight
#
# print(f"{middle_transp_price:.2f}")
# print(f"{minibus_tons / total_weight * 100:.2f}%")
# print(f"{truck_tons / total_weight * 100:.2f}%")
# print(f"{train_tons / total_weight * 100:.2f}%")

# #Extra4
#
# amount_of_students = int(input())
# top_students  = 0
# between4_499_students = 0
# between3_399_students = 0
# between0_299_students = 0
#
# total_mark = 0
# for _ in range(amount_of_students):
#     mark = float(input().replace(',', '.'))
#     if mark >= 5.0:
#         # Top
#         top_students += 1
#     elif mark >= 4.00 and mark <= 4.99:
#         between4_499_students += 1
#     elif mark >= 3.00 and mark <= 3.99:
#         between3_399_students += 1
#     else:
#         between0_299_students += 1
#     total_mark += mark
#
# print(f"Top students: {top_students/amount_of_students*100:.2f}%")
# print(f"Between 4.00 and 4.99: {between4_499_students/amount_of_students*100:.2f}%")
# print(f"Between 3.00 and 3.99: {between3_399_students/amount_of_students*100:.2f}%")
# print(f"Fail: {between0_299_students/amount_of_students*100:.2f}%")
# print(f"Average: {total_mark/amount_of_students:.2f}")

# #Extra5
#
# amount_of_rounds = int(input())
# final_result  = 0
# between0_9 = 0
# between10_19 = 0
# between20_29 = 0
# between30_39 = 0
# between40_50 = 0
# invalid_number = 0
# final_result = 0
#
# for _ in range(amount_of_rounds):
#     mark = int(input())
#     if mark >= 0 and mark <= 9:
#         between0_9 += 1
#         final_result += mark*0.2
#     elif mark >= 10 and mark <= 19:
#         between10_19 += 1
#         final_result += mark * 0.3
#     elif mark >= 20 and mark <= 29:
#         between20_29 += 1
#         final_result += mark * 0.4
#     elif mark >= 30 and mark <= 39:
#         between30_39 += 1
#         final_result += 50
#     elif mark >= 40 and mark <= 50:
#         between40_50 += 1
#         final_result += 100
#     else:
#         invalid_number += 1
#         final_result /= 2
#
#
# print(f"{final_result:.2f}")
# print(f"From 0 to 9: {between0_9/amount_of_rounds * 100:.2f}%")
# print(f"From 10 to 19: { between10_19/amount_of_rounds* 100:.2f}%")
# print(f"From 20 to 29: { between20_29/amount_of_rounds * 100:.2f}%")
# print(f"From 30 to 39: { between30_39/amount_of_rounds* 100:.2f}%")
# print(f"From 40 to 50: {between40_50/amount_of_rounds * 100:.2f}%")
# print(f"Invalid numbers: {invalid_number/amount_of_rounds * 100:.2f}%")

# #Extra6
#
# WATER = 20
# INTERNET = 15
#
# amount_of_monthes = int(input())
# other = 0.0
#
# total_amount_of_water_paiment = WATER*amount_of_monthes
# total_amount_of_internet_paiment = INTERNET*amount_of_monthes
# total_amount_of_other_paiment = 0.0
# total_amount_of_electricity_paiment = 0.0
#
# for _ in range(amount_of_monthes):
#
#     electricity = float(input())
#     total_amount_of_electricity_paiment += electricity
#
#     other = (electricity + WATER + INTERNET)*1.2
#     total_amount_of_other_paiment += other
#
#
# middle_payment = (total_amount_of_internet_paiment + total_amount_of_water_paiment
#                   + total_amount_of_other_paiment + total_amount_of_electricity_paiment) / amount_of_monthes
#
# print(f"Electricity: {total_amount_of_electricity_paiment:.2f} lv")
# print(f"Water: {total_amount_of_water_paiment:.2f} lv")
# print(f"Internet: {total_amount_of_internet_paiment:.2f} lv")
# print(f"Other: {total_amount_of_other_paiment:.2f} lv")
# print(f"Average: {middle_payment:.2f} lv")

# #Extra7
#
#
# stadium_capacity = int(input())
# amount_of_fans = int(input())
# TYPE_OF_SECTORS = ["A", "B", "V" , "G"]
# amount_a = 0
# amount_b = 0
# amount_v = 0
# amount_g = 0
#
#
# for _ in range(amount_of_fans):
#     sector = input()
#     if sector not in TYPE_OF_SECTORS:
#         print("Invalid sector")
#
#     if sector == "A":
#         amount_a += 1
#     elif sector == "B":
#         amount_b += 1
#     elif sector == "V":
#         amount_v += 1
#     else:
#         amount_g += 1
#
# stadiumFillRate = (amount_a + amount_b + amount_g + amount_v) / stadium_capacity * 100
#
# print(f"{amount_a / amount_of_fans * 100:.2f}%")
# print(f"{amount_b / amount_of_fans * 100:.2f}%")
# print(f"{amount_v/amount_of_fans*100:.2f}%")
# print(f"{amount_g / amount_of_fans * 100:.2f}%")
# print(f"{stadiumFillRate:.2f}%")

# #Extra7
# import sys
# amount_of_pairs = int(input())
#
# sum_in_pair = 0
# previous_sum = 0
# max_difference = 0
#
# if amount_of_pairs == 0:
#     print("We have no pairs")
#     sys.exit()
# else:
#     number1 = int(input())
#     number2 = int(input())
#
# previous_sum = number1 + number2
#
# for _ in range(amount_of_pairs - 1):
#     number1 = int(input())
#     number2 = int(input())
#     sum_in_pair = number1 + number2
#
#     if previous_sum != sum_in_pair:
#         current_difference = abs(sum_in_pair - previous_sum)
#         if max_difference < current_difference:
#             max_difference = current_difference
#
#     previous_sum =  sum_in_pair
#
# if max_difference == 0:
#     print(f"Yes, value={previous_sum}")
# else:
#    print(f"No, maxdiff={max_difference}")


#Extra8

for hour in range(0, 24):
    for minute in range(0, 60):
        for seconds in range(0, 60):
            print(f"{hour} : {minute} : {seconds}")