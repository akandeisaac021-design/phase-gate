//#pseudocode
//#import the random module
//#initialize user score as 0
//#create a loop to run 10 times
//#generate random numbers
//#generate the first number with a higher range than the second number by setting the random range higher so as to prevent negative results
//#prompt the user to attempt the question
//#check if the input is correct 
//#if input is correct add one to their score and move on to the next randomly generated question
//#else prompt the user again on the same question 
//#if the user fails again move on to the next randomly generated question
//#else add one to their score and move on to the next randomly generated question
//#repeat ten times
//#then print the user final score

import java.util.Scanner;
import java.util.Random;

public class TaskOne{


    public static void main(String [] args){

        Scanner scanner =new Scanner(System.in);
        Random random =new Random();

        int userScore =0;
        System.out.println("Attempt the following questions");

        for(int questionCounter =1; questionCounter <11; questionCounter++){

            int firstNumber =random.nextInt(41)+41;
            int secondNumber =random.nextInt(41);

            System.out.print(firstNumber + " - " + secondNumber + "-->");
            int result =scanner.nextInt();

            if (result !=(firstNumber - secondNumber)){
                System.out.print(firstNumber + " - " + secondNumber + "-->");
                result =scanner.nextInt();
                if (result ==(firstNumber - secondNumber)){
                        userScore++;
                    } 
            }
            else{
                userScore++;
            } 
        } 
System.out.println("Your score final score is -->" + userScore + " out of ten");
    }
}
