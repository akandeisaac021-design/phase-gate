import java.util.Scanner;

public class TaskNine{

    public static void main(String []args){

    Scanner scanner =new Scanner(System.in);


    System.out.print("Enter the price -->");
    double price =scanner.nextDouble();

    double tax =0.1 * price;

    double priceWithTax =tax + price;

    System.out.println("Your new price is -->" + priceWithTax);

    }
}
