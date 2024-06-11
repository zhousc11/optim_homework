# 实验2.1代码
# filename: exp2.1.py
import numpy as np

def f(x):
    return (x[0] - 2)**2 + (x[0] - 2 * x[1])**2

def grad_f(x):
    dfdx1 = 2 * (x[0] - 2) + 2 * (x[0] - 2 * x[1])
    dfdx2 = -4 * (x[0] - 2 * x[1])
    return np.array([dfdx1, dfdx2])

def steepest_descent(f, grad_f, x0, tol=0.4, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        gradient = grad_f(x)
        grad_norm = np.linalg.norm(gradient)
        if grad_norm < tol:
            break
        alpha = armijo_search(f, grad_f, x, -gradient)
        x = x - alpha * gradient
    return x

def armijo_search(f, grad_f, xk, dk, alpha=1, beta=0.5, sigma=1e-4):
    while f(xk + alpha * dk) > f(xk) + sigma * alpha * np.dot(grad_f(xk), dk):
        alpha *= beta
    return alpha

def main():
    x0 = np.array([0, 3])
    tol = 0.4
    result = steepest_descent(f, grad_f, x0, tol)
    print(f"最优解 x = {result}")
    print(f"函数值 f(x) = {f(result)}")

if __name__ == "__main__":
    main()
