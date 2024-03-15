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
control_points = np.array( [(1, 2), (2, 4), (4, 3), (5, 5),(7,2)], dtype=float)
# Ensure control points are sorted
control_points = control_points[np.argsort(control_points[:, 0])]


depth = 2
curve_points = divide_and_conquer_bezier(control_points, depth, [])
curve_points = np.unique(curve_points, axis=0)  # Remove duplicates

plt.figure(figsize=(10, 6))
plt.plot(curve_points[:,0], curve_points[:,1], label='Quadratic Bézier Curve', marker='o', markersize=4, linestyle='-', color='blue')
plt.plot(control_points[:,0], control_points[:,1], marker='o', markersize=4, linestyle='-', color='red')
plt.scatter(control_points[:,0], control_points[:,1], color='red', zorder=5, label='Control Points')

for i, point in enumerate(control_points):
    plt.text(point[0], point[1], f"C{i}: ({point[0]}, {point[1]})", fontsize=9, verticalalignment='bottom', horizontalalignment='right')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quadratic Bézier Curve via Divide and Conquer with All Points')
plt.tight_layout()
plt.show()
