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


import termcolor
import pyfiglet
from tkinter import *
from datetime import timedelta
import random



def main():


    root = Tk()
    root.title("Modulation and Simulation")
    root.geometry('900x400')  # تعيين حجم النافذة

    # إنشاء عنوان نافذة التطبيق
    Title = Label(root, text="TP Modulation and simulation".title(), font=("Arial", 16))
    Title.grid(row=0, column=0, columnspan=8)

    # إنشاء تسمية لإدخال عدد العمال
    Text_Numbers = Label(root, text="Enter Number", font=("Arial", 16))
    Text_Numbers.grid(row=1, column=1)

    # مربع نص لإدخال عدد العمال
    numbers = Entry(root, width=4, border=3)
    numbers.grid(row=1, column=2)

    # زر "Run" لتشغيل الكود
    Run = Button(root, text="Run", font=("Arial", 17), width=13, command=lambda: Run_code(tp2(int(numbers.get()))))
    Run.grid(row=1, column=6)

    # إنشاء أطار التمرير (Canvas) للعرض
    canvas = Canvas(root, borderwidth=0)
    canvas.grid(row=2, column=0, columnspan=8, rowspan=3, sticky="nsew")

    # إنشاء Scrollbar رأسي
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=2, column=6, rowspan=3, sticky="ns")
    canvas.config(yscrollcommand=scrollbar.set)

    # إنشاء إطار داخل أطار التمرير لاستضافة العناصر Label
    scrollable_frame = Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # توسيع الإطار لكامل النص من الغرب إلى الشرق
    root.grid_rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)
    scrollable_frame.grid_rowconfigure(0, weight=1)
    scrollable_frame.grid_columnconfigure(0, weight=1)

    def mint(str):
        
        hours, minutes, seconds = map(int, str.split(':'))
        total_minutes = (hours * 60) + minutes

        return total_minutes



    def tp1(number_of):
        # قوائم تخزن فيها البيانات
        numbers_list = ['Numéro Client']
        start_list = ['Date Arrivée']
        Durée_Service_list = ['Durée de Service']
        start = 8 * 60
        fin = 16*60
        listData=[]
        for x in range(1, number_of + 1):
            # إنشاء رقم عشوائي للمدة الزمنية
            Ds = random.randint(3, 5)
            numbers_list.append(f'{x}')
            start_list.append(f'{timedelta(minutes=start)}')
            Durée_Service_list.append(f'{Ds} min')
            # tsgar_list.append(f'{timedelta(minutes=tsgar)}')
            start += random.randint(3, 5)
            if start > fin:
                break
            
        # تنظيم البيانات في القوائم
        listData.append('\n'.join(numbers_list))
        listData.append('\n'.join(start_list))
        listData.append('\n'.join(Durée_Service_list))
        
        
        return listData 

    def tp2(number_of):
        global dict_client
        global list_dates
        dict_client = {}
        global Date_Arrivée
        global Temps_dattente_moyen_par_client
        global Temps_moyen_passé_par_un_client_dans_le_système
            # قوائم تخزن فيها البيانات
        numbers_list = ['Numéro Client']
        Date_Arrivée_list = ['Date Arrivée']
        Date_Debut_de_Servce_list = ['Date Début Service']
        Durée_Service_list = ['Durée de Service']
        Date_Fin_Service_list = ["Date Fin Service"]
        Temps_dattente_list = ["Temps D'attente"]
        Temps_passé_Dans_le_système_list = ["Temps Passé Dans le Système"]
        list_dates = []
        Date_Arrivée = 8 * 60
        Date_Debut_de_Servce = Date_Arrivée
        fin = 16*60
        listData=[]
        total_Temps_dattente = 0
        total_Temps_passé_Dans_le_système = 0
        for x in range(1, number_of + 1):
            
            # إنشاء رقم عشوائي للمدة الزمنية
            Durée_Service = random.randint(3, 5)
            Temps_dattente =  Date_Debut_de_Servce - Date_Arrivée
            total_Temps_dattente+=Temps_dattente
            Temps_dattente_list.append(f'{Temps_dattente} min')
            Date_Fin_Service  = Date_Debut_de_Servce+Durée_Service
            Temps_passé_Dans_le_système = Date_Fin_Service - Date_Arrivée
            total_Temps_passé_Dans_le_système+=Temps_passé_Dans_le_système
            Temps_passé_Dans_le_système_list.append(f'{Temps_passé_Dans_le_système} min')
            Date_Debut_de_Servce_list.append(f'{timedelta(minutes=Date_Debut_de_Servce)}')
            Date_Fin_Service_list.append(f'{timedelta(minutes=Date_Fin_Service)}')
            numbers_list.append(f'{x}')
            Date_Arrivée_list.append(f'{timedelta(minutes=Date_Arrivée)}')
            Durée_Service_list.append(f'{Durée_Service} min')
            Date_Debut_de_Servce+=Durée_Service
            list_dates.append(Date_Arrivée)
            list_dates.append(Date_Fin_Service)
            Date_Arrivée += random.randint(3, 5)
            while Date_Debut_de_Servce<Date_Arrivée:
                Date_Debut_de_Servce+=1
            # tsgar_list.append(f'{timedelta(minutes=tsgar)}')
            if Date_Arrivée > fin:
                break
        Temps_dattente_list.append(f'Total = {total_Temps_dattente}')
        Temps_passé_Dans_le_système_list.append(f'Total = {total_Temps_passé_Dans_le_système}')
            
        # تنظيم البيانات في القوائم
        listData.append('\n'.join(numbers_list))
        listData.append('\n'.join(Date_Arrivée_list))
        listData.append('\n'.join(Date_Debut_de_Servce_list))
        listData.append('\n'.join(Durée_Service_list))
        listData.append('\n'.join(Date_Fin_Service_list))
        listData.append('\n'.join(Temps_dattente_list))
        listData.append('\n'.join(Temps_passé_Dans_le_système_list))
        Temps_dattente_moyen_par_client = f"TDMC:{total_Temps_dattente}/{number_of}={total_Temps_dattente/number_of}"  
        Temps_moyen_passé_par_un_client_dans_le_système =f"TMPCS :{total_Temps_passé_Dans_le_système}/{number_of} = {total_Temps_passé_Dans_le_système/number_of }" 
        dict_client = list(zip(numbers_list,Date_Arrivée_list,Date_Fin_Service_list))


        return listData

    # ________ Tp 3 it's not over ______#
    """
    def tp3():
        Date_Evénement = 0
        Numéro_Client= 0
        Type_Evénement=0
        Nombre_dans_la_file=0
        Nombre_dans_le_système=0
        Etat_du_Serveur=0
        Temps_Libre_du_Serveur=0
        Date_Evénement_list =         ["Date Evénement"]
        Numéro_Client_list =          ["Numéro Client"]
        Type_Evénement_list =         ["Type Evénement list"]
        Nombre_dans_la_file_list =    ["Nombre dans la file list"]
        Nombre_dans_le_système_list = ["Nombre dans le système list"]
        Etat_du_Serveur_list =        ["Etat du Serveur list"]
        Temps_Libre_du_Serveur_list = ["Temps Libre du Serveur list"]
        for x in range(1,len(dict_client)+1) :
            while Type_Evénement != "Depart":
                if Date_Evénement == 0:
                    Date_Evénement.append(f"0")
                    Numéro_Client_list.append(f"-")
                    Type_Evénement_list.append(f"Debut")
                    Nombre_dans_la_file_list.append(f"0")
                    Nombre_dans_le_système_list.append(f"0")
                    Etat_du_Serveur_list.append(f"libre")
                    Temps_Libre_du_Serveur_list.append(f"-")
                    Date_Evénement = mint(dict_client[x][1])
                else:
                    
                    if dict_client[x][0] == x :
                        Date_Evénement = mint(dict_client[x][1])
                        Date_Evénement_list.append(f"{Date_Evénement}")
                        Numéro_Client = dict_client[x][0]
                        if Numéro_Client not in Numéro_Client_list:
                            Numéro_Client_list.append(f"{Numéro_Client}")
                            Type_Evénement = "Arrivee"
                            Type_Evénement_list.append(f"{Type_Evénement}")
                        else :
                            Type_Evénement = "Depart"
                            Type_Evénement_list.append(f"{Type_Evénement}")
                            
                        Nombre_dans_le_système_list.append(f"0")
                        Etat_du_Serveur_list.append(f"occupe")
                        Temps_Libre_du_Serveur_list.append(f"3.2")
    """
    # ________ Tp 3 it's not over ______#
    def Run_code(lists):
        # عرض البيانات في واجهة المستخدم
        num = Label(scrollable_frame, text=lists[0], relief=RIDGE, font=("Arial", 16))
        num.grid(row=2, column=0)
        Date_Arrivée = Label(scrollable_frame, text=lists[1], relief=RIDGE, font=("Arial", 16))
        Date_Arrivée.grid(row=2, column=1)
        Date_Début_Service = Label(scrollable_frame, text=lists[2], relief=RIDGE, font=("Arial", 16))
        Date_Début_Service.grid(row=2, column=2)
        Durée_Service = Label(scrollable_frame, text=lists[3], relief=RIDGE, font=("Arial", 16))
        Durée_Service.grid(row=2, column=3)
        Date_Fin_Service_lab = Label(scrollable_frame, text=lists[4], relief=RIDGE, font=("Arial", 16))
        Date_Fin_Service_lab.grid(row=2, column=4)
        Temps_Dattents = Label(scrollable_frame, text=lists[5], relief=RIDGE, font=("Arial", 16))
        Temps_Dattents.grid(row=2, column=5)
        Temps_passé_Dans_le_système = Label(scrollable_frame, text=lists[6], relief=RIDGE, font=("Arial", 16))
        Temps_passé_Dans_le_système.grid(row=2, column=6)
        total_Temps_dattente_moyen_par_client= Label(scrollable_frame, text=Temps_dattente_moyen_par_client, relief=RIDGE, font=("Arial", 16))
        total_Temps_dattente_moyen_par_client.grid(row=3, column=6)
        total_Temps_moyen_passé_par_un_client_dans_le_système= Label(scrollable_frame, text=Temps_moyen_passé_par_un_client_dans_le_système, relief=RIDGE, font=("Arial", 16))
        total_Temps_moyen_passé_par_un_client_dans_le_système.grid(row=4, column=6)
        # تحديث الأطار التمرير
        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))




    mainloop()





print(termcolor.colored(pyfiglet.figlet_format("@ddos_attack_co"), color="red"))

print(" Go to my Instagram account < @ddos_attack_co > and Fallowed Me \n Enter...", end="")
enter = input("")
main()

print(termcolor.colored(pyfiglet.figlet_format("THANCKS"), color="red"))

