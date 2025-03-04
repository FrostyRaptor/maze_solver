from windowClass import Window
from pointClass import Line, Point

def main():
    window = Window(800, 600)
    line = Line(Point(50,50), Point(400,400))
    window.draw_line(line)
    window.wait_for_close()

if __name__ == "__main__":
    main()