import java.util.Scanner;

public class TaskSeven{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);


    System.out.print("Enter the radius of the circle --> ");
    double radius =scanner.nextInt();

    double circumference =22/7 * radius * radius;

    System.out.println("The circumference of the circle is --->" + circumference);
    }
}
