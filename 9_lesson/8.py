import json
import csv
from csv import excel


def avg_height():
    with open("8.json", "r") as file:
        data = json.load(file)
        year = int(input("enter your year: "))
        height = 0
        counter = 0
        for item in data:
            birthday = int(item['birthday'].split('.')[-1])
            if birthday < year:
                height += int(item.get('height'))
                counter += 1
        if counter == 0:
            print("there is no people")
        else:
            print(height / counter)


def search_language():
    with open("8.json", "r") as file:
        data = json.load(file)
        language = input("search language: ")
        names = []
        for item in data:
            if language in item.get('languages', []):
                names.append(item['name'])
        print(names)


def search_human():
    with open("8.json", "r") as file:
        data = json.load(file)
        name_of_human = input("Search name: ")

        try:
            human = next(item for item in data if item['name'] == name_of_human)
            print(human)
        except StopIteration:
            print(f"No human found with the name '{name_of_human}'.")


def add_human_cf():
    name = input("Enter name: ")
    birthday = input("Enter birthday: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    car = input("Enter car (True/False): ")
    languages = input("Enter languages : ").split(',')

    new_data = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car.lower() == 'true',
        "languages": [lang.strip() for lang in languages]
    }

    with open("8_result.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=new_data.keys())
        writer.writerow(new_data)


def add_human_jf():
    try:
        with open("8.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("no file")

    name = input("Enter name: ")
    birthday = input("Enter birthday: ")
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    car = input("Enter car (True/False): ")
    languages = input("Enter languages : ").split(',')

    new_data = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car.lower() == 'true',
        "languages": [lang.strip() for lang in languages]
    }

    #
    data.append(new_data)
    with open("8.json", "w") as file:
        json.dump(data, file, indent=4)


def get_from_json():
    with open("8.json", "r") as jf:
        with open("8_result.csv", "w") as cf:
            data = json.load(jf)
            writer = csv.writer(cf)
            first_line = data[0].keys()
            writer.writerow(first_line)
            for item in data:
                writer.writerow(item.values())


def main():
    while True:
        print("Menu:")
        print("1. Calculate average height")
        print("2. Search for language speakers")
        print("3. Search for a human by name")
        print("4. Add human  CSV")
        print("5. Add human  JSON")
        print("6. Export JSON ")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == '1':
            avg_height()
        elif choice == '2':
            search_language()
        elif choice == '3':
            search_human()
        elif choice == '4':
            add_human_cf()
        elif choice == '5':
            add_human_jf()
        elif choice == '6':
            get_from_json()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
