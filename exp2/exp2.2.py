# 实验2.2源代码
# filename: exp2.2.py
import numpy as np

def f(x):
    return x[0]**2 + x[1]**2 + x[0]*x[1] + 2*x[0] - 3*x[1]

def grad_f(x):
    dfdx1 = 2*x[0] + x[1] + 2
    dfdx2 = 2*x[1] + x[0] - 3
    return np.array([dfdx1, dfdx2])

def hessian_f(x):
    return np.array([[2, 1],
                     [1, 2]])

def newton_method(f, grad_f, hessian_f, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        gradient = grad_f(x)
        hessian = hessian_f(x)
        if np.linalg.norm(gradient) < tol:
            break
        step = np.linalg.solve(hessian, -gradient)
        x = x + step
    return x

def main():
    x0 = np.array([0, 0])
    result = newton_method(f, grad_f, hessian_f, x0)
    print(f"最优解 x = {result}")
    print(f"函数值 f(x) = {f(result)}")

if __name__ == "__main__":
    main()
