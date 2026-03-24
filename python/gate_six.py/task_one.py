
def create_parking_slots():

    parking_slots =[]

    for slot_index in range(0, 20):
        parking_slots.append(0)

    return parking_slots


def parking(parking_slots, desired_parking_slot):
    
    desired_slot_status =parking_slots[desired_parking_slot-1]

    if (desired_slot_status ==0) :
        parking_slots[desired_parking_slot-1] =1
        print("You are successfully parked")
        print(f"Slot {desired_parking_slot} -->{parking_slots[desired_parking_slot-1]}")

    else:
        print(" Slot is currently occupied!! ")
        print("Action Failed!!")
 
    return parking_slots     

def unparking(parking_slots, alloted_parking_slot):

    alloted_parking_slot_status =parking_slots[alloted_parking_slot -1]

    if (alloted_parking_slot_status ==1) :
        parking_slots[alloted_parking_slot -1] =0
        print("You have successfully unparked")
        print(f"Slot {alloted_parking_slot} -->{parking_slots[alloted_parking_slot-1]}")

    else :
        print("Slot is empty!!(Are you sure this is where you parked)")
        print("Action Failed!!")

    return parking_slots

def check_slots_statuses(parking_slots):


    for slot_index in range(0, 20):
        print(f"Slot {slot_index+1} -->{parking_slots[slot_index]}     ", end=" ")
        if slot_index ==19:
            return "It works"


