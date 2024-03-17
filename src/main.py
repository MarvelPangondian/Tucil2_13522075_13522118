from bezier_curve import BezierDnC
import numpy as np
from IO import *

print("=============================================================================")
print("Bézier Curve Program")
print("By : ")
print("Marvel Pangondian (13522075)")
print("Berto Richardo Togatorop (13522118)")
end = False 
while not end :
    choice = Mainmenu()
    bezier_curve = orde_iteration_input(choice)
    show_output(bezier_curve,choice)
    save_fig(bezier_curve)


    # order = int(input("input order : "))
    # control_points = [[0,0] for i in range(order + 1)]
    # for i in range(order + 1): 
    #     control_points[i][0] = float(input(f"Sumbu x Control point ke {i + 1}: "))
    #     control_points[i][1] = float(input(f"Sumbu y Control point ke {i + 1}: "))
    # control_points = np.array(control_points)
    # depth = int(input("Masukkan jumlah iterasi: "))
    # method = int(input("Masukkan method: "))
    # bezier = BezierDnC(control_points, depth, method)
    # bezier.showGraph()
    # # if (method == 1):
    # #     bezier.animate()

    lanjut = input("Apakah ingin lanjut?(y/n) ")
    end = (lanjut != "y")

    