"""
Infinity and Infinitesimal classes for Python 3. Derived from numbers.Number.
"""

import sys
import abc
import math
import numbers

assert sys.version.startswith('3'), "Python 3 required."

class ZeroMultiplicationError(ArithmeticError):
    pass

class AbstractInfinite(numbers.Number):
    def __init__(self, positive=True):
        self.positive = positive

    def __repr__(self):
        return (self.positive and '+' or '-') + self.__class__.__name__

    @abc.abstractproperty
    def reciprocal(self): pass

    def __neg__(self):
        return type(self)(positive=not self.positive)

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.positive == other.positive

    @abc.abstractmethod
    def __lt__(self, other): pass

    @abc.abstractmethod
    def __gt__(self, other): pass

    def __abs__(self):
        return type(self)(positive=True)

    @abc.abstractmethod
    def __floor__(self): pass

    @abc.abstractmethod
    def __ceil__(self): pass

    def __mul__(self, other):
        if other == 0:
            raise ZeroMultiplicationError("multiplication by zero")
        elif abs(other) == self.reciprocal():
            return self.positive ^ other.positive and -1 or 1
        return type(self)(positive=self.positive if other > 0 else not self.positive)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (1/other)

    def __floordiv__(self, other):
        return math.floor(self / other)

    def __rtruediv__(self, other):
        return self.reciprocal(self.positive) * other

    def __rfloordiv__(self, other):
        return math.floor(other / self)

    def __add__(self, other):
        if isinstance(other, type(self)):
            if self.positive != other.positive:
                return 0
        return type(self)(positive=self.positive)

    __radd__ = __add__

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return -self + other


class Infinity(AbstractInfinite):
    @property
    def reciprocal(self):
        return Infinitesimal

    def __gt__(self, other):
        return self.positive

    def __lt__(self, other):
        return not self.positive

    def __floor__(self):
        return self

    def __ceil__(self):
        return self


class Infinitesimal(AbstractInfinite):

    def __init__(self, positive=True, origin=0):
        super(Infinitesimal, self).__init__(positive)
        self.origin = origin

    def __repr__(self):
        return (self.origin and str(self.origin) or '') + super(Infinitesimal, self).__repr__()

    @property
    def reciprocal(self):
        return Infinity

    def __neg__(self):
        return super(Infinitesimal, self).__neg__() + -self.origin

    def __eq__(self, other):
        return super(Infinitesimal, self).__eq__(other) and self.origin == other.origin

    def __lt__(self, other):
        if other == self.origin:
            return not self.positive
        return self.origin < other

    def __gt__(self, other):
        if other == self.origin:
            return self.positive
        return self.origin > other

    def __abs__(self):
        return type(self)(positive=True, origin=abs(self.origin))

    def __floor__(self):
        return math.floor(self.origin) + (0 if self.positive else -1)

    def __ceil__(self):
        return math.floor(self.origin) + (1 if self.positive else 0)

    def __mul__(self, other):
        return super(Infinitesimal, self).__mul__(other) + (self.origin * other if self.origin else 0)

    __rmul__ = __mul__

    def __add__(self, other):
        if isinstance(other, Infinity):
            return other + self
        elif isinstance(other, Infinitesimal):
            return super(Infinitesimal, self).__add__(other) + self.origin + other.origin
        else:
            return type(self)(positive=self.positive, origin=self.origin + other)

    __radd__ = __add__


__all__ = ['ZeroMultiplicationError', 'AbstractInfinite', 'Infinity', 'Infinitesimal']
