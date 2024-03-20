def distance1(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    return ((dx**2)+(dy**2))**0.5

def distance2(p1, p2):
    return distance1(p1[0], p1[1], p2[0], p2[1])

def distance3(c1, c2):
    d3 = distance2(c1, c2)
    overlap = False
    if d3 <= (c1[2]+c2[2]) :
        overlap = True
    return d3,overlap
def perimeter(points):
    s = 0
    for i in range(len(points)) :
         s += distance2(points[i], points[(i+1)%len(points)])
    return s



exec(input().strip())