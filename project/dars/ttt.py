"""""""""""
""""""
matn[i] - i indeksidagi harfni qaytaradi
matn[a:b] - a va b gacha bo'lgan so'zni qaytaradi
matn[:b] - boshidan b gacha bo'lgan so'zni qaytaradi
matn[a:] - a dan oxirigacha bo'lgan so'zni qaytaradi
matn[-a:-b] - hisob kitob o'ng tarafdan boshlanadi
matn[:-b] - boshidan boshlab o'ng tarafdan b gacha bo'lgan so'z
matn[-a:] - o'ng tarafdan a indeksidagi harfdan oxiriagacha bo'lgan so'z
matn[a:b:c] - c qadamlar soni (manfiy bo'lsa o'ng tarafdan)
matn[::] - boshidan oxirigacha bo'lgan so'z yani so'zni o'zi 
matn[::-1] - sozni teskarini yozish
"""""

# print("  1 - MISOL  ")
# matn = "salom"

# print(matn[0])

# print("  2 - MISOL  ")
# matn = "salom"

# print(matn[0:3])

# print("  3 - MISOL  ")

# matn = "salom"

# print(matn[:3])

# print("  4 - MISOL  ")

# matn = "salom"
 
# print(matn[3:])

# print("  5 - MISOL  ")

# matn = "salom"

# print(matn[-3:-2])
# print("  6 - MISOL  ")

# matn = "salom"

# print(matn[:-2])

# print("  7 - MISOL  ")

# matn = "salom"

# print(matn[:-3])

# print("  8 - MISOL  ")

# matn = "salom"

# print(matn[1:4:2])

# print("  9 - MISOL  ")

# matn = "salom"

# print(matn[::-1])


# print("  10 - MISOL  ")

# matn = "salom"

# print(matn[::-2])


# print("  11 - MISOL  ")

# for i in range(32):
#     print(i, end=', ')
 

# print("  12 - MISOL  ")

# for i in range(1,32):
#     print(i, end=', ')
 
# print("  13 - MISOL  ")
# son = 0
# while son <=30:
#     print(son, end=", ")
#     son += 1
# print("  14 - MISOL  ")
# son = 0
# while son <=30:
#     son += 1
#     print(son, end=", ")
    
# print("  15 - MISOL  ")
# matn = ''
# while matn != "toxta":
#     matn = input()
#     if matn != "toxta":
#         print(float(matn) ** 2)
    

# print("  16 - MISOL  ")
# son =0
# while son <= 30:
#     if son == 12:
#         break
#     else:
#         print(son, end=' ')
#         son += 1

# print("  17 - MISOL  ")
# son = 0
# while son <= 10:
#     son+=1
#     if son == 5:
#         continue
#     elif son:
#         pass
#     print(son, end=" ")








# print(" 1 - Misol ")
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


# print(" 2 - Misol ")
# soz = input("so'z ")
# matn = input("2ta tildan birini tanlang [uzb/fransuz] ")
# if matn == "uzb":
#     print(soz, "KADIROV SHAROF USTOZ YAXSHIMISIZ? ISHLAR BILAN CHARCHAMAY YURIBSIZMI?")
# elif matn == "fransuz":
#     print(soz, "KADIROV SHAROF PROFESSEUR TU VAS BIEN? NE VOUS FATIGUEZ-VOUS PAS DES CHOSES?")
# else:
#     print("uzb yoki fransuz tilini tanlang")



# print(" 3 - Misol ")
# print("Assalomu alekum. Bizning xizmatdan foydalanishingiz uchun registratsiyadan o'ting. ")
# a = input("Ismingiz? ")
# b = input("Familyangiz? ")
# if a and b:
#     c = input("Manzilingizni kiriting ")
#     if c and a:
#         e = input("Tugilgan yilingizni kiriting ")
#         if e and a:
#             k = input("Telefon nomeringizni kriting ")





# print(" 4 - Misol ")
# a = int(input('son kiriting '))
# if a %10 == 0 and a %5 == 0:
#     print(a, 'soni 5 va 10 ga karrali')
# else:
#     print(a, 'karrali emas')



# print(" 5 - MISOL  ")
# ism = input("ISMINGIZ? ")
# yil = int(input("yil  "))
# if ism and yil:
#     print("Salom", ism, "sizning yoshingiz", 2021 - yil, "da")
# else:
#     print("XATO")


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



# print(" 7 - MISOL  ")

# print("manfiy yoki musbat son ")
# a = float(input('son kiriting: '))
# if a > 0:
#     print('siz musbat son kiritingiz')
# else:
#     print('siz manfiy son kiritdingiz')



# print(" 8 - Misol  ")
# a = int(input('son - '))
# if a // 10>=10000000:
#     print('9 xonali')
# elif a // 10>=1000000:
#     print('8 xonali')
# elif a //10>=100000:
#     print('7 xonali')
# elif a // 10>=10000:
#     print('6 xonali')
# elif a // 10>=1000:
#     print('5 xonali')
# elif a // 10>=100:
#     print('4 xonali')
# elif a // 10>=10:
#     print('3 xonali')
# elif a // 10>=1:
#     print('2 xonali')
# elif a//10>=0:
#     print('1 xonali')
# else: 
#     print('bunday xonali son yoq')


# print(" 9 - misol ")?
# print(" 10 - MISOL ")?








# for i in range(101):
#     if i % 2 == 0:
#         print(i)

# for i in range(101):
#     if i % 2 == 1:
#         print(i)

# matn = input("matn = ")
# natija = ""
# for harf in matn:
#     if harf.isupper():
#         natija += "1"
#     else:
#         natija += harf
# print(natija)




# 8.12.2021yil
# for sikli


# for i in range(10):
#     print(i)


# for i in range(1,10):
#     print(i)



# for i in range(1,11):
#     print(i)


# a = "salom"
# for e in a:
#     print(e)


# matn = input("matn = ")
# natija = ""
# for e in matn:
#     if ord(e) >= 97 or ord(e) <= 120:
#         natija = ord(e) - 32
#     print(chr(natija), end = "")


# for e in range(65, 91):
#     print(chr(e),  end=chr(e + 32))

# a = "salom"
# b = "salum"

# for e, r in zip(a, b):
#     print(e, r)


# a = "salom"
# b = "salum"
# c = "dunyo"
# natija = 0

# for e, b, a in zip(a, b, c):
#     print(e, b, a)


# a = "salom"
# b = "salum"
# natija = 0

# for i, n in zip(a, b):
#     if i == n:
#         natija += 1
# print(natija)


# for i in range(31):
#     if i % 2 == 1:
#         print(i)


# for i in range(31):
#     if i % 2 == 0:
#         print(i) 


# a = "salom"
# for harf in a:
#     print(harf)

# a = "salom"
# natija = 0
# for harf in a:
#     if harf == "a":
#         natija += "A"
#     else:
#         natija += harf
#     print(natija)
















# telefon = int(input("telefon nomerni kriting "))
# if telefon == "+99890":
#     print(telefon, "siz regisratsiyadan o'tdingz")
# elif telefon == "+99891":
#     print("sizga mumkin emas")











# a = int(input("telefon nomerini kiring "))
# b = input("@gmailni kiriting ")

# if a == b:
#     print("siz registarsiyadan o'tdingiz")
# elif a != b:
#     print("siz registratsiyadan o'tmadingiz")



# a = input(input("registratsiyadan oting[tel]"))

# if a == ""
#     print( "siz to'g'ri tel nomer kiritdingiz")
# else:
#     print("siz notog'ri tel nomer kiritdingiz")





# tel = int(input("telefon nomeringizni kiriting ")) 
# if tel:
#     print("to'ri")
# elif tel:
#     print("qaytib tekshing")
# else:
#     print("xato")




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
        # son +=0









