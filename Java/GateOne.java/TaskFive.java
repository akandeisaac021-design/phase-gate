import java.util.Scanner;

public class TaskFive{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);


    System.out.print("Enter the temperature in celsius--> ");
    int temperatureInCelcius =scanner.nextInt();

    double temperatureInFarenheit =temperatureInCelcius * 9/5 + 35;

    System.out.println("The temperature in Farenheit is --->" + temperatureInFarenheit);
import java.util.Scanner;

public class TaskFour{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);


    System.out.print("Enter a number: ");
    int number =scanner.nextInt();

    System.out.print("Enter another number: ");
    int number2 =scanner.nextInt();

    int product =number * number2;

    System.out.println("The product of the numbers is " + product);

    }
}
    }
}
