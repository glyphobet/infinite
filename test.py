"""
>>> from infinite import Infinity, Infinitesimal, ZeroMultiplicationError

>>> -Infinity() == Infinity(False)
True
>>> Infinity() == Infinity()
True
>>> -Infinity() == -Infinity()
True
>>> Infinity() != -Infinity()
True
>>> -Infinity() != Infinity()
True
>>> -Infinity() == Infinity(False)
True
>>> Infinity() == Infinity()
True
>>> -Infinity() == -Infinity()
True
>>> Infinity() != -Infinity()
True
>>> -Infinity() != Infinity()
True
>>> Infinity() * 1 == 1 * Infinity() ==  Infinity() / 1 ==  Infinity() // 1 == Infinity()
True
>>> Infinity() * -1 == -1 * Infinity() ==  Infinity() / -1 ==  Infinity() // -1 == -Infinity()
True
>>> (-Infinity()) * 1 == 1 * -Infinity() == (-Infinity()) / 1 == (-Infinity()) // 1 == -Infinity()
True
>>> 1 / Infinity() == -1 / -Infinity() == Infinitesimal()
True
>>> -1 / Infinity() == 1 / -Infinity() == -Infinitesimal()
True
>>> 1 // Infinity() == -1 // Infinity() == 1 // -Infinity() == -1 // -Infinity() == 0
True

>>> -Infinitesimal() == Infinitesimal(False)
True
>>> Infinitesimal() == Infinitesimal()
True
>>> -Infinitesimal() == -Infinitesimal()
True
>>> Infinitesimal() != -Infinitesimal()
True
>>> -Infinitesimal() != Infinitesimal()
True
>>> -Infinitesimal() == Infinitesimal(False)
True
>>> Infinitesimal() == Infinitesimal()
True
>>> -Infinitesimal() == -Infinitesimal()
True
>>> Infinitesimal() != -Infinitesimal()
True
>>> -Infinitesimal() != Infinitesimal()
True
>>> Infinitesimal() * 1 == 1 * Infinitesimal() ==  Infinitesimal() / 1 == Infinitesimal()
True
>>> Infinitesimal() * -1 == -1 * Infinitesimal() ==  Infinitesimal() / -1 == -Infinitesimal()
True
>>> (-Infinitesimal()) * 1 == 1 * -Infinitesimal() == (-Infinitesimal()) / 1 == -Infinitesimal()
True
>>> Infinitesimal() // 1 == -Infinitesimal() // 1 == Infinitesimal() // -1 == (-Infinitesimal()) // -1 == 0
True
>>> 1 / Infinitesimal() == -1 / -Infinitesimal() == 1 // Infinitesimal() == -1 // -Infinitesimal() == Infinity()
True
>>> -1 / Infinitesimal() == 1 / -Infinitesimal() == -1 // Infinitesimal() == 1 // -Infinitesimal() == -Infinity()
True

>>> Infinity() * Infinitesimal() == (-Infinity()) * -Infinitesimal() ==  Infinitesimal() * Infinity() == (-Infinitesimal()) * -Infinity() == 1
True
>>> Infinity() * -Infinitesimal() == (-Infinity()) * Infinitesimal() == (-Infinitesimal()) * Infinity() ==  Infinitesimal() * -Infinity() == -1
True
>>> Infinity() / Infinitesimal() == Infinity()
True
>>> Infinitesimal() / Infinity() == Infinitesimal()
True

>>> Infinitesimal() // Infinitesimal() == Infinitesimal() // Infinity() == 0
True
>>> Infinity() // Infinity() == 1
True
>>> Infinity() // Infinitesimal() == Infinity()
True

>>> Infinity() * 0
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> Infinitesimal() * 0
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 * Infinity()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 * Infinitesimal()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 / Infinity()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 / Infinitesimal()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 // Infinity()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 // Infinitesimal()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> (-Infinity()) * 0
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> (-Infinitesimal()) * 0
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 * -Infinity()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 * -Infinitesimal()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 / -Infinity()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 / -Infinitesimal()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 // -Infinity()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero
>>> 0 // -Infinitesimal()
Traceback (most recent call last):
    ...
infinite.ZeroMultiplicationError: multiplication by zero

>>> Infinity() / 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> Infinitesimal() / 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> (-Infinity()) / 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> (-Infinitesimal()) / 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> Infinity() // 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> Infinitesimal() // 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> (-Infinity()) // 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> (-Infinitesimal()) // 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
