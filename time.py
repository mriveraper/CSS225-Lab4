# Misael Rivera - Perez
# 5/10/2025
# This program takes your current time and time you want to wait and give you the time it would be

currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)

input("Press ENTER to Exit") # This makes sure the program doesn't close until Enter key is pressed
