import math


# print("5 - misol ")
# print("3 tasidan kattasini topadigan")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a >= b and b >= c:
    # print('a')
# elif b >= a and b >=c:
    # print('b')
# else:
    # print('c')


#print("7 - misol")
# def islower(text):
    # for s in text:
        # if ord(s) >= 65 and ord(s) <= 90:
            # return False
    # return True   
# 
# matn = input("matn: ")
# print(islower(matn))
 

# 
# 
# def sanash(a):
    # n = 0
    # for i in a:
        # n+=1
    # 
    # return n
# matn = input("matn")
# print(sanash(matn))
# 




#print("7 -  misol")
# def lower(text):
    # text1 = ''
    # for s in text:
        # if ord(s)>=65 and ord(s)<=90:
            # text1 += chr(ord(s) + 32)
        # else:
            # text1 += s
    # return text1
# print(lower("SLOMJ"))



#print("8 - misol ")
# def upper(text):
        # text1 = ''
        # for s in text:
                # if ord(s)>=97 and ord(s)<=122:
                    # text1 += chr(ord(s) - 32)
                # else:
                    # text1 += s
        # return text1
# print(upper("salom"))



# print("3  - misol ")
# a = input("son: ")
# d = 0
# if "o'n" in a:
    # d += 10
# elif "yigirma" in a:
    # d += 20
# 
# if 'bir' in a:
    # d += 1
# elif "ikki" in a:
    # d += 2
# print(d)


#  
# print(" 1 - misol" )
# n = input("Enter number: k(0<k<9999")
# n = int(n)
# d1 = n % 10
# d2 = n % 100 // 10
# d3 = n % 1000 // 100
# d4 = n // 1000
# print("Result:", d1 + d2 + d3 + d4)





# 
# 
# print("2 -  misol")
# lst = ['G', 'D', 'E']
#dct = {}
# for s in lst:
        # if not s in dct:
                # dct[s] = 7
        # else:
            # dct[s] = dct[s] + 1
# print(dct)
# 



# print("6 - misol ")
# lst = ["1,2,a,b,h,g"]
# dct = {}
# for s in lst:
    # if not s in dct:
        # dct[s] = 1
    # else:
        # dct[s] = dct[s] + 1

# txt = ""
# for d in dct:
    # txt += d
# print(set([1,2]))




# print("9 - misol ")
# matn = input("matn= ")
# natija = 0
# for harf in matn:
    # if harf == "s" or harf == "s":
        # natija += 1
# print(natija)
# 



# 
# print("10 - misol")
# a = int(input("son kiriting: "))
# d = "" 
# if a // 10 > 0 and a // 10 == 1:
    # d += "X"
# elif a // 10 > 0 and a // 10 == 2:
    # d += "XX"
# elif a // 10 > 0 and a // 10 == 3:
    # d += "XXX"
# elif a // 10 > 0 and a // 10 == 4:
    # d += "XL"
# elif a // 10 > 0 and a // 10 == 5:
    # d += "L"
# if a % 10 == 1:
    # d += 'I'
# elif a % 10 == 2:
    # d += 'II'
# elif a % 10 == 3:
    # d += "III"
# elif a % 10 == 4:
    # d += "IV"
# elif a % 10 == 5: 
    # d += "V"
# elif a % 10 == 6:
    # d += "VI"
# elif a % 10 == 7:
    # d += "VII"
# elif a % 10 == 8:
    # d += "VII"
# elif a % 10 == 9:
    # d += "IX"
# print(d)

# 
# print("8 - misol ")
# matn = input("matn = ")
# natija = ""
# for e in matn:
    # if ord(e) >= 97 or ord(e) <=120:
        # natija = ord(e) - 32
    # print(chr(natija), end = "")