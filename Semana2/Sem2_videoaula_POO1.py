class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get(self):
        return self.x, self.y

    def move(self, offSetX, offSetY):
        self.x += offSetX
        self.y += offSetY

    def reset(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # x + y, se (2,3) + (2,2) = (4,5)
    # x + y, se (2,3) + 8     =(10,11)
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x,
                         self.y + other.y)
        else:
            return Point(self.x + other,
                         self.y + other)
        
