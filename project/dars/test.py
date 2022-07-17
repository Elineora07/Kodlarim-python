# "          1 - TEST SAVOLLARI    "
"""""""""
1) UCHTA SONDAN KATTASINI TOPADIGAN KOD.
2) CHEKSIZ KANKULYATOR KOD KIRITILGAN MISOL type str(), input BIITA BO'LADI.
MISOL: 78 + 15 KIRITILADI. CHIQISH 78 + 15 = 93, AGAR MISOLNI O'RNIGA exit() KIRITILSA KANKULYATOR TO'XTASIN.
3) TRUE bilan FALSE KIRITILADI type==>bool() TRUE kiritiladi TURE QAYTARSIN FALSE BO'LSA FALSE type==>str()bo'lishi  kerak.
4) IKKI KATET KIRITILADI UCHBURCHAKNI YUZINI TOPADIGAN KOD( S = (a * b )/ 2 YUZA TOPISH FORMULASI S YUZ)
5) MUCHALNI YILNI ANIQLAYDIGAN KOD
6) MATNDA NECHTA KICHIK, KATTA HARFLAR VA RAQAMLAR BORLIGINI ANIQLUVCHI KOD
MISOL:"SaloM 145 dUnyO buGuNgi sanA:2001.10.21" ->KATTA HARF:7TA;KICHIK HARF:14;RAQAM:13TA
7) ISM KIRITILADI SHU ISMGA SALOM BERADIGAN KOD
MISOL:"Odil"->"Salom Odil"
8) SON KIRITILADI SHU SONI 1 XONALI SONGA AYLANISHIGA QADAR RAQAMLAR YIG'INDISINI TOPISH
MISOL:1545- > 1 + 5 + 4 + 5 = 15 -> 1 + 5 = 6
CHIQIM: 6
9) SOAT VAQTINI KIRITILADI 00:00 DAN QANCHA MINUT O'TKANINI HISOBLAYDIGAN KOD(soat24 soatli) 
Misol:05:30-> 330 minut
10) IKKITA MATNNI SOLISHTIRIB BIR XIL SO'ZLARNI CHIQAZADIGAN KOD
MISOL: (
    a = "salom dunyo nima gap 12321"
    b = "salom Asad nima 21"
    CHIQISH:salom 21)
11) KIRITILGAN MATNDAGI HARFLARNI KATTA HARFLARGA AYLANTIRISH
12) GAPDAGI SO'ZLARNI BIRINCHI HARFI KATTA QOLGANI KICHIK CHIQAZADIGAN KOD
MISOL: sAloM dUnYO sHaRoF 25.11.2021-> Salom Dunyo Sharof 25.11.2021
13) 2 TA FOR DA ROMB SHAKLINI CHIZING
14) TAVOR QO'SHIB SOTILADIGAN KOD
"""""
# import math
# print("  1 -  MISOL  ")

# print("3 tasidan kattasini topadigan")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a >= b and b >= c:
#     print('a')
# elif b >= a and b >=c:
#     print('b')
# else:
#     print('c')


# print('2  - misol ')
# son1 = ""
# son2 = " "
# q = " "
# a = input('misol kiriting -')
# for i in a:
#     if i.isdigit() :
#         son1 += i
#     if i.isspace():
#         son2 = " "
#     if i.isdigit():
#         son2 += i
# s1 = len(son1) 
# s2 = len(son2) 
# son_1 = (int(son1) - int(son2)) // (10**s2)
# p='/'
# l='*'
# m='-'
# n='+'
# if m in a:
#     q = int(son_1) - int(son2)
# elif p in a:

#     q = int(son_1) / int(son2)
# elif l in a:
#     q = int(son_1) * int(son2)
# elif n in a:
#     q = int(son_1) + int(son2)
# print(q)

# print('3 - misol ')

# a = (input('true - false ==> '))
# a = str(a)
# b = "true"
# c = "false"
# if b in a:
#     print("true")

# elif c in a:
#     print(str("false"))


# print("  4 -  MISOL  ")
# a =float(input("a =  "))
# b =float(input("b = "))

# S =(a*b/2)
# print(S)


# print("5 - misol ")
# a = int(input('son kiriting : '))
# d=""
# if a%12==1:
#     d+=" ilon "
# elif a % 12==2:
#     d+=" baliq "
# elif a % 12==3:
#     d+=" tovuq "
# elif a%12==4:
#     d+=" yolbars "
# elif a %12==5:
#     d+= " sichqon "
# elif a % 12==6:
#     d+=" sigir "
# elif a % 12==7:
#     d+=" quyon "
# elif a % 12==8:
#     d+=" ot "
# elif a % 12==9:
#     d+=" qo'y "
# elif a % 12==10:  
#     d+=" maymun "
# elif a % 12==11:
#     d+=" tongiz "
# elif a%12==0:
#     d+= " it "
# print(d)

# print("   6-  misol ")
# matn = input("matn kiriting - ")
# kichik = 0
# katta = 0
# raqam = 0
# bosh = 0
# for i in matn:
#     if i.isupper():
#         katta+=1
#     elif i.islower():
#         kichik+=1
#     elif i.isdigit():
#         raqam+=1
#     elif i.isspace():
#         bosh+=1
# print('Katta harf-',katta,'ta ; Kichik harf -',kichik,'ta ; Raqamlar ',raqam,'ta ; bosh belgi ',bosh,'ta ekan .')

# print("  7 - misol ")
# ism =input("ism = ")
# print("Salom " + ism)

# print("   8 -  misol  ")
# 
# a = int(input("son kiriting - "))
# d = 0
# raqam = 0
# b = 0

# for i in str(a):
    # d += int(i)
    # if d>9:
        # for k in str(d):
            # b += int(k)
            # print(b)
    # else:
        # print(d)

# print(" 9 - misol ") 
# a = int(input("soat kiriting: "))
# b = int(input("minut: "))
# vaqt=0
# if a==1:
#     vaqt+=b
# elif a >1:
#     vaqt+=60
# if a==2:
#     vaqt+=b
# elif a>2:
#     vaqt+=60
# if a==3:
#     vaqt+=b
# elif a>3:
#     vaqt+=60
# if a==4:
#     vaqt+=b
# elif a>4:
#     vaqt+=60
# if a==5:
#     vaqt+=b
# elif a>5:
#     vaqt+=60
# if a==6:
#     vaqt+=b
# elif a>6:
#     vaqt+=60
# if a==7:
#     vaqt+=b
# elif a>7:
#     vaqt+=60
# if a==8:
#     vaqt+=b
# elif a>8:
#     vaqt+=60
# if a==9:
#     vaqt+=b
# elif a>9:
#     vaqt+=60
# if a==10:
#     vaqt+=b
# elif a>10:
#     vaqt+=60
# if a==11:
#     vaqt+=b
# elif a>11:
#     vaqt+=60
# if a==12:
#     vaqt+=b
# elif a>12:
#     vaqt+=60
# if a==13:
#     vaqt+=b
# elif a>13:
#     vaqt+=60
# if a==14:
#     vaqt+=b
# elif a>14:
#     vaqt+=60
# if a==15:
#     vaqt+=b
# elif a>15:
#     vaqt+=60
# if a==16:
#     vaqt+=b
# elif a>16:
#     vaqt+=b
# elif a>17:
#     vaqt+=60
# if a==17:
#     vaqt+=b
# elif a>18:
#     vaqt+=60
# if a==18:
#     vaqt+=b
# elif a>19:
#     vaqt+=60
# if a==19:
#     vaqt+=b
# elif a>20:
#     vaqt+=60
# if a==20:
#     vaqt+=b
# elif a>21:
#     vaqt+=60
# if a==21:
#     vaqt+=b
# elif a>22:
#     vaqt+=60
# if a==23:
#     vaqt+=b
# elif a>23:
#     vaqt+=60
# if a==24:
#     vaqt+=b
# elif a >24:
#     vaqt+=60

# print(vaqt)

# 
# print(" 10  - misol  ")
# a = input("Matn1 kiriting -")
# b = input("Matn2 kiriting -")
#c = " "
# 
# for i in a:
    # for j in b:
        # if i==j :
            # c +=i
# print(i)
# 


# print("  11 - MISOL ")

# matn1 =input("matn = ")
# print(matn1.upper())


# print("  12  -  MISOL  ")
# matn = input("matn = ")
# matn=matn.title()
# print(matn)

# print(" 13 - misol ")
# a = 18 
# for i in range(a):
    # for j in range(a):
            # shart1 = i==0 or j==0 or i==a-1 or j==a-1
            # shart2 = i==j-9 or j==i-9 or 9-j==j
            # if shart1 or shart2 or 9-j==i-16:
                #    print('=', end='')
            # else: 
            #    print(' ',end="")
    # print()


