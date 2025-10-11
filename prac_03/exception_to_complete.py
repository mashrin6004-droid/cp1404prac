"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: set the flag to end the loop when input is valid
    except:  # TODO - catch the correct exception for invalid integer input
        print("Please enter a valid integer.")
print("Valid result is:", result)
