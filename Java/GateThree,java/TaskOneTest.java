import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class TaskOneTest{

    @Test
    public void testThatNewArrayFunctionsIsAccurateIfNewListLengthIsExcess(){
        
    int [] arrayOfNumbers ={1, 21, 3, 32, 54};

    int newArrayLength =7;

    int [] actual =TaskOne.newArrayFunctions(arrayOfNumbers, newArrayLength);

    int [] expected ={1, 21, 3, 32, 54, -1, -1};

    assertArrayEquals(actual, expected);

    }




    @Test
    public void testThatNewArrayFunctionsIsAccurateIfNewListLengthIsInsufficient(){
        
    int [] arrayOfNumbers ={1, 21, 3, 32, 54};

    int newArrayLength =3;

    int [] actual =TaskOne.newArrayFunctions(arrayOfNumbers, newArrayLength);

    int [] expected ={1, 21, 3};

    assertArrayEquals(actual, expected);

    }



    @Test
    public void testThatNewArrayFunctionsIsAccurateIfNewListLengthIsExact(){
        
    int [] arrayOfNumbers ={1, 21, 3, 32, 54};

    int newArrayLength =5;

    int [] actual =TaskOne.newArrayFunctions(arrayOfNumbers, newArrayLength);

    int [] expected ={1, 21, 3, 32, 54};

    assertArrayEquals(actual, expected);

    }







}
