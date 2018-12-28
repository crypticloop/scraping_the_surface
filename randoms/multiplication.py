# Solving problem on https://brilliant.org/weekly-problems/2018-12-17/basic/?p=2

import math

def DoesCalculatePassReqs(firstNumberTens, secondNumberUnits, thirdNumberTens, thirdNumberUnits):

    firstNumber = (firstNumberTens * 10) + 3
    secondNumber = 30 + secondNumberUnits
    thirdNumber = 300 + (thirdNumberTens * 10) + thirdNumberUnits

    return firstNumber * secondNumber == thirdNumber

for firstRepeat in range(0,10000):
    units = firstRepeat % 10
    tens = int((math.floor(firstRepeat/10)) % 10)
    hundreds = int(math.floor(firstRepeat/100) % 10)
    thousands = int(math.floor(firstRepeat/1000))
    if DoesCalculatePassReqs(thousands, hundreds, tens, units):
        print thousands, hundreds, tens, units

# This is pretty slow, does not need to go through all of the 10000 number combinations, results would not be three digits and start with a 3
