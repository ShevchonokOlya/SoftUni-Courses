# #1
# KURS_USD_TO_BGN = 1.79549
# usd = float(input().replace(',','.'))
# bgn = usd * KURS_USD_TO_BGN
# print(bgn)

# #2
# for i in range(0, 3, +1):
#     import math
#     rad = float(input().replace(',','.'))
#     degrees = rad*180/math.pi
#     print(f"{degrees}")

# #3
# # сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
# dep_sum = float(input().replace(',','.'))
# period= int(input())
# persent = float(input().replace(',','.'))/100
#
# for i in range(0, 2, +1):
#
#     result =  dep_sum+ period*((dep_sum*persent)/12)
#     print(result)

# #4
# import re
# for i in range(0, 3, +1):
#
#     pages_in_book =  int(re.sub(r'[^\d\.]', '', input().replace(',','.')))
#     pages_per_day  = int(re.sub(r'[^\d\.]', '', input().replace(',','.')))
#     days = int(re.sub(r'[^\d\.]', '', input().replace(',','.')))
#     hours = pages_in_book//pages_per_day//days
#     print( hours )

# # 5
# import re
# HIM = 5.8
# MAR = 7.2
# PREP_per_L = 1.2
# for i in range(0, 3, +1):
#     count_of_HIM = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#     count_of_MAR = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#     litres = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#     discount_percent = float(re.sub(r'[^\d\.]', '', input().replace(',', '.')))/100
#     price1  =count_of_HIM*HIM+count_of_MAR*MAR+PREP_per_L*litres
#     price1 -= price1*discount_percent
#
#     print(price1)

# import re
#
# HIM = 5.8
# MAR = 7.2
# PREP_per_L = 1.2
# count_of_HIM = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# count_of_MAR = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# litres = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# discount_percent = float(re.sub(r'[^\d\.]', '', input().replace(',', '.'))) / 100
# price = count_of_HIM * HIM + count_of_MAR * MAR + PREP_per_L * litres
# price -= price * discount_percent
#
# print(price)

# # 6
# import re
# NEYLON_price = 1.5 #+2
# Paint_price = 14.5 #*1.1
# Razred_per_L_price = 5
# bag_price = 0.4
#
# for i in range(0, 3, +1):
#     count_of_NEYLON= int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#     count_of_Paint = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#     count_Razred_litres = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#     count_of_hours_work = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#
#     sum_neylon =  (count_of_NEYLON + 2) * NEYLON_price
#     sum_paint = (count_of_Paint * 1.1) * Paint_price
#     sum_razred =  (Razred_per_L_price*count_Razred_litres)
#
#     sum_for_materials =  float(sum_neylon + sum_razred + sum_paint + bag_price)
#     master_salary = sum_for_materials * 0.3 *  count_of_hours_work
#
#     total_price  =  master_salary + sum_for_materials
#
#     print(total_price)

# # 7
# import re
# Chicken_menu = 10.35
# Fish_menu = 12.4
# Veg_menu = 8.15
# Delivery = 2.5
# Desert_proposal = 1.2 #+20% to total price
#
# for i in range(0, 3, +1):
#     count_of_chicken_menu= int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#     count_of_Fish_menu = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#     count_of_Veg_menu = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
#
#     sum_menu = count_of_Veg_menu*Veg_menu + count_of_Fish_menu*Fish_menu+count_of_chicken_menu*Chicken_menu
#     sum_menu *= Desert_proposal
#     sum_menu += Delivery
#     print(format(sum_menu, '.2f'))

# # 8
# import re
#
# tax_per_year = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
# Sneakers_price = 0.6*tax_per_year # 60% from year price
# Clothes = 0.8*Sneakers_price # 80% from sneakers price
# Ball = 0.25*Clothes
# Accessories = 0.2 * Ball
#
# total_price  = tax_per_year + Sneakers_price + Clothes + Accessories + Ball
#
# print(total_price)

# 9
import re

length = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
width = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
height = int(re.sub(r'[^\d\.]', '', input().replace(',', '.')))
percent  = 1 - float(input().replace(',', '.')) /100

total_volume  = length * width * height/1000 * percent #litres

print(total_volume)