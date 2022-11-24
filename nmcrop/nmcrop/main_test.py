"""
test nmcrop with command: `pytest --pyargs nmcrop`
"""
#  pylint: disable=C0103

from . import find_min, create_sequence


def test_find_min():
    """tests for find_min function"""

    assert find_min([1]) == 1
    assert find_min([1,2]) == 1
    assert find_min([2,1]) == 1
    assert find_min([3,2,1,3,4,5]) == 1

    for L in [1, 10, 100, 1000]:
        x_ast, x = create_sequence(L)
        assert find_min(x) is x_ast
