import scipy
import numpy as np
import random
import math
import numpy.linalg
from helpFunctions import *
import queue

class node:
    def __init__(self, type, L, P):
        self.left = None
        self.right = None
        self.type = type
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
            # print('P', P)
            
            median = int(np.ceil(len(P)/2) - 1)
            L = P[median][0]
            # nod = node('n', L, None)

            # print(P[median])

            P1 = P[:median+1]
            P2 = P[median+1:]

        else:
            P.sort(key=getY)
            # print('P', P)
            
            median = int(np.ceil(len(P)/2) - 1)
            L = P[median][1]
            # nod = node('n', L, None)

            P1 = P[:median+1]
            P2 = P[median+1:]
        


        # print(P1)
        # print(P2)
        N = node('l', L, None)

        N.setL(create_KDtree(P1, depth+1))
        N.setR(create_KDtree(P2, depth+1))
        return N


def search_KDtree(root, _range):
    if root.type == 'n':
        print()

def main():
    # point_list = genRandompoints(10, 100, 0, method='rect')
    point_list = []
    point_list.append(np.array([-3, 5]))
    point_list.append(np.array([2, -4]))
    point_list.append(np.array([0, 1]))
    point_list.append(np.array([-5, 3]))
    point_list.append(np.array([1, -2]))
    point_list.append(np.array([-4, 0]))
    
    root = create_KDtree(point_list, 0)
    print_KDtree(root, depth=0)

    # from sklearn.neighbors import KDTree
    # tree = KDTree(point_list, leaf_size=1)
    # tree.get_tree_stats()
    
if __name__ == "__main__":
    main()