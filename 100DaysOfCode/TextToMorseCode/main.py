MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def text_to_morse():
    print("Welcome To Morse Code Text Converter!")
    text_to_convert = input("Enter the text you wish to convert to Morse: ").upper()

    # Checks to see if there are any special characters in the string (Not includes whitespace)
    if any((not ch.isalnum() and not ch.isspace())for ch in text_to_convert):
        print("Sorry your string contains characters which can not ne converted to Morse :(")
    else:
        morse_converted_text = ""
        for ch in text_to_convert:
            # Checks if current char is in the dict, if not it must be a space, so it adds 2 whitespaces
            if ch in MORSE_CODE_DICT:
                morse_converted_text += MORSE_CODE_DICT[ch]
            else:
                morse_converted_text += "  "
        print("Your Morse code text:")
        print(f"{morse_converted_text}")

    # Asks the user if he wants to continue, if so calls the function again
    to_continue = input("Do you wish to convert more text (y/n)? ") == 'y'
    if to_continue:
        text_to_morse()


text_to_morse()
