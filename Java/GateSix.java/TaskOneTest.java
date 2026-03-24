import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class TaskOneTest{

    @Test
    public void testCreateParkingSlotsMethod(){
    
        int [] actual =TaskOne.createParkingSlots();

        int [] expected ={0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

        assertArrayEquals(actual, expected);
    }


    @Test
    public void testParkingMethod(){

        int [] parkingSlots ={0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,};    

        int desiredParkingSlot =5;

        int [] actual =TaskOne.parking(parkingSlots, desiredParkingSlot);

        int [] expected ={0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,};

        assertArrayEquals(actual, expected);

    }

    @Test
    public void testParkingMethodIfDesiredParkingSlot(){

        int [] parkingSlots ={0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,};    

        int desiredParkingSlot =5;

        int [] actual =TaskOne.parking(parkingSlots, desiredParkingSlot);

        int [] expected ={0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,};

        assertArrayEquals(actual, expected);


    }






}
