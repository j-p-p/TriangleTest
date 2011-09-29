#!/usr/bin/python
"""
Copyright John Poyau

A program that reads three numbers.The three numbers
represent the lengths of the sides of a triangle. The program 
prints a message that states whether the triangle is scalene, isosceles, 
or equilateral, and whether it is a right triangle as well.

For example
>>> triangle(['4','5','5'])
Sides of length (4,5,5) forms an isosceles triangle

>>> triangle(['5e-51','4e-51','3e-51'])
Sides of length (5E-51,4E-51,3E-51) forms a right triangle

>>> triangle(['51','51','51'])
Sides of length (51,51,51) forms an equilateral triangle

>>> triangle(['4','5','8'])
Sides of length (4,5,8) forms a scalene triangle

>>> triangle(['4','5','5e10'])
Sides of length (4,5,5E+10) cannot form a triangle

>>> triangle(['0','1','1'])
Error: Sides of length (0,1,1) are invalid. all sides length must positive

>>> triangle(['-40','-30','-50'])
Error: Sides of length (-40,-30,-50) are invalid. all sides length must positive

>>> triangle(['1','1','1.4142135623730950488016887241'])
Sides of length (1,1,1.4142135623730950488016887241) forms an isosceles right triangle


>>> triangle(['10.1','20.2','22.584'])
Sides of length (10.1,20.2,22.584) forms a right triangle

"""	
import sys
from decimal import *
getcontext().prec=28

def isValidLength(sideA, sideB, sideC):
    if sideA <= 0 or sideB <= 0 or sideC <= 0:
        return False
    return True

def isValidTriangleSides(sideA, sideB, sideC):
    if sideA + sideB <= sideC or sideB+sideC <= sideA or sideC+sideA <= sideB:
        return False
    return True

def isEquilateralTriangle(sideA, sideB, sideC):
    if sideA == sideB and sideB == sideC:
        return True
    return False

def isIsoscelesTriangle(sideA, sideB, sideC):
    if sideA == sideB or sideA == sideC or sideB == sideC:
        return True
    return False

def isRightTriangle(sideA, sideB, sideC):
    squaredSides = sorted([x*x for x in [sideA, sideB, sideC]])
    if abs(squaredSides[2]-(squaredSides[0]+squaredSides[1])) <= Decimal('0.012944') :
        return True
    return False


def testTriangle(sideA, sideB, sideC):
    response = "Sides of length ({0},{1},{2})".format(sideA, sideB, sideC)
    if not isValidLength(sideA, sideB, sideC):
        print("Error: {0} are invalid. all sides length must positive".format(response))
        return 

    if not isValidTriangleSides(sideA, sideB, sideC):
        print(response+" cannot form a triangle")
        return

    response = response + " forms a"	
    if isEquilateralTriangle(sideA, sideB, sideC):
        print(response+"n equilateral triangle")
        return

    if isIsoscelesTriangle(sideA, sideB, sideC):
        response = response + "n isosceles"

    if isRightTriangle(sideA, sideB, sideC):
        response = response + " right"

    if (not isRightTriangle(sideA, sideB, sideC) and 
        not isIsoscelesTriangle(sideA, sideB, sideC)):
        response = response + " scalene"

    response = response + " triangle"
    print response

def triangle(argv):
    # Check that we only have three arguments.
    # The first argument is the program name.
    assert(len(argv) == 3)
    # Convert the side to a decimal object that will
    # make easier to handle corner cases of small
    # or large decimal numbers.
    sideA = Decimal(argv[0])
    sideB = Decimal(argv[1])
    sideC = Decimal(argv[2])
    try:
        testTriangle(sideA, sideB, sideC)
    except Exception:
        print("\nError: Cannot process triangle sides\n")

if __name__== "__main__":
    try:
        triangle(sys.argv[1:])
    except Exception:
        print("\nInput Error: {0}\nYou must enter three double for sides ".format(sys.argv[1:]))
        print("\nusage: {0} <double> <double> <double>\n".format(sys.argv[0]))
