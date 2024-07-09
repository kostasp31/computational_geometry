import numpy as np
from helpFunctions import *
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# kd tree node item
class node:
    def __init__(self, type, L, P):
        self.left = None
        self.right = None
        self.type = type
        self.Range = None
        if self.type == 'l':    # 2 types, one contains the value to seperate
            self.l = L
            self.p = None
        elif self.type == 'n':  # or leaf
            self.l = None
            self.p = P  # contains inly a point
    
    def setR(self, r):  # right child
        self.right = r
   
    def setL(self, l):  # left child
        self.left = l

    def setRange(self, x1, x2, y1, y2):
        self.range = ((x1, x2), (y1, y2))

# for debugging
def print_KDtree(root_P, depth):
    if root_P == None:
        return  
    
    st = ''
    for i in range(0,depth):
        st += '\t'

    if root_P.type == 'l':
        print(st, root_P.type, root_P.l)
    else:
        print(st, root_P.type, root_P.p)

    print_KDtree(root_P.left, depth=depth+1)
    print_KDtree(root_P.right, depth=depth+1)


def create_KDtree(P, depth):
    if len(P) == 1:
        leaf = node('n', None, P[0])
        return leaf
    else:
        # in even depth, divide points by X coordinate
        if depth % 2 == 0:
            P.sort(key=getX)

            median = int(np.ceil(len(P)/2) - 1)
            L = P[median][0]

            # seperate them in 2 subspaces
            P1 = P[:median+1]
            P2 = P[median+1:]
        # in odd depth, divide by Y coordinate
        else:
            P.sort(key=getY)
            
            median = int(np.ceil(len(P)/2) - 1)
            L = P[median][1]

            P1 = P[:median+1]
            P2 = P[median+1:]
        
        N = node('l', L, None)  # create new, non leaf node
        N.setL(create_KDtree(P1, depth+1))  # repeat for children
        N.setR(create_KDtree(P2, depth+1))  
        return N

# return the rectangle region that occurs by splitting in x or y
# the region 'range1' in the line that 'val' creates 
# and keep the left (top for y dimension) or right (bottom for y dimension) area
def intersect(range1, val, where, dimension):
    if where == 'left':
        range2 = (float('-inf'), val)
    else:
        range2 = (val, float('inf'))

    if dimension == 'x':
        inter = ((max(range1[0][0], range2[0]), min(range1[0][1], range2[1])), range1[1])
    else:
        inter = (range1[0], (max(range1[1][0], range2[0]), min(range1[1][1], range2[1])))
    
    return inter

# check if region1 is completely inside region2
def completely_in(region1, region2):
    if region1[0][0] >= region2[0][0] and region1[0][1] <= region2[0][1] and region1[1][0] >= region2[1][0] and region1[1][1] <= region2[1][1]:
        return True
    return False


accepted_points = []
# traverse subtree with 'Node' as root, get to the leaves
# and add points found in these leaves in the accepted point list
def report_subtree(Node):
    if Node.type == 'n':
        accepted_points.append(Node.p)
        return

    report_subtree(Node.left)
    report_subtree(Node.right)    

# search a kd tree for a point and decide if it lays within a range
def search_KDtree(Node, _range, noderange, depth):
    if Node.type == 'n':    # if Node is a leaf
        # keep the point given that it lays inside the _range
        if (Node.p[0] >= _range[0][0] and Node.p[0] <= _range[0][1]) and (Node.p[1] >= _range[1][0] and Node.p[1] <= _range[1][1]):
            accepted_points.append(Node.p)
    else:   # non leaf node
        # calculate the ranges of the 2 children nodes
        if depth%2 == 0:
            noderange_l = intersect(noderange, Node.l, 'left', 'x')
            noderange_r = intersect(noderange, Node.l, 'right', 'x')
        else:
            noderange_l = intersect(noderange, Node.l, 'left', 'y')
            noderange_r = intersect(noderange, Node.l, 'right', 'y')

        # if the region of the left node is completely inside the range, accept all points in subtree
        if completely_in(noderange_l, _range):
            report_subtree(Node.left)
        else:   # else recursively call search
            search_KDtree(Node.left, _range, noderange_l, depth+1)
        # the same for the right child
        if completely_in(noderange_r, _range):
            report_subtree(Node.right)
        else:
            search_KDtree(Node.right, _range, noderange_r, depth+1)

def print_accepted():
    for pt in accepted_points:
        print('[', pt[0], ', ', pt[1], ']')

# create a plot of the points that are accepted or rejected using the kd tree
def print_rect_problem(points, accepted, _range):
    x_vals_discarded = []   # all points not in range
    y_vals_discarded = []
    x_vals_accepted = []    # all points in range
    y_vals_accepted = []
    for itm in points:
        if vecInList(itm, accepted):
            x_vals_accepted.append(itm[0])
            y_vals_accepted.append(itm[1])
        else:
            x_vals_discarded.append(itm[0])
            y_vals_discarded.append(itm[1])

    fig = plt.figure(figsize=(12, 8))
    title = 'Orthogonal Range Search\nRange: x ∈ [%.2f, %.2f]  y ∈ [%.2f %.2f]' % (_range[0][0], _range[0][1], _range[1][0], _range[1][1])
    fig.suptitle(title, fontsize=14)

    ax = fig.add_subplot()
    # draw a rectangle of the acccepted range
    ax.add_patch(Rectangle((_range[0][0], _range[1][0]), _range[0][1] - _range[0][0], _range[1][1] - _range[1][0], facecolor="blue", alpha=0.3))
    # non accepted points are red
    ax.scatter(x_vals_discarded, y_vals_discarded, color='red')
    # accepted points are blue
    ax.scatter(x_vals_accepted, y_vals_accepted, color='green')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')

    plt.grid()
    plt.show()

# get a random range for x and y inside the region defined by barrier
def getRandomRange(barrier=100):
    x = [random.uniform(-barrier, barrier), random.uniform(-barrier, barrier)]
    y = [random.uniform(-barrier, barrier), random.uniform(-barrier, barrier)]
    return ((min(x), max(x)), (min(y), max(y)))