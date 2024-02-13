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
def translate_to_english(morse_code):
   """Translates Morse code to English text."""
   english_text = ''
   morse_to_eng = {v: k for k, v in morse_code_dict.items()}
   morse_words = morse_code.split()
   for word in morse_words:
       if word in morse_to_eng:
           english_text += morse_to_eng[word]
       else:
           return f"Error: '{word}' is not in the dictionary."
   return english_text
