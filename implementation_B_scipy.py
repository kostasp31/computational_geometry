from scipy import optimize

def main():
    # declare the decision variable bounds
    x1_bounds = (0, None)
    x2_bounds = (0, None)

    # declare coefficients of the objective function 
    c = [3, -12]

    # declare the inequality constraint matrix
    A = [[-1, 2], [-2, 3], [-1, 3], [-1, 6], [4, -9]]

    # declare the inequality constraint vector
    b = [-1, -6, 0, 12, 27]

    # solve 
    results = optimize.linprog(c=c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method='simplex')

    # print results
    if results.status == 0: print(f'The solution is optimal.') 
    print(f'Objective value: z* = {-results.fun}')
    print(f'Solution: x1* = {results.x[0]}, x2* = {results.x[1]}')

if __name__ == "__main__":
    main()