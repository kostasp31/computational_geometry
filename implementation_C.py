from convex_hull_algs import *
from delaunay import *


def main():
    point_range = 100
    total_points = 100
    print("Computational Geometry")
    point_list = genRandompoints(total_points, point_range, 0, method='circle')

    point_list_3d, hull_3d_down, delaunay = delaunay_triangulation(point_list)

    delaunay_steps(delaunay, point_list_3d, hull_3d_down)
    delaunay_plot_2d(delaunay)


if __name__ == "__main__":
    main()