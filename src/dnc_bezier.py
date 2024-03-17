import numpy as np

def divide_and_conquer_bezier(points, depth, curve_points=[], intermediates=[]):
    if depth == 0:
        curve_points.extend([points[0],points[-1]])
        return curve_points, intermediates
    
    start_needed = [points[0]]
    last_needed = [points[-1]]
    final_piece = []

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
    all = []
    all.extend(start_needed)
    all.extend(final_piece)
    all.extend(last_needed)
    divide_and_conquer_bezier(np.array(all[0 : (len(all)//2) + 1]), depth - 1, curve_points,intermediates)
    divide_and_conquer_bezier(np.array(all[(len(all) // 2) : ]), depth - 1, curve_points,intermediates)
    return curve_points, intermediates
    