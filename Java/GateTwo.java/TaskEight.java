import java.util.Scanner;

public class TaskSix{
    public static void main (String []args){

    Scanner scanner =new Scanner(System.in);

        System.out.print("Enter a number -->");
        int userInput =scanner.nextInt();


        int newNumber =0;
        newNumber +=userInput;
        while(userInput !=0){
            System.out.print("Enter a number -->");
            userInput =scanner.nextInt();

            newNumber +=userInput;

        }

        System.out.print(newNumber);
    }
}
