# Exercise 7
# Your solution comes here

number = input() #user inputs a number
total = 0  #set total to zero to incriment later

for x in range(4):        #for loop in range 4 because there is 4 digit numbers
  total += int(number[x]) #add the number in the incrimented position(x) to the total 
  
print(total)

