def v_encrypt(message, shift):
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                new_letter = chr((ord(letter) - 65 + shift) % 26 + 65)
            else:
                new_letter = chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            new_letter = letter       # keep spaces as they are
        result += new_letter
    return result                     # return once at the end
def v_decrypr(message,shift):
    return v_encrypt(message, -shift)
message = input("ENTER THE MESSAGE: ")
shift   = int(input("BY HOW MUCH TO SHIFT: "))
choice=input("ENCRYPT OR DECRYPT?(e/d::)")
if choice=="e":
    print(v_encrypt(message,shift))
elif choice=="d":
    print(v_decrypr(message,-shift))
else:
    print("INVALID CHOICE!!")

