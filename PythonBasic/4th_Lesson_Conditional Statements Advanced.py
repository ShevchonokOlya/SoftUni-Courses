# #2
# budget = float(input().replace(',', '.'))
# typeOfTicket = input().replace(' ', '').lower()
# countOfPeople = int(input().replace(',', '.'))
# 
# if countOfPeople <= 4:
#     partOfBudgetStays = 0.25
# elif countOfPeople <= 9:
#     partOfBudgetStays = 0.4
# elif countOfPeople <= 24:
#     partOfBudgetStays = 0.5
# elif  countOfPeople <= 49:
#     partOfBudgetStays = 0.6
# else:
#     partOfBudgetStays = 0.75
# 
# enoughtBudget: bool = True
# 
# priceForTicket = 249.99 if typeOfTicket == "normal" else 499.99
# 
# budget = budget*partOfBudgetStays - priceForTicket * countOfPeople
# 
# if budget >= 0:
#     print(f"Yes! You have {format(budget, '.2f')} leva left.")
# else:
# 
#     print(f"Not enough money! You need {format(budget.__abs__(),'.2f')} leva.")

# #3
# juniorCyclist = int(input().replace(' ', ''))
# seniorCyclist = int(input().replace(' ', ''))
# typeOfRoadTrail = input().replace(' ', '').lower()
#
# TaxDecreasing = 0.75 if (typeOfRoadTrail == "cross-country"
#                          and (juniorCyclist + seniorCyclist) >= 50) else 1
#
# Expenses = 0.95
#
#
# Taxes_data = {
#     "juniors": {
#         "trail": 5.50,
#         "cross-country": 8,
#         "downhill": 12.25,
#         "road": 20
#     },
#     "seniors": {
#         "trail": 7,
#         "cross-country": 9.50,
#         "downhill": 13.75,
#         "road": 21.50
#     }
# }
#
#
# budget = ((Taxes_data["juniors"][typeOfRoadTrail] * juniorCyclist
#           + Taxes_data["seniors"][typeOfRoadTrail] * seniorCyclist)
#         * Expenses * TaxDecreasing)
#
#
# print(format(budget, '.2f'))

# #4
# hrizCounnt = int(input().replace(' ', ''))
# roseCount = int(input().replace(' ', ''))
# tulipCount = int(input().replace(' ', ''))
# season = input().replace(' ', '').lower()
# if season == "spring" or season == "summer" :
#     typeOfSeason = "WarmSeason"
# elif season == "autumn" or season ==  "winter":
#     typeOfSeason = "ColdSeason"
#
# increasingСoefficient = 1.15 if input().replace(' ', '').lower() == "y" else 1
#
# ArrangingPrice = 2
# FlowerPrice = {
#      "WarmSeason": {
#          "Hriz" : 2,
#          "Rose" : 4.10,
#          "Tulip" : 2.50
#      },
#     "ColdSeason" : {
#          "Hriz" : 3.75,
#          "Rose" : 4.5,
#         "Tulip": 4.15
#     }
# }
#
#
#
# if tulipCount + roseCount + hrizCounnt >= 20:
#     saleForAmount = 0.8
# else:
#     saleForAmount = 1
#
# if roseCount >= 10 and season == "winter":
#     saleForRoses = 0.9
# else:
#     saleForRoses = 1
#
# if tulipCount > 7 and season == "spring":
#     saleFortulip = 0.95
# else:
#     saleFortulip = 1
#
#
# price = ((hrizCounnt*FlowerPrice[typeOfSeason]["Hriz"]
#          + roseCount*FlowerPrice[typeOfSeason]["Rose"]
#          + tulipCount*FlowerPrice[typeOfSeason]["Tulip"])
#          * increasingСoefficient
#          * saleForAmount*saleForRoses*saleFortulip
#          + ArrangingPrice)
#
#
# print(format(price, '.2f'))

# #5
# # Seasons = ["Summer", "Winter"]
# # TypeOfACar = [ "Cabrio" , "Jeep"]
# # Class = ["Economy class", "Compact class",  "Luxury class"]
#
# budget = float(input().replace(',', '.'))
# theSeason = input()
#
# if budget <= 100:
#     classOfACar = "Economy class"
#     if theSeason == "Summer":
#         typeOfACar = "Cabrio"
#         priceCoefficient = 0.35
#     elif theSeason == "Winter":
#         typeOfACar = "Jeep"
#         priceCoefficient = 0.65
# elif budget < 500:
#     classOfACar = "Compact class"
#     if theSeason == "Summer":
#         typeOfACar = "Cabrio"
#         priceCoefficient = 0.45
#     elif theSeason == "Winter":
#         typeOfACar = "Jeep"
#         priceCoefficient = 0.8
# else:
#     classOfACar = "Luxury class"
#     typeOfACar = "Jeep"
#     priceCoefficient = 0.9
#
# print(classOfACar)
# print(f"{typeOfACar} - {priceCoefficient*budget:.2f}")

# #11
#
# results = []
#
# while True:
#     inputNumer = float(input().replace(',', '.'))
#
#     if inputNumer < 0:
#         results.append("Negative number!")
#         break
#     else:
#         results.append(f"Result: {(inputNumer*2):.2f}")
#         continue
#
# for result in results:
#     print(result)

#10

#for i in range(1,11): print(i)

# #6
#
# budget = float(input().replace(',', '.'))
# theSeason = input()
#
# if budget <= 1000:
#     classOfAHotel = "Camp"
#     if theSeason == "Summer":
#         typeOfAPlace = "Alaska"
#         priceCoefficient = 0.65
#     elif theSeason == "Winter":
#         typeOfAPlace = "Morocco"
#         priceCoefficient = 0.45
# elif budget > 1000 and budget <= 3000:
#     classOfAHotel = "Hut"
#     if theSeason == "Summer":
#         typeOfAPlace = "Alaska"
#         priceCoefficient = 0.8
#     elif theSeason == "Winter":
#         typeOfAPlace = "Morocco"
#         priceCoefficient = 0.6
# else:
#     classOfAHotel =  "Hotel"
#     if theSeason == "Summer":
#         typeOfAPlace = "Alaska"
#     elif theSeason == "Winter":
#         typeOfAPlace = "Morocco"
#     priceCoefficient = 0.9
#
# print(f"{typeOfAPlace} - {classOfAHotel} - {priceCoefficient * budget:.2f}")



# #7
# theSeason = input()
# kilometers = float(input().replace(',', '.'))
# Taxes = 0.9
#
# if kilometers <= 5000:
#     if theSeason == "Spring" or theSeason == "Autumn":
#         priceFORkm = 0.75
#     elif theSeason == "Summer":
#         priceFORkm = 0.9
#     elif theSeason == "Winter":
#         priceFORkm = 1.05
# elif kilometers > 5000 and kilometers <= 10000:
#     if theSeason == "Spring" or theSeason == "Autumn":
#         priceFORkm = 0.95
#     elif theSeason == "Summer":
#         priceFORkm = 1.1
#     elif theSeason == "Winter":
#         priceFORkm = 1.25
# else:
#     priceFORkm = 1.45
#
# print(f"{priceFORkm * 4 * kilometers * Taxes:.2f}")

# #8
# theSeason = input()
# typeOfaGroup = input()
# countOfChildren = int(input().replace(',', '.'))
# countOfNights = int(input().replace(',', '.'))
#
# if countOfChildren >= 50:
#         priceSale = 0.5
# elif countOfChildren >=20  and countOfChildren < 50:
#         priceSale = 0.85
# elif countOfChildren >=10  and countOfChildren < 20:
#     priceSale = 0.95
# else:
#     priceSale = 1
#
# if typeOfaGroup == 'girls':
#     if theSeason == 'Winter':
#         dailyTax = 9.6
#         typeOfaSport = "Gymnastics"
#     elif theSeason == 'Spring':
#         dailyTax = 7.2
#         typeOfaSport = "Athletics"
#     elif theSeason == 'Summer':
#         dailyTax = 15
#         typeOfaSport = "Volleyball"
#
# elif typeOfaGroup == 'boys':
#     if theSeason == 'Winter':
#         dailyTax = 9.6
#         typeOfaSport = "Judo"
#     elif theSeason == 'Spring':
#         dailyTax = 7.2
#         typeOfaSport = "Tennis"
#     elif theSeason == 'Summer':
#         dailyTax = 15
#         typeOfaSport = "Football"
#
# elif typeOfaGroup == 'mixed':
#     if theSeason == 'Winter':
#         dailyTax = 10
#         typeOfaSport = "Ski"
#     elif theSeason == 'Spring':
#         dailyTax = 9.5
#         typeOfaSport = "Cycling"
#     elif theSeason == 'Summer':
#         dailyTax = 20
#         typeOfaSport = "Swimming"
# else:
#     dailyTax = 0
#     print("Mistake")
#
# price = dailyTax * countOfNights * countOfChildren * priceSale
#
# print(f"{typeOfaSport} {price:.2f} lv.")

# #9
# x1 = float(input().replace(',', '.'))
# y1 = float(input().replace(',', '.'))
# x2 = float(input().replace(',', '.'))
# y2 = float(input().replace(',', '.'))
#
# targetX = float(input().replace(',', '.'))
# targetY = float(input().replace(',', '.'))
#
# if (targetX in [x1, x2] and (targetY >= y1 and targetY <= y2)) or (targetY in [y1, y2] and (targetX >= x1 and targetX <= x2)):
#     print("Border")
# else:
#     print("Inside / Outside")


#9
# hallRent = int(input().replace(',', '.'))
# statuetki = 0.7*hallRent
# keitering = 0.85*statuetki
# saunDesign = 0.5*keitering
#
# total_price = hallRent + statuetki + keitering + saunDesign
# print(format(total_price, '.2f'))
#
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
