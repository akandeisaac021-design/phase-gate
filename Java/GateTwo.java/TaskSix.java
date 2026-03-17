import java.util.Scanner;

public class TaskSix{
    public static void main (String []args){

    Scanner scanner =new Scanner(System.in);

    System.out.print("Enter a number -->");
    int userInput =scanner.nextInt();


        for(int number =1; number <=userInput; number++){
            System.out.println(number);
            userInput +=number;

        }
    int sumOfNumbers =userInput;

    System.out.println("The sum Of Numbers is -->" + sumOfNumbers);
    }
}
