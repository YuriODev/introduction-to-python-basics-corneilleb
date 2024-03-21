# Exercise 9
# Your solution comes here


def calculate_hour_angle(h, m, s):
    hour_angle = (360 / 12) * (h % 12) + (30 / 60) * m + (30 / 3600) * s
    return hour_angle


h = int(input("Enter the number of hours passed since the beginning of the day: "))
m = int(input("Enter the number of minutes passed past the hour: "))
s = int(input("Enter the number of seconds passed past the minute: "))


hour_angle = calculate_hour_angle(h, m, s)
print(f"The angle in degrees of the hour hand's rotation since the start of the day is: {hour_angle}")