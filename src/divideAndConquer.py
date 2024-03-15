import numpy as np
import matplotlib.pyplot as plt


def divide_and_conquer_bezier(points, depth, curve_points=None):
    if curve_points is None:
        curve_points = []
    if depth == 0:
        # Use numpy to calculate and append points without unpacking
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

# Convert control points to a numpy array
control_points = np.array( [(-2,-3),(-3,-2),(0,-2),(1,-3),(2,1)], dtype=float)

depth = 1
curve_points = divide_and_conquer_bezier(control_points, depth, [])
curve_points_array = np.array(curve_points)
_, unique_indices = np.unique(curve_points_array, axis=0, return_index=True)

curve_points_unique = curve_points_array[sorted(unique_indices)]

plt.figure(figsize=(10, 6))
plt.plot(*zip(*curve_points_unique), label='Quadratic Bézier Curve', marker='o', markersize=4, linestyle='-', color='blue')
plt.plot(*zip(*control_points), marker='o', markersize=4, linestyle='-', color='red')
plt.scatter(*zip(*control_points), color='red', zorder=5, label='Control Points')
for i, point in enumerate(control_points):
    plt.text(point[0], point[1], f"C{i}: {point}", fontsize=9, verticalalignment='bottom', horizontalalignment='right')


annotation_interval = len(curve_points) // 10 or 1 

for i, point in enumerate(curve_points):
    if i % annotation_interval == 0:
        plt.text(point[0], point[1], f"{point}", fontsize=6, verticalalignment='top')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quadratic Bézier Curve via Divide and Conquer with All Points')
plt.grid(True) 
plt.tight_layout()
plt.show()


