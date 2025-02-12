print("Hello World")

# Write a program that calculates area of a rectangle
# width = 20
# length = 30
# area = width * length
# print(f"Area is = {area}")

# def calculate_area(width, length):
#     area = width * length
#     print(f"Area is = {area}")
#
# calculate_area(30,60)

# Write a program that multiplies a variable by 5 using the *= operator

# num = 40
# num *= 5
# print(num)

# Write a program that checks if two variables have the same value and type.

# name = "Roland"
# is_male = False
#
# if type(name) == type(is_male):
#     print(f"{name} is equal to {is_male}")
# else:
#     print(f"{name} is not equal {is_male}")

# Concatenate the strings "Hello" and "World" with a space between them.
# print("Hello" + " " + "World")

# Extract the word "fun" from the string "Coding is fun" using the slice() method.
# str_list = "Coding is fun".split()
# str_list.remove("fun")
# print(str_list)

# Write a program that checks if a number is positive, negative, or zero.
# num = 20
# if num > 0:
#     print(f"{num} is a positive")
# elif num == 0:
#     print(f"{num} is zero")
# else:
#     print(f"{num} is negative")

# Use a ternary operator to check if a number is odd or even.
# num = 15
# print(f"{num} is even") if num%2 == 0 else print(f"{num} is odd")

#  Write a function greet that takes a name as an argument and returns "Hello, [name]!"
# def greet_user(name):
#     print(f"Hello, {name}!")
#
# greet_user("Roland")

# Create a function add that takes two numbers and returns their sum.

# def sum_nums(a,b):
#     return a + b
# print(sum_nums(1,6))

# Write a function isEven that checks if a given number is even.
# def is_even(num):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is not even")
# is_even(12)
# is_even(15)

# Use a for loop to print numbers from 1 to 10.
# for num in range(1,11):
#     print(f"{num}..")

# Write a while loop to print the first 5 multiples of 3
# count = 1
# while count <= 5:
#     print(count * 3)
#     count += 1

# Use a for loop to calculate the factorial of a number n
# result = 1
# num = 3
# for value in range(1,num+1):
#     result = result * value
# print(f"{num}! is {result}")

# Write a program that counts how many times the letter "a" appears in the string "JavaScript is amazing!"
# some_str = "JavaScript is amazing!"
# count = 0
# for letter in some_str:
#     if letter == 'a':
#         count += 1
#
# print(f"There are {count} a's ")

# Create a function sumArray that takes an array of numbers and returns their sum.
# nums_arr = [1,2,3,4,5]
# num_sum = 0
# for num in nums_arr:
#     num_sum += num
#
# print(f"The sum of nums in {nums_arr} is {num_sum}")

# Write a loop to log all key-value pairs of the object {a: 1, b: 2, c: 3}
# obj = {"a": 1, "b": 2, "c": 3}
# for prop in obj:
#     print(f"{prop}:{obj[prop]}")


# Check if the number 5 exists in the list [1, 2, 3, 4, 5] using the includes() method.
# some_arr = [1,2,3,4,5]
# # ask user to enter number
# num_to_check = input("Find which number?\n")
# if int(num_to_check) in some_arr:
#     print("Yes it exists")

# Write a function findMax that returns the largest number from an array of numbers.
some_arr = [1,5,2,9,4,12,54,20,394,3937,33,282]
max_num = some_arr[0]

for num in some_arr:
    if num > max_num:
        max_num = num

print(f"The Maximum number is {max_num}")

