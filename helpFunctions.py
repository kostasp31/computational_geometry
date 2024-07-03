import scipy
import numpy as np
import random
import math
import numpy.linalg

def complists(l1, l2):
    ll = len(l1)
    if (ll != len(l2)):
        return False
    for i in range(0, ll):
        if not np.array_equal(l1[i], l2[i]):
            return False
    return True

# Calculate the orientation of 3 points in 2D
# Returns 1 if positive, -1 if negative and 0 if the points tn the same line
def CCW(p0, p1, p2):
    mat = np.ones((3,3), dtype=float)
    mat[0][1] = p0[0]
    mat[0][2] = p0[1]
    mat[1][1] = p1[0]
    mat[1][2] = p1[1]
    mat[2][1] = p2[0]
    mat[2][2] = p2[1]
    det_ = np.linalg.det(mat)
    if (det_ > 0):
        return 1
    elif (det_ < 0):
        return -1
    else: 
        return 0


# 1   x0  y0  z0
# 1   x1  y1  z1
# 1   x2  y2  z2
# 1   x3  y3  z3

def CCW_3d(p0, p1, p2, p3):
    mat = np.ones((4,4), dtype=float)
    mat[0][1] = p0[0]
    mat[0][2] = p0[1]
    mat[0][3] = p0[2]
    mat[1][1] = p1[0]
    mat[1][2] = p1[1]
    mat[1][3] = p1[2]
    mat[2][1] = p2[0]
    mat[2][2] = p2[1]
    mat[2][3] = p2[2]
    mat[3][1] = p3[0]
    mat[3][2] = p3[1]
    mat[3][3] = p3[2]

    det_ = np.linalg.det(mat)
    # print(mat)
    # print(det_)
    if (det_ > 0):
        return 1
    elif (det_ < 0):
        return -1
    else: 
        return 0

# return the X of a nparray (point)
def getX(nparray):
    return nparray[0]

def getY(nparray):
    return nparray[0]

def dist(a, b):
    d = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return d

def minKey(point):
    x = point[0]
    y = point[1]
    return (x,y)

def vecInList(v, li):
    for itm in li:
        if np.array_equal(v,itm):
            return True
    return False

def remVec(v, li):
    for i in range(0, len(li)):
        if np.array_equal(v,li[i]):
            del li[i]
            break

def getNext(i, points):
    l = len(points)
    if i+1 >= l:
        return 0
    else:
        return i+1

def getPrev(i, points):
    l = len(points)
    if i-1 < 0:
        return l-1
    else:
        return i-1
    
def getDiffPoint(points, p1, p2):
    for p in range(0, len(points)):
        if np.array_equal(points[p], p1) or np.array_equal(points[p], p2):
            continue
        else:
            return p

def getIndexOfRightmost(H):
    rightMost = 0
    for i in range(0, len(H)):
        if H[i][0] > H[rightMost][0]:
            rightMost = i
    return rightMost


# distance of c from line that a,b define
def distFromLine(a, b, c):
    return np.linalg.norm(np.cross(b-a, a-c))/np.linalg.norm(b-a)

def printHull(L, point_list, title):
    import matplotlib.pyplot as plt 
    x1 = []
    y1 = []
    for itm in point_list:
        x1.append(itm[0])
        y1.append(itm[1])

    x2 = []
    y2 = []
    for itm in L:
        x2.append(itm[0])
        y2.append(itm[1])

    fig, ax = plt.subplots(1, 1, constrained_layout=True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.plot(x1,y1,'o', color='red')
    fig.suptitle(title, fontsize=14)
    plt.plot(x2,y2,'o', color='red')
    for i in range(0, len(x2), 2):
        plt.plot(x2[i:i+2], y2[i:i+2], 'blue')
    for i in range(1, len(x2), 2):
        plt.plot(x2[i:i+2], y2[i:i+2], 'blue')

    x = np.array([x2[0], x2[-1]])
    y = np.array([y2[0], y2[-1]])
    plt.plot(x, y, 'blue')
    plt.show()

def genRandompoints(count, _range, _seed, method='circle'):
    p_list = []
    if _seed:
        random.seed(_seed)
    if method=='circle':
        # radius of the circle
        circle_r = _range
        circle_x = 0
        circle_y = 0
        for i in range(0,count):
            # random angle
            alpha = 2 * math.pi * random.random()
            # random radius
            r = circle_r * math.sqrt(random.random())
            p_list.append(np.array([r * math.cos(alpha) + circle_x, r * math.sin(alpha) + circle_y]))
    elif method=='rect':
        for i in range(0,count):
            p_list.append(np.array([random.uniform(-_range, _range), random.uniform(-_range, _range)]))
    return p_list

def getRandompoints_3d(count, _range, _seed, method='circle'):
    p_list = []
    if _seed:
        random.seed(_seed)

    if method == 'circle':
        circle_r = _range
        circle_x = 0
        circle_y = 0
        for i in range(0,count):
            # random angle
            alpha = 2 * math.pi * random.random()
            beta = 2 * math.pi * random.random()
            # random radius
            r = circle_r * math.sqrt(random.random())
            d_2 = np.array([r * math.cos(alpha) + circle_x, r * math.sin(alpha) + circle_y, 0])
        
            rotation_axis = np.array([1, 1, 0])     # z
            rotation_vector = beta * rotation_axis
            rotation = scipy.spatial.transform.Rotation.from_rotvec(rotation_vector)
            rotated_vector = rotation.apply(d_2)
            p_list.append(rotated_vector)
    elif method=='rect':
        for i in range(0,count):
            p_list.append(np.array([random.uniform(-_range, _range), random.uniform(-_range, _range), random.uniform(-_range, _range)]))
    return p_list


def print_edge(e):
    print("{:10.4f}".format(e.p1[0]), '\t', "{:10.4f}".format(e.p2[0]))
    print("{:10.4f}".format(e.p1[1]), '  -->', "{:10.4f}".format(e.p2[1]))
    print("{:10.4f}".format(e.p1[2]), '\t', "{:10.4f}".format(e.p2[2]))
    print('\n')

class edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.visited = False

def edgeInList(e, li):
    for itm in li:
        if (np.array_equal(e.p1, itm.p1) and np.array_equal(e.p2, itm.p2)):
            return True
    return False

def equalEdges(e1, e2):
    if (np.array_equal(e1.p1, e2.p1) and np.array_equal(e1.p2, e2.p2)) or (np.array_equal(e1.p1, e2.p2) and np.array_equal(e1.p2, e2.p1)):
        return True   
    else:
        return False
    
def graphicalTriangle(p1, p2, p3):
    x = [p1[0], p2[0], p3[0]]
    y = [p1[1], p2[1], p3[1]]
    z = [p1[2], p2[2], p3[2]]
    poly3d = [list(zip(x,y,z))]
    return poly3d

def graphicalTriangle_2d(p1, p2, p3):
    x = [p1[0], p2[0], p3[0]]
    y = [p1[1], p2[1], p3[1]]
    z = [0, 0, 0]
    poly3d = [list(zip(x,y,z))]
    return poly3d

def removeDupFromList(li):
    for item in li:
        for itm in li.remove(item):
            if np.array_equal(item, itm):
                continue

def hull_3d_print(p_list, hull):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')

    x_vals = []
    y_vals = []
    z_vals = []
    for itm in p_list:
        x_vals.append(itm[0])
        y_vals.append(itm[1])
        z_vals.append(itm[2])

    ax.scatter(x_vals, y_vals, z_vals, 'green')

    #plot the xy plane
    # x = np.outer(np.linspace(-100, 100, 32), np.ones(32))
    # y = x.copy().T # transpose
    # z = (np.outer(np.linspace(-100, 100, 32), np.zeros(32)))
    # ax.plot_surface(x,y,z, alpha=0.2)

    for tri in hull:
        triangle = graphicalTriangle(tri[0], tri[1], tri[2])

        i = random.randint(0,3)
        if i==0:
            c = 'red'
        elif i==1:
            c = 'blue'
        else:
            c = 'green'
        t = ax.add_collection3d(Poly3DCollection(triangle, facecolors=c, linewidths=1, alpha=0.5))
        t.set_edgecolor('k')
        fig.canvas.draw()  
        plt.pause(0.1)

    plt.show()


# def get_lower_hull_3d(hull_2d):
#     hull_2d_down = []
#     for tri in hull_2d:
#         Dir = np.cross((tri[1] - tri[0]),(tri[2] - tri[0]))
#         if Dir > 0:
#             hull_2d_down.append(tri)