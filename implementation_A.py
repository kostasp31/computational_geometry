import scipy
import numpy as np
import random

def main():
    print("Computational Geometry")
    # random.seed(5733839)
    point_list = []
    for i in range(0,1000):   # 10 random real numbers
        point_list.append(np.array([random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0)]))
    
    # for i in range(0,10):   # 10 random real numbers
    #     point_list.append(np.array([random.randint(1,50), random.randint(1,50)]))

    # print(point_list)
    L = incremental(point_list)
    print(L)

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

    plt.plot(x1,y1,'o', color='red')
    plt.plot(x2,y2,'o', color='blue')
    for i in range(0, len(x2), 2):
        plt.plot(x2[i:i+2], y2[i:i+2], 'blue')
    for i in range(1, len(x2), 2):
        plt.plot(x2[i:i+2], y2[i:i+2], 'blue')

    x = np.array([x2[0], x2[-1]])
    y = np.array([y2[0], y2[-1]])
    plt.plot(x, y, 'blue')
    plt.show()



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

# return the X of a nparray (point)
def getX(nparray):
    return nparray[0]

# points in general position
def incremental(points):
    points.sort(key=getX)  # sort points in ascending order
    L_upper = []
    L_upper.append(points[0])   # insert the first 2 points
    L_upper.append(points[1])
    for i in range(2, len(points)): # 3 to n
        L_upper.append(points[i])
        while (len(L_upper) > 2) and (CCW(L_upper[-3], L_upper[-2], L_upper[-1]) >= 0):
            del L_upper[-2]
    
    L_lower = []
    L_lower.append(points[-1])   # insert p_n
    L_lower.append(points[-2])   # insert p_n-1
    for i in range(len(points)-3, -1, -1): # n-2 to 1
        L_lower.append(points[i])
        while (len(L_lower) > 2) and (CCW(L_lower[-3], L_lower[-2], L_lower[-1]) >= 0):
            del L_lower[-2]

    del L_lower[0]  # remove first and last element
    del L_lower[-1]
    L = L_upper+L_lower
    return L
        
    












if __name__ == "__main__":
    main()