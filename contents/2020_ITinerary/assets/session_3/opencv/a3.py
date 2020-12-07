import math


class Dot:
    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input

    def dot_add(self, other):
        return Dot(self.x + other.x, self.y + other.y)

    def dot_sub(self, other):
        return Dot(self.x - other.x, self.y - other.y)

    def dot_dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot_dist_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def dot_G(self, other1, other2):
        return Dot((self.x + other1.x + other2.x) / 3,
                   (self.y + other1.y + other2.y) / 3)

    def dot_midpoint(self, other):
        return Dot((self.x + other.x) / 2, (self.y + other.y) / 2)

    def dot_get_x(self):
        return self.x

    def dot_get_y(self):
        return self.y

    def dot_get_line(self, other):
        x_same = abs(other.x - self.x) < 0.0001
        y_same =  abs(other.y - self.y) < 0.0001
        if x_same and y_same:
          return "Invaild"
        elif x_same:
          return "x = " + str(self.x)
        elif y_same:
          return "y = " + str(self.y)

        slope = (other.y - self.y) / (other.x - self.x)
        intercept = ((self.x * other.y) - (self.y * other.x)) \
                    / (self.x - other.x)
        return "y = " + str(slope) + "x + " + str(intercept)


a = Dot(1, 2)
b = Dot(2, 3)
