# Exercise 6
# Your solution comes here

a = int(input("Enter a number: "))#ask user to input two numbers
b = int(input("Enter a number: "))

check = "YES" * (a % b == 0) or "NO" # uses boolean to check if remainder of a divided by b is zero. if true then it will equate to 1. 

print(check)


