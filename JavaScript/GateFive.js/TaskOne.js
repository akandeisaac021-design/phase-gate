//#pseudocode
//#import the random module
//#initialize user score as 0
//#create a loop to run 10 times
//#generate random numbers
//#generate the first number with a higher range than the second number by setting the random range higher so as to prevent negative results
//#prompt the user to attempt the question
//#check if the input is correct 
//#if input is correct add one to their score and move on to the next randomly generated question
//#else prompt the user again on the same question 
//#if the user fails again move on to the next randomly generated question
//#else add one to their score and move on to the next randomly generated question
//#repeat ten times
//#then print the user final score

let userScore =0;
console.log("Answer the following questions");

for(let questionCounter =1; questionCounter <11; questionCounter++){

    let firstNumber =Math.floor(Math.random(41)+41);
    let secondNumber =Math.floor(Math.random(41));

    console.log(firstNumber + " - " + secondNumber + "-->");
    let result =20;

    if (result !=(firstNumber - secondNumber)){
        console.log(firstNumber + " - " + secondNumber + "-->");
        result =20;
        if (result ==(firstNumber - secondNumber)){
                userScore++;
            } 
    }
    else{
        userScore++;
    } 
} 
console.log("Your score final score is -->" + userScore + " out of ten");
