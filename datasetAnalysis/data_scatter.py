import tkinter as tk

import pandas as pd
import matplotlib as mpl
from matplotlib.axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import dataset

class DataScatter:
    root : tk.Tk
    data_set : pd.DataFrame
    graph : Figure
    axis : Axes
    canvas : FigureCanvasTkAgg
    x : int = 0
    y : int = 1

    def __init__(self, root : tk.Tk, data_set : pd.DataFrame) -> None:
        self.root = root
        self.data_set = data_set

        self.root.title("Data Scatter")

        self.graph = Figure(dpi = 100)
        self.canvas = FigureCanvasTkAgg(self.graph, master = root)

        self.axis = self.graph.add_subplot(111)
        self.axis.grid(True)
        self.update_plot()

        self.canvas_widget = self.canvas.get_tk_widget()

        self.left_frame = tk.Frame(self.root)
        self.bottom_frame = tk.Frame(self.root)

        for i in range(self.data_set.shape[1]):
            button_l = tk.Button(self.left_frame, text = self.data_set.columns[i], command = lambda y = i: self.y_column_but(y))
            button_l.pack(padx = 5, pady = 5, fill = 'x')

            button_b = tk.Button(self.bottom_frame, text = self.data_set.columns[i], command = lambda x = i: self.x_column_but(x))
            button_b.pack(side = 'left', padx = 5, pady = 5)


        self.left_frame.grid(row = 0, column = 0, sticky = 'ns')
        self.canvas_widget.grid(row = 0, column = 1, sticky = 'nsew')
        self.bottom_frame.grid(row = 1, column = 1, sticky = 'ew')

        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(1, weight = 1)

        self.root.update_idletasks()
        self.root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())

    def x_column_but(self, x : int) -> None:
        self.set_x(x)
        self.update_plot()

    def y_column_but(self, y : int) -> None:
        self.set_y(y)
        self.update_plot()

    def update_plot(self) -> None:
        self.axis.clear()
        self.axis.plot(self.data_set.iloc[:,self.x].tolist(), self.data_set.iloc[:,self.y].tolist(), marker = '*', linestyle = 'None',
                       color = 'red')
        self.axis.set_xlabel(self.data_set.columns[self.x])
        self.axis.set_ylabel(self.data_set.columns[self.y])
        self.canvas.draw()

    def set_x(self, x : int) -> None:
        self.x = x

    def set_y(self, y : int) -> None:
        self.y = y



if __name__ == "__main__":
    root = tk.Tk()
    app = DataScatter(root, dataset.df)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nProgram stopped by user")