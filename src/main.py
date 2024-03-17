from bezier_curve import BezierCurve
import numpy as np
from IO import *

print("=============================================================================")
print("Bézier Curve Program")
print("By : ")
print("Marvel Pangondian (13522075)")
print("Berto Richardo Togatorop (13522118)")

end = False 
while not end :
    method = method_input()
    bezier_curve = bezier_attribute_input(method)
    show_output(bezier_curve,method)
    save_fig(bezier_curve)

    cont = input("Do you wish to continue?(y/n) ")
    end = (cont != "y")
