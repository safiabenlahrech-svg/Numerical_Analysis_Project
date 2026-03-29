import math
def f(x): 
    # تعريف الدالة: يمكنك تغييرها حسب المسألة
    return x**2 - 2
def methode_dichotomie(a, b, E, N ):
    # التحقق من شرط الإشارة
    if f(a) * f(b) > 0:
        print(" لا يوجد حل في هذا المجال")
        return None

    print(f"{'Iter':<10} | {'x':<15} | {'Error':<15}")
    
    for i in range(1, N + 1):
        c = (a + b) / 2
        error = abs(b - a) / 2
        
    
        print(f"{i:<10} | {c:<15.8f} | {error:<15.8e}")

        # شرط التوقف
        if error < tol or f(c) == 0:
            return c

        # تحديث المجال
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

            # التعديل هنا: إذا خرجنا من الحلقة بلا ما يتحقق شرط error < tol
    print("\nتنبيه: تم الوصول للحد الأقصى من الدورات دون تحقيق الدقة المطلوبة.")
    return c

# تشغيل الطريقة
result = methode_dichotomie(1, 2, 0.0001, 20)
print(f"\nالنتيجة النهائية: {result}")
