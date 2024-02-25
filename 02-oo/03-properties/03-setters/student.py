class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self, hours):
        if hours in range(0, 23+1):
            self.__hours = hours
        else:
            raise ValueError()

    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self, minutes):
        if minutes in range(0, 59+1):
            self.__minutes = minutes
        else:
            raise ValueError()

    @property
    def seconds(self):
        return self.__seconds
    @seconds.setter
    def seconds(self, seconds):
        if seconds in range(0, 59+1):
            self.__seconds = seconds
        else:
            raise ValueError()

# time = Time(0, 0, 0)
# time.hours = 8
# time.hours = -1 # ValueError
# time.hours = 24 # ValueError
