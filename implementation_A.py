from convex_hull_algs import *

def main():
    point_range = 100
    total_points = 100
    print("Computational Geometry")
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

    printHull(LG, point_list.copy(), 'Gift Wrapping')
    printHull(LI, point_list.copy(), 'Incremental')
    printHull(LQ, point_list.copy(), 'Quick Hull')
    printHull(LD, point_list.copy(), 'Divide and Conquer')

    gift_wrapping_show_steps(point_list.copy(), delay=0.001, _range=point_range)

    p_list_3d = getRandompoints_3d(85, 100, 73663, method='circle')
    hull_3d = gift_wrapping_3d(p_list_3d.copy())

    hull_3d_print(p_list_3d, hull_3d)
    

if __name__ == "__main__":
    main()