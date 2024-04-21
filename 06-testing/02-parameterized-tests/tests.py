import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    (''),
    ('()'),
    ('()()'),
    ('(())'),
    ('(())(())'),
    ('(()())')
])
def test_matching_parentheses_when_True_should_be_returned(string):
    assert matching_parentheses(string), f'Asserted "{string}". Expected True, received False.'

@pytest.mark.parametrize('string', [
    ('('),
    (')'),
    (')('),
    ('))(('),
    ('(((())'),
    ('())')
])
def test_matching_parentheses_when_False_should_be_returned(string):
    assert not matching_parentheses(string), f'Asserted "{string}". Expected False, received True.'