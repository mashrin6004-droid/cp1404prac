
class Guitar:
    def __init__(self, name: str, year: int, cost: float):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def is_vintage(self) -> bool:
        """Return True if guitar is vintage (older than 50 years)."""
        from datetime import date
        return date.today().year - self.year >= 50

    def __str__(self):
        vintage = " (vintage)" if self.is_vintage() else ""
        return f"{self.name}, {self.year}, ${self.cost:.2f}{vintage}"

    def __repr__(self):
        return f"Guitar(name={self.name!r}, year={self.year}, cost={self.cost})"

    def __lt__(self, other):
        """Less-than compares by year (oldest first)."""
        if not isinstance(other, Guitar):
            return NotImplemented
        return self.year < other.year
