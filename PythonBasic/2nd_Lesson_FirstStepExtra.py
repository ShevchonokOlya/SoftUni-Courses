#1
# import re
#
# V = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# P1_per_hour = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# P2_per_hour = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# hours = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#
# volume_from_p1 = P1_per_hour*hours
# volume_from_p2 = P2_per_hour*hours
# total_volume = volume_from_p1 + volume_from_p2
#
# if total_volume <= V:
#     pool_filling_in_percent = total_volume/V*100
#     percent_from_p1 = round(volume_from_p1/total_volume*100, 2)
#     percent_from_p2 = round(volume_from_p2/total_volume*100, 2)
#     print(f"The pool is {pool_filling_in_percent}% full. Pipe 1: {percent_from_p1}%. Pipe 2: {percent_from_p2}%.")
# elif total_volume > V:
#     litres_overflowing = total_volume - V
#     print(f"For {hours} hours the pool overflows with {litres_overflowing} liters.")
import math
# # 2
# import re
# import math
#
# Work_day_time = 63
# Weekend_play_time = 127
# DAYS_PER_YEAR = 365
# Total_amount_per_year = 30000
#
# count_of_weekends = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# count_of_working_days = DAYS_PER_YEAR-count_of_weekends
# amount_of_play_time = Weekend_play_time*count_of_weekends + Work_day_time*count_of_working_days
#
# dif = Total_amount_per_year - amount_of_play_time
# sleep = False
#
# if dif > 0:
#     sleep = True
# else:
#     dif = math.fabs(dif)
#
# h = int(dif//60)
# min = int(dif%60)
# if sleep:
#     print("Tom sleeps well")
#     print(f"{h} hours and {min} minutes less for play")
# else:
#     print("Tom will run away")
#     print(f"{h} hours and {min} minutes more for play")


# # 3
# import re
# import math
#
#
# x = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# part_of_harvest = x*0.4
# y = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# amount_of_grapes = y*part_of_harvest
# amount_of_wine = amount_of_grapes/2.5
# z = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# dif = amount_of_wine-z
#
# w = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#
# # math.floor(): округляет в меньшую сторону (например, math.floor(3.14) будет 3, а math.floor(-3.14) будет -4).
# # math.ceil(): округляет в большую сторону (например, math.ceil(3.14) будет 4, а math.ceil(-3.14) будет -3).
#
# if dif<0:
#     dif = math.fabs(dif).__floor__()
#     print(f"It will be a tough winter! More {dif} liters wine needed.")
#     # закръглен към по-ниско цяло число
# else:
#     amount_of_wine =  amount_of_wine.__floor__()
#     dif = dif.__ceil__()
#     litres_per_worker = (dif / w).__ceil__()
#     print(f"Good harvest this year! Total wine: {amount_of_wine} liters.") #закръглен към по-ниско цяло число
#     print(f"{dif} liters left -> {litres_per_worker} liters per person.") #закръглени към по-високото цяло число


# kilometers = int(input())
# part_of_the_day =  input()
#
# Taxi_start = 0.7
# Taxi_night_price = 0.9
# Taxi_day_price = 0.79
#
# Bus_price_per_km = 0.09
# Bus_min_km = 20
# bus_available = kilometers >= Bus_min_km
#
# Train_price_per_km: float = 0.06
# Train_min = 100
# train_available = kilometers >= Train_min
#
# price_list = list()
#
# if part_of_the_day == "night":
#      taxi_price = Taxi_start + Taxi_night_price*kilometers
#
# else :
#      taxi_price = Taxi_start + Taxi_day_price*kilometers
#
# price_list.append(taxi_price)
#
# if train_available:
#     train_price = kilometers*Train_price_per_km
#     price_list.append(train_price)
#
# if bus_available:
#     bus_price = kilometers*Bus_price_per_km
#     price_list.append(bus_price)
#
# price_list.sort()
#
# print(format(price_list[0],'.2f'))

# # 5
# import re
# import math
#
# day_amount = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# food_stays_for_pets = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# dog_food_per_day = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# cat_food_per_day = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# turt_food_per_day = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))/1000
#
# dog_will_eat = dog_food_per_day*day_amount
# cat_will_eat = cat_food_per_day*day_amount
# turt_will_eat = turt_food_per_day*day_amount
# animals_ate = dog_will_eat + cat_will_eat + turt_will_eat
#
# kilogram_of_food =  (food_stays_for_pets - animals_ate)
#
# if animals_ate < food_stays_for_pets:
#     kilogram_of_food = kilogram_of_food.__floor__()
#     print(f"{kilogram_of_food} kilos of food left.")
#
# else:
#     kilogram_of_food = math.fabs(kilogram_of_food).__ceil__()
#     print(f"{kilogram_of_food} more kilos of food are needed.")


# # 6
# import re
# import math
#
# magnolii_amount = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# zyumbuli_amount = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# roses_amount = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# cactus_amount = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# money_in_the_wallet = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#
# Magn_price = 3.25
# Zyumb_price = 4
# Roses_price = 3.5
# Cactus_price = 8
# Taxes = 0.95 #5%
#
#
# price_for_all_flowers = (Magn_price * magnolii_amount + Zyumb_price * zyumbuli_amount
#                          + roses_amount * Roses_price + cactus_amount*Cactus_price)*Taxes
#
# if price_for_all_flowers >= money_in_the_wallet:
#     money = (math.fabs(money_in_the_wallet - price_for_all_flowers)).__floor__()
#     print(f"She is left with {money} leva.")
#
# else:
#     money = (money_in_the_wallet - price_for_all_flowers).__ceil__()
#     print(f"She will have to borrow {money} leva.")

# # 7
# import re
#
# type_of_fuel =  input() #Diesel Gasoline Gas
# fuel_amount_in_vehical = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#
# Critical_level_of_fuel = 25
# TypesOfFuel = ["Diesel", "Gasoline" , "Gas"]
#
# if type_of_fuel in TypesOfFuel:
#     if fuel_amount_in_vehical >= Critical_level_of_fuel:
#         print(f"You have enough {type_of_fuel.lower()}.")
#
#     else:
#         print(f"Fill your tank with {type_of_fuel.lower()}!")
# else:
#     print("Invalid fuel!")

# # 8
# import re
#
# type_of_fuel =  input().lower() #Diesel Gasoline Gas
# fuel_amount = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# card_for_loyal_client =  input()
#
# card = True if card_for_loyal_client.lower() == 'yes' else False
#
# Gas_price_per_l = 0.93
# Gas_sale = 0.08
#
# Diesel_price_per_l = 2.33
# Diesel_sale = 0.12
#
# Gasoline_price_per_l = 2.22
# Gasoline_sale = 0.18
#
# TypesOfFuel = ["diesel", "gasoline", "gas"]
#
# if type_of_fuel in TypesOfFuel:
#     if type_of_fuel == 'gas':
#         price_per_l = Gas_price_per_l
#         if card:
#             price_per_l -= Gas_sale
#
#     elif type_of_fuel == 'gasoline':
#         price_per_l = Gasoline_price_per_l
#         if card:
#             price_per_l -= Gasoline_sale
#     else:
#         price_per_l = Diesel_price_per_l
#         if card:
#             price_per_l -= Diesel_sale
#
#
#
#     if fuel_amount > 25:
#         fuelDiscountFactor = 0.9
#     elif fuel_amount >= 20 and fuel_amount <= 25:
#         fuelDiscountFactor = 0.92
#     else:
#         fuelDiscountFactor = 1
#
#     final_price = format(fuel_amount * price_per_l*fuelDiscountFactor, '.2f')
#
#     print(f"{final_price} lv.")
# else:
#     print("Invalid fuel!")

