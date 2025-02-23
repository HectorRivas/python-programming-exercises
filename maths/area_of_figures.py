###
# Title: Area of figures
# Description: This program calculates the area of geometric figures
###

def area_triangle(base, height):
    area = (base * height) / 2
    print(f"The area of the triangle is: {area}")


def area_square(side):
    area = side * side
    print(f"The area of square is: {area}")

def area_rectangle(base, height):
    area = base * height
    print(f"The area of rectangle is: {area}")

def area_circle(radius):
    PI =  3.14159265358979323846
    area = PI * (radius ** 2)
    print(f"The area of circle is: {area}")

print("This program calculates the area of geometric figures")

while True:
    print("Choose an option: ")
    print("1. Triangle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Circle")
    print("5. Exit")

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Invalid option")
        continue

    if option == 1:
        base = int(input("Enter the base value: "))
        height = int(input("Enter the height value: "))
        area_triangle(base, height)
    elif option == 2:
        side = int(input("Enter the value of side: "))
        area_square(side)
    elif option == 3:
        base = int(input("Enter the base value: "))
        height = int(input("Enter the height value: "))
        area_rectangle(base, height)
    elif option == 4:
        radius = int(input("Enter the value of radius: "))
        area_circle(radius)
    elif option == 5:
        print("Goodbye!")
        break
