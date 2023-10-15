# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------

#install this
#pip install termcolor
#pip install pyfiglet


from datetime import timedelta
import random
from tkinter import *
import termcolor
import pyfiglet
def main():
    root  = Tk()
    root.title("Modulation and Simulation")

    # إنشاء عنوان نافذة التطبيق
    Title = Label(root, text="TP Modulation and simulation".title(), font=("Arial", 16))
    Title.grid(row=0, column=0, columnspan=4)

    # إنشاء تسمية لإدخال عدد العمال
    Text_Numbers = Label(root, text="Enter Number", font=("Arial", 16))
    Text_Numbers.grid(row=1, column=0)

    # مربع نص لإدخال عدد العمال
    numbers = Entry(root, width=4, border=3)
    numbers.grid(row=1, column=1)

    # زر "Run" لتشغيل الكود
    Run = Button(root, text="Run", font=("Arial", 17), width=13, command=lambda: Run_code(tp1(int(numbers.get()))))
    Run.grid(row=1, column=2)

    def tp1(number_of):
        # قوائم تخزن فيها البيانات
        numbers_list = ['Number']
        start_list = ['Start Time']
        end_list = ['End Time']
        tsgar_list = []
        Ds_list = ['Duration (minutes)']

        start = 8 * 60
        tsgar = 0
        fin = 16*60

        listData = []

        for x in range(1, number_of + 1):
            # إنشاء رقم عشوائي للمدة الزمنية
            Ds = random.randint(10, 30)
            tsgar += Ds
            # إضافة البيانات إلى القوائم
            numbers_list.append(f'{x}')
            start_list.append(f'{timedelta(minutes=start)}')
            Ds_list.append(f'00:{Ds}')
            # tsgar_list.append(f'{timedelta(minutes=tsgar)}')
            start += Ds
            end_list.append(f'{timedelta(minutes=start)}')
            if start > fin:
                break

        # تنظيم البيانات في القوائم
        listData.append('\n'.join(numbers_list))
        listData.append('\n'.join(start_list))
        listData.append('\n'.join(Ds_list))
        listData.append('\n'.join(end_list))
        
        return listData

    def Run_code(lists):
        # عرض البيانات في واجهة المستخدم
        num = Label(root, text=lists[0], relief=RIDGE, font=("Arial", 16)).grid(row=2, column=0)
        start = Label(root, text=lists[1], relief=RIDGE, font=("Arial", 16)).grid(row=2, column=1)
        Ds = Label(root, text=lists[2], relief=RIDGE, font=("Arial", 16)).grid(row=2, column=2)
        end = Label(root, text=lists[3], relief=RIDGE,font=("Arial", 16)).grid(row=2, column=3)

    mainloop()

print(termcolor.colored(pyfiglet.figlet_format("@ddos_attack_co"), color="red"))

print(" Go to my Instagram account < @ddos_attack_co > and Fallowed Me \n Enter...", end="")
enter = input("")
main()

print(termcolor.colored(pyfiglet.figlet_format("THANCKS"), color="red"))
