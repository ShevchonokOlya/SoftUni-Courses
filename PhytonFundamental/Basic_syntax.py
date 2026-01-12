
# number = float(input())
# if number == 0:
#     print("zero")
# if abs(number) > 1_000_000:
#     print("large", end=" ")
# elif 0 < abs(number) < 1:
#     print("small", end=" ")
#
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")

#1  Statements and Loops - Lab - 02. Largest Of Three Numbers
#
# number_1  = int(input())
# number_2 = int(input())
# number_3 = int(input())
#
# numbers = [number_1, number_2, number_3]
# print(max(numbers))

# #1  Statements and Loops - Lab - 03. Word Reverse
# word = input()
# for i in range(len(word) - 1, -1, -1):
#     print(word[i], end="")
# print()

# #04. Even Numbers
# number_of_numbers = int(input())
# for _ in range(0, number_of_numbers ):
#     number = int(input())
#     if (number % 2 != 0):
#         print(f"{number} is odd!")
#         break
# else:
#     print(f"All numbers are even.")

#05. Number Between 1 and 100
# need_continue = True
#
# while need_continue:
#      number = float(input())
#      if 1 <= number <= 100:
#          print(f"The number {number} is between 1 and 100")
#          need_continue = False

# Shopping
# bugdet = int(input())
#
# while bugdet >=0:
#     word = input()
#     if word == "End":
#         print("You bought everything needed.")
#         break
#     else:
#         spend  = int(word)
#
#     if spend > bugdet:
#         print("You went in overdraft!")
#         break
#     else:
#         bugdet -= spend
#
# # 07. Patterns
# number = int(input())
# for stars in range(1, number + 1):
#     print("*" * stars)
# for stars_under in range(number - 1, 0, -1):
#     print("*" * stars_under)
#
# #Conditional Statements and Loops - Exercise 01. Jenny's Secret Message
# name = input()
# if name == "Johnny":
#     name = "my love"
#
# print(f"Hello, {name}!")

# #Conditional Statements and Loops - Exercise 02. Drink Something
#
# age = int(input())
# print("drink ", end="")
# if age <= 14:
#     drink = "toddy"
# elif age <= 18:
#     drink = "coke"
# elif age <= 21:
#     drink = "beer"
# else:
#     drink = "whisky"
# print(drink)

# #Conditional Statements and Loops - Exercise 03. Chat Codes
#
def chatCodes():
    numbers_count = int(input())

    for _ in range(numbers_count):
        number = int(input())
        if number == 88:
            print("Hello")
        elif number == 86:
            print("How are you?")
        elif number < 88 and number != 86:
            print("GREAT!")
        elif number > 88:
            print("Bye.")

#Conditional Statements and Loops - Exercise 04. Maximum Multiple

def maximum_multiple()-> None:
    first_int = int(input())
    second_int = int(input())
    for number in range(second_int, 0, -1):
        if number % first_int == 0:
            print(number)
            break
def orders() -> None:
    number_of_orders = int(input())
    total_price = 0.00

    for number in range(number_of_orders):
        price_per_capsule = float(input())
        days = int(input())
        capsules_per_day = int(input())
        if ((price_per_capsule < 0.01 or price_per_capsule > 100)
                or ( days < 1 or days > 31)
                or (capsules_per_day < 1 or capsules_per_day > 2000)):
            continue
        price = price_per_capsule * days * capsules_per_day

        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price
    print(f"Total: ${total_price:.2f}")

def stringPureness() -> None:
    number_of_strings = int(input())
    for _ in range(number_of_strings):
        string_of_char = input()
        prohibited_characters = ",._"
        for character in string_of_char:
            if character in prohibited_characters:
                print(f"{string_of_char} is not pure!")
                break
        else:
            print(f"{string_of_char} is pure.")

def doubleChar() -> None:
    while True:
        given_string = input()
        if given_string == "End":
            break
        elif given_string == "SoftUni":
            continue
        newWord = ""
        for character in given_string:
            newWord += character * 2
        print(newWord)

def howMuchCoffee() -> None:
    list_of_problems = ["cat", "dog","coding", "movie"]
    coffee = 0

    while True:
        listen_the_word = input()
        if listen_the_word == "END":
            break

        if listen_the_word.lower() in list_of_problems:
            if listen_the_word.isupper():
                coffee += 2
            else:
                coffee += 1
    if coffee > 5:
        print("You need extra sleep")
    else:
        print(coffee)

def sortingHat() -> None:
    while True:
        given_string = input()
        if given_string == "Welcome!":
            print("Welcome to Hogwarts.")
            break
        elif given_string == "Voldemort":
            print("You must not speak of that name!")
            break

        if len(given_string) < 5:
            print(f"{given_string} goes to Gryffindor.")
        elif len(given_string) == 5:
            print(f"{given_string} goes to Slytherin.")
        elif len(given_string) == 6:
            print(f"{given_string} goes to Ravenclaw.")
        else:
            print(f"{given_string} goes to Hufflepuff.")


def mutateStrings() -> None:
    string1 = input()
    string2 = input()
    length = len(string1)

    previous_string = string1

    for index in range(length):
        current_word  = previous_string[:index] + string2[index] + previous_string[index + 1:]
        if current_word != previous_string:
            print(current_word)
        previous_string = current_word

def easterBread() -> None:
    budget = float(input())
    flour_price = float(input())
    eggs_price = flour_price * 0.75
    milk_price = flour_price * 1.25 * 0.25
    one_bread_price = flour_price + eggs_price + milk_price
    number_of_loaves = int(budget // one_bread_price)
    count_of_eggs_loose = number_of_loaves // 3
    colored_eggs = number_of_loaves * 3
    colored_eggs_lost = count_of_eggs_loose * ( 3 * count_of_eggs_loose - 1)/2
    colored_eggs -= colored_eggs_lost
    money_left = budget - number_of_loaves * one_bread_price
    print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {int(colored_eggs)} eggs and {money_left:.2f}BGN left.")

def christmasSpirit() -> None:

    quantity = int(input())
    days = int(input())

    '''decorations = { "name" : [price, point]'''

    decorations = {
        "Ornament Set" :
            [2 , 5],
        "Tree Skirt" :
            [5 , 3] ,
        "Tree Garland" :
            [3 , 10] ,
        "Tree Lights" :
            [15 , 17]
    }
    decor_price = 0
    spirit = 0

    for day in range(1, days + 1):
        if day % 11 == 0:
            quantity += 2

        if day % 2 == 0:
            decor_price += decorations["Ornament Set"][0] * quantity
            spirit += decorations["Ornament Set"][1]

        if day % 3 == 0:
            decor_price += (decorations["Tree Skirt"][0] + decorations["Tree Garland"][0]) * quantity
            spirit += decorations["Tree Skirt"][1] + decorations["Tree Garland"][1]

        if day % 5 == 0:
            decor_price += decorations["Tree Lights"][0] * quantity
            spirit += decorations["Tree Lights"][1]

        if day % 3 == 0 and day % 5 == 0:
            spirit += 30

        if day % 10 == 0:
            if day == days:
                spirit -= 30
            spirit -= 20
            decor_price += decorations["Tree Skirt"][0] + decorations["Tree Garland"][0] + decorations["Tree Lights"][0]

    print(f"Total cost: {decor_price}")
    print(f"Total spirit: {spirit}")


def findTheLargest() -> None:
    number_list = list(input())
    number_list.sort(reverse=True)
    delimiter_space = ''

    print(delimiter_space.join(number_list))

def findTheCapitals() -> None:
    word =  input()
    list_of_upper = []
    for index in range(len(word)):
        if word[index].isupper():
            list_of_upper.append(index)
    print(list_of_upper)

def wolfInSheepsClothing() -> None:
    list_of_sheeps = list(input().replace(" ", "").split(","))
    for index , sheep  in enumerate(list_of_sheeps):
        if sheep == "wolf":
            total_sheeps = len(list_of_sheeps)
            if index == total_sheeps - 1:
                print("Please go away and stop eating my sheep")
            else:
                print(f"Oi! Sheep number {total_sheeps - index - 1 }! You are about to be eaten by a wolf!")


def sumOfABeach() -> None:
    list_of_beaches_words = ["sand", "water", "fish","sun"]
    word_input = input().lower()
    number = 0
    for word in list_of_beaches_words:
        number += word_input.count(word)
    print(number)

def concatNames() -> None:
    name1= input()
    name2 = input()
    delimiter_char = input()
    print(f'{name1}{delimiter_char}{name2}')

def convertMeterstoKilometers():
    meters = int(input())
    print(f'{meters/1000:.2f}')

def poundsToDollars():
    pounds = int(input())
    print(f'{pounds*1.31:.3f}')

def centuriesToMinutes():
    centuries = int(input())
    days = int(centuries*36524.22)
    print(f'{centuries} centuries = {centuries*100} years = {days} days = {days * 24} hours = {days * 24 * 60} minutes')

def sumOfNumbers(n: int) -> int:
    if n < 10:
        return n
    else:
        return n % 10 + sumOfNumbers(n // 10)
def specialNumbers():
    n = int(input())
    special_numbers = [5, 7, 11]
    for number in range(1, n+1):
        sum = sumOfNumbers(number)
        if sum in special_numbers:
            parametr = True
        else:
            parametr = False

        print(f"{number} -> {parametr}")


def nextHappyYear() -> None:
    year_counter = int(input())
    while True:
        year_counter += 1
        year_str = str(year_counter)
        year_set = set(year_str)
        if len(year_set)  != len(year_str):
            continue
        else:
            print(year_str)
            break



def nextHappyYear1() -> None:
    year_counter = int(input())
    year_counter += 1
    year_str = str(year_counter)
    while True:
        need_new_start = False

        for start_index in range(len(year_str) - 1):
            for next_index in range(start_index + 1, len(year_str)):
                if year_str[start_index] == year_str[next_index]:
                    need_new_start = True
                    new_number = year_str[:next_index+1]
                    new_n  = int(new_number) + 1
                    zeros_needed = len(year_str) - len(str(new_number))
                    year_str = str(new_n) + "0" * zeros_needed
                    break
            if need_new_start:
                break
        if not need_new_start:
            print(year_str)
            break

def integerOperations()-> None:
    input_number1 = int(input())
    input_number2 = int(input())
    input_number3 = int(input())
    input_number4 = int(input())
    result = (input_number1 + input_number2)//input_number3*input_number4
    print(result)

def charstoString() -> None:
    word = input() + input() + input()
    print(word)

def elevator():
    number_of_students = int(input())
    number_of_places = int(input())
    count_of_courses = number_of_students // number_of_places
    if number_of_students % number_of_places != 0:
        count_of_courses += 1
    print(count_of_courses)

def sumofChars():
    number_of_chars = int(input())
    sum = 0
    for _ in range(number_of_chars):
        sum += ord(input())
    print(f"The sum equals: {sum}")

def asciiTable():
    startNumber = int(input())
    endNumber = int(input())

    for char_num in range(startNumber, endNumber + 1):
        print(chr(char_num), end = " ")
    print()

def triplesOfLatinLetters():
    num = int(input())
    for i in range (0, num):
        for j in range (0, num):
            for k in range (0, num):
                print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")


def waterOverflow():
    num = int(input())
    WATER_TANK = 255
    current_amount = 0

    for _ in range(0, num):
        litres = int(input())
        if litres <= WATER_TANK - current_amount:
            current_amount += litres
        else:
            print("Insufficient capacity!")
    print(current_amount)


def partyProfit():
    group_size = int(input())
    days = int(input())
    profit = 0

    for day in range(1, days + 1):
        if day % 10 == 0:
            group_size -= 2
        if day % 15 == 0:
            group_size += 5

        profit += 50
        profit -= 2 * group_size

        if day % 3 == 0:
            profit -= 3 * group_size
        if day % 5 == 0:
            profit += 20 * group_size
            if day % 3 == 0:
                profit -= 2 * group_size


    print(f"{group_size} companions received {int(profit/group_size)} coins each.")

def snowballs():
    import sys
    number_of_snowballs = int(input())
    highest_value = - sys.maxsize
    for _ in range(0, number_of_snowballs):
        snowball_weight = int(input())
        snowball_time = int(input())
        snowball_quality = int(input())
        snowball_value = (snowball_weight // snowball_time) ** snowball_quality

        if snowball_value > highest_value:
            max_snowball_value = snowball_value
            max_snowball_weight = snowball_weight
            max_snowball_time = snowball_time
            max_snowball_quality = snowball_quality
            highest_value = snowball_value

    print(f"{max_snowball_weight} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})")

def gladiatorExpenses():
    lost_fights_count = int(input())
    helmet_price = float(input())
    sword_price = float(input())
    shield_price = float(input())
    armor_price = float(input())

    count_of_helmets = lost_fights_count // 2
    count_of_swords = lost_fights_count // 3
    count_of_shields = lost_fights_count // 6
    count_of_armors = count_of_shields // 2

    expenses = (helmet_price*count_of_helmets + sword_price*count_of_swords
                + shield_price*count_of_shields + armor_price * count_of_armors)

    print(f"Gladiator expenses: {expenses:.2f} aureus")


def exchangeIntegers() -> None:
    number_1 = int(input())
    number_2 = int(input())
    print(f"Before:\na = {number_1}\nb = {number_2}")

    number_1 , number_2 = number_2 , number_1
    print(f"After:\na = {number_1}\nb = {number_2}")

def primeNumber():
    number = int(input())
    itIsPrime = True
    if number <= 1:
        itIsPrime = False
    else:
        for i in range(2, number):
            if number % i == 0 and i != number:
                itIsPrime = False

    print(itIsPrime)

def decryptingMessages():
    key = int(input())
    number_lines = int(input())
    chars = []
    for _ in range(0, number_lines):
        chars.append(chr(ord(input()) + key))
    print("".join(chars))

def balancedBrackets():
    number_lines = int(input())
    bracket_open = False
    for _ in range(0, number_lines):
        current_line = input()
        #if bracket was open
        if current_line == "(":
            # if bracket was open on the previous step and it is one more opening
            if bracket_open:
                break
            bracket_open = True
            continue
        # if bracket was open AND closed

        if bracket_open and current_line == ")":
            bracket_open = False
            continue

        # if bracket wasN't (!!) open BUT was closed
        if not bracket_open and current_line == ")":
            bracket_open = True
            break

    if bracket_open:
        print("UNBALANCED")
    else:
        print("BALANCED")

def strangeZoo():
    tail = input()
    body = input()
    head = input()
    meerkat = [tail, body, head]
    meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
    print(meerkat)

def courses():
    number_lines = int(input())
    course =[]
    for _ in range(0, number_lines):
        course.append(input())
    print(course)

def listStatistics():
    number_lines = int(input())
    positive = []
    negative = []
    for _ in range(0, number_lines):
        number = int(input())
        positive.append(number) if number >= 0 else negative.append(number)

    print(positive)
    print(negative)
    print(f"Count of positives: {len(positive)}\nSum of negatives: {sum(negative)}")

def search_f():
    number_lines = int(input())
    word = input()
    sentances = []
    for _ in range(0, number_lines):
        sentances.append(input())
    print(sentances)

    for i in range(len(sentances) - 1, -1, -1):
        if word not in sentances[i]:
            sentances.pop(i)
    print(sentances)




def numbersFilter():
    number_lines = int(input())
    numbers = []
    filtered = []
    for _ in range(0, number_lines):
        numbers.append(int(input()))

    key_word = input()

    match key_word:
        case "even":
            filtered = list(filter(lambda x: x % 2 == 0, numbers))
        case "odd":
            filtered =  list(filter(lambda x: x % 2 == 1, numbers))
        case "negative":
            filtered =  list(filter(lambda x: x < 0, numbers))
        case "positive":
            filtered =  list(filter(lambda x: x >= 0, numbers))
    print(filtered)

def split_func():
    number_lines =  input()
    list_of_string_numbers = number_lines.split(" ")
    new_list_of_numbers = [int(number)*(-1) for number in list_of_string_numbers]

    print(new_list_of_numbers)

def multiplesList():
    factor = int(input())
    count = int(input())
    newlist = list(range(factor, count*factor + 1, factor))
    print(newlist)

def footballCards():
    theGame = input().split()
    teamA = list(range(1, 12))
    teamB = list(range(1, 12))
    gameWasTerm = False
    for card in theGame:
        card_date = card.split("-")
        player_number = int(card_date[1])

        if "A" in card:
            if player_number in teamA:
                teamA.remove(player_number)
        else:
            if player_number in teamB:
                teamB.remove(player_number)
        if len(teamA) < 7 or len(teamB) < 7:
            gameWasTerm = True
            break

    print(f"Team A - {len(teamA)}; Team B - {len(teamB)}")
    if gameWasTerm:
        print("Game was terminated")

def numberBeggars():
    money_pockets = input().split(", ")
    count_of_beggars = int(input())
    pockets = [0]*count_of_beggars
    for beggar_number in range(len(money_pockets)):
        number_of_pocket = beggar_number%count_of_beggars
        pockets[number_of_pocket] += int(money_pockets[beggar_number])
    print(pockets)


def faroShuffle():
    string_of_cards = input().split()
    number_of_shuffles = int(input())


    for shuffle in range(number_of_shuffles):
        result_list = []
        middle = len(string_of_cards)//2
        left_list = string_of_cards[:middle]
        right_list = string_of_cards[middle:]

        for index in range(0, len(left_list)):
            result_list.append(left_list[index])
            result_list.append(right_list[index])

        string_of_cards = result_list

    print(string_of_cards)

def survivaloftheBiggest():
    number_lines = input().split()
    n = int(input())
    number_list = [int(number) for number in number_lines]
    for _ in range(n):
        number_list.remove(min(number_list))
    print(", ".join(map(str, number_list)))



def easterGifts():
    gifts = list(input().split())
    while True:
        command  = input()
        if command == "No Money":
            break
        string_of_command = command.split(" ")
        command_name = string_of_command[0]
        present = string_of_command[1]
        if command_name == "OutOfStock":
            for numb in range(len(gifts)):
                if gifts[numb] == present:
                    gifts[numb] = "None"
        elif command_name == "Required":
            num = int( string_of_command[2])
            if 0 <= num < len(gifts):
                gifts[num] = present
        elif command_name == "JustInCase":
            gifts[-1] = present
    for gift in gifts:
        if gift != "None":
            print(gift, end= " ")
    print()

def sizeOfFire():
    fire_cells = input().split("#")
    water = int(input())
    total_fire = 0
    effort = 0

    print("Cells:")
    for fire in fire_cells:
        fire_in_the_cell = fire.split(" = ")
        typeOfFire = fire_in_the_cell[0]
        valueOfCell = int(fire_in_the_cell[1])
        reducingFire = False

        if typeOfFire == "High":
            if 81 <= valueOfCell <= 125 and water >= valueOfCell:
                effort += valueOfCell * 0.25
                water -= valueOfCell
                total_fire += valueOfCell
                reducingFire = True

        elif typeOfFire == "Medium":
            if 51 <= valueOfCell <= 80 and water >= valueOfCell:
                effort += valueOfCell * 0.25
                water -= valueOfCell
                total_fire += valueOfCell
                reducingFire = True

        elif typeOfFire == "Low":
            if 1 <= valueOfCell <= 50 and water >= valueOfCell:
                effort += valueOfCell * 0.25
                water -= valueOfCell
                total_fire += valueOfCell
                reducingFire = True

        if reducingFire:
            print(f"- {valueOfCell}")
    else:
        print(f"Effort: {effort:.2f}")

    print(f"Total Fire: {total_fire}")

def helloFrance():
    items_for_sell = input().split("|")
    budget = float(input())
    sells = []
    PRICE_OF_TRAVELLING = 150.0

    for item in items_for_sell:
        item_info = item.split("->")
        type = item_info[0]
        price = float(item_info[1])
        if((type == "Clothes" and price <= 50.0)
                or ( type == "Shoes" and price <= 35.0)
                or (type == "Accessories" and price <= 20.50)):
            if budget >= price:
                budget -= price
                sells.append(price)


    for sell in sells:
        print(f"{sell * 1.4:.2f}", end=" ")
    print()
    print(f"Profit: {sum(sells) * 0.4 :.2f}")

    total_money = budget + sum(sells) * 1.4
    print("Hello, France!") if total_money >= PRICE_OF_TRAVELLING else print("Not enough money.")



def breadFactory():
    initial_money = 100
    initial_energy = 100
    events = input().split("|")
    for event in events:
        event_info = event.split("-")
        type_of_event = event_info[0]
        amount_of_event = int(event_info[1])
        if type_of_event == "rest":

            if initial_energy + amount_of_event > 100:
                amount_of_event = 100 - initial_energy

            initial_energy += amount_of_event
            print(f"You gained {amount_of_event} energy.")
            print(f"Current energy: {initial_energy}.")

        elif type_of_event == "order":
            if initial_energy >= 30:
                initial_energy -= 30
                print(f"You earned {amount_of_event} coins.")
                initial_money += amount_of_event
            else:
                initial_energy += 50
                print("You had to rest!")
        else:
            if initial_money >= amount_of_event:
                print(f"You bought {type_of_event}.")
                initial_money -= amount_of_event
            else:
                print(f"Closed! Cannot afford {type_of_event}.")
                break
    else:
        print(f"Day completed!\nCoins: {initial_money}\nEnergy: {initial_energy}")

def zerostoBack():
    integers_string = [int(number) for number in input().split(", ")]
    newList = sorted(integers_string, key = lambda x: x == 0)
    print(newList)

    ''' newlist2 = []
    for listItem in integers_string:
        if listItem != 0:
            newlist2.append(listItem)
    list_for_print = newlist2 + [0] * integers_string.count(0)
    print(list_for_print) '''

def messaging():
    sequence_of_numbers = [int(number) for number in input().split(" ")]
    string_line = input()
    result_word = ""

    for number in sequence_of_numbers:
        sum_of_number = 0
        while number != 0:
            sum_of_number += number %  10
            number //= 10

        sum_of_number %= len(string_line)
        character = string_line[sum_of_number]
        string_line = string_line[:sum_of_number] + string_line[sum_of_number + 1:]
        result_word += character

    print(result_word)

def  sumOfNumbers_exclude_zero(integer_list) -> float:
    from decimal import Decimal
    sum_of_list = 0.0
    for number in integer_list:
        if number != 0:
            sum_of_list  += number
        else:
            sum_of_list  *= 0.8
    return  sum_of_list

def carRace():
    raceres = [int(number) for number in input().split(" ")]
    middle = len(raceres) // 2
    first = raceres[:middle]
    second = raceres[middle + 1:]
    second.reverse()
    sumOfNumbers_left = sumOfNumbers_exclude_zero(first)
    sumOfNumbers_right = sumOfNumbers_exclude_zero(second)
    #winner_name = ""

    if sumOfNumbers_right < sumOfNumbers_left:
        winner_name = "right"
    else:
        winner_name = "left"

    print(f"The winner is {winner_name} with total time: {min(sumOfNumbers_left, sumOfNumbers_right):.1f}")

def stringFromNumber(numbers) -> str:
    if len(numbers) == 1:
        return str(numbers[0])
    return str(numbers[0]) + "," + stringFromNumber(numbers[1:])

def josephusPermutation():
    list_of_members = [int(number) for number in input().split(" ")]
    number_of_victimes = int(input())
    current_vict_numb = 0
    list_of_dead = []

    while len(list_of_members) > 0:
        current_vict_numb = (current_vict_numb + number_of_victimes - 1) % len(list_of_members)
        victime = list_of_members.pop(current_vict_numb)
        list_of_dead.append(victime)

    print(f"[{','.join(map(str, list_of_dead))}]")

def isTheSame(a: tuple[int, int, int] ) -> bool:
     return True if a[0] == a[1] and a[2] == a[3] else False



def ticTacToe():
    first_Line = input().split()
    second_Line = input().split()
    third_Line = input().split()
    winner = "None"

    board = [first_Line, second_Line, third_Line]
    for row in board:
        if row[0] != "0" and row[0] == row[1] == row[2]:
           if row[0] == '1':
               winner = "First"
           elif row[0] == '2':
               winner = "Second"

    for column_number in range(3):
        if board[0][column_number] != "0" and board[0][column_number] ==  board[1][column_number] == board[2][column_number] :
            if board[0][column_number] == '1':
                winner = "First"
            elif board[0][column_number] == '2':
                winner = "Second"


    if board[1][1] != '0' and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] ):
            if board[1][1] == '1':
                winner = "First"
            elif board[1][1] == '2':
                winner = "Second"

    if winner != "None":
        print(f"{winner} player won")
    else:
        print("Draw!")

def listManipulator():

    from sys import maxsize


    list_of_numbers = [int(number) for number in input().split(" ")]

    while True:

        command_for_list = input().split()

        if command_for_list[0] == "end":
            print(f"[{', '.join(map(str, list_of_numbers))}]")
            break

        elif command_for_list[0] == "exchange":
            number_for_exchange = int(command_for_list[1])
            if number_for_exchange >= len(list_of_numbers) or number_for_exchange < 0:
                print("Invalid index")
            else:
                new_list = list_of_numbers[number_for_exchange + 1:] + list_of_numbers[:number_for_exchange + 1]
                list_of_numbers = new_list

        elif command_for_list[0] == "max":
            max = -maxsize
            remainder = 1 if command_for_list[1] == "odd" else 0
            target_index = -1

            for index, number in  enumerate(list_of_numbers):
                if number%2 == remainder and number >= max:
                    max = number
                    target_index = index

            if target_index == -1:
                print("No matches")
            else:
                print(target_index)

        elif command_for_list[0] == "min":
            min = maxsize
            remainder = 1 if command_for_list[1] == "odd" else 0
            target_index = -1

            for index, number in enumerate(list_of_numbers):
                if number % 2 == remainder and number <= min:
                    min = number
                    target_index = index

            if target_index == -1:
                print("No matches")
            else:
                print(target_index)

        elif command_for_list[0] == "first":
            lengh = int(command_for_list[1])

            if lengh > len(list_of_numbers):
                print("Invalid count")
                continue

            remainder = 1 if command_for_list[2] == "odd" else 0

            new_list_numbers = []

            for  number in  (list_of_numbers):
                if number % 2 == remainder:
                    new_list_numbers.append(number)


            if len(new_list_numbers) >= lengh and new_list_numbers:
                new_list_numbers = new_list_numbers[:lengh]

            print(f"[{', '.join(map(str, new_list_numbers))}]")

        elif command_for_list[0] == "last":
            lengh = int(command_for_list[1])

            if lengh > len(list_of_numbers):
                print("Invalid count")
                continue

            remainder = 1 if command_for_list[2] == "odd" else 0

            new_list_numbers = []

            for number in (list_of_numbers):
                if number % 2 == remainder:
                    new_list_numbers.append(number)

            if len(new_list_numbers) >= lengh and new_list_numbers:
                new_len = len(new_list_numbers) - lengh
                new_list_numbers = new_list_numbers[new_len:]

            print(f"[{', '.join(map(str, new_list_numbers))}]")

def retunAbs()-> None:
    list_of_numbers = [abs(float(number)) for number in input().split()]
    print(f"[{', '.join(map(str, list_of_numbers))}]")




#
# def grades(grade: float) -> str:
#     mark = ""
#     if 2.00 <= grade <= 2.99:
#         mark = "Fail"
#     elif 3.00 <= grade <= 3.49:
#         mark = "Poor"
#     elif 3.50 <= grade <= 4.49:
#         mark = "Good"
#     elif 4.50 <= grade <= 5.49:
#         mark = "Very Good"
#     elif 5.50 <= grade <= 6.00:
#         mark = "Excellent"
#     return mark
# number = float(input())
# print(grades(number))



# def calculations(number1: int,number2: int, operator: str):
#     result = None
#     if operator == "multiply":
#         result = number1 * number2
#     elif operator == "divide":
#         result = number1 / number2
#     elif operator == "add":
#         result = number1 + number2
#     elif operator == "subtract":
#         result = number1 - number2
#     return result
#
# manipulation = input()
# number1 = int(input())
# number2 = int(input())
#
# print(int(calculations(number1 ,number2 , manipulation)))

#
# string_of_letters = input()
# counter = int(input())
# result = lambda a,b : a*b
#
# print(result(string_of_letters, counter))

#
#
# def my_orders(product: str, count: int) -> float:
#     price = 0.0
#     if product == "coffee":
#         price = 1.50
#     elif product == "water":
#         price = 1.00
#     elif product == "coke":
#         price = 1.40
#     elif product == "snacks":
#         price = 2.00
#
#     return price * count
#
#
# boated_product = input()
# count = int(input())
# total_price = my_orders(boated_product, count)
#
# print(f"{total_price:.2f}")

# def recArea(a: int, b: int) -> int:
#    return a * b
#
# side1 = int(input())
# side2 = int(input())
# squer = recArea(side1, side2)
# print(squer)
#
# def rounding(numbers_string: str) -> list[int]:
#     numbers_list = numbers_string.split(" ")
#     new_numbers = []
#     for number in numbers_list:
#         current_number = round(float(number))
#         new_numbers.append(current_number)
#     return new_numbers
#
# list_of_numbers =  input()
# print(rounding(list_of_numbers))

# def smallestOfThree(number1: int, number2: int, number3: int) -> int:
#
#     smallerOfThree = number1
#
#     if number2 <= smallerOfThree:
#         smallerOfThree = number2
#     if number3 <= smallerOfThree:
#         smallerOfThree = number3
#
#     return smallerOfThree
#
# numb1 = int(input())
# numb2 = int(input())
# numb3 = int(input())
#
# print(smallestOfThree(numb1, numb2, numb3))

# def sum_numbers(number1: int, number2: int) -> int:
#     return number1 + number2
#
# def subtract(number1: int, number2: int) -> int:
#     difference = number1 - number2
#     return difference
#
# def  add_and_subtract(numberForSum1: int, numberForSum2: int, numberForSubtract: int) -> None:
#     sum_of_first_2 = sum_numbers(numberForSum1, numberForSum2)
#     print(subtract(sum_of_first_2 , numberForSubtract))
#
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# add_and_subtract(number1, number2, number3)
#
#
# def charsBetween(char1, char2) -> list:
#     list_of_chars = []
#     number_of_char1 = ord(char1)
#     number_of_char2 = ord(char2)
#     for number in range(number_of_char1 + 1, number_of_char2):
#         charFromNumb = chr(number)
#         list_of_chars.append(charFromNumb)
#     return list_of_chars
#
#
#
# char1 = input()
# char2 = input()
# print(f"{' '.join(map(str, charsBetween(char1, char2)))}")



# def sumOfOdds(list_of_number: list) -> int:
#     sumOfOdd = 0
#     for number in list_of_number:
#         if number % 2 == 1:
#             sumOfOdd += number
#     return sumOfOdd
#
# def sumOfEvens(list_of_number: list) -> int:
#     sumOfEven = 0
#     for number in list_of_number:
#         if number % 2 == 0:
#             sumOfEven += number
#     return sumOfEven
#
# stringnumber = input()
# list_of_numbers = [int(number) for number in stringnumber]
#
# sum_of_odd_digits = sumOfOdds(list_of_numbers)
# sum_of_even_digits = sumOfEvens(list_of_numbers)
# print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
#
#
# def filter(listOfNumbers: list) -> list:
#
#     list_of_numbers = (lamda x: x%2== 0)
#
# list_of_numbers = [int(number) for number in input().split()]
# listNew = list(filter(lambda number: number % 2 == 0, list_of_numbers))
# print(listNew)
#
# def letItSort(list_of_numbers: list) -> None:
#     list_of_numbers = sorted(list_of_numbers)
#     print(f"[{', '.join(map(str, list_of_numbers))}]")
#
# letItSort(int(number) for number in input().split())

#
# list_of_numbers = [int(number) for number in input().split()]
# print(f"The minimum number is {min(list_of_numbers)}")
# print(f"The maximum number is {max(list_of_numbers)}")
# print(f"The sum number is: {sum(list_of_numbers)}")

# def isItPolindrome(numberString: str) -> bool:
#     for index in range(len(numberString)):
#         if numberString[index] != numberString[len(numberString) - index - 1]:
#             return False
#     else:
#         return True
#
# list_of_numbers = [ string_number for string_number in input().split(", ")]
# [print(isItPolindrome(nums)) for nums in list_of_numbers]

# def isItCorrectPass(stringPass: str) -> None:
#
#     result_mistakes = set()
#
#     if   len(stringPass) < 6 or len(stringPass) > 10:
#         result_mistakes.add("Password must be between 6 and 10 characters")
#
#     digit_count = 0
#     for char in stringPass:
#
#         code = ord(char)
#         if   code < 48  or (58 <= code <= 64) or (91 <= code <= 96) or code >= 123:
#             result_mistakes.add("Password must consist only of letters and digits")
#         if char.isdigit():
#             digit_count += 1
#     else:
#         if digit_count < 2:
#             result_mistakes.add("Password must have at least 2 digits")
#
#     if len(result_mistakes) == 0:
#         result_mistakes.add("Password is valid")
#
#     for element in result_mistakes:
#         print(element)
#
#
#
# inputword = input()
# isItCorrectPass(inputword)

# def isPerfect(target_number: int) -> bool:
#     sum_of_divisors = 0
#
#     for number in range(1, target_number):
#         if target_number % number == 0:
#             sum_of_divisors += number
#     if sum_of_divisors == target_number:
#         return True
#     else:
#         return False
#
# number = int(input())
# print("We have a perfect number!") if isPerfect(number) else print("It's not so perfect.")

# def printLoadingBar(percent: int) -> None:
#     bar_len = int(percent / 10)
#     if bar_len < 10:
#         print(f"{percent}% [" + "%"*bar_len + "."*(10-bar_len) + "]")
#         print("Still loading...")
#     else :
#         print(f"{percent}% Complete!")
#         print("[" + "%" * bar_len + "]")
#
# entered_number = int(input())
# printLoadingBar(entered_number)


# def factorial_for_number(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_for_number(n - 1)
#
# number1 = int(input())
# number2 = int(input())
#
# print(f"{(factorial_for_number(number1)/factorial_for_number(number2)):.2f}")

# def solve_data_type(type_name, value_input):
#     if type_name == "int":
#         print(f"{int(value_input) * 2}")
#     elif type_name == "real":
#         print(f"{float(value_input)*1.5 :.2f}")
#     elif type_name == "string":
#         print(f"${value_input}$")
#
# string_type = input()
# string_value = input()
# solve_data_type(string_type, string_value)
#
# def min_center_distance(x1: float, y1: float, x2: float, y2: float) -> (int, int):
#     from math import sqrt, floor
#     distance1 = sqrt((x1)**2 + (y1)**2)
#     distance2 = sqrt((x2)**2 + (y2)**2)
#     if distance1 < distance2:
#         return floor(x1), floor(y1)
#     else:
#         return floor(x2), floor(y2)
#
#
# numberX1 = float(input())
# numberY1 = float(input())
# numberX2 = float(input())
# numberY2 = float(input())
#
# print(min_center_distance(numberX1, numberY1, numberX2, numberY2))
# from math import sqrt, floor  # Все инструменты берем на входе
#
#
# def min_center_distance(x1: float, y1: float, x2: float, y2: float) -> int:
#
#     dist1 = sqrt(x1 ** 2 + y1 ** 2)
#     dist2 = sqrt(x2 ** 2 + y2 ** 2)
#
#     if dist1 <= dist2:  # Если первая ближе или они равны
#         return 1
#     else:
#         return 2
#
#
# def print_ordered_line(x1, y1, x2, y2):
#     closer_point = min_center_distance(x1, y1, x2, y2)
#
#     if closer_point == 1:
#         print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
#     else:
#         print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")
#
#
# def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> float:
#     return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
#
# startX1 = float(input())
# startY1 = float(input())
# endX1 = float(input())
# endY1 = float(input())
#
# startX2 = float(input())
# startY2 = float(input())
# endX2 = float(input())
# endY2 = float(input())
#
# line1 = distance_between_points(startX1, startY1, endX1, endY1)
# line2 = distance_between_points(startX2, startY2, endX2, endY2)
#
# if line1 >= line2:
#     print_ordered_line(startX1, startY1, endX1, endY1)
# else:
#     print_ordered_line(startX2, startY2, endX2, endY2)
#
# def tribonacci_list(number_of_digits: int) -> None:
#     list_of_numbers = []
#
#     current_digit = 0
#     while current_digit < number_of_digits:
#         if current_digit  < 2:
#             list_of_numbers.append(1)
#         elif current_digit == 2:
#             list_of_numbers.append(2)
#         else:
#             current_number = (list_of_numbers[current_digit - 1]
#                                                + list_of_numbers[current_digit - 2]
#                                                + list_of_numbers[current_digit - 3])
#             list_of_numbers.append(current_number)
#
#         current_digit += 1
#     print(f"{' '.join(map(str, list_of_numbers))}")
#
#
# input_number = int(input())
# tribonacci_list(input_number)
#

# def isItPositiveMultiple(list_of_numbers: list[int]) -> bool | None:
#     positive = True
#     for number in list_of_numbers:
#         if number < 0:
#             positive = not positive
#         elif number == 0:
#             return None
#     return positive
#
# inputed_list = []
# for _ in range(3):
#     inputed_list.append(int(input()))
# result = isItPositiveMultiple(inputed_list)
# if result == True:
#     print("positive")
# elif result == None:
#     print("zero")
# elif result == False:
#     print("negative")

# entered_word = input()
# new_word = list(charakter  for charakter in entered_word if charakter.lower() not in "aouei")
# print("".join(map(str, new_word)))


# length = int(input())
# my_train = [0] * length
#
# while True:
#     command_for_list = input().split()
#     if command_for_list[0] == "End":
#         break
#     event_type =  command_for_list[0]
#     if event_type == "add":
#         count_of_passangers = int(command_for_list[1])
#         my_train[-1] += count_of_passangers
#
#     elif event_type == "insert":
#         wagon = int(command_for_list[1])
#         count_of_passangers = int(command_for_list[2])
#
#         my_train[wagon] += count_of_passangers
#
#     elif event_type == "leave":
#         wagon = int(command_for_list[1])
#         count_of_passangers = int(command_for_list[2])
#
#         my_train[wagon] -= count_of_passangers
#
# print(my_train)

# list_events = [0] * 10
# while True:
#     command_for_list = input().split("-")
#     if command_for_list[0] == "End":
#         break
#     event_importance =  int(command_for_list[0]) - 1
#     event_note = command_for_list[1]
#     list_events.pop(event_importance)
#     list_events.insert(event_importance, event_note)
#
# print([event for event in list_events if event != 0])

# words_list = input().split(" ")
# palindrome_target = input()
# number_of_polidromes = 0
# palindrome_list = []
#
# for word in words_list:
#     if  word == ''.join(reversed(word)):
#         palindrome_list.append(word)
#
# print(f"{palindrome_list}")
# print(f"Found palindrome {palindrome_list.count(palindrome_target)} times")

# names_list = input().split(", ")
# sorted_list = sorted(names_list, key = lambda x:(-len(x), x))
# print(sorted_list)

# number_list = [int(number) for number in input().split(", ")]
# indexes_list_of_evens = [index for index, number in enumerate(number_list) if number % 2 == 0]
#
# print(list(indexes_list_of_evens))

#number_list = [int(number) for number in input().split(", ")]
# indexes_list_of_evens2 = map(lambda x: x if number_list[x]%2 == 0 else "no", range(len(number_list)))
# even_indices2 = list(filter(lambda a: a!= "no", indexes_list_of_evens2))


# employees = [int(number) for number in input().split(" ")]
# factor = int(input())
# employees = list(map(lambda x: x * factor, employees))
# filtered = list(filter(lambda x: x >= (sum(employees)/ len(employees)), employees))
# happy_people = len(filtered)
# total_people = len(employees)
#
# not_or_happy = "" if happy_people >= total_people / 2 else "not "
# print(f"Score: {happy_people}/{total_people}. Employees are {not_or_happy}happy!")
#
#
# words = [string_word for string_word in input().split(", ")]
# stencil_words = [string_stencil for string_stencil in input().split(", ")]
#
# list_result = []
# for word in words:
#     for stencil_word in stencil_words:
#         if word in stencil_word and word not in list_result:
#             list_result.append(word)
#
# print(list_result)

# version = [int(v) for v in input().split(".")]
# flag_incresing = False
#
# for index in range(len(version) -1, -1, -1):
#
#
#     if flag_incresing or index == 2:
#         version[index] += 1
#
#     if version[index] == 10:
#         version[index] = 0
#         flag_incresing = True
#     else:
#         flag_incresing = False
#
# print(f"{'.'.join(map(str, version))}")


# word_list = [w for w in input().split() if len(w) % 2 == 0 ]
# [print(word) for word in word_list]

# numbers = [int(number) for number in input().split(', ')]
# positive = [nubmer for nubmer in numbers if nubmer >= 0]
# negative = [nubmer for nubmer in numbers if nubmer < 0]
# even = [nubmer for nubmer in numbers if nubmer % 2 == 0]
# odd = [nubmer for nubmer in numbers if nubmer % 2 != 0]
#
# print(f"Positive: {', '.join(map(str, positive))}")
# print(f"Negative: {', '.join(map(str, negative))}")
# print(f"Even: {', '.join(map(str, even))}")
# print(f"Odd: {', '.join(map(str, odd))}")

# number_of_rooms = int(input())
# enought = True
# total_free_chairs = 0
#
# for i in range(number_of_rooms):
#     chairs_information = input().split()
#     chairs = len(chairs_information[0])
#     visitors = int(chairs_information[1])
#     if chairs < visitors:
#         print(f'{visitors - chairs} more chairs needed in room {i + 1}')
#         enought = False
#     else:
#         total_free_chairs += (chairs - visitors)
#
# if enought:
#     print(f"Game On, {total_free_chairs} free chairs left")
#
# def electrons_distribution(current_number_of_electrons : int) -> None:
#     list_of_electrons = []
#     n = 1
#
#     while True:
#
#         electrons_on_the_line = 2 * (n ** 2)
#         n += 1
#
#         if electrons_on_the_line <= current_number_of_electrons:
#             list_of_electrons.append(electrons_on_the_line)
#         else:
#             list_of_electrons.append(current_number_of_electrons)
#
#         current_number_of_electrons -= electrons_on_the_line
#         if current_number_of_electrons <= 0:
#             break
#
#     print(list_of_electrons)
#
# number = int(input())
# electrons_distribution(number)

# def groupOf10s(list_of_numbers : [int]) -> None:
#     n = 1
#     while len(list_of_numbers) != 0:
#         list_of_group = []
#         group = n * 10
#
#         for index in range(len(list_of_numbers) -1, -1, -1):
#             if list_of_numbers[index] <= group:
#                 list_of_group.insert(0, list_of_numbers.pop(index))
#
#         print(f"Group of {group}'s: {list_of_group}")
#         n += 1
#
# list_of_numbers = [int(number) for number in input().split(", ")]
# groupOf10s(list_of_numbers)

#
# def decipherThis() -> None:
#     list_of_word = [word for word in input().split()]
#
#     result = []
#     for word in list_of_word:
#         current_word = ''
#         digits = ""
#         letters = ""
#
#         for char in word:
#             if char.isdigit():
#                 digits += char
#             else:
#                 letters += char
#
#         first_letter = chr(int(digits))
#         word_as_list = list(letters)
#         word_as_list[0] , word_as_list[-1]  = word_as_list[-1] , word_as_list[0]
#
#         current_word =first_letter + "".join(word_as_list)
#         result.append(current_word)
#
#     print(' '.join(result))
#
#
# decipherThis()

def anonymousThreat():
    list_of_words = [word for word in input().split()]

    while True:
        input_command = input()
        if input_command  == "3:1":
            break
        else:
            commands_list = input_command.split()
            command = commands_list[0]


            if command == "merge":
                start_index = int(commands_list[1])
                end_index = int(commands_list[2])

                start_index = max(0, start_index)
                end_index = min(len(list_of_words) - 1, end_index)

                if start_index >= end_index:
                    continue

                merged_string = "".join(list_of_words[start_index: end_index + 1])
                list_of_words = list_of_words[:start_index] + [merged_string] + list_of_words[end_index + 1:]

            elif command == "divide":
                index = int(commands_list[1])
                partitions = int(commands_list[2])

                element_to_divide = list_of_words[index]

                step = len(element_to_divide) // partitions

                divided_elements = []
                start = 0

                for i in range(partitions - 1):
                    piece = element_to_divide[start: start + step]
                    divided_elements.append(piece)

                    start += step

                last_piece = element_to_divide[start:]
                divided_elements.append(last_piece)

                list_of_words = list_of_words[:index] + divided_elements + list_of_words[index + 1:]

    print(' '.join(list_of_words))

def pockemon_game():
     sequence_of_integer =  [int(number) for number in input().split()]
     sum = 0
     while True:
         current_sequence_of_integer = []
         index = int(input())

         if index >= len(sequence_of_integer):
             number = sequence_of_integer[0]
             number_for_pop = sequence_of_integer.pop(-1)
             sequence_of_integer.append(number)
         elif index < 0:
             number = sequence_of_integer[-1]
             number_for_pop = sequence_of_integer.pop(0)
             sequence_of_integer.insert(0, number)
         else:
            number_for_pop = sequence_of_integer.pop(index)

         sum += number_for_pop

         if len(sequence_of_integer) == 0:
            break

         for element in sequence_of_integer:
             if element > number_for_pop:
                 element -= number_for_pop
             else:
                 element += number_for_pop
             current_sequence_of_integer.append(element)
         sequence_of_integer = current_sequence_of_integer

     print(sum)

def softUniCoursePlanning():
    list_of_courses = [word for word in input().split(", ")]
    while True:
        input_command = input()
        if input_command == "course start":
            break
        command_Lesson = input_command.split(":")
        command = command_Lesson[0]

        if command == "Add":
            lesson = command_Lesson[1]
            if lesson not in list_of_courses:
                list_of_courses.append(lesson)

        elif command == "Insert":
            lesson = command_Lesson[1]
            if lesson not in list_of_courses:
                index = int(command_Lesson[2])
                list_of_courses.insert(index, lesson)


        elif command == "Remove":

            lesson = command_Lesson[1]
            if lesson in list_of_courses:
                list_of_courses.remove(lesson)
                exercise_name = f"{lesson}-Exercise"

                if exercise_name in list_of_courses:
                    list_of_courses.remove(exercise_name)

        elif command == "Swap":
            lesson1 = command_Lesson[1]
            lesson2 = command_Lesson[2]
            if lesson1 in list_of_courses and lesson2 in list_of_courses:
                index1 = list_of_courses.index(lesson1)
                index2 = list_of_courses.index(lesson2)

                list_of_courses[index1], list_of_courses[index2] = list_of_courses[index2], list_of_courses[index1]

                ex1 = f"{lesson1}-Exercise"
                if ex1 in list_of_courses:
                    ex1_index = list_of_courses.index(ex1)
                    exersise1 = list_of_courses.pop(ex1_index)
                    index_ex1 = list_of_courses.index(lesson1)
                    list_of_courses.insert(index_ex1 + 1, exersise1)

                ex2 = f"{lesson2}-Exercise"
                if ex2 in list_of_courses:
                    ex2_index = list_of_courses.index(ex2)
                    exersise2 = list_of_courses.pop(ex2_index)
                    index_ex2 = list_of_courses.index(lesson2)
                    list_of_courses.insert(index_ex2 + 1, exersise2)




        elif command == "Exercise":
            lesson = command_Lesson[1]
            exercise_name = f"{lesson}-Exercise"
            if lesson in list_of_courses:
                if exercise_name not in list_of_courses:
                    lesson_index = list_of_courses.index(lesson)
                    list_of_courses.insert(lesson_index + 1, exercise_name)
            else:
                list_of_courses.append(lesson)
                list_of_courses.append(exercise_name)

    lesson_counter = 1
    for course in list_of_courses :
        print(f"{lesson_counter}.{course}")
        lesson_counter += 1


def socialDistribution():
    population = [int(number) for number in input().split(", ")]
    minimal_wealth = int(input())

    if minimal_wealth > (sum(population)/len(population)):
        print("No equal distribution possible")
        return


    for index_pure, pure in enumerate(population):
        if pure < minimal_wealth:
            maximal_wealth = max(population)
            index_reachest = population.index(maximal_wealth)

            need_money = minimal_wealth - pure
            if maximal_wealth - need_money >= 0:
                population[index_pure] = minimal_wealth
                population[index_reachest] -= need_money

    print(population)

def takeOrSkipRope():
    text = input()
    Skip_list = []
    TAKE_LIST = []
    message_text = []
    evenFlag = True

    for character in text:
        if character.isdigit():
            if evenFlag:
                TAKE_LIST.append(int(character))
            else:
                Skip_list.append(int(character))

            evenFlag = not evenFlag
        else:
            message_text.append(character)

    new_message_text = []
    start_index = 0

    for i in range(len(TAKE_LIST)):
        offset = TAKE_LIST[i]
        new_message_text.append("".join(message_text[start_index : start_index + offset]))
        start_index += Skip_list[i] + offset

    print(''.join(new_message_text))



def kateWayOut():

    rows_count = int(input())
    maze = []
    k_point_row = -500
    k_point_column = -500

    for row_number in range(rows_count):
        cols = [sign for sign in input()]
        maze.append(cols)
        if 'k' in cols:
            k_point_row = row_number
            k_point_column = cols.index('k')

    max_length = [0]

    def find_pass(row: int, col: int,  step: int) -> None:
        if row < 0 or row >= rows_count or col < 0 or col >= len(maze[0]):
            if step > max_length[0]:
                max_length[0] = step
            return
        if maze[row][col] == '#' or maze[row][col] == '*':
            return

        maze[row][col] = '*'

        find_pass(row + 1, col, step + 1)
        find_pass(row - 1, col, step + 1)
        find_pass(row , col + 1, step + 1)
        find_pass(row, col - 1, step + 1)

        maze[row][col] = ' '

    find_pass(k_point_row, k_point_column, 0)


    if max_length[0] > 0:
        print(f"Kate got out in {max_length[0]} moves")
    else:
        print("Kate cannot get out")



def battleShips():
    rows_count = int(input())
    field_of_battle = []

    for row_number in range(rows_count):
        ships = [int(ship) for ship in input().split()]
        field_of_battle.append(ships)

    fights = [(number.split("-")) for number in input().split()]
    destroyed_ship = 0

    for fight in fights:
        row_number = int(fight[0])
        col_number = int(fight[1])
        strength_of_ship = field_of_battle[row_number][col_number]
        
        if  strength_of_ship != 0:
            fighting_result = strength_of_ship - 1
            field_of_battle[row_number][col_number] = fighting_result
            if fighting_result == 0:
                destroyed_ship += 1
            
    print(destroyed_ship)


def dotsGame():
    n = int(input())
    dashboard = []

    for _ in range(n):
        line = input().split()
        dashboard.append(line)


    def findLine(row: int, col: int) -> int:
        if row < 0 or row >= n or col < 0 or col >= len(dashboard[0]):
            return 0
        if dashboard[row][col] != '.':
            return 0
        else:
            dashboard[row][col] = '*'
            return 1 + findLine(row - 1, col) + findLine(row + 1, col) + findLine(row, col + 1) + findLine(row, col - 1)

    max_dots = 0

    for row in range(n):
        for column in range(len(dashboard[0])):
            if dashboard[row][column] == '.':
                current_dots = findLine(row, column)
                if current_dots > max_dots:
                    max_dots = current_dots


    print(max_dots)

dotsGame()
