#def new_list_functions(list_of_numbers, number):
#
#
#    default_value =-1
#    length_of_list_of_numbers =len(list_of_numbers)
#
#
#    new_list_of_numbers =[]
#
#
#    for index in range(0, length_of_list_of_numbers):
#        new_list_of_numbers.append(list_of_numbers[index])
#        if (index ==number-1):
#            return new_list_of_numbers      
#
#
#
#    length_of_new_list_of_numbers =len(new_list_of_numbers)
#
#
#
#    if (length_of_new_list_of_numbers < number):
#
#
#        for _ in range(length_of_new_list_of_numbers, number):
#            new_list_of_numbers.append(default_value)
#
#    return new_list_of_numbers
#
#



def case_sensitive_word_counter(name):

    lower_case_alphabet ="abcdefghijklmnopqrstuvwxyz"
    upper_case_alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    characters_in_name =[]
    characters_in_name =name

    characters_in_lower_case_alphabet =[]
    characters_in_lower_case_alphabet =lower_case_alphabet

    index_of_lower_case_list =0
    index_of_list_name =0

    count =0

    output =""

    while (index_of_lower_case_list <26):

        for character in name:
            if characters_in_lower_case_alphabet[index_of_lower_case_list] ==characters_in_name[index_of_list_name]:
                count +=1
            index_of_list_name +=1
        if count >0 :
           output =f"{output} {characters_in_lower_case_alphabet[index_of_lower_case_list]}{count}"
        index_of_lower_case_list +=1
        index_of_list_name =0
        count =0
        
    characters_in_upper_case_alphabet =[]
    characters_in_upper_case_alphabet =upper_case_alphabet

    index_of_upper_case_list =0
    index_of_list_name =0

    count =0


    while (index_of_upper_case_list <26):

        for character in name:
            if characters_in_upper_case_alphabet[index_of_upper_case_list] ==characters_in_name[index_of_list_name]:
                count +=1
            index_of_list_name +=1
        if count >0 :
           output =f"{output} {characters_in_upper_case_alphabet[index_of_upper_case_list]}{count}"
        index_of_upper_case_list +=1
        index_of_list_name =0
        count =0




    return output

name ="Isaac"
print(case_sensitive_word_counter(name))
