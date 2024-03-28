from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    new_cell = Cell(win)
    new_cell.draw(20,20,50,50)
    win.wait_for_close()
    

main()
