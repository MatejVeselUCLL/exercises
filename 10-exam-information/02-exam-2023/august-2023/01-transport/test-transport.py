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

# You must write tests which sufficiently test the property maximum_occupants. Include these tests in the test-transport.py file.

# Refer to the description of both Taxi and Bus for information about how to implement maximum_occupants.
# Use the conventions you learned in the Testing chapter to be able to test this functionality.

# Time: 40 minutes

import pytest
from transport import *


@pytest.mark.parametrize('amount_of_seats, expected', [
    (2, 2),
    (4, 4),
    (5, 5),
    (8, 8),
    (99, 99)
])
def test_maximum_occupants_taxi(amount_of_seats, expected):
    my_taxi = Taxi("1-NGL-760", amount_of_seats)

    received = my_taxi.maximum_occupants

    assert expected == received



@pytest.mark.parametrize('amount_of_seats, expected', [
    (7.5, 15), # Q& Is this ok?
    (15, 30),
    (30, 60),
    (40, 80)
])
def test_maximum_occupants_bus(amount_of_seats, expected):
    my_bus = Bus("1-HUE-344", amount_of_seats)

    received = my_bus.maximum_occupants

    assert expected == received