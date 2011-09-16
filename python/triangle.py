#!/usr/bin/python
	
import sys
from decimal import *

def isValidLength(sideA, sideB, sideC):
	if sideA <= 0 or sideB <= 0 or sideC <= 0:
		return False
	return True
	
def isValidTriangleSides(sideA, sideB, sideC):
	if sideA + sideB < sideC or sideB+sideC < sideA:
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
	if squaredSides[2] == squaredSides[0]+squaredSides[1]:
		return True
	return False
	

def testTriangle(sideA, sideB, sideC):
	response = "Sides of length ({0},{1},{2})".format(sideA, sideB, sideC)
	if not isValidLength(sideA, sideB, sideC):
		print("Error: {0} are invalid. all sides lengh must positive".format(response))
		return 
	
	if not isValidTriangleSides(sideA, sideB, sideC):
		print(response+" cannot form a triangle")
		return
		
	response = response + " forms"	
	if isEquilateralTriangle(sideA, sideB, sideC):
		print(response+" an equilateral triangle")
		return
		
	if isIsoscelesTriangle(sideA, sideB, sideC):
		response = response + " an isoceles"
	
	if isRightTriangle(sideA, sideB, sideC):
		response = response + " right"
		
	if (not isRightTriangle(sideA, sideB, sideC) and 
		not isIsoscelesTriangle(sideA, sideB, sideC)):
		response = response + " scalene"
		
	response = response + " triangle"
	print response
	
if __name__ == "__main__":
	try:
		sideA = Decimal(sys.argv[1])
		sideB = Decimal(sys.argv[2])
		sideC = Decimal(sys.argv[3])
		try:
			testTriangle(sideA, sideB, sideC)
		except Exception:
			print("\nError: Cannot process triangle sides\n")
	except Exception:
		print("\nError: you must enter three double for sides"+str(sys.argv[1:]))
		print("\nusage: {0} <double> <double> <double>\n".format(sys.argv[0]))
	
