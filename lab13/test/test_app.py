import pytest
from app import bubble_sort

testdata = [
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([1, 1, 1, 0], [0, 1, 1, 1])
    ]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_text_contain_word(sample, expected_output):

    assert bubble_sort(sample) == expected_output