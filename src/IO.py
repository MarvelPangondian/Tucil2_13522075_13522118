import numpy as np
from bezier_curve import BezierCurve
import os

# Function to accept user input for selecting a preferred algorithm.
# It ensures that the input is a valid integer representing a choice between two algorithms.
def method_input() -> int:
    print("=============================================================================")
    valid = False
    choice = 0
    while (not valid):
        # Prompting the user to choose between two algorithms and handling invalid input.
        print("Choose your prefered algorithm !")
        print("1. Divide and Conquer")
        print("2. Brute Force")
        try:
            choice = int(input("Input : "))
            if (choice == 1 or choice == 2):
                valid = True
            else:
                print("Please choose a valid option !")
        except ValueError:
            print("Please input a valid integer !")
        print()
    # Return the user's choice of algorithm.
    return choice


# Accept bezier atribute starting from order, the control points and then the number of iteration
def bezier_attribute_input(choice : int) -> BezierCurve:
    valid = False
    print("=============================================================================")
    while (not valid):
        try:
            # order input
            order = int(input("Bézier Curve order : "))
            if (order <= 0):
                print("Please input a valid order !")
                print()
                continue
            
            #control points
            control_points = [[0,0] for i in range(order + 1)]
            for i in range(order + 1): 
                control_points[i][0] = float(input(f"X-axis Control point number  {i + 1}: "))
                control_points[i][1] = float(input(f"Y-axis Control point number  {i + 1}: "))
            control_points = np.array(control_points)

            # number of iteration
            depth = int(input("Input number of iterations: "))
            if (depth <0):
                print("Invalid depth input !")
                continue
            print()
            # create the bezier curve
            bezier = BezierCurve(control_points,depth,choice)
            return bezier
        
        except ValueError:
            print("Input is invalid !")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        print()

# Procedure to show the visualisation. It is either a graph or an animation
def show_output(result : BezierCurve , choice : int) -> None:
    if (choice == 1):
        print("=============================================================================")
    valid = False
    while (not valid):
        try:
            if (choice == 1):
                print("Please pick your prefered output")
                print("1. Graph, no animation")
                print("2. Graph with animation (bonus)")
                choice_output = int(input("Input: "))

                # Show graph
                if (choice_output == 1):
                    result.showGraph()
                    valid = True
                #
                elif (choice_output == 2):
                    valid = True
                    result.animate()
                else:
                    print("Please enter the correct choice !")

            elif (choice == 2):
                result.showGraph()
                valid = True
        except ValueError:
            print("Please input the correct type !")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        print()

# Procedure to save the graph figure to the ../test folder. 
def save_fig(result : BezierCurve):
    valid = False
    print("=============================================================================")
    while (not valid):
        save_option = input("Would you like to save the graph ? y(yes) / other key (no): ")
        if (save_option == "y"):
            save_path = "../test/"
            file_name = input("file name (with .png): ")
            save_path_file = os.path.join(save_path, file_name)
            if (os.path.exists(save_path_file)):
                print("File already exists !")
            else:
                result.fig.savefig(save_path_file)
                valid = True
        else:
            valid = True
        print()