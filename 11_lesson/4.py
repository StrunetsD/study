import math


class Sphere:

    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def print_radius(self):
        print(f"Radius: {self.radius}")

    def print_center(self):
        print(f"Center: ({self.x}, {self.y}, {self.z})")

    def set_radius(self, new_radius):
        self.radius = new_radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4/3 * math.pi * pow(self.radius, 3)

    def get_square(self):
        return 4 * math.pi * pow(self.radius, 2)

    def is_point_inside(self, new_x, new_y, new_z):
        if pow((new_x - self.x), 2) + pow((new_y - self.y), 2) + pow((new_z - self.z), 2) < pow(self.radius, 2):
            return True
        else:
            return False


def main():
    sphere = Sphere()
    while True:
        print("Menu:")
        print("1. print_radius")
        print("2. print_center")
        print("3. set_radius")
        print("4. set_center")
        print("5. get_volume")
        print("6. get_square ")
        print("7. is_point_inside ")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == '1':
            sphere.print_radius()
        elif choice == '2':
            sphere.print_center()
        elif choice == '3':
            while True:
                try:
                    new_radius = float(input("enter new radius: "))
                    sphere.set_radius(new_radius)
                    break
                except ValueError:
                    print("you need to enter num!")
        elif choice == '4':
            while True:
                try:
                    x = float(input("enter x: "))
                    y = float(input("enter y: "))
                    z = float(input("enter z: "))
                    sphere.set_center(x, y, z)
                    break
                except ValueError:
                    print("enter numbers!")
        elif choice == '5':
            result = sphere.get_volume()
            print(result)
        elif choice == '6':
            result = sphere.get_square()
            print(result)
        elif choice == '7':
            while True:
                try:
                    new_x = int(input("enter x: "))
                    new_y = int(input("enter y: "))
                    new_z = int(input("enter z: "))
                    flag = sphere.is_point_inside(new_x, new_y, new_z)
                    if flag:
                        print(True)
                    else:
                        print(False)
                    break
                except ValueError:
                    print("enter numbers!")
        elif choice == '8':
            print("Exiting the program.")
            return
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
