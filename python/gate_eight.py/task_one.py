def function_to_add_phone_number(collection_of_phone_numbers, phone_number_to_be_added):

    length_of_collection_of_phone_numbers =len(collection_of_phone_numbers)

    amount_of_times_number_has_been_stored =0

    for index in range(0, length_of_collection_of_phone_numbers):

        if collection_of_phone_numbers[index] == phone_number_to_be_added:
            
            amount_of_times_number_has_been_stored +=1

    if amount_of_times_number_has_been_stored !=0:
        
        return "Error 419 -->The number already exists"
            
    else:
        collection_of_phone_numbers.append(phone_number_to_be_added)
     
    return collection_of_phone_numbers
#
#collection_of_contacts =[]
#collection_first_name =[]
#collection_second_name =[]
#collection_of_phone_numbers =["empty"]
#
#collection_of_contacts.append(collection_first_name)
#collection_of_contacts.append(collection_second_name)
#collection_of_contacts.append(collection_of_contacts)
#
#print("""
#1. Add Contacts
#2. Remove Contacts
#3. Find Contact by Phone number
#4. Find Contact by First Name 
#5. Find Contact by name 
#6. Edit Contact
#""")
#
#user_action_choice =int(input("Enter your choice: "))
#
#match(user_action_choice):
#
#    case 1:
#        phone_number_to_be_added =input("Enter a Phone number: ")
#        function_to_add_phone_number(collection_of_contacts, phone_number_to_be_added)
#        if (function_to_add_phone_number(collection_of_contacts, phone_number_to_be_added) =="Error 419 -->The number already exists"):
#            print(function_to_add_phone_number(collection_of_contacts, phone_number_to_be_added))
#        print(collection_of_phone_numbers)
#

