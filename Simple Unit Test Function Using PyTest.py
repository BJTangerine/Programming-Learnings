# test for a convert_to_int() function that takes an integer valued string with commas as thousand separators e.g. "2,081" as argument
# and should return the integer 2081.

import pytest
from preprocessing_helpers import convert_to_int

def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
    
    # assert statement which prints message on failure
    assert actual is expected, message