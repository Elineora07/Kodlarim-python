# for i in range(6):
#     for j in range(6):
#         if i == 0 or j == 0 or i == 5 or j == 5:
#             print("XEU   ", end='')
#         else:
#             print("  ", end="")
#     print()
# print(" 6 - Misol ")
# a = int(input("1 -sonni kriting = "))
# b = int(input("2 - sonni kiriting = "))
# c = input('amal belgisini kiriting = ')
# if c=='^':
#     print(a**b)
# elif c=='*':
#     print(a*b)
# elif c=='/':
#     print(a/b)
# elif c=='+':
#     print(a+b)
# else:
#     print(a-b)

# ruslan tashlagan 
#1 
# print("1 - misol ")

# a = int(input("Son1 kitiing "))
# b = int(input("Son2 kiriting "))
# c = int(input("Son2 kiriting  "))

# m = max(a,b,c)
# print(m)

#2 
# print("2 - misol ")
# son1= ""
# son2 = ""
# q = ""
# a = input("misol kiriting ")
# for i in a:
#     if i.isdigit():
#         son1 += i
#     if i.isspace():
#         son2 =""
#     if i.isdigit():
#         son2 +=i
# s1 = len(son1)
# s2 = len(son2)
# son_1 = (int(son1) - int(son2)) // (10**s2)
# p='/'
# l="*"
# m="-"
# n="+"
# if m in a:
#     q = int(son_1) - int(son2)
# elif p in a:
#     q = int(son_1) * int(son2)
# elif n in a:
#     q = int(son_1 + int(son2))
#     print(q)


# # 3 
# print("3 - misol ")

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

# a = int(input("son kiriting - "))
# d = 0
# raqam = 0
# b = 0

# for i in str(a):
#     d += int(i)
#     if d>9:
#         for k in str(d):
#             b += int(k)
#             print(b)
#     else:
#         print(d)

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


# print(" 10  - misol  ")
# a = input("Matn1 kiriting -")
# b = input("Matn2 kiriting -")
# c = " "

# for i in a:
#     for j in b:
#         if i==j :
#             c +=i
# print(d)



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
#     for j in range(a):
#             shart1 = i==0 or j==0 or i==a-1 or j==a-1
#             shart2 = i==j-9 or j==i-9 or 9-j==j
#             if shart1 or shart2 or 9-j==i-16:
#                    print('=', end='')
#             else: 
#                print(' ',end="")
#     print()














# print("regestratsiyadan o'ting")
# son=0
# a = input("email pochtangizni kiriting ")
# while son<=100 :
#     if "@gmail.com" in a:
#         son+=101
#         b = input("telefon nomerni kiriting ")
#         tel = 0
#         while tel<=1000 :
#             if "+99891" in b :
#                 tel+=1001
#                 print("registratsiyadan o'tdingiz ")
#             else:
#                 b = input("telfon nomeringizni tekshirib qaytib kiritng! ")
#                 tel+=0
#     else:
#         a = input("email pochtangizni tekshirib qaytaddan kiriting ")
#         son +=0
