"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ANSWER 1: when the user enters something that cannot be converted to an integer
2. When will a ZeroDivisionError occur?
ANSWER 2: when the denominator entered is 0 and the program tries to divide by it
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
ANSWER 3: 
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be zero.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

