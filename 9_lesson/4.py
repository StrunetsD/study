from idlelib.iomenu import encoding


def replace_stop_words():
    file_name = input("Enter name of file: ")

    with open("stop_words.txt", "r") as stop_words_file:
        stop_words = stop_words_file.read().lower().split()

    with open(file_name, "r") as result_file:
        text = result_file.read().lower()

    for stop_word in stop_words:
        text = text.replace(stop_word, '*' * len(stop_word))

    with open("text.txt", "w") as result_file:
        result_file.write(text)


def main():
    replace_stop_words()

if __name__ == "__main__":
    main()



