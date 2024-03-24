def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

text = "Hello, World!"
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Zašifrovaný text:", encrypted_text)  
decrypted_text = caesar_decipher(encrypted_text, shift)
print("Dešifrovaný text:", decrypted_text)  
