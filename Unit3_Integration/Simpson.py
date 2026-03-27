import numpy as np
import matplotlib.pyplot as plt

# 1. تعريف الدالة (نفس الدالة للمقارنة)
def f(x):
    return x**2

def simpson_13_plot(a, b, n):
    # ملاحظة: n يجب أن يكون عدداً زوجياً في طريقة سيمبسون
    if n % 2 != 0:
        n += 1  # تصحيح تلقائي لضمان عمل الخوارزمية
        
    h = (b - a) / n
    x_simpson = np.linspace(a, b, n + 1)
    y_simpson = f(x_simpson)
    
    # --- حساب التكامل بقانون سيمبسون ---
    # القانون: (h/3) * [f(x0) + 4*sum(f_odd) + 2*sum(f_even) + f(xn)]
    integral = y_simpson[0] + y_simpson[-1]
    integral += 4 * np.sum(y_simpson[1:-1:2]) # النقاط الفردية
    integral += 2 * np.sum(y_simpson[2:-2:2]) # النقاط الزوجية
    integral = (h / 3) * integral
    
    print(f"قيمة التكامل بطريقة سيمبسون هي: {integral:.6f}")

    # --- الجزء الخاص بالرسم البياني ---
    x_fine = np.linspace(a, b, 200)
    plt.plot(x_fine, f(x_fine), 'r', label='f(x) = x^2')
    
    # تظليل المساحة (سيمبسون يميل لاستخدام منحنيات بارابولية)
    plt.fill_between(x_simpson, y_simpson, color='lightgreen', alpha=0.5, label='Simpson 1/3 Area')
    
    plt.title(f"Simpson's 1/3 Rule (n={n}, Result={integral:.4f})")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    
    # حفظ المنحنى في مجلد الوحدة الثالثة
    plt.savefig('Unit3_Integration/simpson_result.png')
    plt.show()

# تشغيل الكود (المجال من 0 إلى 1 بـ 10 تقسيمات)
simpson_13_plot(0, 1, 10)