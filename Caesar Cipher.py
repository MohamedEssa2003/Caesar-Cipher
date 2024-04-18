def caesar_cipher(plaintext, shift, mode):
    result = ''
    for char in plaintext:
        if char.isalpha() or char.isspace() or not char.isalnum():
            if char.isalpha():
                if char.isupper():
                    start = ord('A')
                else:
                    start = ord('a')
                if mode == "encrypt":
                    shifted = (ord(char) - start + shift) % 26 + start
                elif mode == "decrypt":
                    shifted = (ord(char) - start - shift) % 26 + start
                result += chr(shifted)
            else:
                result += char
        else:
            print("Invalid input. Please enter only characters, spaces, or symbols.")
            return ''
    return result

def main():
    while True:
        option = input("[*] Press 1 for Encryption🔒🔑\n[*] Press 2 for Decryption🔓🔑\n[*] Press 12 to Exit\n").strip()

        if option == "12":
            print("Exiting...")
            break

        if option not in ['1', '2']:
            print("Invalid option. Please choose '1', '2', or '12' to Exit.")
            continue

        mode = "encrypt" if option == "1" else "decrypt"
        
        if mode == "encrypt":
            while True:
                text = input("Plaintext🔓: ")
                if all(char.isalpha() or char.isspace() or not char.isalnum() for char in text):
                    break
                else:
                    print("Invalid input. Please enter only characters, spaces, or symbols.")

        else:
            while True:
                text = input("Ciphertext🔒: ")
                if all(char.isalpha() or char.isspace() or not char.isalnum() for char in text):
                    break
                else:
                    print("Invalid input. Please enter only characters, spaces, or symbols.")

        while True:
            try:
                shift = int(input("Shift Key 🔑 value: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer value for the shift key.")

        if mode == "encrypt":
            encrypted_text = caesar_cipher(text, shift, "encrypt")
            print("Ciphertext🔒:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, shift, "decrypt")
            print("Plaintext🔓:", decrypted_text)

if __name__ == "__main__":
    main()
