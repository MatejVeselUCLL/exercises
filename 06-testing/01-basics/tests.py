from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (2, 6))
    assert overlapping_intervals((2, 6), (1, 5))
    assert overlapping_intervals((5, 5), (5, 5))

    assert overlapping_intervals((5, 6), (2, 6))
    assert overlapping_intervals((1, 5), (2, 6))

    assert not overlapping_intervals((5, 1), (0, 0))
    assert not overlapping_intervals((0, 0), (5, 1))

    # if not ((left1 <= right1) and (left2 <= right2)):
    #     return False
    # elif left2 <= right1 <= right2 or left1 <= right2 <= right1:
    #     return True
    # elif left2 <= left1 <= right2 or left1 <= left2 <= right1:
    #     return True
    # else:
