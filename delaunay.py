import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from helpFunctions import *
from convex_hull_algs import *

def delaunay_triangulation(point_list):
    point_list_3d = []
    for p in point_list.copy():
        p = np.array([p[0], p[1], p[0]**2 + p[1]**2])
        point_list_3d.append(p)
    
    hull_3d = gift_wrapping_3d(point_list_3d)

    # get only the down-facing faces of the 3d convex hull
    # this is true if the z coord of the normal vector of the face
    # is positive
    hull_3d_down = []
    for tri in hull_3d:
        normal_vec = np.cross((tri[1] - tri[0]),(tri[2] - tri[0]))
        if normal_vec[2] > 0:
            hull_3d_down.append(tri)

    delaunay = []
    for tri in hull_3d_down:
        tri_2d = []
        for itm in tri:
            tri_2d.append(np.array([itm[0], itm[1]]))
        delaunay.append(tuple(tri_2d))

    return point_list_3d, hull_3d_down, delaunay

def delaunay_steps(delaunay, point_list_3d, hull_3d_down):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')
    # ax.set_xlim([xmin, xmax])
    # ax.set_ylim([ymin, ymax])
    ax.set_zlim([0, 10000])
    ax.view_init(elev=14., azim=-40)

    x_vals = []
    y_vals = []
    z_vals = []
    for tri in delaunay:
        for itm in tri:
            x_vals.append(itm[0])
            y_vals.append(itm[1])
            z_vals.append(0.0)

    ax.scatter(x_vals, y_vals, z_vals, 'green')
    fig.canvas.draw()
    plt.pause(1)

    x_vals3 = []
    y_vals3 = []
    z_vals3 = []    
    for itm in point_list_3d:
        x_vals3.append(itm[0])
        y_vals3.append(itm[1])
        z_vals3.append(itm[2])
    ax.scatter(x_vals3, y_vals3, z_vals3, 'green')


    for tri in hull_3d_down:
        triangle = graphicalTriangle(tri[0], tri[1], tri[2])

        i = random.randint(0,3)
        if i==0:
            c = 'red'
        elif i==1:
            c = 'blue'
        else:
            c = 'green'
        t = ax.add_collection3d(Poly3DCollection(triangle, facecolors=c, linewidths=1, alpha=0.5))
        t.set_edgecolor('k')
        fig.canvas.draw()  
        plt.pause(0.03)


    for itm in point_list_3d:
        ax.plot([itm[0], itm[0]], [itm[1], itm[1]], [itm[2], 0], 'magenta') 
        fig.canvas.draw()  
        plt.pause(0.03)




    for tri in delaunay:
        triangle = graphicalTriangle_2d(tri[0], tri[1], tri[2])

        i = random.randint(0,3)
        if i==0:
            c = 'red'
        elif i==1:
            c = 'blue'
        else:
            c = 'green'
        t = ax.add_collection3d(Poly3DCollection(triangle, facecolors='red', linewidths=1, alpha=0.5))
        t.set_edgecolor('k')
        fig.canvas.draw()  
        plt.pause(0.02)

    plt.show()


def delaunay_plot_2d(delaunay):
    x1 = []
    y1 = []
    fig, ax = plt.subplots(1, 1, constrained_layout=True)
    fig.suptitle('Delaunay triangulation', fontsize=14)
    for tri in delaunay:
        x1.append(itm[0])
        y1.append(itm[1])

        x2 = []
        y2 = []
        for itm in tri:
            x2.append(itm[0])
            y2.append(itm[1])

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.plot(x1,y1,'o', color='red')
        ax.plot(x2,y2,'o', color='red')
        for i in range(0, len(x2), 2):
            ax.plot(x2[i:i+2], y2[i:i+2], 'blue')
        for i in range(1, len(x2), 2):
            ax.plot(x2[i:i+2], y2[i:i+2], 'blue')

        x = np.array([x2[0], x2[-1]])
        y = np.array([y2[0], y2[-1]])
        ax.plot(x, y, 'blue')
    plt.show()