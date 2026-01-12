# number = int(input())
# for j in range(number):
#     for i in range(j+1):
#         print('$', end=' ')
#     print()

# number = int(input())
#
# for row in range(1, number + 1):
#     for col in range(1, number + 1):
#         if (row == col == 1) or (row == col == number) or (row == 1 and col == number)  or (row == number and col == 1):
#             print("+", end=" ")
#         elif (col == 1 or col == number) and 1 < row < number + 1 :
#             print("|", end=" ")
#         else:
#             print("-", end=" ")
#     print()


#Drawing Figures with Loops -06. Rhombus of Stars
# n = int(input())
# for row in range(0, n + 1):
#     print(" " * (n - row), end="")
#     print("*" * row, end="")
#     print(" | ", end="")
#     print("*" * row)

# #Drawing Figures with Loops - 08. Sunglasses
# n = int(input())
# print("*" * 2 * n , end =" " * n )
# print("*" * 2 * n)
#
# for row in range(n - 2):
#     if row ==(n-3)//2:
#         print("*", end = '')
#         print("/" *(2*n-2) , end = '')
#         print("*", end = '')
#         print("|"*n, end = '')
#         print("*", end='')
#         print("/" * (2*n-2), end='')
#         print("*")
#     else:
#         print("*", end='')
#         print("/"  *(2*n-2), end='')
#         print("*", end='')
#         print(" " * n, end='')
#         print("*", end='')
#         print("/"  *(2*n-2), end='')
#         print("*")
#
# print("*" * 2 * n, end=" " * n)
# print("*" * 2 * n)
#
# #Drawing Figures with Loops - 09. House
# n = int(input())
# roof_rows = (n + 1)//2
# current_stars = 1 if n % 2 != 0 else 2
#
# for i in range(1, roof_rows + 1):
#
#     print("-" * ((n - current_stars) // 2), end="")
#     print("*" * current_stars , end="")
#     print("-" *((n - current_stars) // 2), end="")
#     print()
#     current_stars += 2
#
# for j in range(1, n//2 + 1):
#     print("|", end="")
#     print("*" * (n-2), end="")
#     print("|", end="")
#     print()


#
# #Drawing Figures with Loops - 10. Diamond
# n = int(input())
# left_right = (n - 1)//2
# mid = n - 2 * left_right - 2
#
# for row in range(n + 1):
#     print("-" * left_right, end="")
#     print("*", end="")
#     if (mid >= 0):
#         print("-" * mid, end="")
#         print("*", end="")
#
#     print("-" * left_right, end="")
#     print()
#
#     if left_right <= 0:
#         break
#     left_right -= 1
#     mid += 2
#
#
# left_right = 0
# mid = n - 2
#
# for row_down in range(2, n):
#     left_right += 1
#     mid -= 2
#     print("-" * left_right, end="")
#     print("*", end="")
#     if (mid >= 0):
#         print("-" * mid, end="")
#         print("*", end="")
#
#     print("-" * left_right, end="")
#     print()
#
#     if mid <= 0:
#         break

def is_good_size(value):
    return ((0 < value <= 54) or
            (162 < value <= 270) or
            (375 < value <= 432))


def is_money_size(value):

    if (0 <= value <= 54) or (375 <= value <= 432):
        return True

    if (175.5 <= value <= 189.0):
        print("Dop dohod")
        return True

    if (202.5 <= value <= 215.0):
        print("Udacha i pozitiv sobitiya")
        return True

    if (229.5 <= value <= 243.5):
        print("Udacha v sdelkah")
        return True

    if (243.5 < value <= 256.5):
        print("Rost dohodov")
        return True


    return False

new_number = 900
for effective_side in range(210, 900, 5):

    if effective_side > 432:
         new_number= effective_side % 432
    else:
        new_number = effective_side

    if is_good_size(new_number):
        small_side = effective_side / 3
        if is_good_size(small_side):
            if  is_money_size(new_number) or is_money_size(small_side):
                print(f"Number is {effective_side} ({new_number}) , small square is {small_side:.1f}")



