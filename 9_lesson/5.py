import json

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def members_of_class():
   with open("FIO.json", "r", encoding="utf-8") as json_file:
       data = json.load(json_file)
       for value in data.values():
           if value < 3:
               print(get_key(data,value))


def main():
    members_of_class()


if __name__ == "__main__":
    main()
