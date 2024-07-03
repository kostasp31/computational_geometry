from convex_hull_algs import *

def main():
    point_range = 10
    total_points = 30
    # print("Computational Geometry")
    # point_list = genRandompoints(total_points, point_range, 634774, method='circle')

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

    # gift_wrapping_show_steps(point_list.copy(), delay=0.001, _range=point_range)



    p_list = []
    # random.seed(43549)
    circle_r = 100
    circle_x = 0
    circle_y = 0
    for i in range(0,100):
        # random angle
        alpha = 2 * math.pi * random.random()
        beta = 2 * math.pi * random.random()
        # random radius
        r = circle_r * math.sqrt(random.random())
        d_2 = np.array([r * math.cos(alpha) + circle_x, r * math.sin(alpha) + circle_y, 0])
    

        rotation_axis = np.array([1, 1, 0])     # z
        rotation_vector = beta * rotation_axis
        rotation = scipy.spatial.transform.Rotation.from_rotvec(rotation_vector)
        rotated_vector = rotation.apply(d_2)

        # print(rotated_vector)
        p_list.append(rotated_vector)
    # p_list.append(np.array([0, -60, 40]))
    # p_list.append(np.array([0, -20, 10]))
    # p_list.append(np.array([23, 89, 52]))
    # p_list.append(np.array([54, -51, -77]))
    # p_list.append(np.array([-76, -54, -22]))


    # for i in range(0,100):
    #     p_list.append(np.array([random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(-100, 100)]))

    e1,proj,hull = gift_wrapping_3d(p_list.copy())

    print(hull)

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')

    x_vals = []
    y_vals = []
    z_vals = []
    for itm in p_list:
        x_vals.append(itm[0])
        y_vals.append(itm[1])
        z_vals.append(itm[2])

    xe = []
    ye = []
    ze = []
    xe.append(e1.p1[0])
    xe.append(e1.p2[0])
    ye.append(e1.p1[1])
    ye.append(e1.p2[1])
    ze.append(e1.p1[2])
    ze.append(e1.p2[2])

    p_x = []
    p_y = []
    p_z = []
    for itm in proj:
        p_x.append(itm[0])
        p_y.append(itm[1])
        p_z.append(0.0)

    # plt.plot(x_vals, y_vals, z_vals, 'red')
    ax.scatter(x_vals, y_vals, z_vals, 'green')
    # ax.scatter(p_x, p_y, p_z, 'blue')

    #plot the xy plane
    # x = np.outer(np.linspace(-100, 100, 32), np.ones(32))
    # y = x.copy().T # transpose
    # z = (np.outer(np.linspace(-100, 100, 32), np.zeros(32)))
    # ax.plot_surface(x,y,z, alpha=0.2)

    #plot the first edge
    # plt.plot(xe, ye, ze, 'blue')

    for tri in hull:
        triangle = graphicalTriangle(tri[0], tri[1], tri[2])
        ax.add_collection3d(Poly3DCollection(triangle, facecolors=['red', 'blue', 'crimson', 'red', 'blue', 'crimson'], linewidths=3, alpha=0.7))


    plt.show()
    

if __name__ == "__main__":
    main()