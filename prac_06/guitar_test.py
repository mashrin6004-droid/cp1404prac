from guitar import Guitar
from datetime import date

def main():
    current_year = date.today().year
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 100.0)

    expected_gibson_age = current_year - 1922
    expected_another_age = current_year - 2013

    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {gibson.get_age(current_year)}")
    print(f"{another.name} get_age() - Expected {expected_another_age}. Got {another.get_age(current_year)}")

    print(f"{gibson.name} is_vintage() - Expected {expected_gibson_age >= 50}. Got {gibson.is_vintage(current_year)}")
    print(f"{another.name} is_vintage() - Expected {expected_another_age >= 50}. Got {another.is_vintage(current_year)}")

if __name__ == "__main__":
    main()
