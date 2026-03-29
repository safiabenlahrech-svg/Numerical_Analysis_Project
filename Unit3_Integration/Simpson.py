import numpy as np
import matplotlib.pyplot as plt
import os
import math


# إنشاء المجلد إذا لم يكن موجوداً لضمان عدم حدوث خطأ
folder = 'Unit3_Integration'
if not os.path.exists(folder):
    os.makedirs(folder)

# 1. تعريف الدالة المراد تكاملها (مثلاً f(x) = exp(x)
def f(x):
    return np.exp(x)

def simpson_full_project(a, b, n):
    # سيمبسون يتطلب n زوجي
    if n % 2 != 0: n += 1
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    # 2. حساب قيمة التكامل بالقانون
    integral = (h/3) * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))
    
    print(f"--- النتيجة النهائية ---")
    print(f"قيمة التكامل التقريبية: {integral:.6f}")
    
    # 3. الجزء الخاص بالرسم البياني الاحترافي
    x_curve = np.linspace(a, b, 100)
    y_curve = f(x_curve)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x_curve, y_curve, 'r', label='f(x) = exp(x)', linewidth=2)
    
    # تظليل المساحة (تقريب سيمبسون)
    plt.fill_between(x, y, color='skyblue', alpha=0.4, label='Simpson Area')
    plt.scatter(x, y, color='black', s=15) # نقاط التقسيم
    
    plt.title(f"Simpson's 1/3 Rule (n={n}, Result={integral:.4f})")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # 4. الحفظ التلقائي (هذا أهم سطر لتجدي الرسمة)
    image_path = os.path.join(folder, 'simpson_final_plot.png')
    plt.savefig(image_path)
    print(f"تم حفظ الرسمة بنجاح في: {image_path}")
    
    plt.show()

# تشغيل المشروع
simpson_full_project(a=0, b=1, n=10)