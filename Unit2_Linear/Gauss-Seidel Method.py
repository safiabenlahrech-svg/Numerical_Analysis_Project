import numpy as np

def gauss_elimination(A, b):
    """
    الوحدة 2: حل نظام معادلات خطية بطريقة حذف غوص
    المدخلات: المصفوفة A، الشعاع b
    """
    n = len(b)
    # دمج المصفوفة A مع الشعاع b لتكوين المصفوفة الموسعة (Augmented Matrix)
    # نستخدم float لضمان دقة الحسابات العشرية
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)

    print("--- مرحلة الرفع إلى الصيغة المثلثية العلوية ---")
    for i in range(n):
        # البحث عن أكبر عنصر في العمود (Pivot) لزيادة الاستقرار العددي
        max_row = np.argmax(abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]

        for j in range(i + 1, n):
            if Ab[i, i] == 0:
                print("خطأ: العنصر القائد يساوي الصفر!")
                return None
            
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] = Ab[j, i:] - factor * Ab[i, i:]
    
    print("المصفوفة بعد الحذف:")
    print(Ab)

    print("\n--- مرحلة التعويض الرجوعي ---")
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, n] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
        
    return x

# --- مثال لتشغيل الكود ---
# نظام معادلات: 
# 3x + 2y - z = 1
# 2x - 2y + 4z = -2
# -x + 0.5y - z = 0

matrix_A = np.array([[3, 2, -1], 
                     [2, -2, 4], 
                     [-1, 0.5, -1]])

vector_b = np.array([1, -2, 0])

solution = gauss_elimination(matrix_A, vector_b)

if solution is not None:
    print("\nالحل التقريبي للمتغيرات")