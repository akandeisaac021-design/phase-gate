import java.util.Scanner;

public class TaskNine{
    public static void main (String []args){

    Scanner scanner =new Scanner(System.in);

    int row =5;
    int column =5;

        for (int columnCount =0; columnCount <column ; columnCount++){
            for (int rowcount =0; rowcount <row; rowcount++){
                System.out.print("*");
                    }
            row--;
            System.out.println(" ");
        }
    }
}
