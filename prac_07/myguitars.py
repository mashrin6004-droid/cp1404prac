
from guitar import Guitar

DEFAULT_FILENAME = "guitars.csv"

def load_guitars(filename=DEFAULT_FILENAME):
    guitars = []
    try:
        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) < 3:
                    continue
                name = parts[0].strip()
                year = int(parts[1].strip())
                cost = float(parts[2].strip())
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        # If no file, return empty list
        pass
    return guitars

def save_guitars(guitars, filename=DEFAULT_FILENAME):
    with open(filename, 'w', encoding='utf-8') as f:
        for g in guitars:
            f.write(f"{g.name},{g.year},{g.cost:.2f}\n")

def display_guitars(guitars):
    if not guitars:
        print("No guitars available.")
        return
    for i, g in enumerate(guitars):
        print(f"{i+1}. {g}")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value

def main():
    guitars = load_guitars()
    print(f"Loaded {len(guitars)} guitars.")
    display_guitars(guitars)

    # Allow user to add guitars
    while True:
        add = input("Add a new guitar? (y/n): ").strip().lower()
        if add not in ('y', 'yes'):
            break
        name = get_non_empty("Name: ")
        year_str = get_non_empty("Year: ")
        cost_str = get_non_empty("Cost: ")
        try:
            year = int(year_str)
            cost = float(cost_str)
            guitars.append(Guitar(name, year, cost))
            print("Guitar added.")
        except ValueError:
            print("Invalid year or cost. Guitar not added.")

    # Sort by year (oldest first)
    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    save = input("Save guitars to file? (y/n): ").strip().lower()
    if save in ('y', 'yes'):
        save_guitars(guitars)
        print(f"Guitars saved to {DEFAULT_FILENAME}.")

if __name__ == "__main__":
    main()
