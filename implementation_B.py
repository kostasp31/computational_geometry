from scipy import optimize
import numpy as np

def main():
    # objective function
    fx = np.array([3, -12, 0])
    # the limittations in fotm H_i(x) <= 0
    H = np.array([
        [-1, 2, 1],
        [-2, 3, 6],
        [-1, 3, 0],
        [-1, 6, -12],
        [4, -9, -27]
    ])
    # d=2, n=5

    results = optimize.linprog(c=fx, A_ub=H, b_ub=np.array([0, 0, 0, 0, 0]), bounds=[(0, float('inf')), (0, float('inf'))], method='simplex')
    print(results)

if __name__ == "__main__":
    main()