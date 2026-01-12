from importlib.metadata import pass_none
from operator import index


def computerStore() -> None:
    total_price = 0.0

    while True:

        purchase = input()
        koef_sale = 1.0
        tax = 0.2

        if purchase == "special":
            koef_sale = 0.9
            break
        elif purchase == "regular":

            break

        purchase_price = float(purchase)
        if purchase_price < 0:
            print("Invalid price!")
        else:
            total_price += purchase_price

    if total_price == 0.0:
        print("Invalid order!")
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price:.2f}$")
        final_taxes = total_price * tax
        print(f"Taxes: {final_taxes:.2f}$")
        print("-----------")
        final_price = (total_price + final_taxes) * koef_sale
        print(f"Total price: {final_price:.2f}$")

def theLift():
    MAX_LIFT_SIZE = 4
    people_in_the_queue = int(input())

    lift_space = [int(number) for number in input().split()]

    for index, lift_seats in enumerate(lift_space):
        empty_space =  MAX_LIFT_SIZE - lift_seats
        if people_in_the_queue >= empty_space:
            people_in_the_queue -= empty_space
            lift_space[index] = MAX_LIFT_SIZE
        else:
            lift_space[index] += people_in_the_queue
            people_in_the_queue = 0


    if people_in_the_queue > 0:
        print(f"There isn't enough space! {people_in_the_queue} people in a queue!")
        print(" ".join(map(str, lift_space)))
    elif any(wagon < MAX_LIFT_SIZE for wagon in lift_space):
        print("The lift has empty spots!")
        print(" ".join(map(str, lift_space)))
    elif people_in_the_queue == 0 and lift_space[-1] == MAX_LIFT_SIZE:
        print(" ".join(map(str, lift_space)))

def memoryGame():
    game_cards = input().split()
    steps = 0
    while True:

        game = input()
        if game == "end":
            number_of_game_cards = len(game_cards)

            if number_of_game_cards != 0:
                print(f"Sorry you lose :(")
                print(" ".join(game_cards))
                break
        game_pair = [int(number) for number in game.split()]
        steps += 1

        index0 = game_pair[0]
        index1 = game_pair[1]
        if index0 == index1 or index0 < 0 or index1 < 0 or index0 >= len(game_cards) or index1 >= len(game_cards):
            game_cards.insert(len(game_cards)//2 , "-"+f"{steps}"+"a" )
            game_cards.insert(len(game_cards) // 2 + 1, "-" + f"{steps}" + "a")
            print("Invalid input! Adding additional elements to the board")
        else:
            if game_cards[index0] == game_cards[index1]:
                print(f"Congrats! You have found matching elements - {game_cards[index0]}!")
                game_cards.pop(min(index0, index1))
                game_cards.pop(max(index1, index0) - 1)
            else:
                print("Try again!")

        if len(game_cards) == 0:
            print(f"You have won in {steps} turns!")
            break

def registration():
    first_name = input()

    while True:
        input_string = input()
        if input_string == "Registration":
            break
        command = input_string.split()

        if command[0] == "Letters":
             if command[1] == "Lower":
                 first_name = first_name.lower()
             elif command[1] == "Upper":
                 first_name = first_name.upper()
             print(first_name)

        elif command[0] == "Reverse":
            start_index = int(command[1])
            end_index = int(command[2])
            if end_index > start_index and start_index >= 0 and end_index <= len(first_name):

                reversed_part = (first_name[start_index:end_index + 1])
                reversed_part = reversed_part[::-1]
                print(reversed_part)


        elif command[0] == "Substring":
            substring = command[1]
            if substring in first_name:
                first_name = first_name.replace(substring, "")
                print(first_name)
            else:
                print(f"The username {first_name} doesn't contain {substring}.")


        elif command[0] == "Replace":
            character = command[1]
            for character_of_name in first_name:
                if character == character_of_name:
                    first_name = first_name.replace(character_of_name, "-")
            print(first_name)

        elif command[0] == "IsValid":
            validator_char = command[1]
            if validator_char in first_name:
                print("Valid username.")
            else:
                print(f"{validator_char} must be contained in your username.")

def destinationMapper():
    input_string = input()
    started_word_equal = False
    started_word_slash = False
    start_index = -500
    destination_words = []

    for index, character in enumerate(input_string):

        if character == "=" and not started_word_equal:
            started_word_equal = True
            started_word_slash = False
            start_index = index
            continue
        if character == "/" and not started_word_slash:
            started_word_slash = True
            started_word_equal = False
            start_index = index
            continue


        if (started_word_equal and character == "=") or (character == "/" and started_word_slash):
            end_index = index
            destination_word = input_string[start_index + 1 : end_index]
            if  len(destination_word) >= 3 and destination_word[0].isupper() and destination_word.isalpha():
                destination_words.append(destination_word)

            start_index = index

            if character == "=":
                started_word_equal = True
                started_word_slash = False
            elif character == "/":
                started_word_slash = True
                started_word_equal = False


    destination_points = sum([len(destination_word) for destination_word in destination_words])
    print(f"Destinations: " + ", ".join(destination_words))
    print(f"Travel Points: {destination_points}")



def bakeryShop():
    from collections import defaultdict
    sold_food = 0
    products_in_the_Bakery = defaultdict(int)

    while True:
        input_string = input().split(" ")


        if input_string[0] == "Complete":
            break
        else:
            event = input_string[0]
            amount = int(input_string[1])
            type_of_food = input_string[2]

        if event == "Receive":
            if amount <= 0:
                continue

            if type_of_food not in products_in_the_Bakery:
                products_in_the_Bakery[type_of_food] = 0

            products_in_the_Bakery[type_of_food] += amount

        if event == "Sell":
            if type_of_food not in list(products_in_the_Bakery.keys()):
                print(f"You do not have any {type_of_food}.")
                continue

            solding_quantity = products_in_the_Bakery[type_of_food]

            if amount > solding_quantity:
                print(f"There aren't enough {type_of_food}. You sold the last {solding_quantity} of them.")
                amount = solding_quantity
            else:
                print(f"You sold {amount} {type_of_food}.")

            products_in_the_Bakery[type_of_food] -= amount
            sold_food += amount

            if products_in_the_Bakery[type_of_food] == 0:
                products_in_the_Bakery.pop(type_of_food)

    for t, q  in products_in_the_Bakery.items():
        print(f"{t}: {q}")
    print(f"All sold: {sold_food} goods")

def softUniReception():
    from math import ceil
    employees_efficiency = 0
    for _ in range(3):
        employees_efficiency += int(input())

    students_count = int(input())
    if students_count == 0:
        time = 0
    else:
        time =  ceil(students_count / employees_efficiency)
        time_for_rest = (time -1) // 3
        time  += time_for_rest

    print(f"Time needed: {time}h.")


def arrayModifier():

    string_array = [int(number) for number in input().split()]

    while True:
        input_string = input()
        if input_string == "end":
            break
        command = input_string.split()

        if command[0] == "swap":
            index1 = int(command[1])
            index2 = int(command[2])
            string_array[index1], string_array[index2] = string_array[index2], string_array[index1]

        elif command[0] == "multiply":
            index1 = int(command[1])
            index2 = int(command[2])
            string_array[index1] *= string_array[index2]

        elif command[0] == "decrease":
            string_array = [(number - 1) for number in string_array]
    print(f"{', '.join(map(str, string_array))}")


def numberPreExam():
    numbers =  [int(number) for number in input().split()]
    numbers.sort(reverse=True)

    middle = sum(numbers) / len(numbers)
    greater_than_middle = []

    for number in numbers:
        if number > middle:
            greater_than_middle.append(number)
            if len(greater_than_middle) == 5:
                break

    if len(greater_than_middle) == 0:
        print("No")
    else:
        print(" ".join(map(str, greater_than_middle)))

def counterStrike():

    current_energy = int(input())
    count_of_win = 0
    dont_have_energy = False

    while True:
        input_string = input()

        if input_string == "End of battle":
            break
        distance = int(input_string)

        if current_energy >= distance:
            count_of_win += 1
            current_energy -= distance
        else:
            dont_have_energy = True
            break

        if count_of_win % 3 == 0:
            current_energy += count_of_win

    if dont_have_energy:
        print(f"Not enough energy! Game ends with {count_of_win} won battles and {current_energy} energy")
    else:
        print(f"Won battles: {count_of_win}. Energy left: {current_energy}")

def shootForTheWin():
    targets =  [int(number) for number in input().split()]
    while True:
        input_string = input()
        if input_string == "End":
            break
        shot_index = int(input_string)
        if shot_index in range(0, len(targets)):
            shot = targets[shot_index]
            targets[shot_index] = -1
            for target_index in range(0, len(targets)):
                if targets[target_index] != -1 and target_index != shot_index :
                    if targets[target_index] > shot:
                        targets[target_index] -= shot
                    elif targets[target_index] <= shot:
                        targets[target_index] += shot

    count = sum(1 for x in targets if x == -1)
    print(f"Shot targets: {count} -> " + " ".join(map(str, targets)))


def movingTarget():
    targets = [int(number) for number in input().split()]
    while True:
        input_string = input()
        if input_string == "End":
            break
        command_string = input_string.split()
        command = command_string[0]
        index = int(command_string[1])
        parametr = int(command_string[2])

        if command == "Shoot":
            if index in range(0, len(targets)):
                targets[index] -= parametr
                if targets[index] <= 0:
                    targets.pop(index)

        elif command == "Add":
            if index in range(0, len(targets)):
                targets.insert(index, parametr)
            else:
                print("Invalid placement!")

        elif command == "Strike":
            if index in range(0, len(targets)) and index + parametr < len(targets) and  index - parametr >= 0:
                 targets = targets[: index - parametr] + targets[index + parametr + 1:]
            else:
                print("Strike missed!")
    print("|".join(map(str, targets)))


def guineaPig():
    food = float(input()) * 1000
    hay = float(input()) * 1000
    cover = float(input()) * 1000
    weight = float(input()) * 1000
    for day in range(1, 31):
        food -= 300
        if day % 2 == 0:
            hay -= food * 0.05
        if day % 3 == 0:
            cover -= weight * 1/3
        if food <= 0 or hay <= 0 or cover <= 0:
            print("Merry must go to the pet store!")
            break
    else:
        print(f"Everything is fine! Puppy is happy! Food: {(food/1000):.2f}, Hay: {(hay/1000):.2f}, Cover: {(cover/1000):.2f}.")

def shoppingList_preExam():
    shopping_list = [item for item in input().split("!") if item]
    while True:
        input_string = input()
        if input_string == "Go Shopping!":
            break

        command_list = input_string.split()
        command = command_list[0]
        item = command_list[1]

        if command == "Urgent":
            if item not in shopping_list:
                shopping_list.insert(0, item)
        elif command == "Unnecessary":
            if item  in shopping_list:
                shopping_list.remove(item)
        elif command == "Correct":
            if item in shopping_list:
                correct_item = command_list[2]
                index = shopping_list.index(item)
                shopping_list[index] = correct_item
        elif command == "Rearrange":
            if item in shopping_list:
                shopping_list.remove(item)
                shopping_list.append(item)
    print(", ".join(map(str, shopping_list)))

def heartDelivery():
    houses = [int(number) for number in input().split("@") if number]
    house_index = 0
    while True:
        input_string = input()
        if input_string == "Love!":
            break
        else:
            jump = int(input_string.split()[1])
        house_index += jump
        if house_index >= len(houses):
            house_index = 0

        if houses[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
        else:
            houses[house_index] -= 2
            if houses[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")
    print(f"Cupid's last position was {house_index}.")
    feltInLove = sum([1 for house in houses if house == 0])
    if feltInLove == len(houses):
        print("Mission was successful.")
    else:
        print(f"Cupid has failed {len(houses) - feltInLove} places.")

def bonusScoringSystem():
    from math import ceil
    number_of_students = int(input())
    total_lectures = int(input())
    additional_bonus = int(input())

    max_bonus = 0
    max_attendances = 0

    for _ in range(number_of_students):
        attendance= int(input())
        current_bonus = 0
        if total_lectures > 0:
            current_bonus = attendance / total_lectures * (5 + additional_bonus)


        if current_bonus > max_bonus:
            max_bonus = current_bonus
            max_attendances = attendance

    print(f"Max Bonus: {ceil(max_bonus)}.")
    print(f"The student has attended {max_attendances} lectures.")

def muOnline():
    INICIAL_HEALTH   = 100
    INITIAL_BITCOINS = 0
    room_string = [room for room in input().split("|")]

    health = INICIAL_HEALTH
    money = INITIAL_BITCOINS

    for room in room_string:
        command_list = room.split()
        command = command_list[0]
        value = int(command_list[1])
        if command == "potion":
            if health + value > INICIAL_HEALTH:
                value = INICIAL_HEALTH - health
            health += value
            print(f"You healed for {value} hp.")
            print(f"Current health: {health} hp.")

        elif command == "chest":
            money += value
            print(f"You found {value} bitcoins.")

        else:
            health -= value
            if health > 0:
               print(f"You slayed {command}.")
            else:
                print(f"You died! Killed by {command}.")
                room =  room_string.index(room) + 1
                print(f"Best room: {room}")
                break
    else:
        print("You've made it!")
        print(f"Bitcoins: {money}")
        print(f"Health: {health}")


def inventory():
    collecting_items = [item_c for item_c in input().split(", ") if item_c]

    while True:
        input_string = input()
        if input_string == "Craft!":
            break
        else:
            command_list = input_string.split(" - ")
            command = command_list[0]
            item = command_list[1]

            if command == "Collect":
                if item not in collecting_items:
                    collecting_items.append(item)
            elif command == "Drop":
                if item in collecting_items:
                    collecting_items.remove(item)
            elif command == "Combine Items":
                combine_Items = item.split(":")
                old_item = combine_Items[0]
                new_item = combine_Items[1]
                if old_item in collecting_items:
                    index = collecting_items.index(old_item)
                    collecting_items.insert(index + 1, new_item)
            elif command == "Renew":
                if item in collecting_items:
                    collecting_items.remove(item)
                    collecting_items.append(item)

    print(", ".join(map(str, collecting_items)))

def blackFlag():
    days = int(input())
    daily_plunder = int(input())
    target_plunder = float( input())
    total_gain  = 0.0

    for day in range(1, days + 1):
        total_gain += daily_plunder

        if day % 3 == 0:
            total_gain += daily_plunder * 0.5

        if day % 5 == 0:
            total_gain  = total_gain * 0.7


    else:
        if total_gain >= target_plunder:
            print(f"Ahoy! {total_gain:.2f} plunder gained.")
        else:
            print(f"Collected only {(total_gain/target_plunder):.2%} of the plunder.")

def treasureHunt():
    loot_string = [room for room in input().split("|")]

    while True:
        input_string = input()
        if input_string == "Yohoho!":
            break
        else:
            command_list = input_string.split()
            command = command_list[0]


            if command == "Loot":
                value = command_list[1:]
                treasures = value
                for treasure in treasures:
                    if treasure not in loot_string:
                        loot_string.insert(0, treasure)

            elif command == "Drop":
                index = int(command_list[1])
                if index < len(loot_string):
                   loot_string.append(loot_string.pop(index))

            elif command == "Steal":
                count = int(command_list[1])
                if count >= len(loot_string):
                    print(", ".join(map(str, loot_string)))
                    loot_string.clear()
                else:
                    stolen = loot_string[(len(loot_string) - count):]
                    loot_string = loot_string[:(len(loot_string) - count)]
                    print(", ".join(map(str, stolen)))

    if loot_string:
        #print(", ".join(map(str, loot_string)))
        averageGain = sum([len(loot) for loot in loot_string]) / len(loot_string)
        print(f"Average treasure gain: {averageGain:.2f} pirate credits.")
    else:
       print("Failed treasure hunt.")


def manOWar():
    pirate_ships = [int(ship) for ship in input().split(">")]
    warships = [int(ship) for ship in input().split(">")]
    max_health = int(input())

    while True:
        input_string = input()
        if input_string == "Retire":
            print(f"Pirate ship status: {sum(pirate_ships)}")
            print(f"Warship status: {sum(warships)}")
            break
        else:
            command_list = input_string.split()
            command = command_list[0]
            if command == "Fire":
                index = int(command_list[1])
                damage = int(command_list[2])
                if 0 <= index < len(warships):
                    warships[index] -= damage
                    if warships[index] <= 0:
                        print("You won! The enemy ship has sunken.")
                        return

            elif command == "Defend":
                start_index = int(command_list[1])
                end_index = int(command_list[2])
                damage = int(command_list[3])
                if (len(pirate_ships) > start_index >= 0
                        and start_index <= end_index < len(pirate_ships) and end_index >= 0):
                    for ship_number in range(start_index, end_index + 1):
                        pirate_ships[ship_number] = pirate_ships[ship_number]-damage if pirate_ships[ship_number] > damage else 0
                        if pirate_ships[ship_number] == 0:
                            print("You lost! The pirate ship has sunken.")
                            return


            elif command == "Repair":
                index = int(command_list[1])
                health = int(command_list[2])

                if 0 <= index < len(pirate_ships):
                    pirate_ships[index] = min(pirate_ships[index] + health, max_health)

            elif command == "Status":
                count_ships_to_repair = 0
                for pirate in pirate_ships:
                    if pirate < max_health * 0.2:
                        count_ships_to_repair += 1

                print(f"{count_ships_to_repair} sections need repair.")



manOWar()