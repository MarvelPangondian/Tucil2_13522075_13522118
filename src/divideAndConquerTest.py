
import numpy as np
import matplotlib.pyplot as plt

def quadratic_bezier(p0, p1, p2, t):
    return (1 - t)**2 * np.array(p0) + 2 * (1 - t) * t * np.array(p1) + t**2 * np.array(p2)

def divide_and_conquer_bezier(points, depth, curve_points=[]):
    if depth == 0:
        curve_points += [quadratic_bezier(*points, t) for t in [0, 1]]
        return curve_points
    mid_p0_p1 = (np.array(points[0]) + np.array(points[1])) / 2
    mid_p1_p2 = (np.array(points[1]) + np.array(points[2])) / 2
    mid_curve = quadratic_bezier(*points, 0.5)
    divide_and_conquer_bezier([points[0], mid_p0_p1, mid_curve], depth - 1, curve_points)
    divide_and_conquer_bezier([mid_curve, mid_p1_p2, points[2]], depth - 1, curve_points)
    return curve_points

control_points = [(1, 2), (3, 5), (6, 2)] # example of control points
control_points = sorted(control_points, key=lambda point: point[0]) # sort them
depth =  1 # something is wrong with depth 1
curve_points = divide_and_conquer_bezier(control_points, depth, [])
curve_points = np.unique(curve_points, axis=0)  # Remove duplicates if needed

plt.figure(figsize=(10, 6))
plt.plot(*zip(*curve_points), label='Quadratic Bézier Curve', marker='o', markersize=4, linestyle='-', color='blue')
plt.plot(*zip(*control_points), marker='o', markersize=4, linestyle='-', color='red')
plt.scatter(*zip(*control_points), color='red', zorder=5, label='Control Points')

for i, point in enumerate(control_points):
    plt.text(point[0], point[1], f"C{i}: {point}", fontsize=9, verticalalignment='bottom', horizontalalignment='right')

# Adjusted annotation logic
annotation_interval = len(curve_points) // 10 or 1  # Avoid division by zero

for i, point in enumerate(curve_points):
    if i % annotation_interval == 0:
        plt.text(point[0], point[1], f"{point}", fontsize=6, verticalalignment='top')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Quadratic Bézier Curve via Divide and Conquer with All Points')
plt.tight_layout()
plt.show()
