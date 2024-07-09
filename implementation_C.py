from convex_hull_algs import *
from delaunay import *
import time

def main():
    point_range = 100

    for i in range(3,7):
        total_points = i**3
        point_list = genRandompoints(total_points, point_range, 0, method='circle')

        tic = time.time()
        point_list_3d, hull_3d_down, delaunay = delaunay_triangulation(point_list)
        toc = time.time() - tic

        print('Delaunay triangulation of', total_points, 'points')
        for i in delaunay:
            print('[', i[0], i[1], ']')

        title = 'Delaunay triangulation, ' + str(total_points) + ' points,' + ' time to compute: ' + "{:.2f}".format(toc) + ' sec'
        delaunay_plot_2d(delaunay, title)
    
    pt = genRandompoints(30, point_range, 0, method='circle')
    pt3,hull,de = delaunay_triangulation(pt)
    delaunay_steps(de, pt3, hull)


if __name__ == "__main__":
    main()