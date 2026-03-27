import numpy as np

def jacobi_method(A, b, x0, tol=1e-6, max_iter=100):
    """
    الوحدة 2: حل نظام معادلات خطية بطريقة يعقوبي
    المدخلات: المصفوفة A، الشعاع b، الحل الأولي x0، الدقة tol
    """
    n = len(b)
    x = x0.copy().astype(float)
    x_new = np.zeros(n)
    
    # استخراج عناصر القطر الرئيسي
    diag = np.diag(A)
    # مصفوفة العمليات (A بدون القطر الرئيسي)
    R = A - np.diag(diag)
    
    print("-" * 60)
    print(f"{'التكرار':<10} | {'الحل التقريبي':<35} | {'الخطأ':<10}")
    print("-" * 60)
    
    for k in range(max_iter):
        # قانون يعقوبي: x_new = (b - R*x_old) / diag
        x_new = (b - np.dot(R, x)) / diag
        
        # حساب الخطأ (الفرق المطلق الأكبر بين التكرارين)
        error = np.linalg.norm(x_new - x, ord=np.inf)
        
        # طباعة سطر الجدول المطلوب في المشروع
        print(f"{k+1:<10} | {str(np.round(x_new, 4)):<35} | {error:.2e}")
        
        # شرط التوقف (الدقة المطلوبة)
        if error < tol:
            print("-" * 60)
            print("تم الوصول إلى الدقة المطلوبة بنجاح.")
            return x_new, k + 1
            
        x = x_new.copy()
        
    print("-" * 60)
    print("تنبيه: تم الوصول للحد الأقصى من التكرارات.")
    return x, max_iter

# --- مثال لتشغيل الكود ---
# المصفوفة A والشعاع b [cite: 51, 52]
A_mat = np.array([[10, -1, 2], 
                  [-1, 11, -1], 
                  [2, -1, 10]])

b_vec = np.array([6, 25, -11])
initial_x = np.zeros(len(b_vec))

# استدعاء الدالة
final_solution, iters = jacobi_method(A_mat, b_vec, initial_x)

print("\nالحل النهائي للمتغيرات:")
print(final_solution)