"""
    This the main entry of the GUI layer for StockMate application
"""
import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import stockdata as sd

def draw_graph(stockNum):
    """
    Display stock curve in the graph
    """

    # clear the curent axis(instead of the parent figure) before drawing new data
    graph.figure.ax1.cla()
    try:
        print("loading data for stock:{0}".format(stockNum))
        dataframe = sd.getYearlyCloseData(stockNum)
        # plot into the embedded axis instead of popping up a standalone dialog
        # dataFrame.show()
        dataframe.plot(legend=True, ax=graph.figure.ax1, title = "YearlyCloseCurve:{0}".\
            format(stockNum), grid = "on", color = ['blue','gold'])
        graph.figure.ax1.set_xlabel("Over a year")
    except Exception as ex:
        print("Caught exception:{0}.".format(str(ex)))

    graph.canvas.show()
    print("done drawing")


if __name__ == "__main__":
    # create and configure root to be fit the resizing window
    root=tk.Tk()
    # Be noticed that for making widgets automatically fit the window, we must:
    # 1. configure the weight on the container grid cell 
        # configure the grid rows and columns within which the widget instance is placed to have a non-zero 
        # weight so that they will take up the extra space
    # 2. configure the sticky attribute on the widget instance so that they will expand to fill the grid cell
    # The tk.Grid.grid(instPath,**options) function is equal to instPath.grid(**options)

    # First create the toolbar and graph frames on root
    toolbar = tk.Frame(root, height=30)
    toolbar.grid(row = 0, sticky=tk.N+tk.E+tk.W)
    graph=tk.Frame(root, bg="blue")
    # make graph frame fit the vertical resizing
    graph.grid(row = 1, sticky=tk.N+tk.S+tk.E+tk.W)
    root.rowconfigure(1, weight=1)
    # make both toolbar and graph frames fit the horizontal resizing
    root.columnconfigure(0, weight=1)
    
    # Then create label and buttons on toolbar
    label = tk.Label(toolbar,text='请输入股票代码：')
    label.grid(row=0, column=0, sticky=tk.W)
    inputEntry = tk.Entry(toolbar)
    inputEntry.grid(row=0, column=1,sticky=tk.W+tk.E)
    # make inputEntry fit the horizontal resizing
    toolbar.columnconfigure(1, weight=1)
    inputEntry.insert(0,"300104")
    # use lamda to wrap the callback method with arguments, otherwise the callback will be evaluated 
    # immediately and its return value will be set to the command attribute, in a result button click
    # would not behave.
    btn1 = tk.Button(toolbar,text='收盘趋势线', command = lambda:draw_graph(inputEntry.get()))
    btn1.grid(row=0, column=2, sticky=tk.E)
    
    # create canvas on graph for displaying the figure
    matplotlib.use("TkAgg")
    graph.figure = Figure(figsize=(5, 4))
    # a figure can contain several axes, here we just create one for displaying the curve
    graph.figure.ax1 = graph.figure.add_subplot(111)
    graph.canvas = FigureCanvasTkAgg(graph.figure, master = graph)
    graph.canvas.show()
    # expand canvas in both directions to fill the graph
    graph.canvas.get_tk_widget().grid(row = 0, column = 0, sticky = tk.W+tk.E+tk.N+tk.S)
    graph.rowconfigure(0, weight = 1)
    graph.columnconfigure(0, weight = 1)
    
    # start event pump
    root.mainloop()
