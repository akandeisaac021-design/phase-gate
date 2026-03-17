import java.util.Scanner;

public class TaskSix{
    public static void main (String []args){

    Scanner scanner =new Scanner(System.in);

    System.out.print("Enter a number -->");
    int userInput =scanner.nextInt();
    int sumOfNumbers = 0;

        for(int number =1; number <=userInput; number++){
            System.out.println(number);
            sumOfNumbers +=number;

        }
   

    System.out.println("The sum Of Numbers is -->" + sumOfNumbers);
    }
}
