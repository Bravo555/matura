with open('2016/punkty.txt', 'r') as f:
    data = [tuple(map(int, i.split())) for i in f.readlines()]

def inside_square(point):
    distance_squared = (point[0] - 200)**2 + (point[1] - 200)**2
    return distance_squared < 200 ** 2

inside = []
for point in data:
    if inside_square(point):
        inside.append(point)

print(inside, len(inside))

# 2
def approx_pi(points):
    inside = 0
    for point in points:
        if inside_square(point):
            inside += 1
    return (inside / len(points)) * 4 

print(approx_pi(data[:100]))
print(approx_pi(data[:5000]))
qt314=approx_pi(data)
print(qt314)

# 3
from math import pi
print(abs(pi - qt314))

errors = []
for i in range(1700):
    error = abs(approx_pi(data[:i+1]) - pi)
    errors.append('{} {}\n'.format(i, error))

with open('wyniki_4.txt', 'w') as f:
    f.writelines(errors)