import java.util.Arrays;

public class TaskOne{
    

    public static int[] newArrayFunctions(int [] arrayOfNumbers, int newArrayLength){

        int defaultValue =-1;
        int lengthOfArrayOfNumbers =arrayOfNumbers.length;

        int index =0;

        int [] newArrayOfNumbers =new int [newArrayLength];

        for( ; index <lengthOfArrayOfNumbers; index++){
            
            newArrayOfNumbers[index] =arrayOfNumbers[index];
            if (index ==newArrayLength-1){
                return newArrayOfNumbers;
            }

        }

        int lengthOfNewArrayOfNumbers =newArrayOfNumbers.length;

        if (lengthOfNewArrayOfNumbers < newArrayLength){

            for ( ;lengthOfNewArrayOfNumbers <newArrayLength; lengthOfNewArrayOfNumbers++){

                newArrayOfNumbers[index] =defaultValue;
                index++;

            }

        }

        return newArrayOfNumbers;

    }


} 
