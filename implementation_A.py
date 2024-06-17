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


def main():
    print("Computational Geometry")
    for j in range(10,1000):
        random.seed(j)
        print('SEED', j)
        while (1):
            point_list = []
            for i in range(0,j):   # 10 random real numbers
                point_list.append(np.array([random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0)]))
            
            # li = random.sample(range(0,40), 24)
            # for i in range(0,10):   # 10 random real numbers
            #     point_list.append(np.array([li[i], li[i+1]]))

            # print("GIFT WRAPPING")
            # LG = gift_wrapping(point_list.copy())
            # print('LG',LG)
            # print('\n')

            h = quick_hull(point_list.copy())
            if h == None:
                continue
            else:
                break

        print("INCREMENTAL")
        L = incremental(point_list.copy())
        print(L)
        print("QUICKHULL")
        print(h)

        # print("DIVIDE AND CONQUER")
        # LD = divide_and_conquer(point_list.copy())
        # print(LD)

        if not complists(L, h):
            printHull(L, point_list.copy())
            printHull(h, point_list.copy())

def printHull(L, point_list):
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
    plt.plot(x2,y2,'o', color='red')
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
    points.sort(key=minKey)  # sort points in ascending order
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

def gift_wrapping(S):
    chain = []
    r = min(S, key=minKey)    # point with min x, if many, the one with min y
    chain.append(r)

    while (1):
        tempL = []
        tempL = [item for item in S if not vecInList(item, chain)] # choose a random point that has not been selected yet
        if tempL == []:
            print('EMPTYYYY')
            return chain
        u = tempL[0]
        for t in S: # t in S 
            if np.array_equal(t, u):   #S\{u}
                continue
            if CCW(r, u, t) > 0 or (CCW(r,u,t) == 0 and dist(r,u) < dist(r,t) and dist(t,u) < dist(t,r)):
                u = t
        if np.array_equal(u, chain[0]):   # u == r0
            return chain
        else:
            r = u
            # remVec(r, S) # S <- S\{r}
            chain.append(r)

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
        
def merge(A, B):
    # print('Merging:', A, B)
    finalHull = []
    # if len(A) == 1 or len(B) == 1:
        # print('a')
    
    i = getIndexOfRightmost(A)
    j = 0
    upper = []
    lower = []
    while (1):  # upper tangent
        changed = False
        # print(i, getNext(i,A), getDiffPoint(A, A[i], A[getNext(i, A)]))
        # print(j, getPrev(j,B), getDiffPoint(B, B[j], B[getPrev(j, B)]))
        init_i = i
        init_j = j
        # if getNext(i, A) != 0:
        while  (CCW(A[i], A[getPrev(i, A)], B[j]) < 0):
            i = getPrev(i, A)
            changed = True
        # if getPrev(j, B) != len(B)-1:
        while (CCW(B[j], B[getNext(j, B)], A[i]) > 0):
            j = getNext(j, B)
            changed = True
        if i == init_i and j == init_j:
            break
    # print('Upper:', A[i], ',', B[j])
    upper.append(A[i])
    upper.append(B[j])

    i = getIndexOfRightmost(A)
    j = 0
    while (1):  # lower tangent
        changed = False
        # print(i, getPrev(i,A), getDiffPoint(A, A[i], A[getPrev(i, A)]))
        # print(j, getNext(j,B), getDiffPoint(B, B[j], B[getNext(j, B)]))
        init_i = i
        init_j = j
        # if getPrev(i, A) != 0:
        while  (CCW(A[i], A[getNext(i, A)], B[j]) > 0):
            i = getNext(i, A)
            changed = True
        # if getNext(j, B) != len(B)-1:
        while (CCW(B[j], B[getPrev(j, B)], A[i]) < 0):
            j = getPrev(j, B)
            changed = True
        if i == init_i and j == init_j:
            break
    # print('Lower:', A[i], ',', B[j])
    lower.append(A[i])
    lower.append(B[j])

    finalHull = []
    i=0
    while (1):
        if not np.array_equal(A[i], upper[0]):
            if not vecInList(A[i], finalHull):
                finalHull.append(A[i])
        else:
            if not vecInList(upper[0], finalHull):
                finalHull.append(upper[0])
            if not vecInList(upper[1], finalHull):
                finalHull.append(upper[1])
            break
        i = getNext(i, A)

    start_from = 0
    for j in range(0, len(B)):
        if np.array_equal(B[j], upper[1]):
            start_from = j#getNext(j, B)

    j = start_from
    while(1):
        if not np.array_equal(B[j], lower[1]):
            if not vecInList(B[j], finalHull):
                finalHull.append(B[j])
        else:
            if not vecInList(lower[1], finalHull):
                finalHull.append(lower[1])
            if not vecInList(lower[0], finalHull):
                finalHull.append(lower[0])
            break
        j = getNext(j, B)

    cont_from = 0
    for i in range(0, len(A)):
        if np.array_equal(A[i], lower[0]):
            cont_from = i#getNext(i, A)
    
    i = cont_from
    while(1):
        if np.array_equal(A[i], upper[0]):
            break
        else:
            if not vecInList(A[i], finalHull):
                finalHull.append(A[i])
        i = getNext(i, A)

    # print(finalHull)
    return finalHull

def divide_and_conquer(points):
    if len(points) <= 2:
        return (points)   
    
    points.sort(key=getX)  # sort points in ascending order
    A = points[:math.ceil(len(points)/2)]
    B = points[(math.ceil(len(points)/2)):]
    CHA = divide_and_conquer(A)
    CHB = divide_and_conquer(B)
    m = merge(CHA, CHB)
    return m

# distance of c from line that a,b define
def distFromLine(a, b, c):
    return np.linalg.norm(np.cross(b-a, a-c))/np.linalg.norm(b-a)

def quick_hull(points):
    top = 0
    bottom = 0
    right = 0
    left = 0
    for i in range(0, len(points)):
        if points[i][1] > points[top][1]:
            top = i
        if points[i][1] < points[bottom][1]:
            bottom = i
        if points[i][0] > points[right][0]:
            right = i
        if points[i][0] < points[left][0]:
            left = i

    hull = []
    hull.append(top)
    hull.append(right)
    hull.append(bottom)
    hull.append(left)
    if len(set(hull)) != 4:
        print('We should assume that the 4 extreme points are different')
        print(top)
        print(right)
        print(bottom)
        print(left)
        return None
    
    h = hull_rec(points[top], points[right], points)+hull_rec(points[right], points[bottom], points)+hull_rec(points[bottom], points[left], points)+hull_rec(points[left], points[top], points)
    
    first = h[0]
    stopAt = len(h)-1
    for i in range(1, len(h)):
        if np.array_equal(h[i], first):
            stopAt = i
            break
    h = h[0:stopAt]
    # 'reset' index to start from the leftmost point
    h0 = h.copy()
    h0.sort(key=getX)
    shiftBY = 0
    i = 0
    for el in h:
        if np.array_equal(el, h0[0]):
            shiftBY = i
        i += 1

    h = [h[(i + shiftBY) % len(h)] for i, x in enumerate(h)]

    i = 0
    while i < len(h)-1:
        if np.array_equal(h[i], h[i+1]):
            del h[i]
        else:
            i+=1

    return h

def hull_rec(A, B, S):
    hull = []
    if len(S) == 2 and ((np.array_equal(A, S[0]) and np.array_equal(B, S[1])) or (np.array_equal(A, S[1]) and np.array_equal(B, S[0]))):
        hull.append(A)
        hull.append(B)
        return hull
    else:
        maxDist = float('-inf')
        C = np.array([float('-inf'), float('-inf')])
        noneType = C
        for p in S:
            if np.array_equal(A, p) or np.array_equal(B, p):
                continue
            d = distFromLine(A, B, p)
            if d > maxDist:
                maxDist = d
                C = p
        if np.array_equal(C, noneType):
            hull.append(A)
            hull.append(B)
            return hull            
        M = []
        N = []
        M.append(A)
        N.append(C)
        for p in S:
            if CCW(A, C, p) > 0:
                M.append(p)
            elif CCW(C, B, p) > 0:
                N.append(p)
        M.append(C)
        N.append(B)
        return hull_rec(A, C, M)[:-1] + hull_rec(C, B, N)
        











if __name__ == "__main__":
    main()