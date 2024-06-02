class Duration:
    def __init__(self, duration_in_seconds):
        self.duration_in_seconds = duration_in_seconds

    @property
    def seconds(self):
        return self.duration_in_seconds
    @property
    def minutes(self):
        return self.duration_in_seconds // 60
    @property
    def hours(self):
        return self.duration_in_seconds // 3600

    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)
    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes * 60)
    @staticmethod
    def from_hours(hours):
        return Duration(hours * 3600)

# duration = Duration.from_seconds(60)
# print(60, duration.seconds)
# print(1, duration.minutes)
# duration = Duration.from_hours(1)
# print(60, duration.minutes)
# print(3600, duration.seconds)