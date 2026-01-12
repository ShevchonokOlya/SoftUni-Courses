# num1 = int(input())
# counter = 0
# total = 0
#
# for i in range(num1+1):
#     for j in range(num1+1):
#         for k in range(num1+1):
#             total += 1
#             if (i+j+k) == num1:
#                 counter += 1
#                 break
#
# print(counter)
# print(total)

# num1 = int(input())
# counter = 0
#
# for i in range(num1 + 1):
#     # j идёт только до "остатка" от n (n - i)
#     for j in range(num1 - i + 1):
#         k = num1 - i - j
#         print(f"{i} {j} {k}")
#         counter += 1
#
# print(counter)


# start = int(input())
# end = int(input())
# magic_number = int(input())
# is_found = False
# counter = 0
#
# for i in range(start, end+1):
#     for j in range(start, end+1):
#         counter += 1
#         if (i+j == magic_number):
#             is_found = True
#             print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
#             break
#     if is_found:
#         break
# if not is_found:
#     print(f"{counter} combinations - neither equals {magic_number}")
#
# while True:
#     destination = input()
#     if destination == "End":
#         break
#     budget = float(input())
#     money = 0.0
#     while budget > money:
#         salary = float(input())
#         money += salary
#     else:
#         print(f"Going to {destination}!" )

# floor_number = int(input())
# flat_number = int(input())
#
# for floor in range(floor_number, 0, -1):
#
#     if floor == floor_number:
#         letter = "L"
#     elif floor % 2 == 0:
#         letter = "O"
#     else:
#         letter = "A"
#
#     for flat in range(flat_number):
#         if flat == flat_number - 1:
#             print(f"{letter}{floor}{flat}")
#         else:
#             print(f"{letter}{floor}{flat}", end=" ")



########################



########################

#WHILE Loop - Exercise

########################



########################


# number = int(input())
# current  = 1
# row = 1
# while current <= number:
#     for column in range(current , current + row, 1):
#         if current <= number:
#             print(current, end=" ")
#             current += 1
#         else:
#             break
#
#     print("")
#     row += 1

# #2
# number1 = int(input())
# number2 = int(input())
#
# for number in range(number1, number2 + 1):
#     string_digits = str(number)
#     even_sum = 0
#     odd_sum = 0
#     for index, char in enumerate(string_digits):
#         if (index + 1) % 2 == 0: #четно
#             even_sum += int(char)
#         else:
#             odd_sum += int(char)
#
#     if even_sum == odd_sum:
#         print(number, end=' ')

# prim_sum = 0
# non_prim_sum = 0
#
# while True:
#     input_str = input()
#     if input_str == 'stop':
#         break
#
#     number = int(input_str)
#
#     if number < 0:
#         print('Number is negative.')
#         continue
#     elif number < 2:
#         non_prim_sum += number
#         continue
#
#     is_prime = True
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#
#
#     if  is_prime:
#         prim_sum += number
#     else:
#         non_prim_sum += number
#
# print(f"Sum of all prime numbers is: {prim_sum}")
# print(f"Sum of all non prime numbers is: {non_prim_sum}")

#4
# judges_number = int(input())
# count_of_students = 0
# marks_of_students = 0.0
#
# while True:
#     presentation_text = input()
#     if presentation_text == 'Finish':
#         break
#
#     count_of_students +=1
#     student_mark = 0.0
#
#     for judge_num in range(judges_number):
#         student_mark += float(input())
#     student_mark /= judges_number
#     marks_of_students += student_mark
#     print(f'{presentation_text} - {student_mark:.2f}.')
#
# print(f"Student's final assessment is {marks_of_students/count_of_students:.2f}." )





# #5
# number = int(input())
#
# for looking_number in range(1111, 10000):
#     is_special = True
#     digit = looking_number
#
#     while digit > 0:
#         cur_number = digit % 10
#         digit //= 10
#
#
#         if cur_number == 0 or number % cur_number != 0:
#             is_special = False
#             break
#
#     if is_special:
#             print(looking_number, end=' ')

# #6
# count_of_student = 0
# count_of_standard = 0
# count_of_kid = 0
#
# while True:
#     film_name  = input() #name or Finish
#     if film_name == 'Finish':
#         break
#     place = int(input()) #1...100
#
#     count_of_ticket_in_the_Hall = 0
#
#     while (place > count_of_ticket_in_the_Hall):
#
#         type_of_ticket = input() # "student", "standard", "kid" or End
#         if type_of_ticket == "End":
#             break
#
#         if type_of_ticket == "student":
#             count_of_student += 1
#         elif type_of_ticket == "standard":
#             count_of_standard += 1
#         elif type_of_ticket == "kid":
#             count_of_kid += 1
#
#         count_of_ticket_in_the_Hall += 1
#
#         if place == count_of_ticket_in_the_Hall:
#             break
#     print(f"{film_name} - {(count_of_ticket_in_the_Hall / place):.2%} full.")
#
#
# total_ticket = count_of_student+ count_of_standard + count_of_kid
#
# print(f"Total tickets: {total_ticket}")
# print(f"{(count_of_student/total_ticket):.2%} student tickets.")
# print(f"{(count_of_standard/total_ticket):.2%} standard tickets.")
# print(f"{(count_of_kid/total_ticket):.2%} kids tickets.")

#
# # Nested Loops - More Exercises -01. Unique PIN Codes
# from math import sqrt
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# upper_limit_first_number = int(input())
# upper_limit_second_number = min(int(input()), 7)
# upper_limit_third_number = int(input())
#
# #first_number = 2 #even
# #second_number = 2 #2..7 prime number
# #third_number = 2 #even
#
# for first_number in range(2, upper_limit_first_number + 1):
#     if first_number % 2 == 0:
#         for second_number in range(2, upper_limit_second_number + 1):
#             if is_prime(second_number):
#                 for third_number in range(2, upper_limit_third_number + 1):
#                     if third_number % 2 == 0:
#                         print(first_number, second_number, third_number)

# # Nested Loops - More Exercises -02. Letters Combinations
# start_letter = ord(input())
# finish_letter = ord(input())
# skip_letter = ord(input())
# counter = 0
#
# for first in range(start_letter, finish_letter + 1):
#     if first != skip_letter:
#         for second in range(start_letter, finish_letter + 1):
#             if second != skip_letter:
#                 for third in range(start_letter, finish_letter + 1):
#                     if third != skip_letter:
#                         word = chr(first) + chr(second) + chr(third)
#                         print(word , end = ' ')
#                         counter += 1
#
# print(counter)

# Nested Loops - More Exercises 03. Lucky Numbers
#
# number = int(input())
#
# max_number = 9 if number >= 10 else number
#
#
# for first in range(1, max_number + 1):
#    for second in range(1, max_number + 1):
#        if number % (first + second)  == 0:
#            for third in range(1, max_number + 1):
#                for fourth in range(1, max_number + 1):
#                    if third + fourth == first + second:
#                        print(f"{first}{second}{third}{fourth}", end = " ")

#
# # Nested Loops - More Exercises - 04. Car Number
# start_number = int(input())
# end_number = int(input())
#
# for first_number in range(start_number + 1, end_number + 1):
#     for second_number in range(start_number, end_number + 1):
#         for third_number in range(start_number, end_number + 1):
#           if (second_number + third_number) % 2 == 0:
#             for fourth_number in range(start_number, end_number):
#                 if ((first_number % 2 == 0 and fourth_number % 2 == 1)
#                     or (first_number % 2 == 1 and fourth_number % 2 == 0)):
#                     if first_number > fourth_number:
#                        print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")


# Nested Loops - More Exercises - 05. Challenge the Wedding
# men_number = int(input())
# women_number = int(input())
# tables = int(input())
# counter = 0
# for men in range(1, men_number + 1):
#     for women in range(1, women_number + 1):
#         counter += 1
#
#         print(f"({men} <-> {women})", end=" ")
#         if counter >= tables:
#             break
#     if counter >= tables:
#         break

#
# # Nested Loops - More Exercises - 06. Wedding Seats
# start_sector = ord("A")
# end_sector = ord(input())
# rows_in_first_sector = int(input())
# odd_row_number_of_seats = int(input())
# counter = 0
#
# even_row_number_of_seats= odd_row_number_of_seats + 2
# current_row = rows_in_first_sector
#
# for sector in range(start_sector, end_sector + 1):
#     for number_row in range(1, current_row + 1):
#         number_of_seats = even_row_number_of_seats  if number_row % 2 == 0 else odd_row_number_of_seats
#         for seat in range(0, number_of_seats):
#             letter_of_seat = chr(ord("a") + seat)
#             print(f"{chr(sector)}{number_row}{letter_of_seat}")
#             counter += 1
#     current_row += 1
#
# print(counter)


# # Nested Loops - More Exercises - 07. Safe Passwords Generator
# number_a = int(input())
# number_b = int(input())
# max_count = int(input())
# Acode = 35
#
# Bcode= 64
#
# pass_counter = 0
# passwords_list = []
#
# for x in range(1,  number_a + 1):
#     for y in range(1, number_b + 1):
#
#         if pass_counter >= max_count:
#             break
#
#         password = chr(Acode)  + chr(Bcode) + str(x) + str(y) + chr(Bcode)+ chr(Acode) + "|"
#         passwords_list.append(password)
#         pass_counter += 1
#
#         Bcode +=1
#         Acode +=1
#
#         if Acode > 55:
#             Acode = 35
#         if Bcode > 96:
#             Bcode = 64
#
#     if pass_counter >= max_count:
#         break
#
# print("".join(passwords_list))
#
# # Nested Loops - More Exercises - 08. Secret Door's Lock
# from math import sqrt
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# upper_100 = int(input())
# upper_10= int(input())
# upper_1 = int(input())
#
# for i in range(1,upper_100+1):
#     if i%2==0:
#         for j in range(1, upper_10 + 1):
#             if is_prime(j):
#                 for k in range(1, upper_1 +1):
#                     if k%2==0:
#                         print(f"{i} {j} {k}")
#
# # # Nested Loops - More Exercises - 09. Sum of Two Numbers
# start = int(input())
# end = int(input())
# magic_number = int(input())
# is_found = False
# counter = 0
#
# for i in range(start, end+1):
#     for j in range(start, end+1):
#         counter += 1
#         if (i+j == magic_number):
#             is_found = True
#             print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
#             break
#     if is_found:
#         break
# if not is_found:
#     print(f"{counter} combinations - neither equals {magic_number}")

#
# # Nested Loops - More Exercises -10. Profit
# number_1_leva = int(input())
# number_2_leva = int(input())
# number_5_leva = int(input())
# sum_need = int(input())
#
# for lev in range(0, number_1_leva + 1):
#     for lev2 in range(0, number_2_leva + 1):
#         for lev5 in range(0, number_5_leva + 1):
#             if (lev * 1 + lev2 * 2 + lev5 * 5) == sum_need:
#                 print(f"{lev} * 1 lv. + {lev2} * 2 lv. + {lev5} * 5 lv. = {sum_need} lv.")




# # Nested Loops - More Exercises -11. HappyCat Parking
#
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


# # Nested Loops - More Exercises -12. The song of the wheels
# control_sum = int(input()) #4--144
# counter = 1
# password = ""
# for a in range(1, 10):
#     for b in range(1, 10):
#         if a < b :
#             for c in range(1, 10):
#                 for d in range(1, 10):
#                     if c > d :
#                         if a * b  + c * d == control_sum:
#                             print(f"{a}{b}{c}{d}", end=" ")
#
#                             if counter == 4:
#                                 password = f"Password: {a}{b}{c}{d}"
#                             counter += 1
# print()
# if counter > 4:
#     print(password)
# else:
#     print("No!")


#
#
# # Nested Loops - More Exercises -13. Prime Pairs
#
# from math import sqrt
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# start_number1 = int(input())
# start_number2 = int(input())
# final_number1 = start_number1 +  int(input())
# final_number2 = start_number2 + int(input())
#
# for first_number in range(start_number1, final_number1 + 1):
#     for second_number in range(start_number2, final_number2 + 1):
#         if is_prime(first_number) and is_prime(second_number):
#             print(f"{first_number}{second_number}")


# Nested Loops - More Exercises -14. Password Generator
n = int(input())
l = int(input())
for first in range(1, n + 1):
    for second in range(1, n + 1):
        for third in range(97, 97 + l):
            for fourth in range(97, 97 + l):
                for fifth in range(1, n + 1):
                    if fifth > first and fifth >second:
                        print(f"{first}{second}{chr(third)}{chr(fourth)}{fifth}", end=" ")

