# Misael Rivera - Perez
# 5/10/2025
# This program will take the time and how long you have to wait and print out when the alarm will sound

str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)

input("Press ENTER to Exit") # This makes sure the program doesn't close until Enter key is pressed