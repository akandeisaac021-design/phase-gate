import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Test.Assertions.assertEquals;


public class LevelFourTest{

    @Test
    public void sumOfNumbersTest(){

        int actual =LevelFour.sumOfNumbers(3, 5);

        int expected =8;

        assertEquals(actual, expected);
    }


    @Test
    public void sumOfNumbersTest2(){

        int actual =LevelFour.sumOfNumbers(75, 2);

        int expected =77;

        assertEquals(actual, expected);
    }
}
