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
def main():
   while True:
       print("\nMenu:")
       print("1. convert English to Morse code")
       print("2. convert Morse code to English")
       print("3. Main menu")
       choice = input("Enter your choice (1/2/3): ")
       if choice == '1':
           text_to_translate = input("Enter the text to translate to Morse code: ")
           result = translate_to_morse(text_to_translate)
           print("Translated to Morse code:", result)
       elif choice == '2':
           morse_to_translate = input("Enter the Morse code to translate to English: ")
           result = translate_to_english(morse_to_translate)
           print("Translated to English:", result)
       elif choice == '3':
           print("Thank you for using morse code. Goodbye!")
           break
       else:
           print("Invalid choice. Please enter a valid option (1/2/3).")
if __name__ == "__main__":
   main()