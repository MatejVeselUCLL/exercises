def closest(points, target_point):
    def distance(a, b):
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        return (dx**2 + dy**2)**0.5

    return min(points, key=lambda point: distance(point, target_point))

# points = [(3, 4), (1, 2), (-5, 0), (-7, -2)]
# print("Expected: (3, 4)\n", "Actual:", closest(points, (5, 5)))