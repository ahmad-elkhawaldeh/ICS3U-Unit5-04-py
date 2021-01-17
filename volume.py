# !/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program calculates the volume of cylinder


def calculate_volume_of_cylinder(radius_string, Height_string):
    # return volume

    radius = int(radius_string)
    Height = int(Height_string)
    volume = 3.14 * radius**2 * Height
    return volume


def main():
    print(" calculate the area of a cylinder ")
    try:
        radius_string = input('Enter radius(cm): ')
        Height_string = input('Enter the height(cm): ')

        cylinder_v = calculate_volume_of_cylinder(radius_string, Height_string)
        print("Volume is: ", cylinder_v)

    except Exception:
        print("This is not a number")


if __name__ == "__main__":
    main()
