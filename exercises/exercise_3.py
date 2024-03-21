# Exercise 3
# Your solution comes here

seconds = int(input())

hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(f"{hours}:{minutes}:{seconds}")
