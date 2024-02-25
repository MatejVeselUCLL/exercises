class Duration:
    def __init__(self, *, seconds):
        self.duration_in_seconds = seconds

    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds = seconds)
    
    @staticmethod
    def from_minutes(minutes):
        return Duration(seconds = minutes * 60)

    @staticmethod
    def from_hours(hours):
        return Duration(seconds = hours * 3600)

    @property
    def seconds(self):
        return self.duration_in_seconds
    
    @property
    def minutes(self):
        return self.seconds / 60

    @property
    def hours(self):
        return self.seconds / 3600

# duration = Duration.from_seconds(60)
# print(60, duration.seconds)
# print(1, duration.minutes)
# duration = Duration.from_hours(1)
print(60, duration.minutes)
print(3600, duration.seconds)
