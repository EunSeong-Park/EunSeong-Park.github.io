# example@gmail.com
import math

class Dot:
    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input
    def dot_get_x(self):
        return self.x
    def dot_get_y(self):
        return self.y
    def dot_add(self, other):
        # return (x, y) = (x1 + x2, y1 + y2) (Dot)
        return Dot(self.x + other.x, self.y + other.y)
    def dot_sub(self, other):
        # return (x, y) = (x1 - x2, y1 - y2) (Dot)
        return Dot(self.x - other.x, self.y - other.y)
    def dot_dist_origin(self):
        # return the distance from the origin (0,0) (number)
        # (1, 1) -> 1.414....
        # sqrt((x1-0)**2 + (y1-0)**2)
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def dot_dist(self, other):
        # return the distance between the two points (number)
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    def dot_midpoint(self, other):
        # return the midpoint between the two points (Dot)
        # x_new = (x1 + x2) / 2, y_new = (y1 + y2) / 2
        return Dot((self.x + other.x) / 2, (self.y + other.y) / 2)
    def dot_get_line(self, other):
        # return the linear function passes through the two points (string)
        # Ex 1: y = 12x + 5
        # Ex 2: y = 3 (if the line is parallel to x-axis)
        # Ex 3: x = 15 (if the line is parallel to y-axis)
        # Ex 4: Invalid (if the two points are in the same position)
        x_same = self.x == other.x
        y_same = self.y == other.y

        # (1, 1) (0, 1) y = 1

        if x_same and y_same: # (x1, y1) = (x1, y1)
            return "Invalid"
        elif y_same: # parallel to x-axis
            return "y = " + str(self.y)
        elif x_same: # parallel to y-axis
            return "x = " + str(self.x)

        # y = ax + b
        slope = (self.y - other.y) / (self.x - other.x)
        intercept = ((self.x * other.y) - (self.y * other.x)) / (self.x - other.x)# (x1*y2 - y1*x1) / (x1 - x2)

        return "y = " + str(slope) + "x + " + str(intercept)

    def dot_G(self, other1, other2):
        # return the "center of mass" (Dot)
        # for x_1, y_1) x_2, y_2), x_3, y_3)
        # G = (x_1 + x_2 + x_3) / 3 , (y_1 + y_2+ y_3) / 3
        return Dot((self.x + other1.x + other2.x) / 3,
                   (self.y + other1.y + other2.y) / 3)

a = Dot(1, 1)
b = Dot(0, 0)
c = Dot(1, 2)
print(a.dot_get_x())
print(a.dot_get_line(b))
print(b.dot_get_line(c))

