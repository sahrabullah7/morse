from morsecode import MORSECODE,Morse_function,English_function,choosing_input

# Import the 'unittest' module, which provides a testing framework
import unittest

# Define a test class thats from 'unittest.TestCase'
class TestMorseCodeConversion(unittest.TestCase):

# test the convertion of English to Morse 
    def test_english_to_morse(self):
        # The expected Morse code result for the input 'TKH USER'
        expected_result = '- -.- .... / ..- ... . .-. '
        
        # Call the function to convert 'TKH USERS' to Morse code
        actual_result = Morse_function('TKH USER', MORSECODE)
        
        # Assert that the actual result matches the expected result; otherwise, raise an AssertionError with a custom error message
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\nActual: {actual_result}")

 # test THE CONVERSION Morse to English
    def test_morse_to_english(self):
        # Define the expected English result for the input Morse code
        expected_result = 'TKH USER' 
        
        # Call the 'English_function' function to convert the Morse code to English
        actual_result = English_function(' - -.- .... / ..- ... . .-.', MORSECODE)
        
        # check that the actual result matches the expected result; otherwise, raise an AssertionError with a custom error message
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\nActual: {actual_result}")

# raising an error for invalid morse code input
    def test_invalid_morse_to_english(self):

        with self.assertRaises(ValueError):  

            English_function('.... ----- / -..--- / .-.. .-.. .-', MORSECODE)   #call a wrong function

# Test conversion from Morse code with space
    def test_morse_code_with_space(self): #check the less spaces in the sentence
        
        expected_result = 'TKH USER'  # Expected English text for '- -.- .... / ..- ... . .-.'
        actual_result = English_function('- -.- .... ..- ... . .-.', MORSECODE)
        print(f"Expected: {expected_result}\nActual: {actual_result}")

if __name__ == '__main__':
    unittest.main()