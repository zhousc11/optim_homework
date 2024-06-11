# 实验1.3内容
# filename: exp1.3.py
import numpy as np

def f(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

def grad_f(x):
    dfdx1 = -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0])
    dfdx2 = 200 * (x[1] - x[0]**2)
    return np.array([dfdx1, dfdx2])

def armijo_search(f, grad_f, xk, dk, alpha=1, beta=0.5, sigma=1e-4):
    while f(xk + alpha * dk) > f(xk) + sigma * alpha * np.dot(grad_f(xk), dk):
        alpha *= beta
    return alpha

def main():
    xk = np.array([-1, 1])
    dk = np.array([1, 1])
    alpha = armijo_search(f, grad_f, xk, dk)
    x_new = xk + alpha * dk

    print(f"最优步长 α = {alpha}")
    print(f"更新后的 x = {x_new}")
    print(f"函数值 f(x_new) = {f(x_new)}")

if __name__ == "__main__":
    main()
