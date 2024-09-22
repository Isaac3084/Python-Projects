def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as file:
        plaintext = file.read()

    encrypted_text = ''.join([chr((ord(char) + key - 65) % 26 + 65) if char.isalpha() else char for char in plaintext])

    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()

    decrypted_text = ''.join([chr((ord(char) - key - 65) % 26 + 65) if char.isalpha() else char for char in encrypted_text])

    with open(output_file, 'w') as file:
        file.write(decrypted_text)

if __name__ == "__main__":
    input_file = "input.txt"
    encrypted_file = "encrypted.txt"
    decrypted_file = "decrypted.txt"
    encryption_key = 3  # Change this key for different encryption

    encrypt_file(input_file, encrypted_file, encryption_key)
    print(f"File '{input_file}' encrypted successfully. Encrypted content saved to '{encrypted_file}'.")

    decrypt_file(encrypted_file, decrypted_file, encryption_key)
    print(f"File '{encrypted_file}' decrypted successfully. Decrypted content saved to '{decrypted_file}'.")
