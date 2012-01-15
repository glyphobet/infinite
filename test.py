"""
>>> import math
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

>>> Infinity() * 1
+Infinity
>>> 1 * Infinity()
+Infinity
>>> Infinity() / 1
+Infinity
>>> Infinity() // 1
+Infinity

>>> Infinity() * -1
-Infinity
>>> -1 * Infinity()
-Infinity
>>> Infinity() / -1
-Infinity
>>> Infinity() // -1
-Infinity

>>> (-Infinity()) * 1
-Infinity
>>> 1 * -Infinity()
-Infinity
>>> (-Infinity()) / 1
-Infinity
>>> (-Infinity()) // 1
-Infinity

>>> 1 / Infinity()
+Infinitesimal
>>> -1 / -Infinity()
+Infinitesimal

>>> -1 / Infinity()
-Infinitesimal
>>> 1 / -Infinity()
-Infinitesimal

>>> 1 // Infinity()
0
>>> -1 // -Infinity()
0

>>> -1 // Infinity()
-1
>>> 1 // -Infinity()
-1

>>> -Infinitesimal() == Infinitesimal(positive=False)
True
>>> Infinitesimal() == Infinitesimal()
True
>>> -Infinitesimal() == -Infinitesimal()
True
>>> Infinitesimal() != -Infinitesimal()
True
>>> -Infinitesimal() != Infinitesimal()
True
>>> -Infinitesimal() == Infinitesimal(positive=False)
True
>>> Infinitesimal() == Infinitesimal()
True
>>> -Infinitesimal() == -Infinitesimal()
True
>>> Infinitesimal() != -Infinitesimal()
True
>>> -Infinitesimal() != Infinitesimal()
True

>>> Infinitesimal() * 1
+Infinitesimal
>>> 1 * Infinitesimal()
+Infinitesimal
>>> Infinitesimal() / 1
+Infinitesimal

>>> Infinitesimal() * -1
-Infinitesimal
>>> -1 * Infinitesimal()
-Infinitesimal
>>> Infinitesimal() / -1
-Infinitesimal

>>> (-Infinitesimal()) * 1
-Infinitesimal
>>> 1 * -Infinitesimal()
-Infinitesimal
>>> (-Infinitesimal()) / 1
-Infinitesimal

>>> Infinitesimal() // 1
0
>>> (-Infinitesimal()) // -1
0
>>> -Infinitesimal() // 1
-1
>>> Infinitesimal() // -1
-1

>>> 1 / Infinitesimal()
+Infinity
>>> -1 / -Infinitesimal()
+Infinity
>>> 1 // Infinitesimal()
+Infinity
>>> -1 // -Infinitesimal()
+Infinity

>>> -1 / Infinitesimal()
-Infinity
>>> 1 / -Infinitesimal()
-Infinity
>>> -1 // Infinitesimal()
-Infinity
>>> 1 // -Infinitesimal()
-Infinity

>>> Infinity() * Infinitesimal()
1
>>> (-Infinity()) * -Infinitesimal()
1
>>> Infinitesimal() * Infinity()
1
>>> (-Infinitesimal()) * -Infinity()
1

>>> Infinity() * -Infinitesimal()
-1
>>> (-Infinity()) * Infinitesimal()
-1
>>> (-Infinitesimal()) * Infinity()
-1
>>> Infinitesimal() * -Infinity()
-1

>>> Infinity() / Infinitesimal()
+Infinity
>>> Infinitesimal() / Infinity()
+Infinitesimal

>>> Infinitesimal() // Infinity()
0
>>> Infinitesimal() // Infinitesimal()
1
>>> Infinity() // Infinity()
1
>>> Infinity() // Infinitesimal()
+Infinity

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

>>> Infinity() + 1
+Infinity
>>> 1 + Infinity()
+Infinity
>>> Infinity() - 1
+Infinity
>>> 1 - Infinity()
-Infinity
>>> Infinity() + Infinity()
+Infinity
>>> Infinity() - Infinity()
0
>>> -Infinity() - Infinity()
-Infinity
>>> -Infinity() + Infinity()
0

>>> Infinitesimal() + 1
1+Infinitesimal
>>> 1 + Infinitesimal()
1+Infinitesimal
>>> -1 + Infinitesimal()
-1+Infinitesimal
>>> Infinitesimal() - 1
-1+Infinitesimal
>>> 1 - Infinitesimal()
1-Infinitesimal
>>> -1 - Infinitesimal()
-1-Infinitesimal

>>> Infinitesimal() - Infinitesimal()
0
>>> -Infinitesimal() + Infinitesimal()
0
>>> Infinitesimal() + Infinitesimal()
+Infinitesimal
>>> -Infinitesimal() -Infinitesimal()
-Infinitesimal

>>> (Infinitesimal() + 1) + (Infinitesimal() + 1)
2+Infinitesimal
>>> (Infinitesimal() - 1) + (Infinitesimal() + 1)
+Infinitesimal
>>> (Infinitesimal() + 1) - (Infinitesimal() + 1)
0
>>> (Infinitesimal() + 1) - (Infinitesimal() - 1)
2
>>> (Infinitesimal() - 1) + (Infinitesimal() - 1)
-2+Infinitesimal
>>> (Infinitesimal() - 1) - (Infinitesimal() + 1)
-2

>>> Infinity() + Infinitesimal()
+Infinity
>>> Infinity() - Infinitesimal()
+Infinity
>>> Infinitesimal() + Infinity()
+Infinity
>>> Infinitesimal() - Infinity()
-Infinity

>>> Infinity() * (1 + Infinitesimal())
+Infinity
>>> Infinity() * (-1 + Infinitesimal())
-Infinity
>>> (-Infinity()) * (1 + Infinitesimal())
-Infinity
>>> (-Infinity()) * (-1 + Infinitesimal())
+Infinity

>>> (1+Infinitesimal())//1
1
>>> (1+Infinitesimal())/1
1.0+Infinitesimal
>>> (2+Infinitesimal())//2
1
>>> (2+Infinitesimal())/2
1.0+Infinitesimal

>>> math.floor(Infinity())
+Infinity
>>> math.ceil(Infinity())
+Infinity
>>> math.floor(-Infinity())
-Infinity
>>> math.ceil(-Infinity())
-Infinity

>>> math.floor(Infinitesimal())
0
>>> math.ceil(Infinitesimal())
1
>>> math.floor(-Infinitesimal())
-1
>>> math.ceil(-Infinitesimal())
0
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
