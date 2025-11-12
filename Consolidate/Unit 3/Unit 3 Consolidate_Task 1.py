"""
Unit 3 Consolidatee-Task 1
"""

print("\n***Area Calculator*** \n")
print("Start\n")

# Loop until user chooses to exit
while True:
    shape = input("Press 1 for Area of Square:\nPress 2 for Area of Rectangle:\nPress 3 for Area of Circle:\nPress 0 to Exit:\n")

    # CONDITIONAL STATEMENTS
    if shape == "1":
        print("\nYour Choice: Area of Square")
        print("\n***Area of Square*** \n")
        print("For area of Square give length: ")
        l = float(input())
        print("For area of Square give width: ")
        w = float(input())
        area_square = float(l * w)
        print("Area of Square: ", area_square, "square meters")
        break  # Exit after successful calculation

    elif shape == "2":
        print("\nYour Choice: Area of Rectangle")
        print("\n***Area of Rectangle*** \n")
        print("For area of Rectangle give length: ")
        l = float(input())
        print("For area of Rectangle give width: ")
        w = float(input())
        area_rectangle = float(l * w)
        print("Area of Rectangle: ", area_rectangle, "square meters")
        break  # Exit after successful calculation

    elif shape == "3":
        print("\nYour Choice: Area of Circle")
        print("\n***Area of Circle*** \n")
        print("For area of Circle give radius: ")
        r = float(input())
        area_circle = float(3.14 * r * r)
        print("Area of Circle: ", area_circle, "square meters")
        break  # Exit after successful calculation

    elif shape == "0":
        print("\nExiting the program.")
        print("Goodbye!!!")
        break  # Exit the loop and end the program

    else:
        print("\nInvalid choice! Please enter 0, 1, 2, or 3.")
        print("Try again...\n")

print("\nEnd")
