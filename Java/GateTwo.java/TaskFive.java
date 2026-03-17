import java.util.Scanner;

public class TaskTwo{
    public static void main (String []args){

    Scanner scanner =new Scanner(System.in);

    System.out.print("Enter a number -->");
    int number =scanner.nextInt();

    int factorial =1;

        for(int multiplier =number; multiplier >1; --multiplier){
            factorial *=multiplier;

        }
    System.out.println("The factorial is -->" + factorial);
    }
}
