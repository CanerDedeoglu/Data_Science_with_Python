
######## COMPREHENSIONS ##########

######### LİST COMPREHENSIONS #########

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 0.2 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    print(new_salary(salary))
    null_list.append(new_salary(salary))

for salary in salaries:
    if salary > 3000 :
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2 ))

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000 ] #Eğer sadece if bloğu var ise if bloğu sağ tarafta yazılır.

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

####### DİCT COMPEHENSİONS


dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4
             }

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k,v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v * 2 for (k, v) in dictionary.items()}

# Amaç : Çift sayıların karesini alınarak bir sözlüğe eklenmek istemektedir.
# Keyler orijinal değerler valueler değişicek

numbers = range(10)
new_dict = {}


for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
print(new_dict)

{n:n ** 2 for n in numbers if n % 2 == 0}

#### LİST-DİCT COMPEHENSİONS UYGULAMALARI

# Bir veri setindeki Değişken isimlerini değiştirmek

# before :
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev' ]

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DİSTRACTED', 'NO_PREVİOUS', 'İNS_PREMİUM', 'İNS_LOSSES', 'ABBREV' ]

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

df = sns.load_dataset("car_crashes")

[col for col in df.columns if "ins" in col ]

["Flag " + col if 'ins' in col else "not_flag" + col  for col in df.columns]


# Amaç key'i string value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.

# Output:

# { 'total' : ['mean', 'min', 'max', 'var' ] ,
#   'speeding': ['mean', 'min', 'max', 'var'],
#   'alcohol': ['mean', 'min', 'max', 'var'],
#   'not_distracted': ['mean', 'min', 'max', 'var'],
#   'no_previous': ['mean', 'min', 'max', 'var'],
#   'ins_premium': ['mean', 'min', 'max', 'var'],
#   'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col  for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ['mean', 'min', 'max', 'var']
for col in num_cols:
    soz[col] = agg_list

# kısa yol
new_dict = { col : agg_list for col in num_cols}

