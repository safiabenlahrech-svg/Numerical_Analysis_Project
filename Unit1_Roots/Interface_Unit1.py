import tkinter as tk
from tkinter import messagebox
import numpy as np

# --- الدوال الحسابية ---

def get_derivative(f, x, h=1e-7):
    """حساب المشتقة عددياً عند النقطة x"""
    return (f(x + h) - f(x - h)) / (2 * h)

def run_dichotomie():
    try:
        func_str = ent_f_dicho.get().replace('^', '**')
        f = lambda x: eval(func_str, {"np": np, "x": x, "math": np, "sin": np.sin, "cos": np.cos, "exp": np.exp, "sqrt": np.sqrt})
        a, b = float(ent_a.get()), float(ent_b.get())
        eps = float(ent_dicho_prec.get())
        
        if f(a) * f(b) >= 0:
            messagebox.showerror("خطأ", "f(a) و f(b) لهما نفس الإشارة! لا يمكن ضمان وجود جذر.")
            return
            
        res_text = "=== نتائج طريقة التنصيف (Dichotomie) ===\n"
        res_text += f"{'It':<4} | {'a':<10} | {'b':<10} | {'m':<10} | {'Error':<12}\n"
        res_text += "-"*65 + "\n"
        
        it = 0
        while abs(b - a) > eps and it < 100:
            it += 1
            m = (a + b) / 2
            err = abs(b - a) / 2
            res_text += f"{it:<4} | {a:<10.6f} | {b:<10.6f} | {m:<10.6f} | {err:<12.6e}\n"
            if f(a) * f(m) < 0: b = m
            else: a = m
            
        txt_out.delete('1.0', tk.END)
        txt_out.config(fg="#2E7D32")
        txt_out.insert(tk.END, res_text)
    except Exception as e:
        messagebox.showerror("خطأ", f"تأكد من كتابة الدالة بشكل صحيح: {e}")

def run_newton():
    try:
        f_str = ent_f_newton.get().replace('^', '**')
        # تعريف الدالة مع دعم الدوال الرياضية الأساسية
        f = lambda x: eval(f_str, {"np": np, "x": x, "sin": np.sin, "cos": np.cos, "exp": np.exp, "sqrt": np.sqrt})
        
        x, eps = float(ent_x0.get()), float(ent_newton_prec.get())
        
        res_text = "=== نتائج طريقة نيوتن (الاشتقاق تلقائي) ===\n"
        res_text += f"{'It':<4} | {'x_n':<12} | {'f(x_n)':<12} | {'Error':<12}\n"
        res_text += "-"*55 + "\n"
        
        for it in range(1, 26):
            fx = f(x)
            dfx = get_derivative(f, x) # حساب المشتقة هنا تلقائياً
            
            if abs(dfx) < 1e-12: 
                res_text += f"\nتنبيه: المشتقة قريبة من الصفر عند x = {x}"
                break
                
            x_next = x - fx / dfx
            err = abs(x_next - x)
            res_text += f"{it:<4} | {x:<12.6f} | {fx:<12.6f} | {err:<12.6e}\n"
            
            if err < eps: break
            x = x_next
            
        txt_out.delete('1.0', tk.END)
        txt_out.config(fg="#BF8F00")
        txt_out.insert(tk.END, res_text)
    except Exception as e:
        messagebox.showerror("خطأ", f"خطأ في الحساب: {e}")

# --- بناء الواجهة ---
root = tk.Tk()
root.title("التحليل العددي - ENS Laghouat")
root.geometry("700x800")
root.configure(bg="#89CFF0")

font_label = ("Arial", 11, "bold")

# --- 1. إطار التنصيف ---
frame_dicho = tk.LabelFrame(root, text=" طريقة التنصيف (Dichotomie) ", bg="#E8F5E9", fg="#2E7D32", font=font_label, padx=10, pady=10)
frame_dicho.pack(fill="x", padx=20, pady=10)

tk.Label(frame_dicho, text=" :f(x) الدالة", bg="#E8F5E9").grid(row=0, column=3, sticky="e")
ent_f_dicho = tk.Entry(frame_dicho, width=35, justify="right"); ent_f_dicho.insert(0, "x**2 - 2"); ent_f_dicho.grid(row=0, column=0, columnspan=3, pady=5)

tk.Label(frame_dicho, text=" :a", bg="#E8F5E9").grid(row=1, column=3, sticky="e")
ent_a = tk.Entry(frame_dicho, width=10, justify="right"); ent_a.insert(0, "1"); ent_a.grid(row=1, column=2)

tk.Label(frame_dicho, text=" :b", bg="#E8F5E9").grid(row=1, column=1, sticky="e")
ent_b = tk.Entry(frame_dicho, width=10, justify="right"); ent_b.insert(0, "2"); ent_b.grid(row=1, column=0)

tk.Label(frame_dicho, text=" :الدقة", bg="#E8F5E9").grid(row=2, column=3, sticky="e")
ent_dicho_prec = tk.Entry(frame_dicho, width=10, justify="right"); ent_dicho_prec.insert(0, "0.001"); ent_dicho_prec.grid(row=2, column=2)

tk.Button(frame_dicho, text="حساب التنصيف", command=run_dichotomie, bg="#4CAF50", fg="white", font=font_label).grid(row=3, column=0, columnspan=4, sticky="we", pady=10)

# --- 2. إطار نيوتن (بدون حقل المشتقة) ---
frame_newton = tk.LabelFrame(root, text=" طريقة نيوتن (Newton) ", bg="#FFF9C4", fg="#FBC02D", font=font_label, padx=10, pady=10)
frame_newton.pack(fill="x", padx=20, pady=10)

tk.Label(frame_newton, text=" :f(x) الدالة", bg="#FFF9C4").grid(row=0, column=3, sticky="e")
ent_f_newton = tk.Entry(frame_newton, width=35, justify="right"); ent_f_newton.insert(0, "x**2 - 2"); ent_f_newton.grid(row=0, column=0, columnspan=3, pady=5)

tk.Label(frame_newton, text=" :x0", bg="#FFF9C4").grid(row=1, column=3, sticky="e")
ent_x0 = tk.Entry(frame_newton, width=10, justify="right"); ent_x0.insert(0, "1.5"); ent_x0.grid(row=1, column=2)

tk.Label(frame_newton, text=" :الدقة", bg="#FFF9C4").grid(row=1, column=1, sticky="e")
ent_newton_prec = tk.Entry(frame_newton, width=10, justify="right"); ent_newton_prec.insert(0, "1e-6"); ent_newton_prec.grid(row=1, column=0)

tk.Button(frame_newton, text="حساب نيوتن", command=run_newton, bg="#FBC02D", fg="white", font=font_label).grid(row=2, column=0, columnspan=4, sticky="we", pady=10)

# --- 3. منطقة النتائج ---
tk.Label(root, text=" :لوحة النتائج التفصيلية", bg="#89CFF0", font=font_label).pack(anchor="e", padx=20)
txt_out = tk.Text(root, height=15, bg="white", font=("Courier New", 10))
txt_out.pack(padx=20, pady=10, fill="both", expand=True)

root.mainloop()