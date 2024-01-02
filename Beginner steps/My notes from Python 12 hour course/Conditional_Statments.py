temp = int(input("What is the temperature outside?: "))

# if 0 < temp <= 30:  # if temp > 0 and temp <= 30
#     print("The temperature is " + str(temp) + "C today, and that's good")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad today")

# Not operator 
if not (0 < temp <= 30):
    print("The temperature is bad today")
elif not (temp < 0 or temp > 30):
    print("The temperature is good today")
