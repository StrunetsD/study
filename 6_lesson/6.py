def encrypt(text, key):
    key_length = len(key)
    key_index = 0

    encrypted = []
    for char in text:
        if char.isalpha():
            step = ord(key[key_index % key_length]) - 65
            new_char = chr((ord(char) - 65 + step) % 26 + 65)
            encrypted.append(new_char)
            key_index += 1
        else:
            encrypted.append(char)

    return ''.join(encrypted)


def decrypt(text, key):
    key_length = len(key)
    key_index = 0
    decrypted = []
    for char in text:
        if char.isalpha():
            step = ord(key[key_index % key_length]) - 65
            new_char = chr((ord(char) - 65 - step) % 26 + 65)
            decrypted.append(new_char)
            key_index += 1
        else:
            decrypted.append(char)

    return ''.join(decrypted)


string = input("enter text: ")
key = input("enter key: ")
while True:
    print("1. encrypt")
    print("2. decrypt")
    cmd = input("choice: ")

    if cmd == "1":
        print("encrypted:", encrypt(string, key))
        break
    elif cmd == "2":
        print("decrypted:", decrypt(string, key))
        break
    else:
        print("try again")