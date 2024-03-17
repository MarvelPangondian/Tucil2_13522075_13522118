import numpy as np
from typing import List, Tuple

# function to get the curve points and intermediates for the bezier curve
def divide_and_conquer_bezier(
        points: List[Tuple[float, float]], 
        depth: int, 
        curve_points=[], 
        intermediates=[]
        ) -> Tuple[List[Tuple[float,float]], List[Tuple[float, float]]]:
    
    # recursion basis
    if depth == 0:
        # merge procesess
        curve_points.extend([points[0],points[-1]])
        return curve_points, intermediates
    
    start_needed = [points[0]]
    last_needed = [points[-1]]
    final_piece = []

    # iterartion to find the curve points and the parameter points for the next recursion
    while (len(points) != 1):
        temp = []
        for i in range(len(points) - 1):
            temp.append( (points[i] + points[i+1])/2 )
        points = temp
        intermediates.append(temp)
        if (len(points) == 1):
            final_piece.append(points[0])
        else :
            start_needed.append(temp[0])
            last_needed.insert(0,temp[-1])

    # List all the points
    all = []
    all.extend(start_needed)
    all.extend(final_piece)
    all.extend(last_needed)

    # recursion that divide the points into left and right
    divide_and_conquer_bezier(np.array(all[0 : (len(all)//2) + 1]), depth - 1, curve_points,intermediates)
    divide_and_conquer_bezier(np.array(all[(len(all) // 2) : ]), depth - 1, curve_points,intermediates)
    return curve_points, intermediates
    