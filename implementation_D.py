from kd_trees import *

def main():
    point_list = genRandompoints(100, 100, 0, method='rect')
    
    root = create_KDtree(point_list, 0)
    # print_KDtree(root, depth=0)

    Range = getRandomRange()
    search_KDtree(root, Range, ((float('-inf'), float('inf')), (float('-inf'), float('inf'))), 0)
    print_rect_problem(point_list, accepted_points, Range)

    
if __name__ == "__main__":
    main()