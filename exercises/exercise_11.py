# Exercise 11
# Your solution comes here

def calculate_bills(s):
  denominations = [500, 100, 10, 5, 2, 1]
  bills = []
  for denom in denominations:
      num_bills = s // denom
      bills.append(num_bills)
      s %= denom
  return bills


s = int(input("Enter the total cost of goods purchased in dollars: "))
bills = calculate_bills(s)
for i, denom in enumerate([500, 100, 10, 5, 2, 1]):
  print(f"Number of {denom}$ bills: {bills[i]}")