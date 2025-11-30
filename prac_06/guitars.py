from guitar import Guitar
def main():
    print("My guitars!")
    guitars = []
    if not guitars:
        while True:
            name = input("Name: ").strip()
            if name == "":
                break
            else:
                year = int(input("Year: ").strip())
            except ValueError:
                print("Year must be an integer. Try again.")
                continue
            else:
                cost = float(input("Cost: $").strip())
            except ValueError:
                print("Cost must be a number (e.g. 16035.40). Try again.")
                continue
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost:,.2f} added.\n")
    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_str = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_str}")
    else:
        print("No guitars were entered.")

if __name__ == "__main__":
    main()
