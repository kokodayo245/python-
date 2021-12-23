# 7-2
number = input("How many people are there?")
number = int(number)
if number > 8:
    print("There are no seat available.")
else:
    print("There are seat available.")

# 7-3
number = input("Please enter a number: ")
number = int(number) % 10
if number == 0:
    print("The number is integral multiple of 10")
else:
    print("The number is not integral multiple of 10")
