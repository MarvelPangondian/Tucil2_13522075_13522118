import numpy as np
from typing import List, Tuple

def interpolate(point1 : float, point2 : float, t : float) -> Tuple[float,float] :
    return (1 - t) * np.array(point1) + t * np.array(point2)


def brute_force_bezier(points : List[Tuple[float,float]], depth : int) -> List[Tuple[float, float]] :
    curve_points = []
    new = []

    for i in range(((2 ** depth) + 1)) : 
        store = points

        t = i / ((2 ** depth))
        
        while (len(store) != 1):
            temp = []
            for i in range(len(store) - 1):
                temp.append(interpolate(store[i], store[i+1], t))
            store = temp
            new.append(temp)

            if (len(store) == 1):
                curve_points.append(store[0])

    return curve_points


