def encrypt_string(text, step):
    encrypt = []

    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            encrypt.append(chr((((ord(char) - 65) + step) % 26) + 65))
        elif ord(char) >= 97 and ord(char) <= 122:
            encrypt.append(chr((((ord(char) - 97) + step) % 26) + 97))
        else:
            encrypt.append(char)

    return ''.join(encrypt)


def encrypt_file():
    with open("7.txt", "r") as file:
        with open("result.txt", "w") as result_file:
            counter = 1
            line = file.readline()
            while line:
                encrypt_line = encrypt_string(line, counter)
                result_file.write(encrypt_line)
                counter += 1
                line = file.readline()


def main():
    encrypt_file()


if __name__ == "__main__":
    main()
