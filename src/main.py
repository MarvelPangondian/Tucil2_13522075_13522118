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

    lanjut = input("Apakah ingin lanjut?(y/n) ")
    end = (lanjut != "y")
