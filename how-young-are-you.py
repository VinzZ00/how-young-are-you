from random import random 
from datetime import date

def pengeccekan_leapYear(tanggal, bulan, tahun) :
    if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0) :
        return "Leap Year"
    else :
        return "Not a Leap year"

def pengecekan_Umur(tangal, bulan, tahun) :
    if tahun > currentyear :
            print ("kamu telah salah memasukan tahun")
            raise Exception
    elif tahun == currentyear :
        if bulan == currentmonth :
                umurhari = currentdate - tanggal
                print ("Hallo babe, umur mu {} hari".format(umurhari))
        if bulan < currentmonth :
                umurbulan = currentmonth - bulan
                umurhari = currentdate - tanggal
                print("Hallow babe, umur mu {} bulan dan {} hari\n".format(umurbulan,umurhari))
        elif bulan > currentmonth :
                print("Tolong masukan bulan yang benar")
                raise Exception
    elif tahun < currentyear :
        if bulan == currentmonth :
            if tanggal > currentdate :
                    umur = (currentyear - tahun) - 1
            if tanggal <= currentdate :
                    umur = currentyear - tahun
        if bulan < currentmonth :
            umur = currentyear - tahun
        if bulan > currentmonth :
            umur = (currentyear - tahun) - 1 
        return umur  
currentdate = date.today()
print ("\ntoday's date ..", currentdate, "\n=========================================\n")

currdate = str(currentdate).split("-")
currentyear = int(currdate[0])
currentmonth = int(currdate[1])
currentdate = int(currdate[2])

while True :
    print ('there is a proverbs said that \n"your maturity are not defined by your age."\n====================================================\n')
    print ("welcome to how young are you?")
    print("1. start liat seberapa mudanya anda?")
    print("2. Exit")
    choose = int(input(">>_ "))
    x = False
    if (choose == 2) :
        print("Terima kasih telah bermain bersama saya")
        break
    elif(choose == 1) :
        while True :
            dateinput = input("Masukan Tanggal yang ingin anda cek")
            # print(date.__len__())
            if(len(dateinput) == 8) :
                # print(int(date[0:2]))
                try :
                    tanggal = int(dateinput[0:2]) 
                    bulan = int(dateinput[2:4])
                    tahun = int(dateinput[4:8])
                except :
                    print("Tolong masukan angka saja")
                # if type(date) is int :
                else :
                    print()
                    break
                # else :
                #     print("kamu telah menepati format 8 char but, Tolong masukan angka saja")
            else :
                print("Tolong input panjang 8 angka saja") 
        checkleap = pengeccekan_leapYear(tanggal, bulan, tahun)
        if bulan < 13 and bulan > 0 :
            if checkleap.__eq__("Leap Year") :
                if bulan == 2 :
                    if tanggal > 0 and tanggal < 30 :
                        x = True
                    else :
                        print("Tolonag masukan tanggal yang benar bulan ini hanya mempunyai 29 hari karena bulan 2 tahun kabisat")
                elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 and bulan == 10 and bulan == 12 :
                    if tanggal > 0 and tanggal <= 31 :
                        x = True
                    else :
                        print("Tolonag masukan tanggal yang benar bulan ini hanya mempunyai 31 hari")
                elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11 :
                    if tanggal > 0 and tanggal <= 30 :
                        x = True
                    else :
                        print("Tolonag masukan tanggal yang benar bulan ini hanya mempunyai 30 hari")
            elif checkleap.__eq__("Not a Leap year") :
                if bulan == 2 :
                    if tanggal > 0 and tanggal < 29 :
                        x = True
                    else :
                        print("Tolonag masukan tanggal yang benar bulan ini hanya mempunyai 28 hari karena bulan 2 tahun  non-kabisat")
                elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 and bulan == 10 and bulan == 12 :
                    if tanggal > 0 and tanggal <= 31 :
                        x = True
                    else :
                        print("Tolonag masukan tanggal yang benar bulan ini hanya mempunyai 31 hari")
                elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11 :
                    if tanggal > 0 and tanggal <= 30 :
                        x = True
                    else :
                        print("Tolong masukan tanggal yang benar bulan ini hanya mempunyai 30 hari")
            print ("anda lahir pada tahun ", tahun) 
            print ("anda lahir pada bulan ", bulan) 
            print ("anda lahir pada tanggal {}".format(tanggal))

            
        else : 
            print("Tolong format masukan bulan yang benar")
        umur = pengecekan_Umur(tanggal, bulan, tahun)
        if (umur != None) :
            print("\numur anda adalah {} \n".format(umur))
        input("Press enter to continue..")

    

                            




