/*
 * Mike Weiss
 * Sep 17th 2011
 * Fall 2011 SSW-567
 * Stevens Institute of Technology
 * Written in C++
 *
 * A program that reads three numbers.The three numbers
 * represent the lengths of the sides of a triangle. The program 
 * prints a message that states whether the triangle is scalene, isosceles, 
 * or equilateral, and whether it is a right triangle as well.
 */


#include <iostream>
#include <sstream>
#include <string>

using namespace std;

bool isValidTriangleSides(double sideA, double sideB, double sideC){
    if(sideA <= 0 || sideB <= 0 || sideC <= 0){
        return false;
    }
    if(sideA + sideB <= sideC || sideB + sideC <= sideA){
        return false;
    } 
        return true; 
}

bool isEquilateralTriangle(double sideA, double sideB, double sideC){
    if(sideA == sideB && sideB == sideC){
       return true;
    }
    return false;
}

bool isIsoscelesTriangle(double sideA, double sideB, double sideC){
    if(sideA == sideB || sideA == sideC || sideB == sideC){
        return true;
    }
    return false; 
}

bool isRightTriangle(double sideA, double sideB, double sideC){
    if(((sideA * sideA) - ((sideB * sideB) + (sideC * sideC))) <= 0.012944) {
        return true;
    }else if(((sideB * sideB) - ((sideA * sideA) + (sideC * sideC))) <= 0.012944){
        return true;
    }else if(((sideC * sideC) - ((sideA * sideA) + (sideB * sideB))) <= 0.012944) {
        return true;
    }
    return false;
}

int main(int argc, char *argv[]) {
   double sideA;
   double sideB;
   double sideC;
 

   if (argc < 4){
        cout << "Usage Example:\n triangle <double> <double> <double>\n";
        return 0;
   }

 
   //make streams
   stringstream s1 (argv[1]);
   stringstream s2 (argv[2]);
   stringstream s3 (argv[3]);
   
   //convert to double
   s1 >> sideA;
   s2 >> sideB;
   s3 >> sideC;


   //convert to strings
   string a = argv[1];
   string b = argv[2];
   string c = argv[3];
   string responce = "Sides of length (" + a + "," + b + "," + c + ") ";


   if (!isValidTriangleSides(sideA, sideB, sideC)){
        cout << responce + "cannot form a triangle\n"; 
        return 0;
   }
   if (isEquilateralTriangle(sideA, sideB, sideC)){
        cout << responce + "forms an equilateral triangle\n";       

   }
   if (isIsoscelesTriangle(sideA,sideB,sideC)){
        cout << responce + "forms an isosceles triangle\n";
   }
   if (isRightTriangle(sideA, sideB, sideC)){
        cout << responce + "forms a right triangle\n";
   } 
   
   if (!isRightTriangle(sideA, sideB, sideC) && !isIsoscelesTriangle(sideA,sideB,sideC)){
        cout << responce + "forms a scalene triangle\n";

   }
 
    return 0;
}

 
