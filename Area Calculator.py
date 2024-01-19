#write a program to create a area calculator ?
print("Area Calculator")
print("""Press 1 to get the area of a square
Press 2 to get the area of a rectangle
Press 3 to get the area of a circle
Press 4 to get the area of a triangle""")
choice = int(input("Choose any one option between 1 to 4: "))

if choice == 1:
    side = float(input("Enter the length of one side: "))
    area = side ** 2
    print("The area of the square is", area)

elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is: ", area)

elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = (22 / 7) * (radius ** 2)
    print("The area of the circle is: ", area)

elif choice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is: ", area)

else:
    print("You have entered an invalid option. Try again!!")
