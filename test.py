from morsecode import MORSECODE,Morse_function,English_function,choosing_input

# Import the 'unittest' module, which provides a testing framework
import unittest

# Define a test class thats from 'unittest.TestCase'
class TestMorseCodeConversion(unittest.TestCase):

# test the convertion of English to Morse code
    def test_english_to_morse(self):
        # The expected Morse code result for the input 'TKH USER'
        expected_result = '- -.- .... / ..- ... . .-. '
        
        # Call the function to convert 'TKH USERS' to Morse code
        actual_result = Morse_function('TKH USER', MORSECODE)
        
        # Assert that the actual result matches the expected result; otherwise, raise an AssertionError with a custom error message
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\nActual: {actual_result}")