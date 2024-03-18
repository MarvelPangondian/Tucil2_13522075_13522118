import numpy as np
from typing import List, Tuple

# interpolation function
def interpolate(point1 : Tuple[float], point2 : Tuple[float], t : float) -> Tuple[float,float] :
    return (1 - t) * np.array(point1) + t * np.array(point2)

# function to get the curve points using brute force method
def brute_force_bezier(points : List[Tuple[float,float]], depth : int) -> List[Tuple[float, float]] :
    curve_points = []

    # the points created is equal to (2 ^ iteration) + 1 
    for i in range(((2 ** depth) + 1)) : 
        # temp variable to store the control points
        temp_cp = points

        # adjust the t variable
        t = i / ((2 ** depth))
        
        # iterate until it get 1 point(the curve point)
        while (len(temp_cp) != 1):
            new_cp = []
            for i in range(len(temp_cp) - 1):
                new_cp.append(interpolate(temp_cp[i], temp_cp[i+1], t))
            temp_cp = new_cp

            if (len(temp_cp) == 1):
                curve_points.append(temp_cp[0])

    return curve_points


