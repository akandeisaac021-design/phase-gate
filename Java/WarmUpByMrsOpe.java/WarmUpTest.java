import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class WarmUpTest{

    @Test
    public void testForRemoveDuplicateNumbersFromAnArrayMethod(){

    int [] numbers ={9, 2, 3, 2, 1};

    int [] actual =WarmUp.removeDuplicateNumbersFromAnArray(numbers);

    int [] expected ={9, 3, 1};

    assertArrayEquals(actual, expected);



    }







}
