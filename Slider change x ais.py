import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


class GraphWithDoubleSlider:
    def __init__(self, root):
        self.root = root
        self.root.title("Double Slider and Graph")

        # Create a figure and a set of subplots
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.25)
        self.ax.set_title("Interactive Graph with Double Slider")

        # Sample data
        self.x = np.linspace(0, 10, 100)
        self.y = np.sin(self.x)
        self.line, = self.ax.plot(self.x, self.y)

        # Vertical bars
        self.vertical_line1 = self.ax.axvline(x=self.x.min(), color='r')
        self.vertical_line2 = self.ax.axvline(x=self.x.max(), color='b')

        # Embed the plot in the tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Slider axes
        slider_ax1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
        slider_ax2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')

        # Sliders
        self.slider1 = Slider(slider_ax1, 'X1', self.x.min(), self.x.max(), valinit=self.x.min())
        self.slider2 = Slider(slider_ax2, 'X2', self.x.min(), self.x.max(), valinit=self.x.max())

        # Update the plot when the sliders' values change
        self.slider1.on_changed(self.update)
        self.slider2.on_changed(self.update)

    def update(self, val):
        x1 = self.slider1.val
        x2 = self.slider2.val
        if x1 > x2:
            x1, x2 = x2, x1  # Ensure x1 is less than x2

        self.vertical_line1.set_xdata([x1])
        self.vertical_line2.set_xdata([x2])

        # Update the plot data
        x = np.linspace(x1, x2, 100)
        y = np.sin(x)
        self.line.set_data(x, y)
        self.ax.set_xlim(x1, x2)
        self.ax.set_ylim(y.min(), y.max())

        self.canvas.draw_idle()


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphWithDoubleSlider(root)
    root.mainloop()
