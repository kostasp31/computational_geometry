import numpy as np
import math
from helpFunctions import *
import queue

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
        


def gift_wrapping(S):
    chain = []
    r = min(S, key=minKey)    # point with min x, if many, the one with min y
    chain.append(r)

    while (1):
        tempL = []
        tempL = [item for item in S if not vecInList(item, chain)] # choose a random point that has not been selected yet
        if tempL == []:
            return chain
        u = tempL[0]
        for t in S: # t in S 
            if np.array_equal(t, u):   #S\{u}
                continue
            # for collinear points check if u is inside the edge r,t
            if CCW(r, u, t) > 0 or (CCW(r,u,t) == 0 and dist(r,u) < dist(r,t) and dist(t,u) < dist(t,r)):
                u = t
        if np.array_equal(u, chain[0]):   # u == r0
            return chain
        else:
            r = u
            chain.append(r)

# merge 2 convex hulls by finding the upper and lower edge
def merge(A, B):
    finalHull = []
    i = getIndexOfRightmost(A)
    j = 0
    upper = []
    lower = []
    while (1):  # upper tangent
        init_i = i
        init_j = j
        while  (CCW(A[i], A[getPrev(i, A)], B[j]) < 0):
            i = getPrev(i, A)
        while (CCW(B[j], B[getNext(j, B)], A[i]) > 0):
            j = getNext(j, B)
        if i == init_i and j == init_j:
            break
    upper.append(A[i])
    upper.append(B[j])

    i = getIndexOfRightmost(A)
    j = 0
    while (1):  # lower tangent
        init_i = i
        init_j = j
        while  (CCW(A[i], A[getNext(i, A)], B[j]) > 0):
            i = getNext(i, A)
        while (CCW(B[j], B[getPrev(j, B)], A[i]) < 0):
            j = getPrev(j, B)
        if i == init_i and j == init_j:
            break
    lower.append(A[i])
    lower.append(B[j])

    finalHull = []
    i=0
    # create final chain of items
    # add upper items of A
    while (1):
        if not np.array_equal(A[i], upper[0]):  # until the left point of upper edge is met
            if not vecInList(A[i], finalHull):
                finalHull.append(A[i])
        else:
            if not vecInList(upper[0], finalHull):  # found the left point of upper edge, add it 
                finalHull.append(upper[0])
            if not vecInList(upper[1], finalHull):  # also add the right point
                finalHull.append(upper[1])
            break
        i = getNext(i, A)

    start_from = 0
    for j in range(0, len(B)):  # get the starting index of B items by 
        if np.array_equal(B[j], upper[1]):  # finding where the right point of upper edge is
            start_from = j#getNext(j, B)

    j = start_from
    while(1):   # continue adding items of B
        if not np.array_equal(B[j], lower[1]):  # untill the right point of the lower edge is found
            if not vecInList(B[j], finalHull):
                finalHull.append(B[j])
        else:
            if not vecInList(lower[1], finalHull):  # if found, add it and the left point of the bridge as well
                finalHull.append(lower[1])
            if not vecInList(lower[0], finalHull):
                finalHull.append(lower[0])
            break
        j = getNext(j, B)

    cont_from = 0   # where to continue adding items from A
    for i in range(0, len(A)):
        if np.array_equal(A[i], lower[0]):
            cont_from = i#getNext(i, A)
    
    i = cont_from
    while(1):   # add all the remaining points until the left point of the bridge is found
        if np.array_equal(A[i], upper[0]):
            break
        else:
            if not vecInList(A[i], finalHull):
                finalHull.append(A[i])
        i = getNext(i, A)

    return finalHull

def divide_and_conquer(points):
    if len(points) <= 2:
        return (points)   
    
    points.sort(key=minKey)  # sort points in ascending order
    A = points[:math.ceil(len(points)/2)]
    B = points[(math.ceil(len(points)/2)):]
    CHA = divide_and_conquer(A)
    CHB = divide_and_conquer(B)
    m = merge(CHA, CHB)
    return m

# fails if the some of the 4 extreme points of the hull are the same
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
    if len(set(hull)) != 4: # ensure that the 4 extreme points are not the same
        print('QuickHull failed --- We should assume that the 4 extreme points are different')
        return []
    
    # get the hull from the points outside the 4 sides of the shape these 4 points create
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

# quickhull algorithm, given 2 points A, B and a set of points S
def hull_rec(A, B, S):
    hull = []
    # simplest case
    if len(S) == 2 and ((np.array_equal(A, S[0]) and np.array_equal(B, S[1])) or (np.array_equal(A, S[1]) and np.array_equal(B, S[0]))):
        hull.append(A)
        hull.append(B)
        return hull
    else:   # more then 3 points
        maxDist = float('-inf')
        C = np.array([float('-inf'), float('-inf')])
        noneType = C
        for p in S: # get the point that has the greates distance from AB line
            if np.array_equal(A, p) or np.array_equal(B, p):
                continue
            d = distFromLine(A, B, p)
            if d > maxDist:
                maxDist = d
                C = p
        if np.array_equal(C, noneType): # this should not happen
            hull.append(A)
            hull.append(B)
            return hull            
        M = []
        N = []
        M.append(A)
        N.append(C)
        # create he 2 subsets of S and recursively call quickhull
        for p in S:
            if CCW(A, C, p) > 0:
                M.append(p)
            elif CCW(C, B, p) > 0:
                N.append(p)
        M.append(C)
        N.append(B)
        return hull_rec(A, C, M)[:-1] + hull_rec(C, B, N)
        
# visulisation of the gift wrapping algorithm
def gift_wrapping_show_steps(S, delay=0.05, _range=100):
    chain = []
    r = min(S, key=minKey)    # point with min x, if many, the one with min y
    chain.append(r)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 1, constrained_layout=True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    fig.suptitle('Gift Wrapping', fontsize=14)

    plt.axis([-_range-10, _range+10, -_range-10, _range+10])
    # plot all points (in red)
    for i in S:
        plt.plot(i[0], i[1],'o', color='red')

    # current point r, becomes blue
    plt.plot(r[0], r[1],'o', color='blue')
    plt.pause(delay)
    while (1):
        tempL = []
        tempL = [item for item in S if not vecInList(item, chain)] # choose a random point that has not been selected yet
        if tempL == []:
            plt.plot([chain[0][0], chain[-1][0]] , [chain[0][1], chain[-1][1]], 'blue')
            plt.pause(delay)
            break
        u = tempL[0]
        # draw a line between r,u
        outln, = plt.plot([r[0], u[0]] , [r[1], u[1]], 'blue')
        plt.pause(delay)
        for t in S: # t in S 
            if np.array_equal(t, u):   #S\{u}
                continue
            # plot a line between r,t
            ln, = plt.plot([r[0], t[0]], [r[1], t[1]], color='green')
            plt.pause(delay)
            if CCW(r, u, t) > 0 or (CCW(r,u,t) == 0 and dist(r,u) < dist(r,t) and dist(t,u) < dist(t,r)):
                u = t
                outln.remove()  # remove the line u,t
                outln, = plt.plot([r[0], t[0]] , [r[1], t[1]], 'blue')
            ln.remove() # remove the line r,u
        if np.array_equal(u, chain[0]):   # u == r0
            plt.plot([chain[0][0], chain[-1][0]] , [chain[0][1], chain[-1][1]], 'blue')
            plt.pause(delay)
            break
        else:
            r = u
            # remVec(r, S) # S <- S\{r}
            chain.append(r)
            # if r is in the hull, make it permanently blue
            plt.plot(r[0], r[1],'o', color='blue')
            plt.pause(delay)

    plt.show()
    return chain


# Choose the first edge of the convex hull (2 points)
# Find a point with minimum x
# Find the next vertex by 2D gift wrapping on the 2D projection of the points on a plane. O(n)
# The third vertex is obtained by comparing the faces built from the above edge and all remaining points. O(n)
def choose_initial_edge(S):
    min_x_point = S[0]
    for point in S:
        if point[0] < min_x_point[0]:
            min_x_point = point
    
    projected_points = []
    for point in S:
        tmp = np.array([point[0], point[1]])
        projected_points.append(tmp)

    chain = []
    r = min_x_point
    chain.append(np.array([r[0], r[1]]))
    tempL = []
    tempL = [item for item in projected_points if not vecInList(item, chain)] # choose a random point that has not been selected yet
    u = tempL[0]
    for t in projected_points: # t in S 
        if np.array_equal(t, u):   #S\{u}
            continue
        if CCW(r, u, t) > 0 or (CCW(r,u,t) == 0 and dist(r,u) < dist(r,t) and dist(t,u) < dist(t,r)):
            u = t
    r = u
    chain.append(r)

    new_point = r
    for item in S:
        if item[0] == new_point[0] and item[1] == new_point[1]:
            new_point = item

    e = edge(min_x_point, new_point)
    return (e,projected_points)

def gift_wrapping_3d(S):
    convex_hull = []    # triangles of convex hull
    e,proj = choose_initial_edge(S)
    visited = []    # visited edges
    Q = queue.Queue()

    e_r = edge(e.p2, e.p1)
    visited.append(e)
    Q.put(e_r)

    while (not Q.empty()):
        ed = Q.get()
        if not edgeInList(ed, visited):
            p3 = getThirdPoint(ed.p1, ed.p2, S)

            convex_hull.append((ed.p1, ed.p2, p3))
            # create all possible edges
            ed23 = edge(ed.p2, p3)
            ed23_r = edge(p3, ed.p2)
            ed31 = edge(p3, ed.p1)
            ed31_r = edge(ed.p1, p3)
            ed12 = edge(ed.p1, ed.p2)
            ed12_r = edge(ed.p2, ed.p1)

            visited.append(ed12)
            visited.append(ed23)
            visited.append(ed31)
            # add them in Q to visit, if not visited
            if not edgeInList(ed12_r, visited):
                Q.put(ed12_r)
            if not edgeInList(ed23_r, visited):
                Q.put(ed23_r)
            if not edgeInList(ed31_r, visited):
                Q.put(ed31_r)
    return convex_hull

# find a point in S that, the triangle it creates with p1, p2 is the best choice
# this is done by getting the point with the max signed volume
def getThirdPoint(p1, p2, S):
    zero_p = np.array([float("-inf"), float("-inf"), float("-inf")])
    new_point = zero_p
    for p3 in S:
        if (not np.array_equal(p1, p3)) and (not np.array_equal(p2, p3)):
            if np.array_equal(new_point, zero_p):
                new_point = p3
                continue
            cross = np.cross((new_point - p1), (p3 - p1))
            vol = np.dot(cross, p1 - p2)/6
            if vol > 0:
                new_point = p3
    return new_point
            