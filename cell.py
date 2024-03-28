from point import Point
from line import Line


class Cell:
    def __init__(self, win):
        self.has_left_wall = True 
        self.has_right_wall= True 
        self.has_top_wall = True 
        self.has_bottom_wall = True
        self._x1 = None 
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            left_point1 = Point(x1, y1)
            left_point2 = Point(x1, y2)
            left_line = Line(left_point1, left_point2)
            self._win.draw_line(left_line)
        if self.has_right_wall:
            right_point1 = Point(x1, y1)
            right_point2 = Point(x2, y1)
            right_line = Line(right_point1, right_point2)
            self._win.draw_line(right_line)
        if self.has_top_wall:
            top_point1 = Point(x2, y1)
            top_point2 = Point(x2, y2)
            top_line = Line(top_point1, top_point2)
            self._win.draw_line(top_line)
        if self.has_bottom_wall:
            btm_point1 = Point(x1, y2)
            btm_point2 = Point(x2, y2)
            btm_line = Line(btm_point1, btm_point2)
            self._win.draw_line(btm_line)