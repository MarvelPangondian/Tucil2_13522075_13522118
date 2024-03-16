import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class BezierDnC:
    def __init__(self, control_points, depth):
        self.control_points = control_points
        self.depth = depth
        start_time = time.time()
        self.curve_points, self.intermediates = self.divide_and_conquer_bezier(control_points, depth, [], [])
        self.execution_time = (time.time() - start_time)*1000
        self.curve_points_array = np.array(self.curve_points)
        _, unique_indices = np.unique(self.curve_points_array, axis=0, return_index=True)
        self.curve_points = self.curve_points_array[sorted(unique_indices)]
        self.curve_points_array = np.array(self.curve_points)
        self.fig, self.ax = None,None
        self.texts = []  

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
        self.divide_and_conquer_bezier(np.array(all[0 : (len(all)//2) + 1]), depth - 1, curve_points,intermediates)
        self.divide_and_conquer_bezier(np.array(all[(len(all) // 2) : ]), depth - 1, curve_points,intermediates)
        return curve_points, intermediates
    
    def init_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('Animating Bézier Curve')
        self.ax.plot([point[0] for point in self.control_points], [point[1] for point in self.control_points], marker='o', markersize=4, linestyle='--', color='#8594e4', label='Control Points')

    def update_text_annotations(self, points):
        # Remove old annotations
        for text in self.texts:
            text.remove()
        self.texts.clear()
        
        # Add new annotations for all points
        for point in points:
            self.texts.append(self.ax.text(point[0], point[1], f'({point[0]:.2f}, {point[1]:.2f})', fontsize=6))

    def animate(self):
        self.init_plot()
        curve_plot, = self.ax.plot([], [], '#6643b5', markersize=4,linestyle='-',label = 'Bezier Curve')  # Bézier curve
        intermediate_plots, = self.ax.plot([], [], marker='o', color='#6643b5', linestyle='None', markersize=3)   # Intermediate points
        intermediate_points_accumulated = []

        def init():
            intermediate_plots.set_data([], [])
            curve_plot.set_data([], [])
            return intermediate_plots, curve_plot
        
        def update(frame):
            nonlocal intermediate_points_accumulated
            if frame == total_frames - 1:
                intermediate_points_accumulated = []
                intermediate_plots.set_data([], [])
                curve_plot.set_data([point[0] for point in self.curve_points], [point[1] for point in self.curve_points])
                self.update_text_annotations(self.curve_points)
            elif frame < len(self.intermediates):
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
        animation = FuncAnimation(self.fig, update, frames=total_frames, init_func=init, blit=False, interval=1500, repeat=False)
        plt.text(0.5, 0.01, f'Execution Time: {self.execution_time:.2f} ms', fontsize=10, transform=plt.gcf().transFigure, horizontalalignment='center')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def showGraph(self):
        plt.figure(figsize=(10, 6))
        plt.plot(*zip(*(self.curve_points)), label='Bézier Curve', marker='o', markersize=4, linestyle='-', color='#6643b5')
        plt.plot(*zip(*control_points), marker='o', markersize=4, linestyle='--', color='#8594e4', label='Control Points')
        plt.scatter(*zip(*control_points), color='#8594e4', zorder=5)
        for i, point in enumerate(control_points):
            formatted_point = f"C{i}: ({point[0]:.2f}, {point[1]:.2f})"
            plt.text(point[0], point[1], formatted_point, fontsize=9, verticalalignment='bottom', horizontalalignment='right')
        
        annotation_interval = len(self.curve_points) // 20 or 1# avoid showing too many points
        
        for i, point in enumerate(self.curve_points):
            if (point not in control_points):
                formatted_point = f"({point[0]:.2f}, {point[1]:.2f})"
                plt.text(point[0], point[1], formatted_point, fontsize=6, verticalalignment='top')
        
        all_points = np.concatenate([self.curve_points, control_points])
        x_coords = all_points[:, 0]
        y_coords = all_points[:, 1]
        x_min, x_max = x_coords.min(), x_coords.max()
        y_min, y_max = y_coords.min(), y_coords.max()

        # Adding some margin
        margin_x = (x_max - x_min) * 0.1 
        margin_y = (y_max - y_min) * 0.1

        plt.xlim(x_min - margin_x, x_max + margin_x)
        plt.ylim(y_min - margin_y, y_max + margin_y)
        plt.text(0.5, 0.01, f'Execution Time: {self.execution_time:.2f} ms', fontsize=10, transform=plt.gcf().transFigure, horizontalalignment='center')
        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Bézier Curve via Divide and Conquer')
        plt.grid(True) 
        plt.tight_layout()
        plt.show()
control_points = np.array( [(-2,-3),(-3,-2),(0,-2), (1,-3),(2,1)], dtype=float)
depth = 2
animation = BezierDnC(control_points, depth)

# animation.animate() # to show animation
animation.showGraph() # to show graph
