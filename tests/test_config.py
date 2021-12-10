
import pytest


class NotInRange(Exception) :
    def __init__(self, message = "Value not in range ") :
        self.message = message
        super().__init__(self.message)


# def test_exception() :
#     a = 1
#     with pytest.raises(ValueError) :
#         if a not in range(10, 20) :
#             raise NotInRange



def test_generic() :
    a = 2
    b = 2
    assert a==b

def test_generic1() :
    a = 2
    b = 21
    assert a!=b



