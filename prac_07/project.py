
from datetime import date

class Project:
    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, completion_percent: int):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percent = int(completion_percent)

    def is_completed(self) -> bool:
        return self.completion_percent >= 100

    def __str__(self):
        start_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percent}%")

    def __repr__(self):
        return (f"Project(name={self.name!r}, start_date={self.start_date!r}, priority={self.priority}, "
                f"cost_estimate={self.cost_estimate}, completion_percent={self.completion_percent})")

    def __lt__(self, other):
        """Sort by priority (lower number = higher priority)."""
        if not isinstance(other, Project):
            return NotImplemented
        return self.priority < other.priority
