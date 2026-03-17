import java.util.Scanner;

public class TaskTwo{
    public static void main (String []args){

    Scanner scanner =new Scanner(System.in);

    System.out.print("Enter a number -->");
    int number =scanner.nextInt();

        for(int multiplier =1;number <13; multiplier++){
            System.out.println(number + "*" + multiplier + "=" + (number * multiplier) );
        }
    }
}
