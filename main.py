# !/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program calculates the area of cylinder


print(" calculate the area of a cylinder ")

def calculate_volume_of_cylinder(radius_string, Height_string):

    radius = int(radius_string)
    Height = int(Height_string)
    volume = 3.14 * radius**2 * Height
    print("The volume of the cylinder is {0} cm² ".format(volume)) 
  
def main():
    try:
        radius_string = input('Enter radius(cm): ')
        Height_string = input('Enter the height(cm): ')

        calculate_volume_of_cylinder(radius_string, Height_string)

    except Exception:
        print("This is not a number")

if __name__ == "__main__":
    main()