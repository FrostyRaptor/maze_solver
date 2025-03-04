from tkinter import Tk, BOTH, Canvas
from pointClass import Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="black", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def draw_line(self, ln, fill_color="red"):
        ln.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Closed the window")
    
    def close(self):
        self.__running = False