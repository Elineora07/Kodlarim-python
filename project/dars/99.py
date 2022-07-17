# 1. KIRITILGAN MATNNI SIMETRIK(CHAPDAN, O'ZINGDAN BIR XIL O'QILADIGAN)EKANLIGINI TEKSHIRISH.
#MISOL: UKKI -> TRUE, IKKI -> TRUE, SALOM ->FALSE.
# 2. KIRITILGAN MATNDAGI KATTA HARFLARNI 1 RAQAMI BILAN ALMASHTIRADIGAN DASTUR TUZING:
# MISOL: Salom DUnYO -> 1alom 11n11
# 3. KIRITILGAN MATNDAGI SONLARNING O'ZINI CHIQARADIGAN DASTUR TUZING:
# MISOL: Salom 123Dunyo333Nima2 -> 1233332
# 4. KIRITILGAN MATNDAGI SO'ZLAR SONINI ANIQLAYDIGAN DASTUR (MATN FAQAT LOTIN HARFLARIDA ' ' PROBEL BO'LADI)
# MISOL: Salom dunyo maktab -> 3
# 5. KIRITILGAN MATNDAGI JUFT O'RINDAGI HARFLAR KICHIK HARFDA, TOQ O'RINDAGI HARFLARNI KATTA HARFLARDA CHIQARADIGAN DASTUR TUZING:
# MISOL: Salom Maktab -> sAlOm mAkTaB
# 6. KIRITILGAN IKKITA MATNDAGI BIR XIL O'RINDA JOYLASHGAN HARFLAR SONINI ANIQLAYDIGAN DASTUR TUZING:
# MISOL: Maktab
#        Maktub 
#        Natija:5 
# 1 - MISOL:
# print("1 - misol")
# a = input("So'z = ")
# if a == "UKKI":
#     print("TURE")
# elif a == "IKKI":
#     print("TRUE")
# else:
#     print("FALSE")

# 2 - MISOL:
# print("2 - misol")
# harf = "Salom DUnYO"
# harf = harf.replace("S", "1")
# harf = harf.replace("DU", "11")
# harf = harf.replace("YO", "11")
# print(harf)

# # 3 - MISOL:
# print("3-misol")
# son = "Salom 123Dunyo333Nima2"
# son = son.isdigit()
# print(son)

# 4 - MISOL:
# print("4 - misol")
# soz = "Salom dunyo maktab, Salom dunyo maktab, Salom dunyo maktab"
# soz = soz.count("Salom dunyo maktab")
# print(soz)

# 5 - MISOL:
# print("5 - misol")
# soz = "SaLoM MaKtAb"
# soz = soz.swapcase()
# print(soz)

# 6 - MISOL:
# print("6 - misol")
# soz = "Maktb Maktb Maktb Maktb Maktb "
# soz = soz.count("Maktb")
# print(soz)

# from speedtest import Speedtest
# st = Speedtest()

# print("Download :",st.download())
# print("Upload :",st.upload())

# st.get_servers([])
# print("Ping :",st.results.ping)









# import calendar

# year = int(input("year: "))
# month = int(input("month: "))
# print(calendar.month(year, month))

# import calendar

# yil=int(input("yil: "))
# oy=int(input("oy: "))
# print(calendar.month(yil, oy,))


# ism = input("Ismimgiz ")
# ty = int(input("Tug'ilgan ylingiz "))
# print("Assalomu aleykum", ism, "sizning yoshingiz", 2022  -  ty, "da" )


# a = int(input("Son1 "))
# b=int(input("Son2 "))
# print()
# print("a", "+", "b", "=",a+b)
# print("a", "-", "b", "=",a-b)
# print("a", "*", "b","=",a*b)
# print("a", "/", "b", "=",a/b)

# print("   1 -  MISOL      ")
 
 
# matn = input("matn = ")

# natija = ""

# for harf in matn:
#     natija = harf + natija

# if natija.lower() == matn.lower():
#     print("simetrik")
# else:
#     print("simetrik emas")
 
# print("   2 -  MISOL      ")
# matn = input("matn = ")
# natija = ""

# for harf in matn:
#     if harf.isupper():
#         natija += "1"
#     else:
#         natija += harf
# print(natija)
# print("   3 -  MISOL      ")
# matn = input("matn = ")
# natija = ""

# for harf in matn:
#     if harf.isdigit():
#         print(harf)
# print("   4 -  MISOL      ")
# matn = input("matn = ")
# print(matn.count(" ") + 1)

# print("   5 -  MISOL      ")

# matn = input("matn = ")
# sanash = 0
# 
# natija = ""
# 
# for harf in matn:
    # if sanash % 2 == 0:
        # natija += harf.lower()
    #else:
        # natija += harf.upper() 
    # sanash += 1
# print(natija)



# print("   6 -  MISOL      ")

# matn1 = input("matn1 = ")
# matn2 = input("matn2 = ")
# sanash = 0
# natija = 0


#  
# for harf in matn1:
    # if harf == matn2[sanash]:
        # natija += 1
    # sanash += 1
# print(natija)
# 
# 

# 
# for harf in matn1:
    # if harf == matn2[sanash]:
        # natija += 1
        # sanash += 1
# print(natija)
# 




# // # print("   7 -  MISOL      ")
# // # matn = input("matn = ")
# // # natija = 0
# // # for harf in matn:
# // #     if harf == "A" or harf == "a" :
# // #          natija+=1
# // # print(natija)













# Bayramingiz bilan OPAJONIM
# count = 1
# width = 20
# for i in range(10):
#     print(("*"*count).center(width))
#     count += 2 
# print("| |".center(width))









