import numpy as np
import matplotlib.pyplot as plt

# 1. تعريف الدالة الرياضية
def f(x):
    return x**2  # يمكنكِ تغييرها لأي دالة أخرى

# 2. دالة حساب التكامل ورسم المنحنى
def plot_trapezoidal(a, b, n):
    x = np.linspace(a, b, 100)
    y = f(x)
    
    # رسم المنحنى الأساسي للدالة
    plt.plot(x, y, 'r', label='f(x) = x^2')
    
    # رسم أشباه المنحرفات وتظليلها
    x_trap = np.linspace(a, b, n+1)
    y_trap = f(x_trap)
    plt.fill_between(x_trap, y_trap, color='skyblue', alpha=0.4, label='Trapezoidal Area')
    
    # إضافة العناوين
    plt.title(f'Trapezoidal Rule (n={n})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    
    # --- السطر السحري للحفظ ---
    plt.savefig('Unit3_Integration/trapezoid_result.png') 
    
    plt.show()

# تشغيل الكود
plot_trapezoidal(0, 1, 10)