def caesar_encrypt(message, shift):
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                new_letter = chr((ord(letter) - 65 + shift) % 26 + 65)
            else:
                new_letter = chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            new_letter = letter
        result += new_letter
    return result

def caesar_decrypt(message, shift):
    return caesar_encrypt(message, -shift)

# ── User input ───────────────────────────────────────────────
print("=" * 40)
print("       CAESAR CIPHER TOOLKIT")
print("=" * 40)

message = input("Enter your message: ")
shift   = int(input("Enter shift number (1-25): "))
choice  = input("Encrypt or Decrypt? (e/d): ")

if choice == "e":
    result = caesar_encrypt(message, shift)
    print(f"\n Encrypted: {result}")
elif choice == "d":
    result = caesar_decrypt(message, shift)
    print(f"\nDecrypted: {result}")
else:
    print("Invalid choice!")

