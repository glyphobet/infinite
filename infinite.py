import pdb
import numbers

class ZeroMultiplicationError(ArithmeticError):
    pass


class Infinite(numbers.Number):
    def __init__(self, positive=True):
        self.positive = positive

    def __eq__(self, other):
        return issubclass(type(other), type(self)) and self.positive == other.positive

    def __neg__(self):
        return type(self)(positive=not self.positive)


class Infinity(Infinite):
    def __gt__(self, other):
        return self.positive

    def __lt__(self, other):
        return not self.positive

    def __repr__(self):
        return (self.positive and '+' or '-') + self.__class__.__name__

    def __mul__(self, other):
        if other == 0:
            raise ZeroMultiplicationError("multiplication by zero")
        return type(self)(positive=self.positive if other > 0 else not self.positive)
    __rmul__ = __mul__

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return self * other
    __floordiv__ = __truediv__


class Infinitesimal(Infinite):
    def __gt__(self, other):
        if self.positive:
            if other > 0:
                return False
            else:
                return True
        else:
            if other >= 0:
                return False
            else:
                return True

    def __lt__(self, other):
        if self.positive:
            if other <= 0:
                return False
            else:
                return True
        else:
            if other < 0:
                return False
            else:
                return True

    def __repr__(self):
        return (self.positive and '+' or '-') + self.__class__.__name__


assert -Infinity() == Infinity(False)
assert  Infinity() ==  Infinity()
assert -Infinity() == -Infinity()
assert  Infinity() != -Infinity()
assert -Infinity() !=  Infinity()
assert  Infinity() *  1 ==  1 *  Infinity() ==  Infinity() /  1
assert  Infinity() * -1 == -1 *  Infinity() ==  Infinity() / -1
assert -Infinity() *  1 ==  1 * -Infinity() == -Infinity() /  1

try:
    Infinity() * 0
except ZeroMultiplicationError:
    pass
else:
    raise AssertionError()

pdb.set_trace()
