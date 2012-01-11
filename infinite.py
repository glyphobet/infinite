"""
Infinity and Infinitesimal classes for Python 3. Derived from numbers.Number.
"""

# To-Do:
# handle addition / subtraction

import sys
import abc
import numbers

assert sys.version.startswith('3'), "Python 3 required."

class ZeroMultiplicationError(ArithmeticError):
    pass

class AbstractInfinite(numbers.Number):
    def __init__(self, positive=True):
        self.positive = positive

    def __repr__(self):
        return (self.positive and '+' or '-') + self.__class__.__name__

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.positive == other.positive

    def __neg__(self):
        return type(self)(positive=not self.positive)

    def __mul__(self, other):
        if other == 0:
            raise ZeroMultiplicationError("multiplication by zero")
        elif isinstance(other, self.reciprocal):
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


__all__ = ['ZeroMultiplicationError', 'AbstractInfinite', 'Infinity', 'Infinitesimal']
