from datetime import date

class Calendar:
    @property
    def today(self):
        return date.today()

# calendar = Calendar()
# print(calendar.today)

class CalendarStub:
    def __init__(self,today):
        self.today = today

# calendar = CalendarStub(date(2000,1,1))
# print(calendar.today)
# calendar.today = date.today()
# print(calendar.today)
