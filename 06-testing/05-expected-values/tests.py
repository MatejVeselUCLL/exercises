from mergesort import split_in_two, merge_sorted, merge_sort
import pytest, itertools

# @pytest.mark.parametrize('ns', [
#     # ([]),
#     (list(range(n))) for n in range(101)
# ])
# def test_split_in_two(ns):
#     left, right = split_in_two(ns)
#     assert left + right  == ns, f"Expected {ns} Received {left + right}"


@pytest.mark.parametrize('left', [
    [],
    [1],
    [1, 2],
    [5, 6, 7],
    [5, 6, 7],
    [1, 1, 1],
    [1, 2, 2],
    [1, 20, 40],
    [-5, 1, 2.4]
])
@pytest.mark.parametrize('right', [
    [],
    [0, 1],
    [1, 2, 3, 4, 5, 6],
    [9, 10, 11],
    [5, 6],
    [5, 6, 7],
    [1, 2, 2],
    [1, 2, 3],
    [-5, 1, 2.4]
])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right), f"Left: {left}, Right: {right}"



expected_lists = [
    [0, 1],
    [1, 2, 3, 4, 5, 6],
    [9, 10, 11],
    [5, 6],
    [5, 6, 7],
    [1, 2, 2],
    [1, 2, 3],
    [-5, 1, 2.4]
]
@pytest.mark.parametrize('ns, expected', [
    (list(permutation), expected_list) 
    for expected_list in expected_lists
    for permutation in list(itertools.permutations(expected_list))
])
def test_merge_sort(ns, expected):
    result = merge_sort(ns)
    assert result == expected, f"Expected {expected} Received {result}"