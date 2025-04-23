alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def encrypt(text, shift):
    text_encrypted = ''
    for i in text:
        if i not in alphabet:
            text_encrypted += i
            continue
        for j in alphabet:
            if i == j:
                new_index= (alphabet.index(j) + shift)
                new_index %= len(alphabet)
                text_encrypted += alphabet[new_index]
    print(f"Your message was encrypted:\n{text_encrypted}")
    

def decrypt(text, shift):
    text_decrypted = ''
    for i in text:
        if i not in alphabet:
            text_decrypted += i 
            continue
        for j in alphabet:
            if i == j:
                new_index= (alphabet.index(j) - shift)
                new_index %= len(alphabet)
                text_decrypted += alphabet[new_index]
    print(f"Your message was encrypted:\n{text_decrypted}")
print("CEASER CYPHER")
while True:
    print("-"*50)
    choice = input("Type 'D' to decrypt, 'E' to encrypt or 'L' to leave the program:\n-> ").upper()
    if choice == "L":
        print("Leaving the program.")
        break
    elif choice == "D":
        text = input("Type your message:\n-> ").lower()
        shift = int(input("Type the shift number:\n-> "))
        decrypt(text = text, shift = shift)
    elif choice == "E":
        text = input("Type your message:\n-> ").lower()
        shift = int(input("Type the shift number:\n-> "))
        encrypt(text = text, shift = shift)
    else:
        print("Enter a valid input.")