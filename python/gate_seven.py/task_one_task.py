from unittest import TestCase
from task_one import *

class task_one_test(TestCase):

    def test_that_number_generated_is_between_1_and_100(self):
        
        actual =False

        actual_value =generate_a_random_number()
    
        if actual_value <100 and actual_value>0: 
            actual =True

        expected =True

        self.assertEqual(expected, actual)

    def test_that_every_sessions_random_number_is_different(self):

        random_number =generate_a_random_number()

        second_sessions_random_number =generate_a_random_number()

        self.assertNotEqual(random_number, second_sessions_random_number)

    def test_if_guess_attempts_have_been_exhausted(self):

        random_number =generate_a_random_number()

        actual =  manage_the_guessing_loop(random_number)

        expected = "Attempts exhausted: you failed"      

        self.assertEqual(actual, expected)

    def test_if_guess_is_correct_before_five_attempts(self):

        random_number =generate_a_random_number()

        actual =  manage_the_guessing_loop(random_number)

        expected =  "Well done: you have sense"    

        self.assertNotEqual(actual, expected)

        
