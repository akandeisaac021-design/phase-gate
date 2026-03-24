public class TaskOne{


    public static int[] createParkingSlots(){

        int [] parkingSlots =new int[20];
        
        for(int slotIndex =0; slotIndex <20; slotIndex++){
            
            parkingSlots[slotIndex] =0;

        }    
        return parkingSlots;

    }


    public static int[] parking(int [] parkingSlots, int desiredParkingSlot){
        
        int desiredParkingSlotStatus =parkingSlots[desiredParkingSlot-1];

        if (desiredParkingSlotStatus ==0){
            parkingSlots[desiredParkingSlot-1] =1;
            System.out.println("You are successfully parked");
            System.out.println("Slot " + desiredParkingSlot + "-->" + parkingSlots[desiredParkingSlot-1]);

        }

        else{
            System.out.println(" Slot is currently occupied!! ");
            System.out.println("Action Failed!!");
        }
        return parkingSlots;
    }




    public static int[] unparking(int [] parkingSlots, int allotedParkingSlot){

        int allotedParkingSlotStatus =parkingSlots[allotedParkingSlot-1];

        if (allotedParkingSlotStatus ==1){
            parkingSlots[allotedParkingSlot-1] =0;
            System.out.println("You have successfully unparked");
            System.out.println("Slot " + allotedParkingSlot + "-->" + parkingSlots[allotedParkingSlot-1]);

        }    
 

        else{
            System.out.println(" Slot is currently occupied!! ");
            System.out.println("Action Failed!!");
        }

        return parkingSlots;
       
    }


    public static String checkSlotsStatuses(int [] parkingSlots){

        for(int slotIndex =0; slotIndex <20; slotIndex++){

            System.out.println("Slot " + slotIndex+1 + "-->" + (parkingSlots[slotIndex]));
            if (slotIndex ==19){
                return "It works";
            }
 
       }
        return "It don't work";
    }



}
