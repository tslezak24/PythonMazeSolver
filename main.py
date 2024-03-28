from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    point1 = Point(20, 20)
    point2 = Point(100, 100)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    win.wait_for_close()
    

main()
