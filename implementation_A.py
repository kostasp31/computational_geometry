from convex_hull_algs import *

def main():
    point_range = 100
    total_points = 30
    # print("Computational Geometry")
    # point_list = genRandompoints(total_points, point_range, 6648841, method='circle')

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

    # # printHull(LG, point_list.copy())
    # # printHull(LI, point_list.copy())
    # # printHull(LQ, point_list.copy())
    # # printHull(LD, point_list.copy())

    # gift_wrapping_show_steps(point_list.copy(), delay=0.001, _range=point_range)

    p_list = []
    for i in range(0,10):
        p_list.append(np.array([random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(-100, 100)]))

    # import matplotlib.pyplot as plt
    # fig = plt.figure(figsize=(100, 100))
    # ax = fig.add_subplot(projection='3d')

    # x_vals = []
    # y_vals = []
    # z_vals = []
    # for itm in p_list:
    #     x_vals.append(itm[0])
    #     y_vals.append(itm[1])
    #     z_vals.append(itm[2])

    # ax.scatter(x_vals, y_vals, z_vals)
    # plt.show()
    

if __name__ == "__main__":
    main()