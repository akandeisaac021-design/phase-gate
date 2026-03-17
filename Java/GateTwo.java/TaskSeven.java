import java.util.Scanner;

public class TaskSix{
    public static void main (String []args){

    Scanner scanner =new Scanner(System.in);

    int sumOfNumbers =0;


        for(int count =0; count !=5; count++){
            System.out.print("Enter a number -->");
            int userInput =scanner.nextInt();
            
            sumOfNumbers +=userInput;

        }
    System.out.println("The sum Of Numbers is -->" + sumOfNumbers);
    }
}
