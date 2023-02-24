import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'{self.x},{self.y}'

    def __lt__(self, other):
        if self.x < other.x:
            return True

        return self.x == other.x and self.y < other.y

'''
class LineSegment:
    def __init__(self, a, b):
        if b < a:
            self.a = b
            self.b = a
        else:
            self.a = a
            self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        return f'{self.a}  {self.b}'

    def point_position(self, point):
        # code from https://stackoverflow.com/questions/1560492/how-to-tell-whether-a-point-is-to-the-right-or-left-side-of-a-line
        a = self.a
        b = self.b

        position = (b.x - a.x) * (point.y - a.y) - (b.y - a.y) * (point.x - a.x)
        if position < 0:
            return -1
        if position > 0:
            return 1
        return 0

def generate_points():
    points = []
    random.seed(a=1)
    for i in range(5):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        point = Point(x, y)
        if point not in points:
            points.append(point)

    return points

def brute_force(points):

    hulls = []

    for i, pointI in enumerate(points):
        foundConvexHull = True
        for j, pointJ in enumerate(points):
            if not foundConvexHull:
                break
            if i != j:
                line = LineSegment(pointI, pointJ)
                prev_position = None

                for k, pointK in enumerate(points):
                    if not foundConvexHull:
                        break
                    if k != i and k != j:
                        position = line.point_position(pointK)
                        if prev_position is None:
                            prev_position = position
                        else:
                            if position != prev_position:
                                foundConvexHull = False
                                break
                if foundConvexHull and line not in hulls:
                    hulls.append(line)

    return hulls
'''

#code from https://www.geeksforgeeks.org/convex-hull-using-divide-and-conquer-algorithm/
def brute2(points):
    convexHulls = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1 = points[i].x
            x2 = points[j].x
            y1 = points[i].y
            y2 = points[j].y

            a1 = y1 - y2
            b1 = x2 - x1
            c1 = x1 * y2 - y1 * x2

            positive = 0
            negative = 0

            for k in range(len(points)):
                value = a1 * points[k].x + b1 * points[k].y + c1
                if value <= 0:
                    negative += 1
                else:
                    positive += 1

            if positive == len(points) or negative == len(points):
#                convexHulls.append(LineSegment(points[i], points[j]))
                convexHulls.append(points[i])
                convexHulls.append(points[j])

    return convexHulls

def orientation(a, b, c):
    o = (b.y - a.y) * (c.x - b.x) - (c.y - b.y) * (b.x - a.x)

    if o == 0:
        return 0
    if o > 0:
        return 1
    return -1

def merge(a, b):
    n1 = len(a)
    n2 = len(b)

    ia = 0
    ib = 0
    
    for i in range(1, len(a)):
        if a[i].x > a[ia].x:
            ia = i

    for i in range(1, len(b)):
        if b[i].x < b[ib].x:
            ib = i

    #finding uppoer tangent
    inda = ia
    indb = ib
    done = False
    while not done:
        done = True
        while orientation(b[indb], a[inda], a[(inda + 1) % n1]) >= 0:
            inda = (inda + 1) % n1

        while orientation(a[inda], b[indb], b[(n2 + indb - 1) % n2]) <= 0:
            indb = (n2 + indb - 1) % n2
            done = False

    uppera = inda
    upperb = indb
    inda = ia
    indb = ib
    done = False
    g = 0
    # finding the lower tangent
    while not done:
        done = True
        while orientation(a[inda], b[indb], b[(indb + 1) % n2]) >= 0:
            indb = (indb + 1) % n2

        while orientation(b[indb], a[inda], a[(n1 + inda - 1) % n1]) <= 0:
            inda = (n1 + inda - 1) % n1
            done = False

    lowera = inda
    lowerb = indb
    result = []

    ind = uppera
    result.append(a[uppera])
    while ind != lowera:
        ind = (ind + 1) % n1
        result.append(a[ind])

    ind = lowerb
    result.append(b[lowerb])
    while ind != upperb:
        ind = (ind + 1) % n2
        result.append(b[ind])

    return result

def divide(points):
    if len(points) <= 5:
        return brute2(points)

    left = []
    right = []

    i = 0
    while i < len(points) / 2:
        left.append(points[i])
        i += 1

    while i < len(points):
        right.append(points[i])
        i += 1

    leftHull = divide(left)
    rightHull = divide(right)

    return merge(leftHull, rightHull)



points = [Point(0,0), Point(0, 4), Point(-4, 0), Point(5, 0), Point(0, -6), Point(1, 0)]
#points = generate_points()
sortedPoints = sorted(points)
for point in sortedPoints:
    print(point)
#for line in brute_force(sortedPoints):
#    print(line)
print()
print()
for line in brute2(sortedPoints):
    print(line)
print()
print()
for line in divide(sortedPoints):
    print(line)
