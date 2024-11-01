from code1 import total


def test_total():
    #The use cases :
    """The sum of several elements of a list must be correct"""
    assert(total([1.0, 2.0, 3.0])) == 6.0

    """1 - 1 = 0"""
    assert total([1,-1]) == 0

    """-1 -1 = -2"""
    assert total([-1,-1]) == -2

    #The edge cases :
    """The sum must be equal to the single element"""
    assert(total([1.0])) == 1.0

    """The sum of an empty list must be 0"""
    assert total([]) == 0
