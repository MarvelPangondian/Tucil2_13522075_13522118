
import numpy as np
import matplotlib.pyplot as plt
def linear_interpolate(point1, point2, t):
    return (1 - t) * np.array(point1) + t * np.array(point2)

def brute_force_bezier(points, depth):
    curve_points = []
    for i in range(2 ** depth + 1):
        t = i / (2 ** depth)
        print(t)
        p0_p1 = linear_interpolate(points[0], points[1], t)
        p1_p2 = linear_interpolate(points[1], points[2], t)
        final_point = linear_interpolate(p0_p1, p1_p2, t)
        curve_points.append(final_point)
    return curve_points


control_points = [(1, 2), (3, 5), (6, 2)]  
depth = 3
curve_points = brute_force_bezier(control_points, depth)

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
plt.title('Bézier Curve via Brute Force')
plt.tight_layout()
plt.show()
