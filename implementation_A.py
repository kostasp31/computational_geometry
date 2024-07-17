from convex_hull_algs import *

def main():
    point_range = 100
    total_points = 100
    # Random points that are not colinear
    point_list = genRandompoints(total_points, point_range, 634774, method='circle')

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

    L = []
    L.append(LG)
    L.append(LI)
    L.append(LD)
    L.append(LQ)
    titles = []
    titles.append('Gift Wrapping')
    titles.append('Incremental')
    titles.append('Divide and Conquer')
    titles.append('Quick Hull')

    printHull(L, point_list.copy(), titles)

    # Generate colinear points and try to find the convex hulls
    point_list_colinear = genColinearpoints(30, _range=10)
    print("GIFT WRAPPING - COLLINEAR POINTS")
    LG_C = gift_wrapping(point_list_colinear.copy())
    print(LG_C)
    print("INCREMENTAL - COLLINEAR POINTS")
    LI_C = incremental(point_list_colinear.copy())
    print(LI_C)
    print("QUICK HULL - COLLINEAR POINTS")
    LQ_C = quick_hull(point_list_colinear.copy())
    print(LQ_C)
    print("DIVIDE AND CONQUER - COLLINEAR POINTS")
    LD_C = divide_and_conquer(point_list_colinear.copy())
    print(LD_C)

    L_C = []
    L_C.append(LG_C)
    L_C.append(LI_C)
    L_C.append(LD_C)
    L_C.append(LQ_C)

    for i in range(0, len(titles)):
        titles[i] = titles[i] + ' with colinear points'

    printHull(L_C, point_list_colinear.copy(), titles)

    # gift wrapping visulisation
    gift_wrapping_show_steps(point_list.copy()[:40], delay=0.001, _range=point_range)

    # not collinear points in 3d
    p_list_3d = getRandompoints_3d(85, 100,  73663, method='circle')
    hull_3d = gift_wrapping_3d(p_list_3d.copy())
    print('3D GIFT WRAPPING')
    for i in hull_3d:
        print('[', i[0], i[1], i[2], ']')

    hull_3d_print(p_list_3d, hull_3d)
    
if __name__ == "__main__":
    main()