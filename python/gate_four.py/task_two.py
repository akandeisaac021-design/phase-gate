def how_many_even_numbers_are_in_a_list(numbers):

    count =0
    
    for number in numbers:

        if number %2 ==0:
            count +=1

    return count

def linear_search(numbers, target):
    count =0

    for number in numbers:

        if number ==target:

            return count

        count +=1
    return -1

def squares(number):
    squares =[]

    for number in range(2, number+2):
        squares.append(number*number)

    return squares

def list_equals(numbers, numbers2):
    if numbers ==numbers2:  return True
    else:   return False

def remove_duplicate_values(numbers):
    
    length_of_numbers =len(numbers)

    for number in numbers:

        index =0

        count =0  
        while index <length_of_numbers:
            if number ==numbers[index]:
                count +=1    
            index +=1        
        if count >1:
            for _ in range(count):

                numbers.remove(number)  
                length_of_numbers -=1


    return numbers


numbers =[1, 2, 3, 4, 5, 5, 6, 7, 7, 1]

print(remove_duplicate_values(numbers))
