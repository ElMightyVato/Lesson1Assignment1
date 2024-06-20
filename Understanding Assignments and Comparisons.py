#Task 1: Value Swapping
#Swap the values of two given numbers using assignment operators (=) and then compare them to ensure they have been swapped.

#First values
a = 10
b = 20

#Swap Time
a = a + b
b = a - b
a = a - b

if a == 20 and b == 10:
    print("Swap was successful")
else:
    print("Swap Failed")