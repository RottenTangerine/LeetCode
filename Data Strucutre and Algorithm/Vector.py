class Vec:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __eq__(self, other):
        return self.x ==  other.x and self.y == other.y

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __abs__(self):
        return self.dot(self) ** 0.5

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

if __name__ == '__main__':
    # compute the area of △APB
    P = Vec(1, 2)
    A = Vec(2, 5)
    B = Vec(-1, 7)

    print(repr(A))

    a, b = A - P, B - P
    print(a, b)
    print((a.dot(a) * b.dot(b) - a.dot(b) ** 2) ** 0.5 / 2)

    # comute the length of vector KQ
    Q = Vec(3, 5)
    K = Vec(10, 7)
    print(abs(Q - K))