
# SAYILAR ( İNTEGER ) : int,float,complex

a=5
type(a)

b=10.5
type(b)

a * 3
a / 7
a * b
a ** 2 #Karesini alma

#Tipleri değiştirmek

int(b)
float(a)

int(a * b / 10)

c= a * b / 10

int(c)

# Karakter Dizileri (Strings)

print("John")
               #Tek tırnak ve iki tırnağın bi farkı yok.Size kalmış :)
print('John')

name = "John"
              #Atama işlemi yaparak yazdırma
print(name)

# Çok satırlı karakter dizileri

""" 
 VeriYapıları: Hızlı Özet,
 Sayılar(Numbers): int,float,complex
 Karakter dizileri(strings):str
 List,Turple,Dictionary,Set
 Boolen(True/False):bool
 
"""

long_str=""" 
 VeriYapıları: Hızlı Özet,
 Sayılar(Numbers): int,float,complex
 Karakter dizileri(strings):str
 List,Turple,Dictionary,Set
 Boolen(True/False):bool """

# Karakter dizilerinde eleman seçmek

name
name[1]
name[3]
name[0]

# Karakter dizilerinde slice işlemi

name= "Caner Dedeoğlu"

name[0:4] #Sıfırdan başla 4'e kadar git

name[0:10:2] #Sıfırdan başla 10'a kadar 2'şer 2'şer git

name[ : :-1] #Tersten yazdırma işlemi

# String içerisinde karakter sorgulama

long_str

"veri" in long_str # İçinde var mı yok mu ? (Büyük küçük harf hassasiyeti olduğundan False der.)

"Veri" in long_str

"Caner" in name

# String(Karakter Dizisi) Methodları

dir(int) #Veri yapısına ait methodları gösterir.

dir(str)

##### len ####

name

len(name) #Name değişkeninin uzunluğunu verir.

len(long_str)

len("Miull")

#Bir fonksiyon class yapısı içerisinde ise method, değilse fonksiyondur.

# upper() - lower() : büyük-küçük dönüşümleri

"miuul".upper() #Yazan ifadeyi büyük harflere dönüştürme

"CANER DEDEOĞLU".lower() #Yazan ifadeyi küçük harflere dönüştürme

# replace : Karakter değiştirme

hi = "Hello AI Era"

hi.replace("l","p")

# split : bölme işlemi için

hi.split()

### LİSTE (LİST) ###

# - Değiştirilebilir.
# - Sıralıdır.Index işlemleri yapılabilir.
# - Kapsayıcıdır.

notes = [0,1,2,3,4]

type(notes)

names= ["a","b","v"]

not_nam = [0,1,2,True,[1,2,3]] #Kapsayıcıdır özelliği

not_nam[0]

not_nam[4]

not_nam[4][1] #Listedeki elemana erişme  #Listeler sıralıdır elemana ulaşılabilir.

notes[0]=99 #Değiştirilebilir.

## Liste Mothodları

dir(list)

# append:eleman ekleme

notes.append(52) #sonuna ekler.

# pop: indexe göre eleman silme

not_nam.pop(3)

# insert: indexe göre eleman ekler.

not_nam.insert(3,True)

## Sözlük (Dictonary]

# -Değiştirilebilir.
# -Sırasızdır.(Python 3.7 sonrası sıralı )
# -Kapsayıcıdır.
# key-value çiftleri

dictionary = { "REG":"Regression",
               "LOG":"Logistic Regression",
               "CART":"Classification and Reg"
             }

type(dictionary)

dictionary["REG"] #Değerini çağırma

sozluk = {
    "REG":["REG",10],
    "LOG":["LOG",20],
    "CART":["CART",30]
}

# Key sorgulama

"REG" in dictionary

# Key'e göre value değerlerine erişme

dictionary["REG"]      #İki türlüde erişme yapılabilir.
dictionary.get("REG")

# Value değiştirmek

dictionary["REG"] = ["REG",15]

# Tüm keylere erişme

dictionary.keys()

# Tüm value değerlerine erişme

dictionary.values()

# Key-value değerlerini güncelleme - Yeni key-value çifti ekleme de yapar.

dictionary.update({"REG":11})

# Tuple(Demet)

# Değiştirilemez.
# Sıralı
# Kapsayıcı

t = (0,1,True,[2,3])

type(t)

t[0]=33 #Değiştirilemez özelliği

# Set

# Değiştirilebilir.
# Sırasız + Eşsizdir.
# Kapsayıcıdır.

