import numpy as np

def gauss_elimination(A, b):
    """
    الوحدة 2: حل نظام معادلات خطية بطريقة حذف غوص
    المدخلات: المصفوفة A، الشعاع b
    المخرجات: الحل التقريبي لكل المتغيرات
    """
    n = len(b)
    # دمج المصفوفة A مع الشعاع b لتكوين المصفوفة الموسعة
    # نستخدم astype(float) لضمان دقة الحسابات العشرية
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1).astype(float)

    print("--- مرحلة الرفع إلى الصيغة المثلثية العلوية ---")
    for i in range(n):
        # البحث عن أكبر عنصر في العمود (Pivot) لضمان استقرار الحل
        max_row = np.argmax(abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]

        # تصفير العناصر الموجودة أسفل القطر الرئيسي
        for j in range(i + 1, n):
            if Ab[i, i] == 0:
                print("خطأ: العنصر القائد يساوي الصفر، النظام قد لا يملك حلاً وحيداً.")
                return None
            
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] = Ab[j, i:] - factor * Ab[i, i:]
    
    print("المصفوفة بعد التحويل (الصيغة المثلثية):")
    print(Ab)

    print("\n--- مرحلة التعويض الرجوعي ---")
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        # حساب قيمة المجهول x[i] بناءً على القيم المحسوبة سابقاً
        sum_ax = np.dot(Ab[i, i+1:n], x[i+1:n])
        x[i] = (Ab[i, n] - sum_ax) / Ab[i, i]
        
    return x

# --- مثال لتشغيل الكود ---