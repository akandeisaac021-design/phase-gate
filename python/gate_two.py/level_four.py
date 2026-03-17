def sum_of_two_numbers(number1, number2):
    return number1 + number2    

def is_number_even(number):
    if number % 2 ==0 : return "Even"
    else :  return "Odd"

def number_squared(number):
    return number * number

def celcius_to_fareneit_converter(celcius):
    return celcius * 9/5 + 35

def number_is_prime(number):
    for factor in range(2, number -1):
        if number % factor ==0: return "Not a prime number"
        else :  return "Tis a prime number"

def largest_of_three_numbers(number1, number2, number3):
    numbers =[number1, number2, number3]
    numbers.sort()

    return numbers[-1]

def simple_interest_calculator(principal, time, rate):

    simple_interest =(principal * time * rate) / 100

    return simple_interest


def multiplication_table(number):
        
    for multiplier in range(1, 13):
        print(f"{multiplier} * {number} -->{number*multiplier}" )

def area_of_a_rectangle(length, breadth):

    return length * breadth

def number_reversal(number):

    number =str(number)
    reversed_number_list =[number]

    new_string =""
    count =-1
    for _ in  number:
        new_string +="" + number[count]
        count -=1

    return new_string
