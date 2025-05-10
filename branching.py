# Misael Rivera - Perez
# 5/20/2025
# This program will ask for your year of origin and will display different messages based on the year

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print('Woah, thats the past!')
elif 1900 >= year <= 2025:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")

input("Press ENTER to Exit") # This makes sure the program doesn't close until Enter key is pressed