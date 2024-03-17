import numpy as np
from bezier_curve import BezierDnC
import os
def Mainmenu() -> BezierDnC:
    print("=============================================================================")
    valid = False
    choice = 0
    while (not valid):
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
    return choice

def orde_iteration_input(choice : int) -> BezierDnC:
    valid = False
    print("=============================================================================")
    while (not valid):
        try:
            order = int(input("input order : "))
            if (order <= 0):
                print("Please input a valid order !")
                print()
                continue

            control_points = [[0,0] for i in range(order + 1)]
            for i in range(order + 1): 
                control_points[i][0] = float(input(f"Sumbu x Control point ke {i + 1}: "))
                control_points[i][1] = float(input(f"Sumbu y Control point ke {i + 1}: "))
            control_points = np.array(control_points)

            depth = int(input("Masukkan jumlah iterasi: "))
            if (depth <0):
                print("Invalid depth input !")
                continue
            print()
            bezier = BezierDnC(control_points,depth,choice)
            return bezier
        
        except ValueError:
            print("Input is invalid !")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        print()

def show_output(result : BezierDnC , choice : int):
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
                if (choice_output == 1):
                    result.showGraph()
                    valid = True
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

def save_fig(result : BezierDnC):
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