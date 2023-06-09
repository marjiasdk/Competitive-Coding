from fractions import Fraction

fraction = input()

a = (Fraction(fraction))

formula = ((a - 32) * 5) / 9

if formula == int(formula):
    print(str(formula) + "/1")
else:
    print(formula)