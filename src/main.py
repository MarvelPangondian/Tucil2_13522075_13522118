from bezier_curve import BezierDnC
import numpy as np

end = False 
while not end : 
    order = int(input("input order : "))
    control_points = [[0,0] for i in range(order + 1)]
    for i in range(order + 1): 
        control_points[i][0] = float(input(f"Sumbu x Control point ke {i + 1}: "))
        control_points[i][1] = float(input(f"Sumbu y Control point ke {i + 1}: "))
    control_points = np.array(control_points)
    depth = int(input("Masukkan jumlah iterasi: "))
    method = int(input("Masukkan method: "))
    bezier = BezierDnC(control_points, depth, method)
    bezier.showGraph()

    lanjut = input("Apakah ingin lanjut?(y/n) ")
    end = (lanjut != "y")

    