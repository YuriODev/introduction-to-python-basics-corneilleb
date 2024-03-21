# Exercise 8
# Your solution comes here

num1 = int(input())
num2 = int(input())
num3 = int(input())



min_value = ((num1 <= num2) and (num1 <= num3)) * num1 + ((num2 <= num3) and (num2 < num1) * num2) + ((num3 < num1) and (num3 < num2) * num3)
max_value = ((num1 >= num2) and (num1 >= num3)) * num1 + ((num2 >= num3) and (num2 > num1) * num2) + ((num3 > num1) and (num3 > num2) * num3)
mid_value = num1 + num2 + num3 - min_value - max_value

print(f"{min_value}\n{mid_value}\n{max_value}")

# a = int(input())
# b = int(input())
# c = int(input())

# Calculate the minimum, middle, and maximum values
# min_value = a * (a <= b and a <= c) + b * (b < a or b < c) + c * (c < a and c < b)
# max_value = a * (a >= b and a >= c) + b * (b > a or b > c) + c * (c > a and c > b)
# mid_value = a + b + c - min_value - max_value

# # Print the sorted numbers
# print(min_value)
# print(mid_value)
# print(max_value)