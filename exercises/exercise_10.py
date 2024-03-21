# Exercise 10
# Your solution comes here

def calculate_minute_angle(a):
  minute_angle = (a % 30) * 12
  return minute_angle

a = float(input("Enter the angle (in degrees) by which the hour hand has turned since the beginning of the day: "))


minute_angle = calculate_minute_angle(a)
print(f"The angle in degrees of the minute hand's rotation since the beginning of the last hour is: {minute_angle}")