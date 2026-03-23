#pseudocode
#import the random module
#initialize user score as 0
#create a loop to run 10 times
#generate random numbers
#generate the first number with a higher range than the second number by setting the random range higher so as to prevent negative results
#prompt the user to attempt the question
#check if the input is correct 
#if input is correct add one to their score and move on to the next randomly generated question
#else prompt the user again on the same question 
#if the user fails again move on to the next randomly generated question
#else add one to their score and move on to the next randomly generated question
#repeat ten times
#then print the user final score
import random

user_score =0;
print("Answer the following questions");
for question_count in range(1, 11):

    first_number =random.randint(41, 100);
    second_number =random.randint(0, 41);
    result =int(input(f"{first_number} - {second_number}-->"));
    
    if result !=(first_number - second_number): 
        result =int(input(f"{first_number} - {second_number}-->"));
        if result ==(first_number - second_number): 
            user_score +=1;

    else:   
        user_score +=1;

print(f"Your final score is {user_score} out of ten");

    


