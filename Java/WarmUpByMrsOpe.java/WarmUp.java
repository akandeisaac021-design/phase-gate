import java.util.Arrays;
import java.util.ArrayList;

public class WarmUp {

    public static int [] removeDuplicateNumbersFromAnArray(int [] numbers){

        ArrayList <Integer> nonDuplicateNumbers =new ArrayList<>();
        
        int lengthOfNumbers =numbers.length;
        for (int numberToCompareIndex =0; numberToCompareIndex <lengthOfNumbers; numberToCompareIndex++){

            int count =0;

            for (int numberToBeComparedsIndex =0; numberToBeComparedsIndex <lengthOfNumbers; numberToBeComparedsIndex++){


                if(numbers[numberToCompareIndex] ==numbers[numberToBeComparedsIndex]){
                    count++;
                }

            }
        

        if (count ==0){
            nonDuplicateNumbers.add(numbers[numberToCompareIndex]);
        }

        }

    return nonDuplicateNumbers;
    }

}


