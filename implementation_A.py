import scipy
import numpy as np
import random
import math
import numpy.linalg
from convex_hull_algs import *

def main():
    print("Computational Geometry")
    random.seed(664884)
    point_list = []
    for i in range(0,100):   # 10 random real numbers
        point_list.append(np.array([random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0)]))
    
    print("GIFT WRAPPING")
    LG = gift_wrapping(point_list.copy())
    print(LG, '\n')

    print("INCREMENTAL")
    LI = incremental(point_list.copy())
    print(LI, '\n')

    print("QUICKHULL")
    LQ = quick_hull(point_list.copy())
    print(LQ, '\n')

    print("DIVIDE AND CONQUER")
    LD = divide_and_conquer(point_list.copy())
    print(LD, '\n')

    printHull(LG, point_list.copy())
    printHull(LI, point_list.copy())
    printHull(LQ, point_list.copy())
    printHull(LD, point_list.copy())

if __name__ == "__main__":
    main()