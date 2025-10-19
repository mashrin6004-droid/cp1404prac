"""
CP1404/CP5632 Practical
Wimbledon data reading, processing and displaying
"""

import csv

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def load_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig", newline="") as in_file:
        reader = csv.reader(in_file)
        try:
            header = next(reader)
        except StopIteration:
            return records
        for row in reader:
            if not row:
                continue
            records.append(row)
    return records


def process_records(records):
    champion_to_count = {}
    countries = set()

    for record in records:
        # defensive: ensure indices exist
        if len(record) <= max(INDEX_COUNTRY, INDEX_CHAMPION):
            # skip / optionally log malformed line
            continue
        country = record[INDEX_COUNTRY].strip()
        champion = record[INDEX_CHAMPION].strip()
        countries.add(country)
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1

    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display Wimbledon champions and the list of countries that have won."""
    print("Wimbledon Champions (wins):")
    # sort by wins descending, then name
    for name, count in sorted(
        champion_to_count.items(), key=lambda x: (-x[1], x[0])
    ):
        print(f"{name}: {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()

