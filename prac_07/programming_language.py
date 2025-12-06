
"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
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
