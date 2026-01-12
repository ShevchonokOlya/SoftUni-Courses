# try:
#     B1 = float(input( ).replace(',','.'))
#     B2 = float(input( ).replace(',','.'))
#     H = float(input().replace(',','.'))
#
#     # print("Area of your shape is (float) ", float((B1 + B2) * H / 2))
#     print(format(float((B1 + B2) * H / 2), '.2f'))
#     # print(round(float((B1 + B2) * H / 2),2))
#
# except ValueError as e:
#     print(f"You input wrong simbol. Reasoning- {e}")
#
# B1 = float(input( ).replace(',','.'))
# B2 = float(input( ).replace(',','.'))
# H = float(input( ).replace(',','.'))
#
# print(format(float((B1 + B2) * H / 2), '.2f'))
import math

# side = float(input( ).replace(',','.'))
# H = float(input( ).replace(',','.'))
#
# print(format(float(side * H / 2), '.2f'))

# for i in range(1, 5):
#     C = float(input( ).replace(',','.'))
#     print(format(float((C * 9 / 5) + 32), '.2f'))


# vegetables_price = float(input( ).replace(',','.'))
# fruits_price = float(input( ).replace(',','.'))
# vegetables_veight = int(input( ).replace(',','.'))
# fruits_veight = int(input( ).replace(',','.'))
# common_veg_price = float(vegetables_price * vegetables_veight)
# common_fruit_price = float(fruits_price * fruits_veight)
# price = common_veg_price + common_fruit_price
# print(format(float(price/1.94), '.2f'))

# width = float(input().replace(',','.'))
# heigh = float(input().replace(',','.'))
#
# if width <= 100:
#     if width >= heigh:
#         if heigh >= 3:
#             table_count_H = int((heigh * 100 - 100) // 70)
#             table_count_W = int((width * 100) // 120)
#             print(int(table_count_H * table_count_W - 3))

# # skumbria
# mackerel_1kg = float(input( ).replace(',','.'))
# # caca
# sprinkle_1kg = float(input( ).replace(',','.'))
# # palamud
# bonito_weight = float(input( ).replace(',','.'))
# bonito_1kg = mackerel_1kg * 1.6
# # safrid
# safrid_weight = float(input( ).replace(',','.'))
# safrid_1kg = sprinkle_1kg * 1.8
# # midi
# mussels_weight = int(input().replace(',', '.'))
# mussels_1kg = 7.5
#
# bonito_price = float(bonito_weight*bonito_1kg)
# safrid_price = float(safrid_weight*safrid_1kg)
# mussels_price = float(mussels_weight*mussels_1kg)
#
#
# common_price = bonito_price + safrid_price + mussels_price
# print(format(common_price, '.2f'))

# # x
# house_width = float(input().replace(',','.'))
# # y
# house_length = float(input().replace(',','.'))
# # h
# house_roof_heigh = float(input().replace(',','.'))
#
# green_paint_consumption = 3.4
# red_paint_consumption = 4.3
#
# common_sq_G = (house_width * house_length  + house_width ** 2)*2 - 1.2*2 - 1.5*1.5*2
# green_paint_L= common_sq_G/green_paint_consumption
# common_sq_R = house_width * house_roof_heigh + 2*house_width * house_length
# red_paint_L = common_sq_R/red_paint_consumption
#
# print(format(green_paint_L, '.2f'))
# print(format(red_paint_L, '.2f'))

# weather_string = input()
#
# if "sunny" in weather_string:
#     print("It's warm outside!")
# else:
#     print("It's cold outside!")
#




# for i in range(1, 4):
#
#     weather = float(input())
#     i = i+1
#     if weather >= 5.00 and weather <= 11.9:
#         print("Cold")
#     elif weather >= 12.00 and weather <= 14.9:
#         print("Cool")
#     elif weather >= 15.00 and weather <= 20:
#         print("Mild")
#     elif weather >= 20.1 and weather <= 25.9:
#         print("Warm")
#     elif weather >= 26 and weather <= 35:
#         print("Hot")
#     else:
#         print("unknown")


import math
r = float(input().replace(',','.'))
Pi = math.pi
area = Pi * r * r
perimeter = 2 * Pi * r
print(format(area, '.2f'))
print(format(perimeter, '.2f'))

print("Hello SoftUni")

#1
# grade = float(input().replace(',','.'))
#
# if (grade >= 5.5):
#     print("Excellent!")
import math

# #2
# firstNumber = int(input())
# secondNumber = int(input())
# if firstNumber >= secondNumber:
#     print(firstNumber)
# else :
#     print(secondNumber)


# #3
# theNumber = int(input())
#
# if theNumber%2 == 0:
#     print('even')
# else :
#     print('odd')

# #4
# passTry =  input()
# PasswordStencil = "s3cr3t!P@ssw0rd"
# if passTry == PasswordStencil:
#     print("Welcome")
# else :
#     print( "Wrong password!")

# #5
# theNumber = int(input())
#
# if theNumber > 200:
#     print("Greater than 200")
# elif theNumber >= 100 and theNumber <= 200 :
#     print("Between 100 and 200")
# else:
#     print("Less than 100")

# #6
# theNumber = float(input())
#
# if theNumber > 1000:
#     print("extremely fast")
# elif theNumber > 150 and theNumber <= 1000:
#     print("ultra fast" )
# elif theNumber > 50 and theNumber <= 150:
#     print("fast")
# elif theNumber > 10 and theNumber <= 50 :
#     print("average" )
# else:
#     print("slow")

# # 6
# import math
# typeOfFigure = input().replace(' ', '.').lower()
#
# Square = 'square'
# Rectangle = 'rectangle'
# Circle = 'circle'
# Triangle = 'triangle'
#
#
# if typeOfFigure == Square:
#     theNumber = float(input().replace(',', '.'))
#     print(format(theNumber**2,'.3f'))
#
# elif typeOfFigure == Rectangle:
#     theNumber1 = float(input().replace(',', '.'))
#     theNumber2 = float(input().replace(',', '.'))
#
#     print(format(theNumber1 * theNumber2, '.3f'))
#
# elif typeOfFigure == Circle:
#     theNumber = float(input().replace(',', '.'))
#     print(format(theNumber**2 * math.pi,'.3f'))
#
# elif typeOfFigure == Triangle :
#     theNumber1 = float(input().replace(',', '.'))
#     theNumber2 = float(input().replace(',', '.'))
#
#     print(format((theNumber1 * theNumber2)/2, '.3f'))
# else:
#     print("Wrong Input")

# name_arc = input()
# projects = int(input())
# hours =  projects * 3
# print(f"The architect {name_arc} will need {hours} hours to complete {projects} project/s.")


#
# dogsFood = int(input( ))
# catsFood = int(input( ))
#
# print(f"{float(dogsFood*2.5+ catsFood*4)} lv.")

# square = float(input( ).replace(',','.'))
# price = (square*7.61)
#
# sale_price =  price * 0.18
# final_price =  price - sale_price
#
# print(f"The final price is: {round(final_price, 2)} lv.")
# print(f"The discount is: {round(sale_price,2)} lv.")