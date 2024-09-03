def encrypt_string(text):
    encrypt = []

    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            encrypt.append(chr((((ord(char) - 65) + 3) % 26) + 65))
        elif ord(char) >= 97 and ord(char) <= 122:
            encrypt.append(chr((((ord(char) - 97) + 3) % 26) + 97))
        else:
            encrypt.append(char)

    return ''.join(encrypt)


def dencrypt_string(text):
    dencrypt = []

    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            dencrypt.append(chr((((ord(char) - 65) - 3) % 26) + 65))
        elif ord(char) >= 97 and ord(char) <= 122:
            dencrypt.append(chr((((ord(char) - 97) - 3) % 26) + 97))
        else:
            dencrypt.append(char)

    return ''.join(dencrypt)


string = input("input your text: ")
while True:
    print("1. encrypt")
    print("2. dencrypt")
    cmd = input(" choice:")

    if cmd == "1":
        print(encrypt_string(string))
        break
    elif cmd == "2":
        print(dencrypt_string(string))
        break
    else:
        print("try again")
