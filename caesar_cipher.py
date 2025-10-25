def encrypt(text, shift):
    
    result = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            
            result += char
            
    return result

def decrypt(text, shift):
    
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Encryption/Decryption Tool ===")
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Shift value must be between 1 and 25.")
                    continue
                encrypted_message = encrypt(message, shift)
                print(f"Encrypted message: {encrypted_message}")
            except ValueError:
                print("Please enter a valid number for the shift value.")
                
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value used for encryption (1-25): "))
                if shift < 1 or shift > 25:
                    print("Shift value must be between 1 and 25.")
                    continue
                decrypted_message = decrypt(message, shift)
                print(f"Decrypted message: {decrypted_message}")
            except ValueError:
                print("Please enter a valid number for the shift value.")
                
        elif choice == '3':
            print("Thank you for using the Caesar Cipher tool. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()