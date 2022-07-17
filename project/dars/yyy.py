# for x in range(0,19):
#     for y in range(28):
#         shart1 = x==0 or x==10 or x==10 or x==9
#         shart2 = y==0 or y==28
#         shart3 = x==2 or (y<11 or y<0 or y<4 or y<3)
#         shart4 = x==4 or (y<4 or y<=8 or y<5 and y<3)
#         shart5 = x==3 or (y<7 and y>9 or y<5 or y<7)
#         shart6 = x==4 or (y<9 or y<2)
#         if shart1 or shart2 or shart3 or shart4 or shart5 or shart6:
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()




# for i in range(10):
#     for j in range(10):
#         if i == 0 or j == 0 or i == 9 or j== 9:
#             print("* **", end=' ')
#         else:
#             print(" ", end=" ")
#     print()




# for sh in range(0,8):
#     if sh == 0:
#         print("EE   EEEEEE")
#     elif sh == 1 or sh == 2 or sh == 4 or sh == 5:
#         print("EE   EE")
#     elif sh == 2:
#         print("EE   EEEE")
#     elif sh == 3:
#         print("EE   EEEE")
#     elif sh == 6:
#         print("EEEE EEEEEEE")






# from googletrans import Translator
# tarjimon=Translator()
# tarjima=tarjimon.translate(text='Men kopyuterni sevaman')
# print(tarjima)





# a = int(input("telefon nomerni kiriting "))
# b = input("@gmailni kiriting ")
 
# if a == b:
#     print("telefon va @gmail to'g'ri")
# elif a == b:
#     print("telefon va @gmail tekshirib kiriting")
# else:
#     print("telefon va @gmail noto'g'ri")








# phone = input("tel: ")
# code = "99,98,97,95,94,93,91,90,88,71,65,55,33"

# while not phone.startswith("+998") or not len(phone) == 13  or not phone[4:6] in code or not phone[1:].isdigit():
#     print("\n\nSiz notog'ri nomer kiritdingiz\n\n")
#     phone = input("tel: ")
# print("\n\nSizning raqamingiz qabul qilindi\n\n")




# for s,  i in zip("salom", range(7)):
#     print(s, i)



# for s,  i in zip("salom", range(2)):
#     print(s, i)




# for s,  i in zip("salom", "dunyo"):
#     print(s, i)




# for s,  i in zip("salom", "du"):
#     print(s, i)



# for s,  i in zip("sa", "dunyo"):
#     print(s, i)



# print("salom {} dunyo".format(12))



# print("salom {} dunyo".format("elineora"))



# print("salom {} dunyo{}".format("elineora", 20))



# print("salom {} dunyo".format("elineora", 20))


# print("salom {1} dunyo".format("elineora", 20))


# print("salom {1} dunyo {0}".format("elineora", 20))


# print("salom {1} dunyo {1}".format("elineora", 20))



# print("salom {0} dunyo {0}".format("elineora", 20))


# ism = input("ism: ")
# familya = input("familya: ")
# yosh = input("yosh: ")

# print("{} {} {} - yil tug'ilgan".format(familya, ism, 2021 - int(yosh)))





# ism = input("ism: ")
# familya = input("familya: ")
# yosh = input("yosh: ")

# print("{} {} {} - yil tug'ilgan".format(familya.capitalize(), ism.capitalize(), 2021 - int(yosh)))





# ism = input("ism: ")
# familya = input("familya: ")
# yosh = input("yosh: ")

# print("{} {} {} - yil tug'ilgan".format(familya.upper(), ism.capitalize(), 2021 - int(yosh)))
 


# ism = input("ism: ")
# familya = input("familya: ")
# yosh = input("yosh: ")
# if 2021 - int(yosh) <= 0:
#     print("{} {} {} - yil tug'ilgan".format(familya.upper(), ism.capitalize(), "yoshni noto'gri kiritdingiz"))
# else:
#     print("{} {} {} - yil tugilgan".format(familya.upper(), ism.capitalize(), 2021-int(yosh)))



# print(f"{12} salom")





# ism = "Elineora"
# print(f"{ism} salom")




# a = float(input("a: "))
# b = float(input("b: "))
# print("{} / {} = {}".format(a, b, a/b))
# print("{} + {} = {}".format(a, b, a+b))
# print("{} - {} = {}".format(a, b, a-b))
# print("{} * {} = {}".format(a, b, a*b))




# 5! = 5 *4*3*2*1
# a = int(input("a = "))
# n = 1
# for s in range(1, a + 1):
#     n *= s
# print(n)




# karra = 9

# for son in range(1, 11):
#     natija = karra * son
#     print("{} * {} = {}".format(karra, son, natija))





# viloyat = input("viloyatni kiriting  ")
# tuman = input("tumanni kiriting  ")
# shahar = input("shaharni kiriting  ")
# sanatoriya = input("sanatoriya kiriting ")
# print(f" {viloyat}, {tuman}, {shahar},  {sanatoriya}, siz shu sanatoriyasini tanladingiz ")







# email = input("email : ")
# nomi = "gmail, mail.ru "

# while not email.startswith("@gmail") or not  len(nomi) == 9  or not   email [1:3] in nomi or not email[2:].isupper:
#     print("\n\nSiz notog'ri email  kiritdingiz\n\n")
#     email = input("email: ")
# print("\n\nSizning emailingiz qabul qilindi\n\n")




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



#       UYGA VAZIFALAR

    # 1 - MISOL

# email = input("email : ")
# nomi = "gmail, mail.ru "

# while not email.startswith("@gmail") or not  len(nomi) == 9  or not   email [1:3] in nomi or not email[2:].isupper:
#     print("\n\nSiz notog'ri email  kiritdingiz\n\n")
#     email = input("email: ")
# print("\n\nSizning emailingiz qabul qilindi\n\n")


#      2 - MISOL 
# a = input("tel nomer kiriting ")
# if "+99890" in a:
#     print("Siz telefon nomerni to'g'ri kiritdingiz")
# else:
#     a = input("telefon nomerni qaytadan teshshirib kiriting")
   

#    3 - MISOL
# viloyat = input("viloyatni kiriting  ")
# tuman = input("tumanni kiriting  ")
# shahar = input("shaharni kiriting  ")
# sanatoriya = input("sanatoriya kiriting ")
# xonana = input("26 - xona")
# print(f" {viloyat}, {tuman}, {shahar},  {sanatoriya},  tanladingiz ")





# a = input("ism kiriting ")
# b = input("familya kiriting ")
# print(a.upper())





# for i in range(5):
#     for j in range(i):
#         print('*', end='')
#         print('')

# print('*\n* *\n*  * *\n* * * *\n* * * * *')

