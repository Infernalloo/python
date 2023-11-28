alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_input, shift_amount) :
    encrypted_text = ""
    for letter in text :
        new_index = alphabet.index(letter)
        new_letter = alphabet[new_index + shift]
        encrypted_text += new_letter
    print(f"The encoded text is {encrypted_text}")

def decrypt(text_input, shift_amount) :
    decrypted_text = ""
    for letter in text :
        new_index = alphabet.index(letter)
        new_letter = alphabet[new_index - shift]
        decrypted_text += new_letter
    print(f"The decoded text is {decrypted_text}")
        
if direction == "encode" :
    encrypt(text_input=text, shift_amount=shift)
elif direction == "decode" :
    decrypt(text_input=text, shift_amount=shift)
else :
    print("Did you type the correct word?")