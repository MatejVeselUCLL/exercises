# Write your own tests for the housing.py file here.
# You must include the tests asked for in the assignment for full credit.
# You may add additional tests if you would like to test your code more thoroughly.
# Additional tests will not result in a higher grade.
# This file must be able to be run without error in order to receive credit for the required testing.
####
# Schrijf hier je eigen tests voor het housing.py bestand.
# Je moet de gevraagde tests in de opdracht opnemen voor volledige waardering.
# Je mag extra tests toevoegen als je je code grondiger wilt testen.
# Extra tests zullen niet leiden tot een hoger cijfer.
# Dit bestand moet zonder fouten uitgevoerd kunnen worden om punten te krijgen voor de vereiste testen.


# These rules must be combined. So a Residence with 72 square meters and 3 rooms can only fit 3 people (the smaller of the two calculations above).
# Other examples:
# A small studio with only 1 room and 30 square meters can have 1 person living in it.
# A slightly larger studio with 1 room and 40 square meters can have 2 people.
# An apartment with 3 rooms and 200 square meters can accommodate up to 6 people.

import pytest
from housing import *

@pytest.mark.parametrize('area, number_of_rooms, expected', [
    (72, 3, 3),
    (30, 1, 1),
    (40, 1, 2),
    (200, 3, 6)
])

def test_maximum_occupants(area, number_of_rooms, expected):
    residence = Villa("address", area, number_of_rooms, 1)

    received = residence.maximum_occupants
    assert received == expected