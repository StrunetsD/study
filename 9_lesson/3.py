def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def function():
    with open("3.txt", "r") as text_file:
        with open("main.txt", "w") as main_file:
            for line in text_file:
                words = {}
                line = line.split()
                for word in line:
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
                if words:
                    max_value = max(words.values())
                    if all(value == max_value for value in words.values()):
                        main_file.write("all words have the same")
                    max_key = get_key(words, max_value)
                    main_file.write(f" {max_key}: {max_value}\n")
                else:
                    main_file.write("no words")


def main():
    function()


if __name__ == "__main__":
    main()
