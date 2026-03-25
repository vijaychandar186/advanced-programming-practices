"""
Lab 03 – Object-Oriented Programming
Program C: Prompt for today's day number (0=Sunday … 6=Saturday) and a
number of days in the future; display the resulting day of the week.
"""


class DayCalculator:
    DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"]

    def future_day(self, today: int, days_after: int) -> str:
        return self.DAYS[(today + days_after) % 7]


if __name__ == "__main__":
    today = int(input("Enter today's day (0=Sunday, 1=Monday, ..., 6=Saturday): "))
    days_after = int(input("Enter number of days after today: "))
    dc = DayCalculator()
    print(f"The day {days_after} day(s) from now is: {dc.future_day(today, days_after)}")
