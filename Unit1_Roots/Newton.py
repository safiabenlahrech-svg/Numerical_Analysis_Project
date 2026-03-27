import math

def f(x):
    """الدالة المراد حلها f(x) = 0"""
    return x**2 - 2  # مثال: حساب جذر 2

def df(x):
    """مشتقة الدالة f'(x) - ضرورية لطريقة نيوتن"""
    return 2*x

def newton_method(x0, tol, max_iter):
    """
    الوحدة 1: حل معادلة غير خطية بطريقة نيوتن
    المدخلات: نقطة الانطلاق x0، الدقة tol، وعدد التكرارات [cite: 27, 28]
    """
    
    print("-" * 55)
    print(f"{'التكرار':<10} | {'x_n':<15} | {'الخطأ تقديري':<15}")
    print("-" * 55)

    x = x0
    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        
        # التأكد من أن المشتقة لا تساوي الصفر لتجنب القسمة على صفر
        if dfx == 0:
            print("خطأ: المشتقة تساوي الصفر. لا يمكن الاستمرار.")
            return None
            
        # قانون نيوتن: x_{n+1} = x_n - f(x_n)/f'(x_n)
        x_new = x - fx / dfx
        
        # حساب الخطأ (الفرق بين قيمتين متتاليتين) [cite: 40]
        error = abs(x_new - x)
        
        # طباعة السطر في الجدول [cite: 39]
        print(f"{i:<10} | {x_new:<15.8f} | {error:<15.8e}")

        # شرط التوقف بناءً على الدقة المطلوبة
        if error < tol:
            print("-" * 55)
            print(f"تم إيجاد الحل التقريبي: {x_new:.8f}")
            return x_new
            
        x = x_new

    print("-" * 55)
    print("تنبيه: تم الوصول للحد الأقصى من التكرارات.")
    return x

# --- تجربة الكود ---
# إدخال البيانات حسب المطلوب [cite: 27, 28]
point_zero = 1.5    # نقطة الانطلاق x0
precision = 1e-6    # الدقة (Error)
max_steps = 20      # عدد التكرارات

result = newton_method(point_zero, precision, max_steps)