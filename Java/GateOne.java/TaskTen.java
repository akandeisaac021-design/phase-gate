import java.util.Scanner;

public class TaskTen{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);


    System.out.print("Enter a number: ");
    int number =scanner.nextInt();

    System.out.print("Enter another number: ");
    int number2 =scanner.nextInt();

    System.out.print("Enter another number: ");
    int number3 =scanner.nextInt();

    int average =(number + number2 + number3) /3;

    System.out.println("The average of the numbers is -->" + average);

    }
}
