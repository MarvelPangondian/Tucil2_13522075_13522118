import numpy as np
import matplotlib.pyplot as plt
import time

def divide_and_conquer_bezier(points, depth, curve_points=None):
    if curve_points is None:
        curve_points = []
    if depth == 0:
        curve_points.extend([points[0],points[-1]])
        return curve_points
    
    start_needed = [points[0]]
    last_needed = [points[-1]]
    final_piece = []

    while (len(points) != 1):
        temp = []
        for i in range(len(points) - 1):
            temp.append( (points[i] + points[i+1])/2 )
        points = temp
        if (len(points) == 1):
            final_piece.append(points[0])
        else :
            start_needed.append(temp[0])
            last_needed.insert(0,temp[-1])
    all = []
    all.extend(start_needed)
    all.extend(final_piece)
    all.extend(last_needed)

    divide_and_conquer_bezier(np.array(all[0 : (len(all)//2) + 1]), depth - 1, curve_points)
    divide_and_conquer_bezier(np.array(all[(len(all) // 2) : ]), depth - 1, curve_points)
    return curve_points

def showGraphDnC(control_points,depth):
    start_time = time.time()  # Start timing
    curve_points = divide_and_conquer_bezier(control_points, depth, [])
    curve_points_array = np.array(curve_points)
    _, unique_indices = np.unique(curve_points_array, axis=0, return_index=True)
    execution_time = (time.time() - start_time)*1000
    curve_points_unique = curve_points_array[sorted(unique_indices)]
    
    plt.figure(figsize=(10, 6))
    plt.plot(*zip(*curve_points_unique), label='Quadratic Bézier Curve', marker='o', markersize=4, linestyle='-', color='#8dc6ff')
    plt.plot(*zip(*control_points), marker='o', markersize=4, linestyle='--', color='#34495e', label='Control Points')
    plt.scatter(*zip(*control_points), color='#22313f', zorder=5)
    for i, point in enumerate(control_points):
        formatted_point = f"C{i}: ({point[0]:.2f}, {point[1]:.2f})"
        plt.text(point[0], point[1], formatted_point, fontsize=9, verticalalignment='bottom', horizontalalignment='right')

    annotation_interval = len(curve_points_unique) // 10 or 1# avoid showing too many points

    for i, point in enumerate(curve_points_unique):
        if (i % annotation_interval == 0 and point not in control_points):
            formatted_point = f"({point[0]:.2f}, {point[1]:.2f})"
            plt.text(point[0], point[1], formatted_point, fontsize=6, verticalalignment='top')

    all_points = np.concatenate([curve_points_array, control_points])
    x_coords = all_points[:, 0]
    y_coords = all_points[:, 1]
    x_min, x_max = x_coords.min(), x_coords.max()
    y_min, y_max = y_coords.min(), y_coords.max()

    # Adding some margin
    margin_x = (x_max - x_min) * 0.1 
    margin_y = (y_max - y_min) * 0.1

    plt.xlim(x_min - margin_x, x_max + margin_x)
    plt.ylim(y_min - margin_y, y_max + margin_y)
    plt.text(0.5, 0.01, f'Execution Time: {execution_time:.2f} ms', fontsize=10, transform=plt.gcf().transFigure, horizontalalignment='center')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Bézier Curve via Divide and Conquer')
    plt.grid(True) 
    plt.tight_layout()
    plt.show()

control_points = np.array( [(-2,-3),(-3,-2),(0,-2), (1,-3),(2,1)], dtype=float)
depth = 6
showGraphDnC(control_points,depth)
