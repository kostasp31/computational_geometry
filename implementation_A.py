from convex_hull_algs import *

def main():
    print("Computational Geometry")
    point_list = genRandompoints(100, 100, 6648841, method='rect')

    # print("GIFT WRAPPING")
    # LG = gift_wrapping(point_list.copy())
    # print(LG, '\n')

    # print("INCREMENTAL")
    # LI = incremental(point_list.copy())
    # print(LI, '\n')

    # print("QUICKHULL")
    # LQ = quick_hull(point_list.copy())
    # print(LQ, '\n')

    # print("DIVIDE AND CONQUER")
    # LD = divide_and_conquer(point_list.copy())
    # print(LD, '\n')

    # printHull(LG, point_list.copy())
    # printHull(LI, point_list.copy())
    # printHull(LQ, point_list.copy())
    # printHull(LD, point_list.copy())

    gift_wrapping_show_steps(point_list.copy(), delay=0.01)

if __name__ == "__main__":
    main()