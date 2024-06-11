# 实验1任务2
import numpy as np

def f(x):
    return np.exp(-x) + x**2

def parabolic_interpolation(a, b, c, tol=1e-5):
    fa, fb, fc = f(a), f(b), f(c)
    
    while abs(c - a) > tol:
        # Parabolic interpolation formula to find the vertex
        numerator = (b - a)**2 * (fb - fc) - (b - c)**2 * (fb - fa)
        denominator = (b - a) * (fb - fc) - (b - c) * (fb - fa)
        x = b - 0.5 * numerator / denominator
        
        fx = f(x)
        
        # Update the points a, b, c
        if x > b:
            if fx > fb:
                c = x
                fc = fx
            else:
                a = b
                fa = fb
                b = x
                fb = fx
        else:
            if fx > fb:
                a = x
                fa = fx
            else:
                c = b
                fc = fb
                b = x
                fb = fx
    
    return b, fb

def main():
    # 获取用户输入的初始区间
    a = float(input("请输入区间左端点 a: "))
    b = float(input("请输入区间中点 b: "))
    c = float(input("请输入区间右端点 c: "))
    
    # 调用抛物线法求解
    result_x, result_fx = parabolic_interpolation(a, b, c)
    
    # 打印最优解和函数值
    print(f"最优解 x = {result_x}")
    print(f"函数值 f(x) = {result_fx}")

if __name__ == "__main__":
    main()
