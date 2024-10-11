'''
Name - Gouravjeet Singh, Student Id 100920691
TPRG 2131 Fall 2024 Assignment 1
Oct, 2024

This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s)

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''

import math # Importing the math module for mathematical operations.
print ("***********A/V_calculater**********")

# Function to calculate the area of a circle.
def area_circle(radius):
    area1 = math.pi * radius ** 2
    area = round(area1, 1)
    return area
# Function to calculate the volume of a cylinder.
def vol_cylinder(radius, height):
    vol1 = area_circle (radius) * height
    vol = round(vol1, 1)
    return vol
# Function to calculate the area of a rectangle.    
def area_rectangular(length, width):
    area1 = length * width
    area = round(area1, 1)
    return area
# Function to calculate the volume of a sphere.
def vol_sphere(radius):
    vol1 = (4/3) * math.pi * radius ** 3
    vol = round(vol1, 1)
    return vol
# Function to calculate the area of a triangle.
def area_triangle(base, height):
    area1 = 0.5 * base * height
    area = round(area1, 1)
    return area
def get_valid_input(message):
 while True:
    try:
        
     # Continue prompting the user until they enter a value greater than zero
        value = float(input(message))
        while value <= 0.0:# Continue prompting the user until they enter a value greater than zero.
            value = float(input("The value must be greater than zero\n"
            + message))
        return value
    except ValueError:
            print("Oops!  That was no valid number.  Try again...")
def get_valid_string(message):# Function to get a valid string input (q/Q, v/V, d/D) from the user.
    value = str(input(message))
    while value!= "q" and value!= "Q" and value != 'v' and value != 'V' and value != 'D' and value != 'd' :# Continue prompting the user until they enter a value greater than zero.
        value = str(input("invalid input try again\n"
        + message))
    return value
# Function to display the result based on the user's view selection.
def display_result(formula, result, selection):
    if selection == "v" or selection == "V":
        return f"Equation: {formula}\nAnswer: {result}"
    elif selection == "d" or selection == "D":
        return f"Answer: {result}"

if __name__ == "__main__":
    
    while True:
        
         # Get the user's choice for viewing the result or quitting the program.
        user_choice = get_valid_string("\nEnter Q/q to quit, V/v for detailed answer view with equation , D/d for answer only view . \n[Q/V/D]??").lower()        
        if user_choice == "q":
            quit("\nexiting, \n Have a nice a Day!")
        
            
            
        while True:
         # Display the menu options.
            print("\n1. Area of a circle")
            print("\n2. Volume of a Cylinder")
            print("\n3. Area of a Rectangle")
            print("\n4.Volume of a Sphere")
            print("\n5. Area of a Triangle")
            print("\n6. Main Menu")
             # Get the user's choice for the calculation.    
            choice = input("\nSelect option from 1-6:-")
                
            if choice == "1":
                radius = get_valid_input("Enter the Radius") # Get the user's choice for the calculation.
                result = area_circle(radius)# Calculate the area of a circle.
                formula = f"\u03c0 * {radius}^2"# Prepare the formula string.
                final = display_result(formula, result, user_choice)
                print(final, "\u33A1")# Display the result.
                    
                             
            elif choice == "2": # Get the radius from the user.
                radius = get_valid_input("Enter the Radius")# Get the radius from the user.
                height = get_valid_input("Enter the height")#Get the height from the user.
                result = vol_cylinder(radius, height)# Calculate the volume of a cylinder.
                formula = f"\u03c0 * {radius}^2 * {height}"# Prepare the formula string.
                final = display_result(formula, result, user_choice)
                print(final, "\u33A5")# Display the result.
                    
            elif choice == "3":
                length = get_valid_input("Enter the Lenght")#Get the lenght from the user.
                width = get_valid_input("Enter the Width")#Get the widht from the user.
                result = area_rectangular(length, width)# Calculate the area of a rectangle.
                formula = f"{length} * {width}"# Prepare the formula string.
                final = display_result(formula, result, user_choice)
                print(final, "\u33A1")# Display the result.
                    
            elif choice == "4":
                radius = get_valid_input("Enter the Radius")#Get the radius from the user.
                result = vol_sphere(radius) # Calculate the volume of a sphere.
                formula = f"(4/3) * \u03c0 * {radius}"# Prepare the formula string.
                final = display_result(formula, result, user_choice)
                print(final, "\u33A5")# Display the result.
                    
            elif choice == "5":
                base = get_valid_input("Enter the Base")#Get the base from the user.
                height = get_valid_input("Enter the height")#Get the height from the user.
                result = area_triangle(base, height)# Calculate the area of a triangle.
                formula = f"0.5 * {base} * {height}"# Prepare the formula string.
                final = display_result(formula, result, user_choice)
                print(final, "\u33A1")# Display the result.
                    
            elif choice == "6":
                print("Going back to main menu")# Go back to the main menu.
                break
                    
            else:
                print("Invalid input, Please try again") # Handle invalid input.
                 
 