"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from prac_07.programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # open the file for reading
    in_file = open('languages.csv', 'r')

    # file format is like: Language,Typing,Reflection,Year
    # 'consume' the first line (header) - we don't need its contents
    in_file.readline()

    # all other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging

        # strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging

        # reflection is stored as a string (Yes/No) and we want a Boolean
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[3] == "Yes"

        # construct a ProgrammingLanguage object using the elements
        # year should be an integer
        language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic, int(parts[4]))

        # add the language we've just constructed to the list
        languages.append(language)

    # close the file as soon as we've finished reading it
    in_file.close()

    # loop through and display all languages (using their str method)
    for language in languages:
        print(language)


main()


def using_csv():
    """Language file reader version using the csv module."""
    # first, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        print(row)

    in_file.close()


# using_csv()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    # Language will be a new subclass of the tuple data type class
    Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
    reader = csv.reader(in_file)  # use default dialect, Excel

    for row in reader:
        # print(row)
        language = Language._make(row)
        print(repr(language))
    in_file.close()


# using_namedtuple()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))

# using_csv_namedtuple()



"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is like: Language,Typing,Reflection,Year
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Reflection is stored as a string (Yes/No) and we want a Boolean
        reflection = parts[2] == "Yes"
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))
        # Add the language we've just constructed to the list
        languages.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


main()


def using_csv():
    """Language file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        print(row)
    in_file.close()


# using_csv()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    # Language will be a new subclass of the tuple data type class
    Language = namedtuple('Language', 'name, typing, reflection, year')
    reader = csv.reader(in_file)  # use default dialect, Excel

    for row in reader:
        # print(row)
        language = Language._make(row)
        print(repr(language))
    in_file.close()


# using_namedtuple()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))

# using_csv_namedtuple()




"""
language_file_reader.py

Client code to read a CSV file of programming languages into ProgrammingLanguage objects.

CSV format (header expected):
Name,Typing,Reflection,PointerArithmetic

Reflection and PointerArithmetic values are "Yes" or "No" (case-insensitive).
"""

import csv
from programming_language import ProgrammingLanguage

DEFAULT_FILENAME = "languages.csv"

def parse_bool(value: str) -> bool:
    if value is None:
        return False
    return value.strip().lower() in ("yes", "y", "true", "1")

def load_languages(filename: str = DEFAULT_FILENAME):
    languages = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)  # skip header
            for row in reader:
                # expected: Name,Typing,Reflection,PointerArithmetic
                if not row or len(row) < 4:
                    continue
                name, typing, reflection_str, pointer_str = row[:4]
                reflection = parse_bool(reflection_str)
                pointer_arithmetic = parse_bool(pointer_str)
                lang = ProgrammingLanguage(name.strip(), typing.strip(), reflection, pointer_arithmetic)
                languages.append(lang)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return languages

def main():
    languages = load_languages()
    if languages:
        print(f"Loaded {len(languages)} languages:")
        for lang in languages:
            print(" -", lang)
    else:
        print("No languages loaded.")

if __name__ == "__main__":
    main()
