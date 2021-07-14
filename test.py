from morse_code import Message

# encrypting a message to morse code format
text1 = Message("I love Music!")
morse_code = text1.encrypt_morse()
print(morse_code)


# # playing morse code encoded earlier
text1.play_morse()


# decrypting a message in morse code format to text format
with open('code.txt', 'r') as code:
    morse = code.readline()
    my_message = Message(morse)

print(my_message.decrypt_morse())



