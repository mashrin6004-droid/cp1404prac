
from programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991) 
    print(python)

    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamic():
            print(lang.name)

if __name__ == "__main__":
    main()
