# 实验一第一次作业，编写0.618法求最优解程序，并运行程序求解最优化问题
import math

def f(x):
    return math.exp(-x) + x**2

def golden_section_search(a, b, tol=1e-5):
    alpha = (math.sqrt(5) - 1) / 2
    
    x1 = a + (1 - alpha) * (b - a)
    x2 = a + alpha * (b - a)
    
    while (b - a) > tol:
        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = a + alpha * (b - a)
        else:
            b = x2
            x2 = x1
            x1 = a + (1 - alpha) * (b - a)
    
    return (a + b) / 2

def main():
    # 获取用户输入的初始区间
    a = float(input("请输入区间下限 a: "))
    b = float(input("请输入区间上限 b: "))
    
    # 调用黄金分割法求解
    result = golden_section_search(a, b)
    
    # 打印最优解和函数值
    print(f"最优解 x = {result}")
    print(f"函数值 f(x) = {f(result)}")

if __name__ == "__main__":
    main()

