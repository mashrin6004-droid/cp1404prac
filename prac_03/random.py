
MAX_COLUMNS = 10
MIN_COLUMNS = 2
LOWER = 33
UPPER = 127
char = input("Enter a character: ")
print(f"The ASCII code for {char} is {ord(char)}")
number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
while number < LOWER or number > UPPER:
    number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
print(f"The character for {number} is {chr(number)}")

for value in range(LOWER, UPPER + 1):
    print(f"{value:3} {chr(value):>4}")

number_of_columns = int(input("Enter number of columns: "))
while number_of_columns < MIN_COLUMNS or number_of_columns > MAX_COLUMNS:
    print(f"Please use a value between {MIN_COLUMNS} and {MAX_COLUMNS}")
    number_of_columns = int(input("Enter number of columns: "))
number_of_values = UPPER - LOWER + 1
number_of_rows = number_of_values // number_of_columns

print("Version 1: Horizontal then vertical ordering")

value = LOWER
for row_number in range(number_of_rows):
    for column_number in range(number_of_columns):
        print(f"{value:6} {chr(value):>2}", end="")
        value += 1
    print()
starting_value = value
for value in range(starting_value, UPPER + 1):
    print(f"{value:6} {chr(value):>2}", end="")
print("\n")
print("Version 2: Vertical then horizontal ordering")
for row_number in range(number_of_rows + 1):
    starting_value = LOWER + row_number
    value = starting_value
    for column_number in range(number_of_columns - 1):
        value_to_print = value + (column_number * number_of_rows)
        print(f"{value_to_print:6} {chr(value_to_print):>2}", end="")
        value += 1
    value_to_print = value + ((column_number + 1) * number_of_rows)
    if value_to_print <= UPPER:
        print(f"{value_to_print:6} {chr(value_to_print):>2}", end="")
    print()