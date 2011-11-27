import pdb
import abc
import numbers

class ZeroMultiplicationError(ArithmeticError):
    pass


class AbstractInfinite(numbers.Number):
    def __init__(self, positive=True):
        self.positive = positive

    def __repr__(self):
        return (self.positive and '+' or '-') + self.__class__.__name__

    def __eq__(self, other):
        return issubclass(type(other), type(self)) and self.positive == other.positive

    def __neg__(self):
        return type(self)(positive=not self.positive)

    def __mul__(self, other):
        if other == 0:
            raise ZeroMultiplicationError("multiplication by zero")
        elif type(other) == self.reciprocal:
            return self.positive ^ other.positive and -1 or 1
        return type(self)(positive=self.positive if other > 0 else not self.positive)
    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (1/other)

    @abc.abstractmethod
    def __floordiv__(self, other): pass

    def __rtruediv__(self, other):
        return self.reciprocal(self.positive) * other

    @abc.abstractmethod
    def __rfloordiv__(self, other): pass

    @abc.abstractmethod
    def __lt__(self, other): pass

    @abc.abstractmethod
    def __gt__(self, other): pass
    
    @abc.abstractproperty
    def reciprocal(self): pass


class Infinity(AbstractInfinite):
    @property
    def reciprocal(self):
        return Infinitesimal

    def __gt__(self, other):
        return self.positive

    def __lt__(self, other):
        return not self.positive

    __floordiv__ = AbstractInfinite.__truediv__

    def __rfloordiv__(self, other):
        if other == 0:
            raise ZeroMultiplicationError("multiplication by zero")
        return 0

class Infinitesimal(AbstractInfinite):
    @property
    def reciprocal(self):
        return Infinity

    def __gt__(self, other):
        if other == 0:
            return self.positive
        return 0 > other

    def __lt__(self, other):
        if other == 0:
            return not self.positive
        return 0 < other

    def __floordiv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return 0

    __rfloordiv__ = AbstractInfinite.__rtruediv__


assert -Infinity() == Infinity(False)
assert  Infinity() ==  Infinity()
assert -Infinity() == -Infinity()
assert  Infinity() != -Infinity()
assert -Infinity() !=  Infinity()
assert   Infinity()  *  1 ==  1 *  Infinity() ==   Infinity()  /  1 ==   Infinity()  //  1 ==  Infinity()
assert   Infinity()  * -1 == -1 *  Infinity() ==   Infinity()  / -1 ==   Infinity()  // -1 == -Infinity()
assert (-Infinity()) *  1 ==  1 * -Infinity() == (-Infinity()) /  1 == (-Infinity()) //  1 == -Infinity()
assert  1 / Infinity() == -1 / -Infinity() ==  Infinitesimal()
assert -1 / Infinity() ==  1 / -Infinity() == -Infinitesimal()
assert 1 // Infinity() == -1 // Infinity() == 1 // -Infinity() == -1 // -Infinity() == 0

assert -Infinitesimal() == Infinitesimal(False)
assert  Infinitesimal() ==  Infinitesimal()
assert -Infinitesimal() == -Infinitesimal()
assert  Infinitesimal() != -Infinitesimal()
assert -Infinitesimal() !=  Infinitesimal()
assert   Infinitesimal()  *  1 ==  1 *  Infinitesimal() ==   Infinitesimal()  /  1 ==  Infinitesimal()
assert   Infinitesimal()  * -1 == -1 *  Infinitesimal() ==   Infinitesimal()  / -1 == -Infinitesimal()
assert (-Infinitesimal()) *  1 ==  1 * -Infinitesimal() == (-Infinitesimal()) /  1 == -Infinitesimal()
assert  Infinitesimal() // 1 == -Infinitesimal() // 1 == Infinitesimal() // -1 == (-Infinitesimal()) // -1 == 0
assert  1 / Infinitesimal() == -1 / -Infinitesimal() ==  1 // Infinitesimal() == -1 // -Infinitesimal() ==  Infinity()
assert -1 / Infinitesimal() ==  1 / -Infinitesimal() == -1 // Infinitesimal() ==  1 // -Infinitesimal() == -Infinity()

assert  Infinity() *  Infinitesimal() == (-Infinity()) * -Infinitesimal() ==   Infinitesimal()  *  Infinity() == (-Infinitesimal()) * -Infinity() ==  1
assert  Infinity() * -Infinitesimal() == (-Infinity()) *  Infinitesimal() == (-Infinitesimal()) *  Infinity() ==   Infinitesimal()  * -Infinity() == -1
assert Infinity() / Infinitesimal() == Infinity()
assert Infinitesimal() / Infinity() == Infinitesimal()

assert Infinitesimal() // Infinitesimal() == Infinitesimal() // Infinity() == 0
assert Infinity() // Infinity() == 1
assert Infinity() // Infinitesimal() == Infinity()

for expr in (
    'Infinity() * 0',
    'Infinitesimal() * 0',
    '0 * Infinity()',
    '0 * Infinitesimal()',
    '0 / Infinity()',
    '0 / Infinitesimal()',
    '0 // Infinity()',
    '0 // Infinitesimal()',
    '(-Infinity()) * 0',
    '(-Infinitesimal()) * 0',
    '0 * -Infinity()',
    '0 * -Infinitesimal()',
    '0 / -Infinity()',
    '0 / -Infinitesimal()',
    '0 // -Infinity()',
    '0 // -Infinitesimal()',
    ):
    try:
        eval(expr)
    except ZeroMultiplicationError:
        pass
    else:
        raise AssertionError(expr)

for expr in (
    'Infinity() / 0',
    'Infinitesimal() / 0',
    '(-Infinity()) / 0',
    '(-Infinitesimal()) / 0',
    'Infinity() // 0',
    'Infinitesimal() // 0',
    '(-Infinity()) // 0',
    '(-Infinitesimal()) // 0',
    ):
    try:
        eval(expr)
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError(expr)

pdb.set_trace()
