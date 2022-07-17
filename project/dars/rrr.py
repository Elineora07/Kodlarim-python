    for x in range(0,16):
        for y in range(25):
            shart1 = x==0 or x==5 or x==10 or x==15
            shart2 = y==0 or y==24
            shart3 = x==1 and (y>5 and y<=10 or y>2 and y<4)
            shart4 = x==2 and (y>5 and y<=9 or y>1 and y<3)
            shart5 = x==3 and(y>5 and y<=8 or y>1 and y<3)
            shart6 = x==4 and(y>2 and y<4)
            if shart1 or shart2 or shart3 or shart4 or shart5 or shart6:
                print("* ",end="")
            else:
                print("  ",end="")
        # print()
        
        
for x in range(10):
    for y in range(25):
        if y == 0 or y==24 or x==0 or x==9:
           print("_ ", end="")
        elif x==3 or x==6:
            print("- ", end='')
        elif x ==1 and (y>5 and y<12): 
            print("%", end='')
        else:
            print("  ", end='')          
    print()
#o'zgaruvchilar 4-dars
# print(7+8)
# ism = "Abdulloh"
# yosh = "25 yoshda"
# print(ism)
# print(yosh)
# ism = "Abdulloh"
# print(ism)
# ism ="Muhammad"
# print(ism)
# a = 6
# b = 7
# c = (a+b)**2
# print(c)
# a = 6 
# b = 7
# c = (6+7)**2
# print(c)
# ism_sharif = 'Anvar Narzullayev '
# print(ism_sharif)
# ism_sharif_ochistva = "ELINEORA XUDOYQULOVA ULUG'BEK QIZI"
# print(ism_sharif_ochistva)
# shahar ="QO'QON"
# print(shahar)
# viloyat = ('FARG\'ONA')
# print(viloyat)
#String yani Matn ustida amaallar
# ism ='ELINEORA'
# print("MENINING ISMIM " + ism)
# ism = 'ELINEORA'
# familya ='XUDOYQULOVA'
# print(ism + familya)
# ism = 'elineora '
# familya = 'xudoyqulova'
# print(ism + familya')

# ism = 'elineora'
# familya = 'xudoyqulova'
# print(ism + ' ' + familya)
#f-stringdan foydalanib  matn yozsak "matnnimizni alohida korishda yani bir qatorda biita probil joy tashlangan korinishda korsatadi" ham boldai. bunda qoshtirnoqdan foydalish maqul
# ism = 'elineora' 
# familya = 'xudoyqulova'
# ism_familya =f"{ism} {familya}"
# print(ism_familya)
# ism = "Elineora"
# familya = "Xudoyqulova"
# # print(f"Salom, Mening ismim {ism}. {familya} {ism}!")
# # print("Salom Mening Ismim Elineora . Xudoyqulova Elineora!")
# print('Hello World')
# print('Hello \tWorld') #bu "\t" belgisi uzun boshliq qoldiradi
# print('Hello \nWorld') # bu "\n" belgisi esa keyingi qatorga o'tkazadi

# STRING METODLARI:

# ism = input("ism kiriting ")
# familya = input("familya kiriting ")
# ism_familya =f"{ism} {familya}"
# print(ism_familya.upper()) #bu so'z "upper" hamma harflarni katta harflar ko'rishida chiqazadi
# # ism_familya = ism_familya.upper() #bunda yozgan sozimizni ozi katta harflarga aylanadi"
# ism = "ELINEORA"
# familya = "XUDOYQULOVA"
# print(ism_familya.lower()) # bu so'z "lower" yozgan matn yoki hokazo sozlarni kichikdan hammasini katta qiladi

# ism_sharf = 'elineora xudoyqulova'
# ism_sharf = ism_sharf.title() # bu so'z "title" matn yoki sozdagi ikkita kelgan matn yoki sozlarni birinchi matn bilan ikkinchi matnni bosh harfga aylantiradi.
# print(ism_sharf)

# ism_sharf = 'elineora xudoyqulova'
# ism_sharf = ism_sharf.capitalize() # bu so'z "capitalize" ikkita matn yoki so'z kelganda birinchi matnni yoki so'zni birinchi harfini katta qilib chiqazadi 
# print(ism_sharf)

# meva = "     olma    "
# print(meva)
# print("Men " + meva.lstrip() + "yaxsi ko'raman") # bu so'z "lstrip" bu qoldirilgan boshliqni chap tarafini oladi yani chap tarafida bo'shliq qolmaydi.

# meva = "    olma    "
# print("Men " + meva.rstrip() + " yaxshi ko'raman") # bu so'z "rstrip" bu qoldirilgan bo'shliqni o'ng tarafini oladi yani o'ng tarafida bo'shliq qoldirmaydi 

# meva = "    olma   "
# print("Meva " + meva.strip() + " yaxshi ko'raman") # bu so'z "strip" chap tarafni ham o'ng tarafni boshliqlarsiz ko'rsatadi.

# meva = "     olma   "
# print("Meva " + meva + " yaxshi ko'raman") # bunda chap tarafdan ham o'ng tarafdan ham bo'shliq qoldirib yozadi.

# INPUT FUNKSIYASI:

# ism = input("Ismingiz nima?")
# print("Assalomu aleykum" + ism)

# ism = input("Ismingiz nima?\n>>>")  # \n keyingi satrga >>> alohida satrga yozadi
# print("Assalomu aleykum" + ism.title())
