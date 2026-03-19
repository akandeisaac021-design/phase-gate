def sorted_list_of_prime_numbers(numbers):
    list_of_prime_numbers =[]

    count =0

    for number in numbers:
        for divisor in range(2, number):
            if number % divisor ==0:
                count +=1
        if count ==0:
            list_of_prime_numbers.append(number)
        count =0

    return list_of_prime_numbers

numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sorted_list_of_prime_numbers(numbers))

def negative_numbers_remover(numbers):
    index =0
    for number in numbers:
        if number <0:
            numbers[index] =0
        index +=1

    return numbers

numbers =[-1, 2, -3, 4, -5, 6, -7, 8, 9, 10]
print(negative_numbers_remover(numbers))


def list_sorter(numbers):

    temporary_space=0

    for index in range(0, len(numbers)):

        for index2 in range(0, len(numbers)):

            if (numbers[index] >numbers[index2]):

                temporary_space =numbers[index]
                numbers[index] =numbers[index2]
                numbers[index2] =temporary_space

    return numbers

numbers =[0, 2, 0, 4, 0, 6, 0, 8, 9, 10]
print(list_sorter(numbers))


def retain_only_duplicate_values(numbers):
    
    length_of_numbers =len(numbers)
    new_numbers =[]
    count =0

    for number in numbers:
        index =0
        while index <length_of_numbers:
            if number ==numbers[index]:
                count +=1    
            index +=1        
        if count >1:
            new_numbers.append(number)
            for _ in range(count):
                numbers.remove(number)  
                length_of_numbers -=1
        count =0  

    return new_numbers

numbers =[0, 2, 0, 6, 0, 6, 0, 8, 2, 10]
print(retain_only_duplicate_values(numbers))

