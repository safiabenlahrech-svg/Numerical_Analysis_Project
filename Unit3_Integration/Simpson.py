import numpy as np

def f(x):
    return x**2  # الدالة المراد تكاملها

def simpson_rule(a, b, n):
    if n % 2 != 0: n += 1  # تصحيح n ليصبح زوجياً
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    # تطبيق قانون سمبسون 1/3
    integral = (h/3) * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))
    return integral

# تجربة الطريقة لعدة قيم n
a, b = 0, 1
for n_val in [4, 10, 100]:
    val = simpson_rule(a, b, n_val)
    print(f"n = {n_val} | النتيجة التقريبية: {val:.8f}")