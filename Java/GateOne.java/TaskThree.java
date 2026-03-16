import java.util.Scanner;

public class TaskThree{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);


    System.out.print("Enter a number: ");
    int number =scanner.nextInt();

    System.out.print("Enter another number: ");
    int number2 =scanner.nextInt();

    int sum =number + number2;

    System.out.println("The sum of the numbers is " + sum);
//celsius * 9/5 +35
    }
}
