
######  KOŞULLAR(CONDITIONS) #########

#True-FALSE'u hatırlayalım.

1==1
1==2

###### İF

if 1==1:
    print("something")

if 1==2:
    print("something")

number=11

if number==10:
    print("number is 10")

number=10

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)

#### ELSE

def number_check(number):
    if number==10:
        print("number is 10")

    else:
        print("Number is not 10")

number_check(12)


##### ELİF

def number_check(number):
    if number>10:
        print("Number is bigger than 10")

    elif number==10:
        print("Number is 10")

    else:
        print("Number is smaller than 10")

number_check(9)