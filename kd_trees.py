import numpy as np
from helpFunctions import *
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class node:
    def __init__(self, type, L, P):
        self.left = None
        self.right = None
        self.type = type
        self.Range = None
        if self.type == 'l':
            self.l = L
            self.p = None
        elif self.type == 'n':
            self.l = None
            self.p = P
    
    def setR(self, r):
        self.right = r
   
    def setL(self, l):
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
        if depth % 2 == 0:
            P.sort(key=getX)

            median = int(np.ceil(len(P)/2) - 1)
            L = P[median][0]

            P1 = P[:median+1]
            P2 = P[median+1:]

        else:
            P.sort(key=getY)
            
            median = int(np.ceil(len(P)/2) - 1)
            L = P[median][1]

            P1 = P[:median+1]
            P2 = P[median+1:]
        
        N = node('l', L, None)
        N.setL(create_KDtree(P1, depth+1))
        N.setR(create_KDtree(P2, depth+1))

        return N

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
def report_subtree(Node):
    if Node.type == 'n':
        accepted_points.append(Node.p)
        # print(Node.p)
        return

    report_subtree(Node.left)
    report_subtree(Node.right)    

def search_KDtree(Node, _range, noderange, depth):
    if Node.type == 'n':    # root is a leaf
        if (Node.p[0] >= _range[0][0] and Node.p[0] <= _range[0][1]) and (Node.p[1] >= _range[1][0] and Node.p[1] <= _range[1][1]):
            # print(Node.p)
            accepted_points.append(Node.p)
    else:
        if depth%2 == 0:
            noderange_l = intersect(noderange, Node.l, 'left', 'x')
            noderange_r = intersect(noderange, Node.l, 'right', 'x')
        else:
            noderange_l = intersect(noderange, Node.l, 'left', 'y')
            noderange_r = intersect(noderange, Node.l, 'right', 'y')

        if completely_in(noderange_l, _range):
            report_subtree(Node.left)
        else:
            search_KDtree(Node.left, _range, noderange_l, depth+1)

        if completely_in(noderange_r, _range):
            report_subtree(Node.right)
        else:
            search_KDtree(Node.right, _range, noderange_r, depth+1)

def print_rect_problem(points, accepted, _range):
    x_vals_discarded = []
    y_vals_discarded = []
    x_vals_accepted = []
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
    ax.add_patch(Rectangle((_range[0][0], _range[1][0]), _range[0][1] - _range[0][0], _range[1][1] - _range[1][0], facecolor="blue", alpha=0.3))
    ax.scatter(x_vals_discarded, y_vals_discarded, color='red')
    ax.scatter(x_vals_accepted, y_vals_accepted, color='green')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')

    plt.grid()
    plt.show()

def getRandomRange(barrier=100):
    x = [random.uniform(-barrier, barrier), random.uniform(-barrier, barrier)]
    y = [random.uniform(-barrier, barrier), random.uniform(-barrier, barrier)]
    return ((min(x), max(x)), (min(y), max(y)))