# Morse code dictionary
morse_code_dict = {
   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
   'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
   'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
   'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
   '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
   ' ': '/'
}
def translate_to_morse(text):
   """Translates English text to Morse code."""
   morse_code = ''
   for char in text.upper():
       if char in morse_code_dict:
           morse_code += morse_code_dict[char] + ' '
       else:
           return f"Error: '{char}' is not in the dictionary."
   return morse_code
