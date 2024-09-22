def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + (shift if direction == "encrypt" else -shift)) % 26 + ascii_offset)
        else:
            result += char
    return result

text = input("Enter text: ")
shift = int(input("Enter shift value: "))
direction = input("Enter 'encrypt' or 'decrypt': ")
print(caesar_cipher(text, shift, direction))
