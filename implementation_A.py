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
    L.append(LQ)
    L.append(LD)
    titles = []
    titles.append('Gift Wrapping')
    titles.append('Incremental')
    titles.append('Divide and Conquer')
    titles.append('Quick Hull')

    printHull(L, point_list.copy(), titles)

    # Generate colinear points and try to find the convex hulls
    point_list_colinear = genColinearpoints(50)
    LG_C = gift_wrapping(point_list_colinear.copy())
    LI_C = incremental(point_list_colinear.copy())
    LD_C = divide_and_conquer(point_list_colinear.copy())
    LQ_C = quick_hull(point_list_colinear.copy())

    L_C = []
    L_C.append(LG_C)
    L_C.append(LI_C)
    L_C.append(LD_C)
    L_C.append(LQ_C)
    for i in range(0, len(titles)):
        titles[i] = titles[i] + ' with colinear points'

    printHull(L_C, point_list_colinear.copy(), titles)

    # gift wrapping visulisation
    gift_wrapping_show_steps(point_list.copy(), delay=0.001, _range=point_range)

    # not collinear points in 3d
    p_list_3d = getRandompoints_3d(85, 100,  73663, method='circle')
    hull_3d = gift_wrapping_3d(p_list_3d.copy())

    hull_3d_print(p_list_3d, hull_3d)
    
if __name__ == "__main__":
    main()