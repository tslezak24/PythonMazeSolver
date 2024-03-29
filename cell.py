from point import Point
from line import Line


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True 
        self.has_right_wall= True 
        self.has_top_wall = True 
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None 
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_start = (self._x1 + self._x2) / 2
        y_start = (self._y1 + self._y2) / 2
        x_end = (to_cell._x1 + to_cell._x2) / 2
        y_end = (to_cell._y1 + to_cell._y2) / 2
        color = "red"
        if undo:
            color = "gray"
        
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_start), Point(x_start, y_start))
            self._win.draw_line(line, color)
            line = Line(Point(x_end, y_end), Point(to_cell._x2, y_end))
            self._win.draw_line(line, color)
            
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_start, y_start), Point(self._x2, y_start))
            self._win.draw_line(line, color)
            line = Line(Point(to_cell._x1, y_end), Point(x_end, y_end))
            self._win.draw_line(line, color)
            
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_start, y_start), Point(x_start, self._y1))
            self._win.draw_line(line, color)
            line = Line(Point(x_end, to_cell._y2), Point(x_end, y_end))
            self._win.draw_line(line, color)
            
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_start, y_start), Point(x_start, self._y2))
            self._win.draw_line(line, color)
            line = Line(Point(x_end, y_end), Point(x_end, to_cell._y1))
            self._win.draw_line(line, color)