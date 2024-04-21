import pytest
from mystatistics import average

@pytest.mark.parametrize('ns, expected', [
    ([1, 2, 3, 4, 5], 3),
    ([0.1, 0.1, 0.1], 0.1),
    ([2.4532, 0.12356, 0.888888888888], 1.155181),
])
def test_average(ns, expected):
    avg = average(ns)
    # assert avg == expected, f"ns = {ns}, received {avg}, expected {expected}"
    assert pytest.approx(avg, abs=0.01) == expected, f"ns = {ns}, received {avg}, expected {expected}"