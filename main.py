import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


class GraphWithDoubleSlider:
    def __init__(self, root):
        self.root = root
        self.root.title("Double Slider and Graphs")

        # Create the first figure and set of subplots for vertical bars
        self.fig1, self.ax1 = plt.subplots()
        plt.subplots_adjust(bottom=0.25)
        self.ax1.set_title("Interactive Graph with Double Vertical Slider")

        # Sample data
        self.x = np.linspace(0, 10, 100)
        self.y = np.sin(self.x)
        self.line1, = self.ax1.plot(self.x, self.y)

        # Vertical bars
        self.vertical_line1 = self.ax1.axvline(x=self.x.min(), color='r')
        self.vertical_line2 = self.ax1.axvline(x=self.x.max(), color='b')

        # Embed the first plot in the tkinter window
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.root)
        self.canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Slider axes for the first graph
        slider_ax1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
        slider_ax2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')

        # Sliders for the first graph
        self.slider1 = Slider(slider_ax1, 'X1', self.x.min(), self.x.max(), valinit=self.x.min())
        self.slider2 = Slider(slider_ax2, 'X2', self.x.min(), self.x.max(), valinit=self.x.max())

        # Update the plot when the sliders' values change
        self.slider1.on_changed(self.update1)
        self.slider2.on_changed(self.update2)

        # Create the second figure and set of subplots for horizontal bars
        self.fig2, self.ax2 = plt.subplots()
        plt.subplots_adjust(bottom=0.25)
        self.ax2.set_title("Interactive Graph with Double Horizontal Slider")

        # Same sample data for the second graph
        self.line2, = self.ax2.plot(self.x, self.y)

        # Horizontal bars
        self.horizontal_line1 = self.ax2.axhline(y=self.y.min(), color='r')
        self.horizontal_line2 = self.ax2.axhline(y=self.y.max(), color='b')

        # Embed the second plot in the tkinter window
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.root)
        self.canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Sliders for the second graph are the same as the first
        self.slider1.on_changed(self.update_horizontal1)
        self.slider2.on_changed(self.update_horizontal2)

    def update1(self, val):
        val = float(val)
        self.vertical_line1.set_xdata([val])
        self.canvas1.draw_idle()

    def update2(self, val):
        val = float(val)
        self.vertical_line2.set_xdata([val])
        self.canvas1.draw_idle()

    def update_horizontal1(self, val):
        val = float(val)
        y_val = np.interp(val, self.x, self.y)
        self.horizontal_line1.set_ydata([y_val])
        self.canvas2.draw_idle()

    def update_horizontal2(self, val):
        val = float(val)
        y_val = np.interp(val, self.x, self.y)
        self.horizontal_line2.set_ydata([y_val])
        self.canvas2.draw_idle()


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphWithDoubleSlider(root)
    root.mainloop()
