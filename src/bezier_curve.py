import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from brute_force_bezier import brute_force_bezier
from dnc_bezier import divide_and_conquer_bezier
from math import ceil as ceil
class BezierDnC:
    def __init__(self, control_points, depth, method):
        self.control_points = control_points
        self.depth = depth
        self.method = method
        start_time = time.time()
        if method == 1 : 
            self.curve_points, self.intermediates = divide_and_conquer_bezier(control_points, depth, [], [])
        else : 
            self.curve_points = brute_force_bezier(control_points, depth)
        self.execution_time = (time.time() - start_time)*1000
        self.curve_points_array = np.array(self.curve_points)
        temp_start = self.curve_points_array[0] # avoid removing duplicate ends of control points
        temp_end = self.curve_points_array[-1]
        self.curve_points_array = self.curve_points_array[1:-1]
        _, unique_indices = np.unique(self.curve_points_array, axis=0, return_index=True)
        self.curve_points = self.curve_points_array[sorted(unique_indices)]
        if (temp_start.any() and temp_end.any()) :
            self.curve_points = np.insert(self.curve_points,0,temp_start,axis=0)
            self.curve_points = np.append(self.curve_points,[temp_end],axis=0)
        self.curve_points_array = np.array(self.curve_points)
        self.fig, self.ax = None,None
        self.texts = []  
        self.interval_points = 1
        if self.depth > 5 :
            self.interval_points = ceil( ( (2**self.depth) + 1 ) / 33 )
            pass

    def init_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('Animating Bézier Curve')
        self.ax.plot([point[0] for point in self.control_points], [point[1] for point in self.control_points], marker='o', markersize=4, linestyle='--', color='#8594e4', label='Control Points')
        for i, point in enumerate(self.control_points):
            formatted_point = f"C{i}: ({point[0]:.2f}, {point[1]:.2f})"
            plt.text(point[0], point[1], formatted_point, fontsize=9, verticalalignment='bottom', horizontalalignment='right')      
    
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
                intermediate_plots.set_data([point[0] for point in self.curve_points if point not in self.control_points], [point[1] for point in self.curve_points if point not in self.control_points])
                curve_plot.set_data([point[0] for point in self.curve_points], [point[1] for point in self.curve_points])
                count = 0
                points_last_frame = []
                for points in self.curve_points:
                    if points not in self.control_points:
                        count += 1
                        if (count % self.interval_points == 0):
                            points_last_frame.append(points)
                
                self.update_text_annotations(points_last_frame)
            elif frame < len(self.intermediates):
                points = np.array(self.intermediates[frame]).reshape(-1, 2)
                intermediate_points_accumulated.extend(points)
                xs = [point[0] for point in intermediate_points_accumulated]
                ys = [point[1] for point in intermediate_points_accumulated]
                intermediate_plots.set_data(xs, ys)
            else:
                curve_frame = frame - len(self.intermediates)
                curve_plot.set_data([point[0] for point in self.curve_points_array[:curve_frame+1]], [point[1] for point in self.curve_points_array[:curve_frame+1]])
            return intermediate_plots, curve_plot,
    
        total_frames = len(self.intermediates) + len(self.curve_points)
        interval = 1500
        if (self.depth > 5 and self.depth < 10):
            interval = 1000
        elif (self.depth >= 10):
            interval = 500
        animation = FuncAnimation(self.fig, update, frames=total_frames, init_func=init, blit=False, interval=interval, repeat=False)
        plt.text(0.5, 0.01, f'Execution Time: {self.execution_time:.2f} ms', fontsize=10, transform=plt.gcf().transFigure, horizontalalignment='center')
        plt.legend()
        plt.grid(True) 
        plt.tight_layout()
        plt.show()
        
    def showGraph(self):
        self.fig = plt.figure(figsize=(10, 6))
        plt.plot(*zip(*(self.curve_points)), label='Bézier Curve', marker='o', markersize=4, linestyle='-', color='#6643b5')
        plt.plot(*zip(*(self.control_points)), marker='o', markersize=4, linestyle='--', color='#8594e4', label='Control Points')
        plt.scatter(*zip(*(self.control_points)), color='#8594e4', zorder=5)
        for i, point in enumerate(self.control_points):
            formatted_point = f"C{i}: ({point[0]:.2f}, {point[1]:.2f})"
            plt.text(point[0], point[1], formatted_point, fontsize=9, verticalalignment='bottom', horizontalalignment='right')
        
        # annotation_interval = len(self.curve_points) // 20 or 1# avoid showing too many points
        count = 0
        for i, point in enumerate(self.curve_points):
            if (point not in self.control_points):
                count += 1
                if (count % self.interval_points == 0):
                    formatted_point = f"({point[0]:.2f}, {point[1]:.2f})"
                    plt.text(point[0], point[1], formatted_point, fontsize=6, verticalalignment='top')
        
        all_points = np.concatenate([self.curve_points, self.control_points])
        x_coords = all_points[:, 0]
        y_coords = all_points[:, 1]
        x_min, x_max = x_coords.min(), x_coords.max()
        y_min, y_max = y_coords.min(), y_coords.max()

        # Adding some margin
        margin_x = (x_max - x_min) * 0.1 
        margin_y = (y_max - y_min) * 0.1

        graph_title = "Bézier Curve via Divide and Conquer"
        if (self.method == 2):
            graph_title = "Bézier Curve via Brute Force"
        plt.xlim(x_min - margin_x, x_max + margin_x)
        plt.ylim(y_min - margin_y, y_max + margin_y)
        plt.text(0.5, 0.01, f'Execution Time: {self.execution_time:.2f} ms', fontsize=10, transform=plt.gcf().transFigure, horizontalalignment='center')
        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(graph_title)
        plt.grid(True) 
        plt.tight_layout()
        plt.show()
