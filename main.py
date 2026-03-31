import os
from colorama import Fore, Back, Style, init

# استيراد الدوال من المجلدات التي أنشأتِها
# تأكدي أن أسماء الدوال تطابق ما كتبتِهِ داخل الملفات
try:
    from Unit1_Roots.Dichotomie import solution_dichotomie
    from Unit1_Roots.Newton import solution_newton
    # من المفترض أنكِ برمجتِ هذه الدوال أيضاً:
    # from Unit2_Linear.Gauss import solution_gauss
    # from Unit3_Integration.Simpson import solution_simpson
    # from Unit4_Diff.Derivee import calculate_diff
except ImportError:
    pass # لتجنب التوقف إذا كانت بعض الملفات فارغة حالياً

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print(Fore.CYAN + Style.BRIGHT + "==================================================")
        print(Fore.YELLOW + Style.BRIGHT + "   تطبيق التحليل العددي - ENS Laghouat 2025/2026")
        print(Fore.CYAN + Style.BRIGHT + "==================================================")
        print(Fore.WHITE + "1. " + Fore.GREEN + "الوحدة 1: حل معادلة غير خطية f(x)=0")
        print(Fore.WHITE + "2. " + Fore.GREEN + "الوحدة 2: حل نظام معادلات خطية Ax=B")
        print(Fore.WHITE + "3. " + Fore.GREEN + "الوحدة 3: التكامل العددي")
        print(Fore.WHITE + "4. " + Fore.GREEN + "الوحدة 4: الاشتقاق العددي")
        print(Fore.RED + "5. خروج")
        print(Fore.CYAN + "--------------------------------------------------")
        
        choix = input(Fore.YELLOW + "اختر رقم الوحدة: " + Fore.WHITE)

        if choix == "1":
            menu_unite1()
        elif choix == "2":
            menu_unite2()
        elif choix == "3":
            menu_unite3()
        elif choix == "4":
            menu_unite4()
        elif choix == "5":
            print(Fore.RED + "بالتوفيق! وداعاً.")
            break

def menu_unite1():
    clear_screen()
    print(Back.GREEN + Fore.BLACK + " --- الوحدة 1: حل المعادلات غير الخطية --- ")
    print("1. طريقة التنصيف (Dichotomie)")
    print("2. طريقة نيوتن (Newton)")
    m = input(Fore.YELLOW + "اختر الطريقة: ")
    # هنا تطلبين f(x) والمجال [a,b] أو x0
    input(Fore.CYAN + "\nاضغط Enter للعودة...")

def menu_unite2():
    clear_screen()
    print(Back.BLUE + Fore.WHITE + " --- الوحدة 2: حل جملة معادلات خطية --- ")
    print("1. حذف غوص (Gauss)")
    print("2. طريقة يعقوبي (Jacobi)")
    print("3. غوص-سيدل (Gauss-Seidel)")
    m = input(Fore.YELLOW + "اختر الطريقة: ")
    # هنا تطلبين المصفوفة A والشعاع B
    input(Fore.CYAN + "\nاضغط Enter للعودة...")

def menu_unite3():
    clear_screen()
    print(Back.RED + Fore.WHITE + " --- الوحدة 3: التكامل العددي --- ")
    print("1. طريقة شبه المنحرف")
    print("2. طريقة سمبسون")
    # هنا تطلبين الدالة f والمجال و n
    input(Fore.CYAN + "\nاضغط Enter للعودة...")

def menu_unite4():
    clear_screen()
    print(Back.YELLOW + Fore.BLACK + " --- الوحدة 4: الاشتقاق العددي --- ")
    print("1. فروق أمامية")
    print("2. فروق خلفية")
    print("3. فروق مركزية")
    # هنا تطلبين x0 و h
    input(Fore.CYAN + "\nاضغط Enter للعودة...")

if __name__ == "__main__":
    main()