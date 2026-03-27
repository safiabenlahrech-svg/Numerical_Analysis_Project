import numpy as np

def f(x):
    # نكتب هنا الدالة المراد تكاملها (مثال: x مربع)
    return x**2

def trapezoidal_rule(a, b, n):
    """
    a: بداية المجال
    b: نهاية المجال
    n: عدد التقسيمات (كلما زاد زادت الدقة)
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # قانون الشبه منحرف: (h/2) * [f(a) + 2*sum(f(xi)) + f(b)]
    s = y[0] + y[-1] + 2 * np.sum(y[1:-1])
    integral = (h / 2) * s
    return integral

# تجربة الكود: تكامل x^2 من 0 إلى 1 بـ 10 تقسيمات
result = trapezoidal_rule(0, 1, 10)
print(f"نتيجة التكامل التقريبية هي: {result}")