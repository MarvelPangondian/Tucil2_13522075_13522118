
import numpy as np
import matplotlib.pyplot as plt
import time
def linear_interpolate(point1, point2, t):
    return (1 - t) * np.array(point1) + t * np.array(point2)

def brute_force_bezier(points, depth):
    curve_points = []
    for i in range(2 ** depth + 1):
        t = i / (2 ** depth)
        p0_p1 = linear_interpolate(points[0], points[1], t)
        p1_p2 = linear_interpolate(points[1], points[2], t)
        final_point = linear_interpolate(p0_p1, p1_p2, t)
        curve_points.append(final_point)
    return curve_points

def showGraphBF(control_points, depth):
    start_time = time.time()  # Start timing
    curve_points = brute_force_bezier(control_points, depth)
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
    
    annotation_interval = len(curve_points) // 10 or 1 

    for i, point in enumerate(curve_points):
        if (i % annotation_interval == 0):
            is_control_point = any(np.array_equal(point, cp) for cp in control_points)
            if not is_control_point:
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
    plt.title('Bézier Curve via Brute Force')
    plt.grid(True) 
    plt.tight_layout()
    plt.show()


control_points = [(-2,-3),(-3,-2),(0,-2)]  
depth = 3
showGraphBF(control_points,depth)

