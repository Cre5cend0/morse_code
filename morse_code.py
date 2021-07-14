# Morse code constructor
import time
import string
from playsound import playsound


class Message:
    MORSE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----'
    }

    def __init__(self, text):
        self.text = text

    def encrypt_morse(self):
        # Avoiding encrypting an already encrypted message
        for char in self.text:
            if char not in string.ascii_letters:
                return 'Message is not English text based'
            else:
                break

        text = self.text.upper()
        phrase = []
        upper_case = string.ascii_uppercase
        nums = '0123456789'
        for char in text:
            if char in " ":
                phrase.append('|')

            elif char in """!@#$%^&*()-_+={}[]|\:;'<>?,./\\""""":
                phrase.append(char)

            elif char in upper_case or char in nums:  # purposely not using sting.alnum() as it is recognising ! as a char in alnum
                phrase.append(self.MORSE_DICT[char])

        sentence = ' '  # space is required here so that each letter has a space inbetween them
        sentence = sentence.join(phrase)

        return sentence

    def decrypt_morse(self):
        try:
            my_code = self.text
            words = my_code.split('|')
            phrase = ""
            for word in words:
                letters = word.strip(' \n')
                letters = letters.split(' ')
                for letter in letters:
                    try:
                        char = Message.get_key(self.MORSE_DICT, letter)
                        phrase += char
                    except KeyError:
                        letter = letter.strip("""!@#$%^&*()_+="{}[]|\:;'<>?,/\\""") # strip all special chars except dits and dahs
                        char = Message.get_key(self.MORSE_DICT, letter)
                        phrase += char
                phrase += ' '
            return phrase
        except KeyError:
            print("Text not in morse code")

    def play_morse(self):
        code = self.encrypt_morse()
        for char in code:
            if char == '.':
                playsound('beep_short.wav')
            elif char == '-':
                playsound('beep_long.wav')
            elif char == ' ':
                time.sleep(0.2)
            elif char == '|':
                time.sleep(0.6)
        return

    @staticmethod
    def get_key(my_dict, val):
        """function to return key for any value"""
        for key, value in my_dict.items():
            if val == value:
                return key
        raise KeyError
