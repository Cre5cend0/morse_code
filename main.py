# Morse code constructor
import time

from playsound import playsound

MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}


class Message:
    def __init__(self, text):
        self.text = text

    def encrypt_morse(self):
        text = self.text.upper()
        phrase = []
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '0123456789'
        for char in text:
            if char in upper_case or char in nums:
                phrase.append(MORSE_DICT[char])
            elif char in " ":
                phrase.append('|')
            elif char in ("!@#$%^&*()-_+={}[]|\:;'<>?,./\""):
                phrase.append(char)
        sentence = ' '
        sentence = sentence.join(phrase)

        return sentence

    def decrypt_morse(self):
        for key, val in MORSE_DICT.items():
            morse = self.text
            #todo



text1 = Message("I love Music")

morse_code = text1.encrypt_morse()
print(morse_code)

with open('code.txt', 'r') as code:
    morse = code.readline()


def play_morse(code):
    for char in code:
        if char == '.':
            playsound('beep_short.wav')
        elif char == '-':
            playsound('beep_long.wav')
        elif char == ' ':
            time.sleep(0.5)
        elif char == '|':
            time.sleep(1.5)


play_morse(morse)
