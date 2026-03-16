import java.util.Scanner;

public class TaskTwelve{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);

    System.out.print("Enter a number---> ");
    int number =scanner.nextInt();

    if (number <0){
        System.out.println("It is a negative number");
    }    
    else{System.out.println("It is a positive number");}


    }
}
