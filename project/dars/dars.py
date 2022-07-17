import math


# 21  -  DEKABR

#  1 -  MISOL
# meva = ["olma", "anor", "uzum"]
# for a in meva:
#     print(a)

#  2  - MISOL
# for a in "dastur":
#     print(a)

# 3  -  MISOL
# for x in "dastur":
#     print(x)
#     if x == "s":
#         break

# # # 4 - MISOL
# for x in "dastur":
#     if x == "s":
#         break
#     print(x) 
#  5 -  misol 
# for x in "python":
#     if x == 'h':
#         continue
#     print(x)


# 6  -  Misol
# for x in "ravshan":
#     if x == 's':
#         continue
#     print(x)

#  7 -  MISOL
# for x in range(5):
#     print(x)

#  8  - MISOL
# for x in range(101):
#     print(x)

# 9 - MISOL
# for x in range(1,6):
#     print(x)

# # 10 - MISOL
# for x in range(1,41):
#     print(x)

# 11 - MISOL
# for x in range(2,11,2):
#     print(x)  # 2 dan 11 gacha deb belgilaymiz.shunda sanoq 2 dan boshlanadi va 10 gacha davom etadi. har sanoq ikkitaga ortishi uchun uchinchi bolib 2 soni kiritamiz

#  12 - MISOL
# for x in range(5):
#     print("python")
# else:
#     print("\nSikl tugadi!")


#  13 - MISOL
# for x in range(20):
#     print("salom dunyo")
# else:
#     print("\nSikl tugadi!")



#  22  -  DEKABR
# 2  - DARS
# #  DARSIMIZNI TAKRORLASAK
# range(1, 32) degani. 1 dan boshlab, 31 gacha bo'lgan sonlarni oladi. 31 ni olishi uchun 32 soni yoziladi.
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 shu sonlarni chiqazadi.
# Endi shuni 2 qatorli kod orqali chiqazamiz:
# #  1 - MISOL
# for son in range(1, 32):
#     print(son)

# UYGA VAZIFA
# 1 -  Misol
# for i in 'salom dunyo':
#     print(i*2, end='')

# 2 - MISOL
# karra = 9

# for son in range(1, 11):
#     natija = karra * son 
#     print("{} * {} = {}".format(karra, son, natija))

# 3 - MISOL
# satr = input("so'z kiriting: ")
# for s in satr:
#     if s.isdigit():
#         print("sinish jarayoni:" , s)
#         break
#     print(s)

#  4 - MISOL
# satr = input("so'z kiriting: ")
# for s in satr:
#     if s.isdigit():
#         continue
#     print(s)




# 5 - MISOL
# dostlar = ['ALI', 'VALI', 'HASAN', 'OLIM' ]
    
# for dost in dostlar:
#     print("Salom", dost)
#     print("Hayr",  dost)



# 6 - MISOL
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")






# 7 -MISOL
# n = 9
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,'x', j, '=', i*j)

# 8 - MISOL
# while True:
#     soz = input("so'z kiriting: ")
#     print("davom eting")
#     break

# 9 - MISOL
# for i in range(1, 5):
#     for j in range(1, 5):
#         print(i + j, end="\t")
#     print("\n")

# 10 - MISOL
# while True:
#     ch = input("Chiqish uchun Y klavishini bosing")
#     if ch.lower() == 'y':
#         break

# #11 - MISOL
# s = 0
# n = int(input("n = "))
# for i in range(1,n+1):
#     s += i
# print("Summa(1,...,n)=",s)




# a = "Dastur"

# print(a.strip())


# a = "Markaziy Osiyo"
# print(a.lower())



# a = "Markaziy Osiyo"
# print(a.upper())


# a = "Bor"
# b = "markaziy osyo"

# print(a.replace("r", "y"))
# print(b.replace("markaziy", "orta"))


# a = "python bilan ishlash qiziqarli"
# print(a.split(" "))

# yosh = 17
# matn = "mening yoshim {} da"

# print(matn.format(yosh))

# raqam = 2
# kilo = 3
# pul = 5000

# savdo = "{1} kg olmani {0}-do'kondan {2} so'mga sotib oldim"

# print(savdo.format(raqam,kilo,pul))



# raqam = 2
# kilo = 3
# pul = 5000

# savdo = "{} kg olmani {}-do'kondan {} so'mga sotib oldim"

# print(savdo.format(raqam,kilo,pul))


# narx = 30
# satr = "mahsulot narxi {}so'm"

# print(satr.format(narx))


# sana = 4
# oy = "yanvar"
# yil = 2022
# bugun = "bugun {} - {}, {} - yil" 

# print(bugun.format(sana,oy,yil))

# soat = 3
# fan = "dasturlash"
# dars = "bugun {0} soat darsimiz bor. {0} - darsimiz {1}"

# print(dars.format(soat,fan))


# satr = "uning ismi {ism}, yoshi {yosh} da"
# print(satr.format(ism = "ravshanbek", yosh = 17))


# print(chr(2003))

# print(ord("*"))

# ism = "eee"
# print(len(ism))



# a = 10
# if False:
#     print(12)
#     a != 20
# elif False:
#     print(45)
#     a *= 5 
# elif False:
#     print(78)
#     a /= 7
# else:
#     print(20)
#     a -= 30


# l = [1,2,2,3,4,4,3]
# res = []

# for i in l:
#     if i not in res:
#         res.append(i)

# print(res)


# l = [1,2,2,3,4,4,3]

# res = list(set(l))

# print(res)



# a = input().split('+')



# a1 = int(a[0])
# a2 = int(a[1])
# b = a1+a2
# print(b, end=';')


# def welcome():
#     msg ='Xayrli kun! '
#     return msg
# print(welcome())



# def msg():
#     print('Bugun soat 14.00 da ota-onalar majlisi!')

# msg()


# result= int(input('Natijani kiriting(0-5 bahoda):'))
# if result>=3:
#     print('Imtihondan o\'tdingiz!')
#     if result>=5:
#         print('Eng yuqori baho!')



#Misol: Kichik kalkulyator dasturini tuzing


# a=int(input('a='))
# b=int(input('b='))
# amal=input('add/sub/mul/div:')
# if amal=='add':
#     c=a+b
# elif amal=='sub':
#     c=a-b
# elif amal=='mul':
#     c=a*b
# elif amal=='div':
#     c=a/b
# else:
#     c='Error'
# print('Result = ', c)




# xona sonini yigindisini hisoblash

# n = input("Enter number: k(0<k<9999)")
# n = int(n)
# d1 = n % 10
# d2 = n % 100 // 10
# d3 = n % 1000 // 100
# d4 = n // 1000
# print("Result:", d1 + d2 + d3 + d4)




#>>> a = "O'ZBEKISTON"
#>>> a[4]
#4 indeksdagi belgini chiqaradi.
#'E'
#>>> a[3:6]
#'BEK'
#>>> a[:6]
#'O'ZBEK'
#>>> a[6:]
#'ISTON'
#>>> a[3:10:3]

# def circle(r):
#     PI = 3.14
#     len = 2 * PI * r
#     return len
# radius = int(input('Aylana radiusi: '))
# uz = circle(radius)
# print('Aylananing uzunligi: ', uz)


#>>> a=int(input())
#12325458
#>>> b=a//1000000 # necha km
#>>> a=a%1000000 # qolgan qismi
#>>> c=a//1000 # necha metr
#>>> a=a%1000 # qolgan qismi
#>>> d=a//10 # necha cm
#>>> a=a%10 # qolgan qismi mm da
#>>> print(b, 'km' , c, 'm', d, 'cm', a, 'mm')



# res='ha'
# while answer == 'ha':
#     print('Foydalanishingiz mumkin')
# res=input("Ushbu dasturdanfoydalanasizmi? (ha/yo'q)")
# print('Marhamat.')






# def factor(n):
#     res=1
#     for i in range(2,n+1):
#         res*=i
#     return res
# n=int(input('n sonini kiriting:'))
# print(factor(n))


# def factor(n):
#     res=1
#     for i in range(2,n+1):
#         res*=i
#     return res
# n=int(input('n sonini kiriting:'))
# print(factor(n))




# def max(a, b):

#     if a > b:
#         return a 

#     else:
#         return b 


# def max3(a, b, c):


#     return max(max(a, b), c)



# a = int(input())
# b = int(input())
# c = int(input())
# print(max3(a,b,c))








