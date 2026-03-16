import java.util.Scanner;

public class TaskSix{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);


    System.out.print("Enter the length of the rectangle--> ");
    double length =scanner.nextInt();

    System.out.print("Enter the breadth of the rectangle--> ");
    double breadth =scanner.nextInt();


    double areaOfTheRectangle =length * breadth;

    System.out.println("The product of the numbers is " + areaOfTheRectangle);

    }
}
