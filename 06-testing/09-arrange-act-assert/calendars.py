from datetime import date

class Calendar:
    def __init__(self):
        self.__today = date.today()
    
    @property
    def today(self):
        return self.__today

# calendar = Calendar()
# print(calendar.today)

class CalendarStub:
    def __init__(self, today):
        self.today = today
    
# # The constructor allows picking our own date
# d = date(2000, 1, 1)
# calendar = CalendarStub(d)
# print(d == calendar.today)

# # We can change the date as we see fit
# d = date(2001, 1, 1)
# calendar.today = d
# print(d == calendar.today)
