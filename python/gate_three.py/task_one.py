def new_list_functions(list_of_numbers, number):


    default_value =-1
    length_of_list_of_numbers =len(list_of_numbers)


    new_list_of_numbers =[]


    for index in range(0, length_of_list_of_numbers):
        new_list_of_numbers.append(list_of_numbers[index])
        if (index ==number-1):
            return new_list_of_numbers      



    length_of_new_list_of_numbers =len(new_list_of_numbers)



    if (length_of_new_list_of_numbers < number):


        for _ in range(length_of_new_list_of_numbers, number):
            new_list_of_numbers.append(default_value)

    return new_list_of_numbers



number =7

list_of_numbers =[1, 21, 3, 32, 54]
print(new_list_functions(list_of_numbers, number))
