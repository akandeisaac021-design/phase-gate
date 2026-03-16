import java.util.Scanner;

public class TaskTwelve{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);

    System.out.print("Enter a number---> ");
    int number =scanner.nextInt();

    if (number >=50){
        System.out.println("You passed");
    }    
    else{System.out.println("You failed");}


    }
}
