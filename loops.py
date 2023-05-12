
######## DÖNGÜLER (LOOPS)

## FOR LOOP

students = ["Maria", "john", "Venessa", "Mark"]

students[0]
students[1]
students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(salary*0.2 + salary)

for salary in salaries:
    print(salary*0.3 + salary)

for salary in salaries:
    print(salary*0.5 + salary)

def new_salary(salary, rate):
    return salary*rate/100 + salary

new_salary(1500, 10)

for salary in salaries:
    print(new_salary(salary,10))

for salary in salaries:
    if salary > 3000:
        print(new_salary(salary, 20))
    else :
        print(new_salary(salary, 10))

#Amaç : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

#before : "hi my name is john and i am learning python
#after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0 :
            new_string += string[string_index].upper()
        else :
            new_string+= string[string_index].lower()

    print(new_string)

alternating("hi my name is john and i am learning python")

## Break Continue while

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries :
    if salary == 3000:
        break
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

## While

number = 1
while number < 5 :
    print(number)
    number += 1

### Enumerate: Otomatik Counter / Indexer ile For Loop

students = ["John", "Maria", "Venessa", "Mark"]

for student in students:
    print(student)

for index,student in enumerate(students):
    print(index,student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0 :
        A.append(student)
    else:
        B.append(student)

## Uygulama - Mülekat sorusu

# divide_student fonksiyonu yaz.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return dönsün,

students = ["Mark", "john", "Venessa", "Mariam"]

def divide_student(students):
    groups = [[], []]
    for index,student in enumerate(students):
        if index % 2 == 0 :
            groups[0].append(student)
        else:
            groups[1].append(student)

    print(groups)
    return groups

divide_student(students)

### Zip

students = ["Mark", "John", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 15]

list(zip(students,departments,ages))

#### lambda, map, filter, reduce

def summer(a, b):
    return a * b

new_sum = lambda a,b : a+b

new_sum(4,5)

#map

salaries = [100, 200, 300, 400]

def new_salary(x):
    return x * 0.2 + x

new_salary(500)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))

list(map(lambda x: x * 0.2 + x, salaries))

### FILTER

list_store = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(filter(lambda x: x % 2 == 0, list_store))