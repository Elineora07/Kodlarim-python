import math 
# 
print(" 7 - MISOL  ")
# 
print("manfiy yoki musbat son ")
a = float(input('son kiriting: '))
if a > 0:
    print('siz musbat son kiritingiz')
else:
    print('siz manfiy son kiritdingiz')
# 
print(" 5 - MISOL  ")
ism = input("ISMINGIZ? ")
yil = int(input("yil  "))
if ism and yil:
    print("Salom", ism, "sizning yoshingiz", 2021 - yil, "da")
else:
    print("XATO")
# 
print(" 2 - Misol ")
soz = input("so'z ")
matn = input("2ta tildan birini tanlang [uzb/fransuz] ")
if matn == "uzb":
    print(soz, "KADIROV SHAROF USTOZ YAXSHIMISIZ? ISHLAR BILAN CHARCHAMAY YURIBSIZMI?")
elif matn == "fransuz":
    print(soz, "KADIROV SHAROF PROFESSEUR TU VAS BIEN? NE VOUS FATIGUEZ-VOUS PAS DES CHOSES?")
else:
    print("uzb yoki fransuz tilini tanlang")
# 
print(" 4 - Misol ")
a = int(input('son kiriting '))
if a %10 == 0 and a %5 == 0:
    print(a, 'soni 5 va 10 ga karrali')
else:
    print(a, 'karrali emas')
# 
# 
# 
# 
# 
# 
print(" Misol ")
a = int(input("1 -sonni kriting = "))
b = int(input("2 - sonni kiriting = "))
c = input('amal belgisini kiriting = ')
if c=='^':
    print(a**b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='+':
    print(a+b)
else:
    print(a-b)
















def displayhook(value):
    if value is None:
        return
    # Set '_' to None to avoid recursion
    builtins._ = None
    text = repr(value)
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout.buffer.write(bytes)
        else:
            text = bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)
    sys.stdout.write("\n")
    builtins._ = value