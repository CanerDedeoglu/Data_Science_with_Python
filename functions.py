###### FONKSİYONLAR (FUNCTİONS) #########

######### Fonksiyon tanımlama ########

def calculate(x):
    print(x * 2)


calculate(5)


# İki argümanlı / parametreli fonksiyon tanımlama

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(5, 2)


##### Docstring ######


def summer(arg1, arg2):
    """
   Sum of two numbers
   Parameters
   ----------
   arg1: int,float
   arg2: int,float

   Returns
   -------

   """
    print(arg1 + arg2)


summer(2, 5)


##### Fonksiyonların Statement/Body Bölümü

# def function_name(parameters/arguments):
#   statement(function body)

def say_hi():
    print("Merhaba")
    print("Hi")
    print("Bonjurne")


say_hi()


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(1, 5)

#girilen değerleri bir liste içinde saklayacak bir fonksiyon.

list_store=[]

def add_element(a,b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(3, 5)


### Ön tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)

def divide(a,b):
    print(a / b)


divide(1, 2)

def divide(a, b=1):  #B ön tanımlı argüman
    print(a / b)


divide(5)

### Return: Fonksiyon çıktılarını girdi olarak kullanmak

def calculate(warm, moisture, charge):
    print((warm+moisture) / charge)


calculate(98,12,5)

def calculate(warm, moisture, charge):
    return ((warm+moisture) / charge)


calculate(98,12,5)

def calculate(warm, moisture, charge):
    warm=warm * 2
    moisture= moisture * 2
    charge = charge * 2
    output= (warm + moisture) / charge
    return warm,moisture,charge,output


warm,moisture,charge,output=calculate(98,12,5)

#### Fonksiyon içinde fonksiyon Çağırma

def calculate(warm, moisture, charge):
    return int(((warm+moisture) / charge))


calculate(98,12,5)*10

def standartizion(a, p):
    return a * 10 / 100 * p * p

standartizion(45,1)

def all_calculation(warm,moisture,charge,p):
    a=calculate(warm,moisture,charge)
    b=standartizion(a,p)
    print(b * 10)

all_calculation(98,12,5,10)
