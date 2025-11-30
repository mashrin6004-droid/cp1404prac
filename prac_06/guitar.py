
from datetime import date

class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        self.name = str(name)
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year=None):
        if current_year is None:
            current_year = date.today().year
        return current_year - self.year

    def is_vintage(self, current_year=None):
        return self.get_age(current_year) >= 50
