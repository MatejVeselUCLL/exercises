class LengthConverter:
    FEET_PER_METER = 3.280839895
    INCH_PER_METER = 0.0254

    # Meter is the only non-computed field.
    @property
    def meter(self):
        return self.__meter
    @meter.setter
    def meter(self, meter):
        if meter < 0:
            return ValueError("Length must be non-negative.")
        self.__meter = meter

    @property
    def feet(self):
        return self.meter * LengthConverter.FEET_PER_METER
    @feet.setter
    def feet(self, feet):
        self.meter = feet / LengthConverter.FEET_PER_METER

    @property
    def inch(self):
        return self.meter / LengthConverter.INCH_PER_METER
    @inch.setter
    def inch(self, inch):
        self.meter = inch * LengthConverter.INCH_PER_METER


# converter = LengthConverter()
# # Set the distance to 100 meter
# converter.meter = 100
# # Convert the 100 meter into feet
# print(328.084, converter.feet)
# # Convert the 100 meter into inch
# print(3937.01, converter.inch)
# # Convert the 100 meter into meter
# print(100, converter.meter)
# # Set the distance to 5 feet
# converter.feet = 5
# # Convert 5 feet into inches
# print(60, converter.inch)