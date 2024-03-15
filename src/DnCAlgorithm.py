import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class BezierDnC:
    def __init__(self, control_points, depth):
        self.control_points = control_points
        self.depth = depth
        self.curve_points, self.intermediates = self.divide_and_conquer_bezier(control_points, depth, [], [])
        self.curve_points_array = np.array(self.curve_points)
        _, unique_indices = np.unique(self.curve_points_array, axis=0, return_index=True)
        self.curve_points = self.curve_points_array[sorted(unique_indices)]
        self.curve_points_array = np.array(self.curve_points)
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.texts = []  # Initialize text annotations list
        self.init_plot()

    def quadratic_bezier(self, p0, p1, p2, t):
        return (1 - t)**2 * np.array(p0) + 2 * (1 - t) * t * np.array(p1) + t**2 * np.array(p2)

    def divide_and_conquer_bezier(self, points, depth, curve_points=[], intermediates=[]):
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
            if (len(points) == 1):
                final_piece.append(points[0])
            else :
                start_needed.append(temp[0])
                last_needed.insert(0,temp[-1])
        all = []
        all.extend(start_needed)
        all.extend(final_piece)
        all.extend(last_needed)
        intermediates.append(all)
        self.divide_and_conquer_bezier(np.array(all[0 : (len(all)//2) + 1]), depth - 1, curve_points,intermediates)
        self.divide_and_conquer_bezier(np.array(all[(len(all) // 2) : ]), depth - 1, curve_points,intermediates)
        return curve_points, intermediates

    def init_plot(self):
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('Animating Quadratic Bézier Curve Construction')
        self.ax.plot([point[0] for point in self.control_points], [point[1] for point in self.control_points], marker='o', markersize=4, linestyle='-', color='red', label='Control Points')

    def update_text_annotations(self, points):
        # Remove old annotations
        for text in self.texts:
            text.remove()
        self.texts.clear()

        # Add new annotations for all points
        for point in points:
            self.texts.append(self.ax.text(point[0], point[1], f'({point[0]:.2f}, {point[1]:.2f})', fontsize=6))

    def animate(self):
        intermediate_plots, = self.ax.plot([], [], 'bo', markersize=3)  # Intermediate points
        curve_plot, = self.ax.plot([], [], 'b-', markersize=4)  # Bézier curve
        intermediate_points_accumulated = []

        def init():
            intermediate_plots.set_data([], [])
            curve_plot.set_data([], [])
            return intermediate_plots, curve_plot,

        def update(frame):
            nonlocal intermediate_points_accumulated
            if frame < len(self.intermediates):
                points = np.array(self.intermediates[frame]).reshape(-1, 2)
                intermediate_points_accumulated.extend(points)
                xs = [point[0] for point in intermediate_points_accumulated]
                ys = [point[1] for point in intermediate_points_accumulated]
                intermediate_plots.set_data(xs, ys)
                # self.update_text_annotations(intermediate_points_accumulated)
            else:
                curve_frame = frame - len(self.intermediates)
                curve_plot.set_data([point[0] for point in self.curve_points_array[:curve_frame+1]], [point[1] for point in self.curve_points_array[:curve_frame+1]])
                if frame == total_frames - 1:  # Update annotations for the last frame
                    self.update_text_annotations(self.curve_points_array[:curve_frame+1])
            return intermediate_plots, curve_plot,

        total_frames = len(self.intermediates) + len(self.curve_points)
        ani = FuncAnimation(self.fig, update, frames=total_frames, init_func=init, blit=False, interval=500, repeat=False)
        plt.legend()
        plt.tight_layout()
        plt.show()



control_points = np.array( [(-2,-3),(-3,-2),(0,-2), (1,-3),(2,1)], dtype=float)
depth = 3
animation = BezierDnC(control_points, depth)
animation.animate()
