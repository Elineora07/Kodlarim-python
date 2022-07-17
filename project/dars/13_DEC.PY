# import math

# a = "salom {} dunyo {}".format("Elineora ", "nima gap ")
# print(a)



# a = "salom {0} dunyo {0}".format("Elineora ", "nima gap ")
# print(a)


# a = "{: ^100}".format("Elineora")
# print(a)


# a = "{:-^100}".format("Elineora")
# print(a)


# a = "{:->100}".format("Elineora")
# # print(a)


# a = "{:-<100}".format("Elineora")
# print(a)

# a = [5,4,56,8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# print(type(a))



# a = [5,4,56,8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# print(a[1])


# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# print(a[1])



# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# print(a[4])



# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# print(a[4][3])




# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# a.append(105)   #oxiriga qo'shadi
# print(a)


# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# a.append(555)  # oxiriga bitta qo'shadi
# print(a)



# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# a.extend([105,222,333,555]) # hamma elementni  qo'shib listni kengaytiradi kop qo'shadi
# print(a)



# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# a.insert(0, 323) #i elementga x qiymat qaytaradi indexs berib qiymat kiritsa. bergan indeksga shu qiymatni qo'shadi
# print(a)



# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# a.pop(1) # ro'yxatni i elementini o'chiradi yoki qaytaradi. Agar indeks korsatilmagan bo'lsa oxirgi elementini o'chiradi
# print(a)


# a = [8,"salom",4,85,[8,9,8,88,55,22],23,5,45,8]
# print(a.index(85)) # index - korsatilgan elementni indeksini chiqazadi


# a = [1,3,5,4,7,8,5]
# a.sort() # sortirofka qiladi raqamni yoki harfni boshidan ketma ketlikda chiqazadi
# # print(a)

# a = [1,3,5,4,7,8,5]
# a.reverse()  kiritgan royxatni teskariga chiqazadi
# print(a)


# a = [1,3,5,4,7,8,5]
# a.sort()
# a.reverse() # sort yani sartirovkani kattasidan kichiika chiqazdi
# print(a)

# a = (5,4,5,4,5,4,2,1,8)
# print(type(a))


# a = [1,3,5,4,7,8,5]
# if 5 in a:
#     print("bor")
# else:
#     print("yoq")


# a = {5,1,1,1,1,2,2,2,2,3,3,3}
# print(type(a)) # set tipi chiqazadi



# a = {5,1,1,1,1,2,2,2,2,3,3,3}
# print(a) # set elementni sanoq boshidan bittadan oladi



# a = {5,1,1,1,1,2,2,2,2,3,3,3}
# a.add(6) #  set tipida add oxiriga qo'shadi
# print(a)



# a = {5,1,1,1,1,2,2,2,2,3,3,3}
# a.remove(5) # setda remove ko'rsatilgan elementni olib tashlaydi
# print(a)



# a = [1,2,5,4,7,86,5]
# a.sort()
# print(a[0] + a[-1]) 



# a = [1,2,5,4,7,86,55,87,77,44,55,99]
# b = [1,2,5,4,7,86,5,55,66,22]
# c = [1,2,5,4,7,86,5]
# a.sort()
# b.sort()
# c.sort()
# print(a[0] + a[-1])
# print(b[0] + b[-1])
# print(c[0] + c[-1])


# a = {}
# b ={1}
# print(type(a))
# print(type(b))



# 1 - UYGA VAZIFA
# adelni ustoz bergan topshiriq

# a = int(input("son "))
# if a%3==0 and a%5==0:
#     a=a/10
# elif a%3==0:
#     a=a+30
# elif a%5==0:
#     a=a+50
# else:
#     print("bolinmadi")
# print(a)


# 2 - UYGA VAZIFA 
# HAMZA USTOZ BERGAN TOPSHIRIQ

# TELEFON NOMER ANIQLAYDIGAN
# a = input("telefon nomer kiriting ")

# if a.startswith('+99890') or len(a) == 13 or a.isdigit():
#     print("siz togri telefon nomer kiritdingiz")
# else:
#     print("siz notogri nomer kiritdingiz")


# HAMZA USTOZ BERGAN TOPSHIRIQ 

#EMAILNI TEKSHIRADIGAN
# a = input("Email pochtangiz kiriting ")
# i=''
# b1=('@mail.ru','@gmail.ru','@gmail.com')
# a1=a.endswith(b1)

# while not a1 and not len(a)>11 or not "."in a:
#     print("qayatdan tekshirb kiriting ")
# a = input("Email pochtangizni kiriting ")

# print("registratsiyadan o'tdingiz" )

# HAMZA USTOZ BERGAN TOPSHIRIQ
#SANATORIYA
# viloyat = input("viloyatni kiriting  ")
# tuman = input("tumanni kiriting  ")
# shahar = input("shaharni kiriting  ")
# sanatoriya = input("sanatoriya nomini kiriting ")
# xona = input("xonani kiriting ")
# print(f" {viloyat}, {tuman}, {shahar},  {sanatoriya}, {xona}, xonani tanladingiz ")





# 3 - UYGA VAZIFA
# LOWER, LEN ISHLATMAY KICHIK HARFDA MATN KIRITSALAR KATTA HARFGA CHIQAZSIN
# 1 - USUL
# a = input('soz ')
# b = 0
# for i in a:
#     if i.isalpha():
        # b+=1

# print(b) 
# 
#  2 - USUL
# matn = input("matn = ")
# natija = ""
# for e in matn:
#     if ord(e) >= 97 or ord(e) <= 120:
        # natija = ord(e) - 32
#     print(chr(natija), end = "")

# 3 - USUL 
# matn = input("matn = ")
# matn=matn.title()
# print(matn)

# 4 - UYGA VAZIFA
# print("10ta ismli registratsiya ")
# a1=input("ismizni kiriting ")
# b1=input("telefon nomerizni kiriting ")
# e1=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e1.endswith(b1)

# while not e and not len(e1)>11 or not'.' in e1:
#     print("tekshirib kiriting ")
#     e1 = input("Email pochtangizni kiriting ")6uu


# a2=input("ismizni kiriting ")
# b2=input("telefon nomerizni kiriting ")
# e2=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e2.endswith(b1)


# while not e and not len(e2)>11 or not'.' in e2:
#     print("tekshirib kiriting ")# print("10ta ismli registratsiya ")
# a1=input("ismizni kiriting ")
# b1=input("telefon nomerizni kiriting ")
# e1=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e1.endswith(b1)

# while not e and not len(e1)>11 or not'.' in e1:
#     print("tekshirib kiriting ")
#     e1 = input("Email pochtangizni kiriting ")
#     e2 = input("Email pochtangizni kiriting ")


# a3=input("ismizni kiriting ")
# b3=input("telefon nomerizni kiriting ")
# e3=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e3.endswith(b1)






# while not e and not len(e3)>11 or not'.' in e3:
#     print("tekshirib kiriting ")
#     e3 = input("Email pochtangizni kiriting ")



# a4=input("ismizni kiriting ")
# b4=input("telefon nomerizni kiriting ")
# e4=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e4.endswith(b1)

# while not e and not len(e4)>11 or not'.' in e4:
#     print("tekshirib kiriting ")
#     e4 = input("Email pochtangizni kiriting ")


# a5=input("ismizni kiriting ")
# b5=input("telefon nomerizni kiriting ")
# e5=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e5.endswith(b1)


# while not e and not len(e5)>11 or not'.' in e5:
#     print("tekshirib kiriting ")
#     e5 = input("Email pochtangizni kiriting ")



# a6=input("ismizni kiriting ")
# b6=input("telefon nomerizni kiriting ")
# e6=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e6.endswith(b1)


# while not e and not len(e6)>11 or not'.' in e6:
#     print("tekshirib kiriting ")
#     e6 = input("Email pochtangizni kiriting ")



# a7=input("ismizni kiriting ")
# b7=input("telefon nomerizni kiriting ")
# e7=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e7.endswith(b1)


# while not e and not len(e7)>11 or not'.' in e7:
#     print("tekshirib kiriting ")
#     e7 = input("Email pochtangizni kiriting ")



# a8=input("ismizni kiriting ")
# b8=input("telefon nomerizni kiriting ")
# e8=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e8.endswith(b1)


# while not e and not len(e8)>11 or not'.' in e8:
#     print("tekshirib kiriting ")
#     e2 = input("Email pochtangizni kiriting ")



# a9=input("ismizni kiriting ")
# b9=input("telefon nomerizni kiriting ")
# e9=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e9.endswith(b1)


# while not e and not len(e9)>11 or not'.' in e9:
#     print("tekshirib kiriting ")
#     e9 = input("Email pochtangizni kiriting ")



# a10=input("ismizni kiriting ")
# b10=input("telefon nomerizni kiriting ")
# e10=input("emailizni kiriting ")
# i=''
# b1=("@mail.ru","@gmail.ru","@gmail.com")
# e = e10.endswith(b1)


# while not e and not len(e10)>11 or not'.' in e10:
#     print("tekshirib kiriting ")
#     e10 = input("Email pochtangizni kiriting ")


# ism_list = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
# tel_list = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
# pop_l = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]

# ism = input("ism  ")
# c=""
# q=0
# z=""
# for i in ism_list:

#     if i==ism:
#         q=ism_list.index(i)
#         c=tel_list[q]
#         z=pop_l[q]


#     else:
#        print("topilmadi")


# print("Hurmatli", ism,"tel".c,"e-pochta",z)


# son1 = int(input("son1 = "))
# son2 = int(input("son2 = "))
# def kopaytma(a):
#     return a * a

# print(kopaytma(son1))
# print(kopaytma(son2))


# son1 = int(input("son1 = "))
# son2 = int(input("son2 = "))
# def kopaytma(a):
#     return a + a

# print(kopaytma(son1))
# print(kopaytma(son2))


# son1 = int(input("son1 = "))
# son2 = int(input("son2 = "))
# def kopaytma(a):
#     return a / a

# print(kopaytma(son1))
# print(kopaytma(son2))


# son1 = int(input("son1 = "))
# son2 = int(input("son2 = "))
# def kopaytma(a):
#     return a - a

# print(kopaytma(son1))
# print(kopaytma(son2))


# #MATN KIRITILSA NECHTA HARF  BORLIGINI CHIQAZADI!!!!

# def sanash(a):
#     n = 0
#     for i in a:
#         n+=1
    
#     return n
# matn = input("matn ")

# print(sanash(matn))

#     # 3 uyga vazifa
# matn = input("matn kiriting - ")
# kichik = 0
# katta = 0
# bosh = 0
# for i in matn:
#     if i.isupper():
#         katta+=1
#     elif i.islower():
#         kichik+=1
#     elif i.isspace():
#         bosh+=1
# print('Katta harf-',katta,'ta ; Kichik harf -',kichik,'ta ; " bosh belgi ',bosh,'ta ekan .')


# 4 uyga vazifa
# matn = input("matn= ")
# print(matn.count(" ")+1)

# 

# matn = input("matn= ")
# natija = 0
# for harf in matn:
#     if harf == "A" or harf == "a":
        # natija +=1
# print(natija)
# 


# 18.12.21
# # HAMZA USTOZ TUSHUNTIRGAN REGISTRATSIYA EMAIL, TEL, ISM
# names = []
# first_names = []
# middle_names = []
# phone_numbers = []
# emails = []

# phone_code = [99,98,97,95,94,93,91,90,88,77,71,65,55,33]
# emails_code = ["gmail.com", "icloud.com","mail.ru", "yahoo.com"]


# while True:
#     name = input("ism: ")
#     if name == "exit":
#         break
#     if len(names) < 2:
#         while not (name.isalpha() and len(name)>2):
#             print("ism noto'ri")
#             name = input("ism: ")

#         names.append(name.capitalize())
        
#         first_name = input("familya: ")
#         while not ( first_name.isalpha() and len(first_name) >= 5):
#             print("familya noto'g'ri")
#             first_name = input("familya: ")
#         first_name.append(first_name.capitalize())

#         middle_name = input("otani ismi: ")
#         while not (middle_name.isalpha() and len(middle_name) > 2):
#             print("otani ismi notog'ri: ")
#         middle_name.append(middle_name.capitalize())

#         phone_nomber = input("tel nomer: ")
#         while not len(phone_nomber) == 13 or not phone_number.starswith("+998") or not int(phone_number[4:6]) in phone_code:
#             print("tel nomer noto'g'ri")
#             phone_numbers.append(phone_number)

#             email = input("email: ")
#             nike_email = ""
#             code_email = ""
#             for s in email:
#                 if s == "@":
#                     nike_email = code_email
#                     code_email = ""
#                 else:
#                     code_email += s
#             while not len(nike_email)>=8 or not nike_email.islower() or not code_email in email_code:
#                 print("email xato")
#                 email = input("email: ")
#             emails.append(email)
#     else:
#         print("uzr joy to'ldi")
#     for n, f ,m, p, e in zip(names, first_names, middle_names, phone_numbers, emails):
        # print(n,f,m,p,e)



# 1 misol 
# a = [1,2,3,4,56,87,8]
# b = a.pop(2)
# print(b)


# # #  2  misol
# a = [1,2,3,4,5,6,7,8,9,10,11]
# n = 0
# d = []
# e = int(input("index: "))
# f = ""
# for s in a:
#     if n == e:
#         f = s 
#         n += 1
#     else:
#         d.append(s)
#         n += 1

# print(f, d)


# # 3   misol 
# a = [456,6454,789,456,465]
# b = input("udsesdi: ")

# a += [b]

# print(a)

# 4 misol 

# list = [1,2,3,4,65,6]
# a = int(input("index: "))
# b = input("value: ")
# n = 0
# f = []

# for s in list:
#     if a == n:
#         n += 1
#         f.extend([b,s])
#     else:
#         f.append(s)
#         n+=1

# print(f)

# # 5 misol 

# l = [1,2,3,4,65,6]
# i = int(input("index: "))
# v = input("value: ")

# def insert(list,index, value):
#     n = 0
#     f = []
#     for s in list:
#         if index == n:
#             n+=1
#             f.extend([value,s])
#         else:
#             f.append(s)
#             n+=1

#     return f

# print(insert(l,i,v))

   
# # 6  misol 
# def islower(text):
#     for s in text:
#         if ord(s) >= 65 and ord(s) <= 90:
#             return False
#     return True    # 123 yozsa terminalga 123 ni chiqazadi

# matn = input("matn: ")
# print(islower(matn))


#  7  misol 

# def len(text):
#     n = 0
#     for i in text:
#         n += 1
#     return n

# matn = input("matn: ")
# print(len(matn))


# # 8  misol
# def len(text):
#     n = 0
#     for i in text:
#         n += 1
#     return n


# def islower(text):
#     for s in text:
#         if ord(s) >= 65 and ord(s) <= 90:
#             return False
        
#         return True
    
# print(islower(input("matn: ")))




#  9  misol 
  
# def len(text):
#     n = 0
#     for i in text:
#         n += 1
#     return n


# def islower(text):
#     for s in text:
#         if ord(s) >= 65 and ord(s) <= 90:
#             return False
        
#         return True
    
# print(len(input("matn: ")))      




# #  10  misol 

# def len(text):
#     n = 0
#     for i in text:
#         n += 1
#     return n


# def islower(text):
#     for s in text:
#         if ord(s) >= 65 and ord(s) <= 90:
#             return False
        
#         return True

# print(len(input("matn: ")), islower(input("matn: ")))



# 11  misol 

# def len(text):
#     n = 0
#     d = 0
#     for i in text:
#         n += 1
#     return n , d


# def islower(text):
#     for s in text:
#         if ord(s) >= 65 and ord(s) <= 90:
#             return False
        
#         return True


# print(islower(input("matn: ")) )
# print(len(input("matn: ")))







































# numbers = [1,2,3,4,5]
# numbers.pop(2)
# print(numbers)



# list = ["ab", "cd"]
# for i in list:
#     i.upper()
# print(list)



# for i in range(0):
#     print(i)


# li = [1,2,3]
# print(li.pop(2))


# x = "--hello-world-"
# x = x.strip("-")
# print(x)

# any_list = [1,2,'3',1,2,5,5,'a','a']

# print(set(any_list))


# any_list = [1,2,'3',1,2,5,5,'a','a']

# for element in set(any_list):
#     count = any_list.count(element)
#     print(f"{element}:{count}")




# #  juft sonlarni topish
# def juft (num):
#         if num % 2 == 0:
#                 return 'juft son'
#         return 'toq son'
# while True :
#         javob = int(input('Raqam: '))

#         print(juft(javob))











# 1   -  misol   len vazifasi 


# def sanash(a):
#     n = 0
#     for i in a:
#         n+=1
    
#     return n
# matn = input("matn ")

# print(sanash(matn))




#  2   -  misol  islower faqat kichik harflarni tekshiradi


# def len(text):
#     n = 0
#     for i in text:
#         n += 1
#     return n


# def islower(text):
#     for s in text:
#         if ord(s) >= 65 and ord(s) <= 90:
                
#                 return False

#     return True
# matn = input("matn: ")
# print(islower(input("matn: "))
# print(len(input("matn: ")))





# print(isupper("HAMZA  USTOZ"))



# 10 - Misol
# def isdigit(text):
#         for s in text:
#                 if not(ord(s)>=48 and ord(s)<=57):
#                         return False
#         return True
# print(isdigit("998902062026"))

#  11  - Misol

# def isalpha(text):
#         text1 = ''
#         for s in text:
#                 if ord(s)>=97 or ord(s)<=12:
#                         text1 += chr(ord(s) + 32)
#                 else:
#                         text1 += s
#                         return False
#         return text
# print(isalpha("eee1"))


#  12  -  Misol
# def replace(text, work1,work2):
#         work = " "
#         text1 = " "
#         for s in text:
#                 if work == work1:
#                         text1 += work2
#                         work = s
#                 elif len(work) == len(work1):
#                         text1 += work[0]
#                         work = work[1:] + s
#                 else:
#                         return text1 + work1
# print(replace("salom apple", "salom",  "apple"))

         

#LIST METODLARI
# ""
# "append"
# "extend"
# def count(list):
#         for element in set(any_list):
#                 count = any_list.count(element)
#                 return True 
# any_list = [1,2,'3',1,2,5,5,'a','a']
# print(f"{element}:{count}")







# any_list = [1,2,'3',1,2,5,5,'a','a']

# for element in set(any_list):
#     count = any_list.count(element)
#     print(f"{element}:{count}")



# def juft (num):
#         if num % 2 == 0:
#                 return 'Juft son'
#         return 'Toq son'
# while True :
#         javob = int(input('Raqam: '))

#         print(juft(javob))




# meva = ["olma", "banan","apelsin", "nok", "uzum"]
# a = [1, 2, 3, 4 , 5 ]
# meva.sort()
# a.sort()
# print(meva)
# print(a)

# meva.reverse()
# a.reverse()
# print(meva)
# print(a)



# def meva(olma, banan, apelsin,nok, uzum):
#         a = [1, 2, 3, 4 , 5 ]
#         meva.sort()
#         a.sort()
#         return "togri"



# o = input("olma")
# b = input("banan")
# a = input("apelsin")
# n = input("nok")
# u = input("uzum")


# print(meva(o,b,a,n,u))
# print(a)

# meva.reverse()
# a.reverse()

# print(meva)
# print(meva(o,b,a,u)



# meva = ["olma", "banan","apelsin", "nok", "uzum"]
# meva.append("anor")
# print(meva)


# meva = ["olma", "banan","apelsin", "nok", "uzum"]
# meva.insert(1, "banan")
# print(meva)




# meva = ["olma", "banan","apelsin", "nok", "uzum"]
# meva.remove("uzum")
# print(meva)
















#  STR  metodlari
# """"""""""
# capitalize
# center
# endswith
# startswith 
# lower
# upper  
# islower
# isdigit
# isalpha
# len
# replace
# """""""""""""""

#    1    -   Misol 
# def len(text):
#         n = 0
#         for s in text:
#                 n += 1
#         return n
# print(len(input("matn: ")))


#   2  - Misol
# def capitalize(text):
#         n = 0
#         text1 = " "
#         for s in text:
#                 if ord(s)>=65 and ord(s)<=90:
#                         text1 += chr(ord(s) + 32)
#                 else:
#                         text1 += s
#         return first + text1
# print(capitalize("sa"))

# #   3  Misol
# def center(text, number):
#         stars = (number - len(text)) // 2
#         ends = (number - len(text)) % 2
#         if len(text)>=number:
#                 return text
#         else:
#                 return " " * (starts + ends) + text  + " " * starts
# print(center("sas", 6))


#    4 - Misol
# def endswith(text, work):
#         d = len(work)
#         return text[-d::] == work
# print(endswith("salom", "om"))


#  5  - Misol
# def starswith(text, work):
#         d = len(work)
#         return text[ :d] == work 
# print(starswith("salom", "sa"))


#  # 6   -  Misol
# def lower(text):
#         text1 = ''
#         for s in text:
#                 if ord(s)>=65 and ord(s)<=90:
#                         text1 += chr(ord(s) + 32)
#                 else:
#                         text1 += s
#         return text1
# print(lower("EEEEEEEE"))



#  7  -  Misol
# def upper(text):
#         text1 = ''
#         for s in text:
#                 if ord(s)>=97 and ord(s)<=122:
#                         text1 += chr(ord(s) - 32)
#                 else:
#                         text1 += s
#         return text1
# print(upper("eeeeee"))


#  8   -  Misol
# def islower(text):
#         for s in text:
#                 if ord(s)>=65 and ord(s)<=90:
#                         return False
#         return True
# print(islower("+998974480400"))


#  9  -  Misol
# def isupper(text):
#         for s in text:
#                 if ord(s)>=97 and ord(s)<=122:
#                         return False
#         return True
# "count"
# "remove"
# "reverse"
# "clear"
# "sort"
# #




#1  -  MIsol
# def append(list,object):
#         return list + [object]
# a = [1,2,2,3,4,5]
# print(append(a, 1))


# 2 - MISOL

# def extend(list,object):
#         return list + object
# a = [1,2,2,3,4,5]
# print(extend(a, [1]))


#3 - MIsol
# def count(list, object):
#         n = 0
#         for s in list:
#                 if object == s:
#                         n += 1
#         return n
# a = [1,2,2,3,4,5]
# print(count(a, 2))


# 4  - MISOL
# def remove(list, object):
#         list = []
#         n = 0
#         for s in list:
#                 if n == 0 and s == object:
#                         s = s
#                 else:
#                         list.append(s)
#                         n += 1
#         return list
# a = [1,2,2,3,4,5]
# print(remove(a, 2))


#  5 -  MISOL
# def reverse(list):
#         return list[::-1]
#         for s in list:
       
#                 if n == 0 and s == object:
#                         s = s
#                 else:
#                         list.append(s)
#                         n += 1
#         return list
# a = [1,2,2,3,4,5]
# print(reverse(a))


# 6 - Misol
# def clear(list):
#         return []

#         for s in list:
#                 if n == 0 and s == object:
#                         s = s
#                 else:
#                         list.append(s)
#                         n += 1
#         return list
# a = [1,2,2,3,4,5]
# print(clear(a))


# #  7 - MISOL 
# lst = [1,2,3,4,5,5,4,3,2,1]
# dct = {}
# for s in lst:
#         if not s in dct:
#                 dct[s] = 1
#         else:
#                 dct[s] = dct[s] + 1

# txt = ""
# for d in dct:
#         txt += str(d)
# lst = []
# for d in dct:
#         lst += [d] * dct[d]

# print(lst)


# file_name = input("file nomi: ")
# matn = input("matn: ") 
# def qoshish(file_name, txt):


# 23 - dekabr
# 1 - misol
# a = [4,5,7,54,5,4,5,4]
# a.sort()
# print(a)

# 2 -  misol
# d = {}
# d['a'] = 2
# print(d)

# 3 - misol
# d = {}
# d['ru'] = "Ru"
# d['uz'] = "Uz"
# print(d)

#4 - misol
# d = {}
# d['olma'] = "apple"
# d['salom'] = "Hi"
# print(d["salom"])


# 5  -  misol
# lst = "salomsalom"
# dct = {}
# for s in lst:
#         if not s in dct:
#                 dct[s] = 1
#         else:
#                 dct[s] = dct[s] + 1

# txt = ""
# for d in dct:
#         txt += d

# print(dct)


# 6  - misol 
# lst = "salomsalom"
# dct = {}
# for s in lst:
#         if not s in dct:
#                 dct[s] = 1
#         else:
#                 dct[s] = dct[s] + 1

# txt = ""
# for d in dct:
#         txt += d

# print(set(txt))

# 7 -  MISOL
# lst = "salomsalom"
# dct = {}
# for s in lst:
#         if not s in dct:
#                 dct[s] = 1
#         else:
#                 dct[s] = dct[s] + 1

# txt = ""
# for d in dct:
#         txt += d

# print(set([1,2,3,4,5,5,4,3,2,1]))



# 8  - MISOL
# lst = "saloma"
# dct = {}
# for s in lst:
#         if not s in dct:
#                 dct[s] = 1
#         else:
#                 dct[s] = dct[s] + 1
# for d in dct:
#         print(d)

# print(dct)


# 9 - MISOL
# lst = "saloma"
# dct = {}
# for s in lst:
#         if not s in dct:
#                 dct[s] = 1
#         else:
#                 dct[s] = dct[s] + 1
# set = set(dct)

# print(dct)




# 1 - MISOL
# with open("salom.txt", "w") as f:
        # f.write("Hi salom")
# 
# 2  - MISOL
# with open("salom.txt", "r") as f:
        # d = f.read()
# print(d)


# 3 -  MISOL
# file_name = input("file nomi: ")
# text = input("matn: ")
# with open("{}". format(file_name),"w") as f:
#         f.write(text)




#  4  -  MISOL
# file_name = input("file nomi: ")
# #text = input("matn: ")
# with open("{}".format(file_name),"r") as f:
#         d = f.read()

# for s in d:
#         print(s)


# #pip #install #num2words
# from num2words import num2words
# num2words(42, lang='fr')
#  # //quarante-deux







#         with open("{}".format(file_name), "r") as f:
#                 d = f.read()

#         if d == "":
#                 with open("salom.txt", "w") as f:
#                         f.write("{}".format(txt))
#         else:
#                 with open("salom.txt", "w") as f:
#                         f.write(d + " {}".format(txt))
# print(qoshish(file_name, matn))











# with open("{}".format(file_name),"r") as f:
#         d = f.read()

# for s in d:
#         print(s)


# #pip #install #num2words
# from num2words import num2words
# num2words(42, lang='fr')
#  # //quarante-deux





# 2 - Uyga vazifa

# a = {"Sharof", "Sharof", "Hamza", "Hamza"}
# print(a)


#  1 -  MISOL
# with open("g1.txt", "w") as f:
#         f.write("g1.txt: erkak: 15 ta; ayol: 1 ta; o'rtacha oylik: 653,0625 so'm")


# with open("g2.txt", "w") as f:
#         f.write("g2.txt: erkak: 15 ta; ayol: 1 ta; o'rtacha oylik: 715,875 so'm")


# with open("u1.txt", "w") as f:
#         f.write("u1.txt: erkak: 15 ta; ayol: 1 ta; o'rtacha oylik: 903,0625 so'm")






# # uyga vazifa ism, familya,oylik
# lst = ["g1.txt", "g2.txt", "u1.txt"]
# m = ""
# for g in lst:
#         gr = [:-4]
#         with open("{}.format(g", "r") as f:
#                 malumotlat = f.read()
#         malumotlar = malumotlar.replace("\n" "-").replace(" ", "+")
#         oylik = 0
#         son = 0
#         n = " "
#         for s in malumotlar:
#                 if ord(s)>=48 and ord(s)<57:
#                         n += s
#                 elif s == "-":
#                         son += 1
#                         oylik += int(n)
#                         n = ""
#         m += "{} da o'rtacha oylik {} \n".format(gr, oylik/son)
#         with open("status.txt", "w") as l:
#                 l.write(m)
#         with open("g1.txt", "r") as f:
#                 data = f.read()
#         data = data.replace("\n","-").replace("", "+")
#         bitta_oldingi = ""
#         n = 1
#         nom = " "
#         ismlar = []
#         familyalar = []
#         for s in data:
#                 if s == "+" and n % 2 == 1 and not(nom in ismlar):
#                         ismlar.append(nom)
#                         nom = ""
#                         n += 1
#                 elif s == "+" and n % 2 == 0:
#                         familyalar.append(nom)
#                         nom = " "
#                         n += 1
#                 elif nom in ismlar:
#                         nom = " "
#                         n += 1
#                 elif 65<=ord(s)<=90 or 97<= ord(s)<=122:
#                         nom +s
# print(ismlar, "\n\n", familyalar)
# erkak = 



# def kupaytir(x, y):
#         return int(x) * int(y)

# a = input("Birinchi raqam: ")
# b = input("Ikkinchi raqam: ")

# print(kupaytir(a, b))


















# lst = ["g1.txt", "g2.txt", "u1.txt"]
# m = ""
# for g in lst:
#         gr = [:-4]
#         with open("{}.format(g", "r") as f:
#                 malumotlat = f.read()
#         malumotlar = malumotlar.replace("\n" "-").replace(" ", "+")
#         oylik = 0
#         son = 0
#         n = " "
#         for s in malumotlar:
#                 if ord(s)>=48 and ord(s)<57:
#                         n += s
#                 elif s == "-":
#                         son += 1
#                         oylik += int(n)
#                         n = ""
#         m += "{} da o'rtacha oylik {} \n".format(gr, oylik/son)
#         with open("status.txt", "w") as l:
#                 l.write(m)
#         with open("g1.txt", "r") as f:
#                 data = f.read()
#         data = data.replace("\n","-").replace("", "+")
#         bitta_oldingi = ""
#         n = 1
#         nom = " "
#         ismlar = []
#         familyalar = []
#         for s in data:
#                 if s == "+" and n % 2 == 1 and not(nom in ismlar):
#                         ismlar.append(nom)
#                         nom = ""
#                         n += 1
#                 elif s == "+" and n % 2 == 0:
#                         familyalar.append(nom)
#                         nom = " "
#                         n += 1
#                         elif nom in ismlar:
#                                 nom = " "
#                                 n += 1
#                 elif 65 <= ord(s)<=90 or 97<=ord(s)<=122:
#                         nom += s
#         print(ismlar, "\n\n", familyalar)
#         erkak = 0
#         ayol = 0
#         for f in familyalar:
#                 if f[-1] == "a":
#                         ayol += 1
#                 else:
#                         erkak += 1
#         print("erkak {} ayol {}."format(erkak, ayol))





# lst = ["g1.txt", "g2.txt", "u1.txt"]
# m = ""
# for g in lst:
#         gr = [ -4]
#         with open("{}".format("g", "r") as f:
#                 malumotlat = f.read()
#         malumotlar = malumotlar.replace("\n" "-").replace(" ", "+")
#         oylik = 0
#         son = 0
#         n = " "
#         for s in malumotlar:
#                 if ord(s)>=48 and ord(s)<57:
#                         n += s
#                 elif  s == "-" :
#                         son += 1
#                         oylik += int(n)
#                         n = ""
#         m += "{} da o'rtacha oylik {} \n".format(gr, oylik/son)
#         with open("status.txt", "w") as l:
#                 l.write(m)
#         with open("g1.txt", "r") as f:
#                 data = f.read()
#         data = data.replace("\n","-").replace("", "+")
#         bitta_oldingi = ""
#         n = 1
#         nom = " "
#         ismlar = []
#         familyalar = []
#         for s in data:
#                 if s == "+" and n % 2 == 1 and not(nom in ismlar):
#                         ismlar.append(nom)
#                         nom = ""
#                         n += 1
#                 elif s == "+" and n % 2 == 0:
#                         familyalar.append(nom)
#                         nom = " "
#                         n += 1
#                 elif nom in ismlar:
#                                 nom = " "
#                                 n += 1
#                 elif 65 <= ord(s)<=90 or 97<=ord(s)<=122:
#                         nom += s
#         print(ismlar, "\n\n", familyalar)
#         erkak = 0
#         ayol = 0
#         for f in familyalar:
#                 if f[-1] == "a":
#                         ayol += 1
#                 else:
#                         erkak += 1
#         print("erkak {} ayol {}" .format(erkak, ayol))




# meva = input("Masulot kiriting: ")
# kilo = input("Kilogram kiriting:")

# print(savdo = "{} kg olmani {}-do'kondan {} so'mga sotib oldim"




# a = input('mahsulot: ')
# b = input("kilo: ")


# while True:
#         if a == b:
#                 print("nechhi kilo olasiz")
#         elif a >= b:
#                 print(f"Siz", a, "mahsulotdan", b, "kilo oldingiz ")
#         print("Yana qanday mahsulot xarid qilasiz? ")
        
        
#         break




# a = input('mahsulot: ')
# b = input("kilo: ")


# while True:
#         if a == b:
#                 print("mahsulotni kirting")
#         elif a >= b:
#                 print(f"Siz", a, "mahsulotdan", b, "kilo oldingiz ")
#         print("Yana qanday mahsulot xarid qilasiz? ")
#         k = input("mahsulot kiriting: ")
#         m = input("kilo kiriting: ")
#         if k == m:
#                 print("mahsulot kiriting")
#         elif k >= m:
#                 print(f"Siz", k, "mahsulotdan", m, "kilo oldingiz ")
#         d = input("mahsulot kiriting: ")
#         s = input("kilo kiriting: ")
#         if d == s:
#                 print("mahsulot kiriting")
#         elif d >= s:
#                 print(f"Siz", d, "mahsulotdan", s, "kilo oldingiz ")
#         sh = input("mahsulot kiriting: ")
#         k = input("kilo kiriting: ")
#         if sh == k:
#                 print("mahsulot kiriting")
#         elif sh >= k:
#                 print(f"Siz", sh, "mahsulotdan", k, "kilo oldingiz ")

#         print("XARINGIZ UCHUN RAHMAT")
#         break




# print("Assalomu aleykum")
# print("Onlane do'konimizga xush kelibsiz")
# print("Bizda qovun - 5 ta, tarvuz - 10 ta bor")
# qovun = 5
# tarvuz = 10
# tovarlar = ["qovun", "tarvuz"]
# print("mahsulot oalsizmi? yoki qo'shasizmi?")
# a = input("qo'shmoqchi bo'lsangiz -- 1 sonini.  \nayirmoqchi bo'lsangiz ---2  sonini kiriting.\n=====> ")
# while not (a == '1' or a == '2'):
#         print("Siz xato kiritdingiz")
#         print("qaytadan kiriting")
#         a = input("qo'shmoqchi bo'lsangiz -- 1 sonini.  \nayirmoqchi bo'lsangiz ---2  sonini kiriting.\n=====> ")
# if a == '1':
#         b = input("qaysi mahsulot qo'shmoqchimisiz? .\n====> ")
#         while not (b == "tarvuz" or b == "qovun"):
#                 print("xato kiritdingiz qaytadan kiriting ")
#                 b = input("qaysi mahsulot qo'shmoqchisiz?.\n====> ")
#         if b == "tarvuz":
#                 b = int(input("tarvuz soni {} ta \nsiz qancha qo'shasiz.\n====> ".format(tarvuz)))
#                 tarvuz += b
#                 print('tarvuz = {} ta qoladi. '.format(tarvuz))
#         elif b == 'qovun' :
#                 b = int(input("qovunlar soni {} ta \nsiz qancha qo'shasiz.\n====>".format(qovun)))
#                 qovun += b
#                 print('qovun = {} ta qoladi.'.forma(qovun))
# elif a == '2':
#         b = input("qaysi mahsulot olmoqchimisiz. \n=====> ")
#         while not (b == 'tarvuz' or b == 'qovun'):
#                 print("xato kiritdingiz qaytadan kiriting ")
#                 b = input("qaysi mahsulot olmoqchisiz?.\n=====>")
#         if b == 'tarvuz':
#                 b = int(input("tarvuz soni {} ta \nsiz qancha olasiz?.\n====> ".format(tarvuz))
#                 tarvuz -= b
#                 print('tarvuz = {} ta qoladi. '.format(tarvuz))
#         elif b == 'qovun':
#                 b = int(input("qovunlar soni {} ta \nsiz qancha olasiz?.\n===> ".format(qovun)))
#                 qovun -= b
#                 print("qovun = {} ta qoladi. ".format(qovun))
# print("savdongiz uch raxmat")
# print("yana biror nima olasizmi? \nsavdo qilmoqchi bo'lsangiz --xa-- deb yozing. \nsavdo qilmoqchi bo'lmasangiz --yo'q deb yozing.")
# qayta = input('\n====[xa-yoki-yoq]===>')
# # 2 marta
# while qayta == 'xa':
#         print("Onlane do'konimizga xush kelibsiz")
#         print("Bizda qovun-{} ta , tarvuz- {} ta bor".format(qovun,tarvuz))
#         tovarlar = ["qovun", "tarvuz"]
#         print("mahsulot olasizmi yoki qo'shasizmi?")
#         a = input("qo'shmoqchi bo'lsangiz -> 1 sonini kiriting. \nayirmoqchi bo'lsangiz -> 2 sonini kiriting.\n=====>")
#         while not(a== '1' or a == '2'):
#                 print("Siz xato kiritdingiz")
#                 print("Qayta kiriting")
#                 a = input("Qo'shmoqchi bo'lsangiz -> 1 sonini kiriting.\nayirmoqchi bo'lsangiz -> 2 sonini kiriting.\n===>")

#         if a == '1':
#                 b = input("Qaysi mahsulot qo'shmoqchisiz?. \n====> ")
#                 while not(b== 'tarvuz' or b == 'qovun'):
#                         print("Xato kiritdingiz qaytadan kiriting ")
#                         b = input("Qaysi mahsulot qo'shmoqchisiz.\n=====>"))
#                 if b == 'tarvuz':
#                         b = int(input("qovunlar sonini {} ta \nsiz qancha qo'shasiz.n\======> ".format(tarvuz)))
#                         tarvuz += b
#                         print("qovun = {} ta qoladi.".format(tarvuz))
#                 elif b == 'qovun':
#                         b = int(input("qovunlar soni {} ta \nsiz qancha qo'shasiz.\n====>".fotmat(qovun))) 
#                         qovun += b
#                         print('qovun = {} ta qoladi.'.format(qovun))
#         elif a == '2':
#                 b = input("Qaysi mahsulot olmoqchisiz.\n====> ")
#                 while not(b== 'tarvuz' or b == 'qovun'):
#                         print("Xato kiritdingiz qaytadan kiriting")
#                         b = input("Qaysi mahsulot olmoqchisiz.\n======> ")
#                 if b == 'tarvuz':
#                         b = int(input("tarvuzlar soni {} ta \nsiz qancha olasiz.\n====> ".format(tarvuz)))
#                         tarvuz-= b
#                         print("tarvuz = {} ta qoladi .".format(tarvuz))
#                 elif b == 'qovun':
#                         b = int(input("qovunlar soni {] ta \nsiz qancha olasiz.\n====> ".format(qovun)))
#                         qovun -= b
#                         print('qovun = {} ta qoladi. '.format(qovun))
#         print("Savdo qilgangiz uchun rahmat")
#         print("yana biror nima olasizmi? \nsavdo qilmoqchi bo'lsangiz --xa-- deb yozing. \nsavdo qilmoqchi bo'lmasangiz --yo'q deb yozing.")
#         qayta = input("\n=====[xa -yoki - yo'q]===>")
# if qayta == "yo'q":
#         print("Xaridingiz uchun rahmat Do'konimizga yana kelib turing ")



# i = 5
# while i < 15:
#         print(i)
#         i = i + 2


# for i in 'hello world':
#         print(i * 2, end='')


# for i in 'hello world':
#         if i == 'o':
#                 continue
#         print(i * 2, end='')








        
       
# def elnora() :
#         abs = ("ASSALOMU ALEYKUM")
#         return(abs)

# print(elnora())


# with open("salom. eee", "w") as f:
        # f.write("assalomu aleykum Elineora")

# with open("salom. eee", "r") as f:
        # d = f.read()
# print(d)
# 










# Cankulyator shaxi
# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5029304354:AAHFmOQb8XuuGIUt9wxrPrdLo0hMD9juToQ")
# def sabr(message):
    # text = len(message.text)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
# def omad(message):
    # text = eval(message.text)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
    # bot.register_next_step_handler(message,shrine)
# def shrine(message):
    # if message.text == "Sabr":
        # bot.send_message(message.chat.id, "so'z yozing", reply_markup=ReplyKeyboardMarkup())
        # bot.register_next_step_handler(message, sabr)
    # elif message.text == "Omad":
        # bot.send_message(message.chat.id, "misol kiriting", reply_markup=ReplyKeyboardMarkup())
        # bot.register_next_step_handler(message, omad)
    # elif message.text == "Baxt":
        # bot.send_message(message.chat.id, "salom")
        # bot.register_next_step_handler(message, shrine)
    # else:
        # bot.send_message(message.chat.id, "87542")
        # bot.register_next_step_handler(message, shrine)
# def get_keyboard():
    # keyboard = ReplyKeyboardMarkup(row_width=1)
    # btn1 = KeyboardButton("Sabr")
    # btn2 = KeyboardButton("Omad")
    # btn3 = KeyboardButton("Baxt")
    # keyboard.add(btn1, btn2, btn3)
    # return keyboard
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
    # bot.send_message(message.chat.id, "Assalomu aleykum", reply_markup=get_keyboard())
    # bot.register_next_step_handler(message,shrine)
# bot.polling()






























#Ustoz o'tgan len(harfni sonini sanaydigan)
# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5029304354:AAHFmOQb8XuuGIUt9wxrPrdLo0hMD9juToQ")
# def sabr(message):
    # text = len(message.text)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
# def shrine(message):
    # if message.text == "Sabr":
        # bot.send_message(message.chat.id, "so'z yozing", reply_markup=ReplyKeyboardRemove())
        # bot.register_next_step_handler(message, sabr)
    # elif message.text == "Omad":
        # bot.send_message(message.chat.id, "2")
        # bot.register_next_step_handler(message, shrine)
    # elif message.text == "Baxt":
        # bot.send_message(message.chat.id, "3")
        # bot.register_next_step_handler(message, shrine)
    # else:
        # bot.send_message(message.chat.id, "4")
        # bot.register_next_step_handler(message, shrine)   
# def get_keyboard():
    # keyboard = ReplyKeyboardMarkup(row_width=1)
    # btn1 = KeyboardButton("Sabr")
    # btn2 = KeyboardButton("Omad")
    # btn3 = KeyboardButton("Baxt")
    # keyboard.add(btn1, btn2, btn3)
    # return keyboard
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
    # bot.send_message(message.chat.id, "Assalomu aleykum", reply_markup=get_keyboard())
    # bot.register_next_step_handler(message, shrine)
# bot.polling()
# 
































# Yuldashev tashagan
# import telebot
# from countryinfo import CountryInfo
# from telebot.types import *
# 
# 
# 
# bot = telebot.TeleBot("5029304354:AAHFmOQb8XuuGIUt9wxrPrdLo0hMD9juToQ")
# def sabr(message):
    # text = len(message.text)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
# def omad(message):
    # text = eval(message.text)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
    # bot.register_next_step_handler(message,shrine)
# def shrine(message):
    # if message.text == "Sabr":
        # bot.send_message(message.chat.id, "so'z yozing", reply_markup=ReplyKeyboardMarkup())
        # bot.register_next_step_handler(message, sabr)
    # elif message.text == "Omad":
        # bot.send_message(message.chat.id, "misol kiriting", reply_markup=ReplyKeyboardMarkup())
        # bot.register_next_step_handler(message, omad)
    # elif message.text == "Baxt":
        # user = User()
        # bot.send_message(message.chat.id, "davlat kiriting", reply_markup = CountryInfo())
        # bot.register_next_step_handler(message, shrine)
    # else:
        # bot.send_message(message.chat.id, "87541")
        # bot.register_next_step_handler(message, shrine)
# def get_keyboard():
    # keyboard = ReplyKeyboardMarkup(row_width=1)
    # btn1 = KeyboardButton("Sabr")
    # btn2 = KeyboardButton("Omad")
    # btn3 = KeyboardButton("Baxt")
    # keyboard.add(btn1, btn2, btn3)
    # return keyboard
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
    # bot.send_message(message.chat.id, "Assalomu aleykum", reply_markup=get_keyboard())
    # bot.register_next_step_handler(message,shrine)
#bot.polling()














import telebot
from telebot.types import *
bot = telebot.TeleBot("5276608966:AAGUbhVLSiAvdzZ6uJH34SWyRRBIvB799sk")
def mirza(message):
    text = len(message.text)
    bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
def shrine(message):
    if message.text == "Mirza":
        bot.send_message(message.chat.id, "soz yozing", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, mirza)
    elif message.text == "Ulugbek":
        bot.send_message(message.chat.id, "2")
        bot.register_next_step_handler(message, shrine)
    elif message.text == "Temuriy":
        bot.send_message(message.chat.id, "3")
        bot.register_next_step_handler(message, shrine)
    else:
        bot.send_message(message.chat.id, "4")
        bot.register_next_step_handler(message, shrine)
def get_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=1)
    btn1 = KeyboardButton("Mirza")
    btn2 = KeyboardButton("Ulugbek")
    btn3 = KeyboardButton("Temuriy")
    keyboard.add(btn1, btn2, btn3)
    return keyboard
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "salom", reply_markup=get_keyboard())
    bot.register_next_step_handler(message, shrine)
bot.polling()





# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5029304354:AAHFmOQb8XuuGIUt9wxrPrdLo0hMD9juToQ")
# def sabr(message):
    # text = len(message.text)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
# def omad(message):
    # text = eval(message.text)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
    # bot.register_next_step_handler(message,shrine)
# def shrine(message):
    # if message.text == "Sabr":
        # bot.send_message(message.chat.id, "so'z yozing", reply_markup=ReplyKeyboardMarkup())
        # bot.register_next_step_handler(message, sabr)
    # elif message.text == "Omad":
        # bot.send_message(message.chat.id, "misol kiriting", reply_markup=ReplyKeyboardMarkup())
        # bot.register_next_step_handler(message, omad)
    # elif message.text == "Baxt":
        # bot.send_message(message.chat.id, "salom")
        # bot.register_next_step_handler(message, shrine)
    # else:
        # bot.send_message(message.chat.id, "87541")
        # bot.register_next_step_handler(message, shrine)
# def get_keyboard():
    # keyboard = ReplyKeyboardMarkup(row_width=1)
    # btn1 = KeyboardButton("Sabr")
    # btn2 = KeyboardButton("Omad")
    # btn3 = KeyboardButton("Baxt")
    # keyboard.add(btn1, btn2, btn3)
    # return keyboard
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
    # bot.send_message(message.chat.id, "Assalomu aleykum", reply_markup=get_keyboard())
    # bot.register_next_step_handler(message,shrine)
# bot.polling()
# 
# 


#Cankulyator ustoz o'rgatganlari
# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5176679667:AAFzZLLfVvx87WNZg1Z7He3R__GE85HH5B0")
# data = {895752511: "123"}
# def user(message):
    # if not message.chat.id in data:
        # data[message.chat.id] = "0"
        # return "0"
    # return data[message.chat.id]
# 
# 
# @bot.callback_query_handler(func=lambda x: x.data == "=")
# def equality(call):
    # exam = data[call.message.chat.id]
    # data[call.message.chat.id] = "0"
    # bot.send_message(call.message.chat.id, eval(exam))
    # bot.send_message(call.mesage.chat.id, user(call.message), reply_markup=get_keyboard())
    # 
# 
# @bot.callback_query_handler(func = lambda x: x.data in "/*-+.")
# def action(call):
    # user_action = call.data
    # user_id = call.message.chat.id
    # exam = data[user_id]
    # if not (exam[-1]) in "/*-+":
        # exam += user_action
    # data[user_id] = exam
    # bot.edit_message_text(
        # exam,
        # call.message.chat.id,
        # call.message.id,
        # reply_markup=get_keyboard()
    # )
# @bot.callback_query_handler(func=lambda x: x.data.isdigit())
# def add_element(call):
    # number = call.data
    # exam = data[call.message.chat.id]
    # if exam == "0":
        # exam = number
    # else:
        # exam = exam + number
    # data[call.message.chat.id] = exam
    # bot.edit_message_text(
        # exam,
        # call.message.chat.id,
        # call.message.id,
        # reply_markup = exam
        # )
    # 
# @bot.callback_query_handler(func=lambda x: x.data == "<-")
# def delete_last(call):
    # if exam != "0":
        # exam = exam[:-1]
    # elif len(exam) == 1:
        # exam = '0'
    # data[call.message.chat.id] = exam
    # bot.edit_message_text(
        # exam,
        # call.message.chat.id,
        # call.message.id,
        # reply_markup =get_keyboard()
    # )
# @bot.callback_query_handler(func=lambda x: x.data ==  "delete_all")
# def delete_all(call):
    # user_id = call.message.chat.id
    # data[user_id] = "0"
    # bot.edit_message_text(
        # "0",
    # call.message.chat.id,
    # call.message.id,
    # reply_markup =get_keyboard()
    # )
    # 
    # 
    # 
# def get_keyboard():
    # keyboard = InlineKeyboardMarkup(row_width=4)
    # btn = InlineKeyboardButton(" ", callback_data = "none")
    # btn1 = InlineKeyboardButton("C", callback_data = "delete_all")
    # btn2 = InlineKeyboardButton("<-", callback_data = "delete_last")
    # btn3 = InlineKeyboardButton("/", callback_data = "/")
    # btn4 = InlineKeyboardButton("*", callback_data = "*")
    # btn5 = InlineKeyboardButton("-", callback_data = "-")
    # btn6 = InlineKeyboardButton("+", callback_data = "+")
    # btn7 = InlineKeyboardButton("=", callback_data = "=")
    # btn8 = InlineKeyboardButton(".", callback_data = ".")
    # 
    # btn9 = InlineKeyboardButton("0", callback_data = "0")
    # btn10 = InlineKeyboardButton("1", callback_data = "1")
    # btn11 = InlineKeyboardButton("2", callback_data = "2")
    # btn12 = InlineKeyboardButton("3", callback_data = "3")
    # btn13 = InlineKeyboardButton("4", callback_data = "4")
    # btn14 = InlineKeyboardButton("5", callback_data = "5")
    # btn15 = InlineKeyboardButton("6", callback_data = "6")
    # btn16 = InlineKeyboardButton("7", callback_data = "7")
    # btn17 = InlineKeyboardButton("8", callback_data = "8")
    # btn18 = InlineKeyboardButton("9", callback_data = "9")
# 
    # keyboard.add(btn, btn1, btn2, btn3)
    # keyboard.add(btn16, btn17, btn18, btn4)
    # keyboard.add(btn13, btn14, btn15, btn5)
    # keyboard.add(btn10, btn11, btn12, btn6)
    # keyboard.add(btn, btn8, btn8, btn7)
# 
    # return keyboard
# 
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
    # bot.send_message(message.chat.id, "salom", reply_markup=get_keyboard())
# 
# 
# 
# bot.polling()


















# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5180793095:AAF1ZBkbBCQJ_SqpD3BOgXp7WAf6UG4GR5s")
# 
# 
# data = {"photo": []}

# 
# def photo(message):
    # if message.photo:
        # photo_id = message.photo[-1].file_id
        # data['photo'] = data['photo'] + photo_id
        # print(data['photo'])
        # bot.send_photo(message.chat.id, photo_id)
    # else:
        # bot.send_message(message.chat.id, "Iltimos rasm kiriting")
        # bot.register_next_step_handler(meassage, photo)




# def photo(message):
    # if message.location:
        # print(message.location)
        # bot.send_location(message.chat.id, message.location.latitude, message.longitude)
        # bot.send_location(message.chat.id, message.location.longitude, message.latitude)
# def photo(message):
    # if message.photo:
        # photo_id = message.photo[-1].file_id
        # bot.send_photo(message.chat.id, photo_id, caption="Algoritm turlari")       
        # 
    # else:
        # bot.send_message(message.chat.id, "Iltimos rasm kiriting")
        # bot.register_next_step_handler(meassage, photo)
# @bot.message_handler(func=lambda x: x.text != "")
# def send_welcome(message):
    # bot.send_message(message.chat.id, "Rasm kiriting")
    # bot.register_next_step_handler(message, photo)
    # 
# @bot.message_handler(func=lambda x: True)
# def send_welcome(message):
    # print(message.content_type)
    # 
# bot.polling()





# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5229530708:AAEbx8gXsujFoXciRwcakD73qxloauc-278")
# 
# 
# 
# def kino(message):
#    text = len(message.text)
#    bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
# def pycharm(message):
#    text = message.text
#    bot.send_message(message.chat.id, f"{text}", reply_markup=get_keyboard())
#    bot.register_next_step_handler(message,shrine)
# def shrine(message):
#    if message.text == "Kino":
    #    bot.send_message(message.chat.id, "kinoni tanlang",)
    #    bot.register_next_step_handler(message, kino)
#    elif message.text == "Pycharm":
    #    bot.send_message(message.chat.id, "Pychramni olasizmi?")
    #    bot.register_next_step_handler(message, pycharm)
#   
# 
# 
# 
# 
# def get_keyboard():
    # keyboard = InlineKeyboardMarkup(row_width=2)
    # btn = InlineKeyboardButton("Majruh")
    # btn1 = InlineKeyboardButton("Hayot")
    # btn2 = InlineKeyboardButton("Qalb gavhari")     
    # keyboard.add(btn, btn1, btn2)
    # 
    # return keyboard
# 
# 
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
    # bot.send_message(message.chat.id, "Assalomu aleykum")
# 
# 
# 
# bot.polling()





















# import telebot
# from telebot.types import *
# bot = telebot.TeleBot("5266261551:AAFmF1WZH6UONiuqMblxbSwsPAGKlRlnRe0")
# 
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
    # bot.send_message(message.chat.id, "Assalomu aleykum")
# 
# 
























































import telebot
from telebot import types
from telebot.types import *

bot = telebot.TeleBot("5130581538:AAEiRhl1JanOZUUf9kYYcXLvURlsga8qdjE")
@bot.message_handler(commands=["start"])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text="KINO")
    btn2 = types.KeyboardButton(text="MUSIC")
    btn3 = types.KeyboardButton(text="PyCharm")
    keyboard.add(btn1,btn2,btn3)
    bot.send_message(message.chat.id,"Select button,which you interested:",reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def start_text(message):
    if message.text =="KINO":
        keyboard = types.InlineKeyboardMarkup()
        url1 = types.InlineKeyboardButton(text="Liga Adjustise 2021",url="https://t.me/Tudum_Netflix/247")
        url2 = types.InlineKeyboardButton(text="Liga Adjustise 2017",url="https://t.me/Tudum_Netflix/245")
        url3 = types.InlineKeyboardButton(text="Forsag 9",url="https://t.me/Tudum_Netflix/242")
        url4 = types.InlineKeyboardButton(text="Infinity",url="https://t.me/Tudum_Netflix/234")
        url5 = types.InlineKeyboardButton(text="Back To Menu",callback_data = "Back")
        keyboard.add(url1,url2,url3,url4,url5)
        
        bot.send_message(message.chat.id,"Choose your movie:",reply_markup=keyboard)
    
    if message.text =="MUSIC":
        keyboard = types.InlineKeyboardMarkup()
        url1 = types.InlineKeyboardButton(text="Several",url="https://t.me/vkm_bot")
        url2 = types.InlineKeyboardButton(text="Uzbek Music",url="https://t.me/Uzbek_zakaz_music_qo_shiqlar")
        url3 = types.InlineKeyboardButton(text="Arabian Musics",url="https://t.me/bass_muzikil999")
        url4 = types.InlineKeyboardButton(text="Russian Music",url="https://t.me/russianmuiscnews")
        url5 = types.InlineKeyboardButton(text="Back To Menu",callback_data = "Back")
        keyboard.add(url1,url2,url3,url4,url5)
        
        bot.send_message(message.chat.id,"Choose your music:",reply_markup=keyboard)

    if message.text =="PyCharm":
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="Yes",callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text="No",callback_data='no')
        keyboard.add(key_no)

        question = f"Do you want to install PyCharm?"
        bot.send_message(message.from_user.id,text = question, reply_markup = keyboard)

@bot.callback_query_handler(func=lambda call:True)
def get_call(call):
    username = call.message.from_user.username
    if call.data == "Back":
        send_welcome(call.message)

    if call.data== "yes": 
        bot.send_message(call.message.chat.id,"https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows")
    elif call.data== "no": 
        bot.send_message(call.message.chat.id,f"Lol {username}, see you again..!")
        bot.register_next_step_handler(call.message,send_welcome)
bot.polling()




# import telebot
# from telebot.types import *
# 
# 
# bot = telebot.TeleBot("5113084134:AAE1Pm_3YzMYEwu0jKVEVUukLVzs4tEwLBs")
# 
# 
# 
# data = {
    # "user": {},
    # "admin": [],
    # "type": {}
    # 
# }
# 
# 
# 
# def get_keyboard():
    # return ReplyKeyboardMarkup(resize_keyboard = True).add(
        # KeyboardButton("Ro'yxatdan o'tish")
    # )
# def data_text(message):
    # user_data = data["user"][message.chat.id]
    # if user_data:
        # text = f"Ism: {user_data['first_name']}\n" \
            #    f"Familiya: {user_data['last_name']}\n" \
            #    f"Tlefon nomer: {user_data['phone']}\n"
        # return text
    # user_data = {
        # "first_name": "-",
        # "last_name": "-",
        # "phone": "-"
    # }
    # return "Ism: -\n" \
        #    "Familiya: -\n" \
        #    "Telefon nomer: -"

# @bot.message_handler(func=lambda x: x.text == "Ro'yxatdan o'tish")
# def registration(message):
    # text = data_text(message)
    # bot.send_message(message.chat.id, f"{text}", reply_markup=get_inlinekeybord())
    # 
# @bot.message_handler(commands="start")
# def start(message):
    # print(message)
    # if message.chat.id not in data['user']:
        # data["user"][message.chat.id] = {}
    # print(data)
    # bot.send_message(message.chat.id, f"salom {message.from_user.first_name}", reply_markup=get_keyboard())

# def get_keyboard():
    # return ReplyKeyboardMarkup(resize_keyboard =True).add(
        # KeyboardButton("Ro'yxatdan o'tish")
    # )
# 
# def get_inlinekeybord():
    # keyboard = InlineKeyboardButton(row_width=1)
    # first_name = InlineKeyboardButton("Ism", callback_data ="first_name+1")
    # last_name = InlineKeyboardButton("Familiya", callback_data="last_name+1")
    # phone = InlineKeyboardButton('telefon nomer', callback_data="phone+1")
    # return keyboard.add(first_name, last_name, phone)
# 
# 
# def uptade_type(message):
    # user_id = message.chat.id
    # user_type = data['type'][user_id]
    # text = message.text
    # if user_type == 'phone':
        # if text.startswith("+998") and len(text) == 13 and text[1:].isdigit():
            # data["user"][user_id][user_type] = message.text
            # bot.send_message(user_id)
        # else:
            # bot.send_message(user_id, "Boshqatdan {type[user_type]} kiriting")
            # bot.register_next_step_handler(message, update_type)
    # else:
        # if text.isalpha():
            # data['user'][user_id][user_type] = message.text
            # bot.send_message(user_id, "Sizning kiritgan malumotingiz qabul qilindi")
        # else:
            # type = {
                # "first_name": "Ism",
                # "last_name": "Familiya"
                # 
            # }
            # bot.send_message(user_id, f"Boshqatdan {type[user_type]} kiriting")
            # bot.register_next_step_handler(message, update_type)
    # 
# 
# @bot.callback_query_handler(func=lambda x: x.data.split("+")[-1] == "1")
# def update_user_data(call):
    # type_user = call.data.split("+")[0]
    # user_id = call.meassage.chat.id
    # data['type']['user_id'] = type_user
    # type ={
        # "first_name": "Ism",
        # "last_name": "Familiya",
        # "phone": "Telefon nomer"
    # }
    # bot.edit_message_text(
        # f"{type[type_user]} kiriting",
        # call.message.chat.id,
        # call.message.id
    # )
    # bot.register_callback_query_handler(call.message, update_type)
# def data_text(message):
    # user_data = data['user'][message.chat.id]
    # print(user_data)
    # if user_data:
        # text = f"Ism: {user_data['first_name']}\n" \
            #    f"Familiya: {user_data['last_name']}\n" \
            #    f"Telefon nomer: {user_data['phone']}"
        # return text
    # data["user"][message.chat.id] = {
        # "first_name": "-",
        # "last_name": "-",
        # "phone": "-"
    # }
    # return "Ism: -\n" \
        #    "Familiya: -\n" \
        #    "Telefon nomer: -"
# i
        #    
# bot.polling()





# n = 12
# def ebo(n):
    # if n == 0:
        # return 0 
    # return n + ebo(n-1)
# print(ebo(12))


# a = int(input('son kiriting: '))
# def ebo(n):
    # if n == 0:
        # return 1
    # return n * ebo(n-1)
# 
# print(ebo(a))


