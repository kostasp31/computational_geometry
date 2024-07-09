from scipy import optimize

def main():
    # coefficients of the objective function 
    c = [3, -12]

    # constraint matrix
    A = [[-1, 2], [-2, 3], [-1, 3], [-1, 6], [4, -9]]

    # constraint vector
    b = [-1, -6, 0, 12, 27]

    # solve 
    results = optimize.linprog(c=c, A_ub=A, b_ub=b, bounds=[(0, None), (0, None)], method='simplex')

    # results
    if results.status == 0: print(f'The solution is optimal.') 
    print(f'Objective value: z* = {-results.fun}')
    print(f'Solution: x1* = {results.x[0]}, x2* = {results.x[1]}')

if __name__ == "__main__":
    main()