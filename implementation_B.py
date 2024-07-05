from scipy import optimize

def main():
    c_ = [3, -12]
    A_ = [[-1, 2], [-2, 3], [-1, 3], [1, -6], [4, -9]]
    b_ = [-1, -6, 0, 12, 27]
    x2_bounds_ = (None, None)
    x1_bounds_ = (None, None)

    res_ = optimize.linprog(c_, A_ub=A_, b_ub=b_, bounds=[x1_bounds_, x2_bounds_], method='simplex')
    print(res_.fun)
    print(res_.x)
    print(res_.message)

if __name__ == "__main__":
    main()