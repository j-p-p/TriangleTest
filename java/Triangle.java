import java.util.Scanner;

public class Triangle {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		
		
		
		System.out.println("Please enter the sides of the triangle in naturals numbers: ");
		
		double side1 = input.nextDouble();
		double side2 = input.nextDouble();
		double side3 = input.nextDouble();
		
		double [] sortN = SelectionSort (side1, side2, side3); // return the size sorted
		 
		double result = rightTriangle(sortN);//return if is a right triangle 
		double result1 = trueTriangle(sortN);
		
		
		
		if (side1 > 0 && side2 > 0 && side3 >0 && result1 == 1 ){
		
			if (side1 == side2 && side2 ==side3){
		 		System.out.println("The triangle is Equilateral and it is not  Right triangle");
					  
			}
			
			else if (side1 == side2 || side1 == side3 || side3 == side2 ) {
				if (result ==1) {
					System.out.println("The triangle is Isosceles and it is  Right triangle");
					            }
				else {
					System.out.println("The triangle is Isosceles and it is not  Right triangle");
					  }
				
			}
			
			else {
				if (result ==1) {
					System.out.println("The triangle is Scalene and it is  Right triangle");
					            }
				else {
					System.out.println("The triangle is Scalene and it is not  Right triangle");
					  }
		}
		
		
		
		} 
		
		else { 
			System.out.print("you have entered an invalid imput; it is not a triangle");
		}
		
		
		 
	}
	
	public static double rightTriangle (double [] num){
		
		double c =num[0];
		double a =num[1];
		double b =num[2];
		double result = 0;
		
		if ((a*a+b*b)==(Math.round((c*c)*10))/10.0){
			 result = 1; 
		}
		
		else { 
			result = 2;
		}
		return result;
		
	}
	
	public static double[] SelectionSort ( double side1, double side2, double side3) //sort the size descending 
	{
		double [ ] num = {side1, side2, side3};
	     int i, j, first;
	     double  temp; 
	    
	     for ( i = num.length - 1; i > 0; i -- ) 
	     {
	          first = 0;   //initialize to subscript of first element
	          for(j = 1; j <= i; j ++)   //locate smallest element between positions 1 and i.
	          {
	               if( num[ j ] < num[ first ] )         
	                 first = j;
	          }
	          temp = num[ first ];   //swap smallest found with element in position i.
	          num[ first ] = num[ i ];
	          num[ i ] = temp; 
	          
	      } 
	     return num;
	} 
public static double trueTriangle (double [] num){
		
		double c =num[0];
		double a =num[1];
		double b =num[2];
		double result = 0;
		
		if ((a+b)> c){
			 result = 1; 
		}
		
		else { 
			result = 2;
		}
		return result;
		
	}
}
