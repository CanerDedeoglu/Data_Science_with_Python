
#############################################################################

###  PYTHON İLE VERİ ANALİZİ ( DATA ANALYSIS WITH PYTHON )

############################################################################

# - Numpy
# - Pandas
# - Veri Görselleştirme : Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Veri Analizi : ( Advanced Functional Exploraty Data Analysis )


# Neden Numpy ?

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a * b

# Numpy Array'i Oluşturmak ( Creating Numpy Arrays )

import numpy as np

np. array([1, 2, 3, 4, 5])

np.zeros(10, dtype=int)

np.random.randint(0, 10, size=10)

np.random.normal(10, 4, size=(3, 4))

# Numpy Array Özellikleri (Attibutes of Numpy Arrays )

import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)

a.ndim
a.shape
a.size
a.dtype

# Yeniden Şekillendirme (Reshaping)

np.random.randint(1, 9, size=9)
np.random.randint(1, 9, size=9).reshape(3, 3)

# İndex Seçimi

a = np.random.randint(10, size=10)

a[0]
a[0: 5]
a[0] = 99

m = np.random.randint(10, size=(3, 5))

m[0, 0]

### PANDAS

import pandas as pd

S = pd.Series([10, 77, 12, 4, 5])

type(S)

S.index

S.dtype

S.size

S.ndim

# Veri Okuma

import pandas as pd

df = pd.read_csv("datasets/Iris.csv")
df.head()

# Veriye Hızlı Bakış

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.describe().T
df.isnull().values.any()
df.isnull().sum() #Değişkenlerdeki eksik verinin sayısını verir.
df["sex"].value_counts()

#Pandas'ta Seçim işlemleri

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0,axis=0).head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)
#df.drop(delete_indexes, axis=0, inplace=True).head(10) inplace methodu yapılan işlemin kalıcı olmasını sağlar.

### iloc & loc

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

#iloc :integer based selection

df.iloc[0: 3]
df.iloc[0, 0] #Belirli satır ve sütundaki elemana erişme

#loc : label based selection

df.loc[0:3]

df.iloc[0: 3, 0: 3] #virgülden öncesi satır,sonrası sütun

df.loc[0:3, 'age'] #label based olduğu için sütun olarak değişkeni seçebiliriz.

col_names = ["age", "embarked", "alive"]

df.loc[0: 3, col_names]

### Koşullu Seçim (Conditional Selection )

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df["age"]
df[df["age"] > 50]
df[df["age"] > 50].count()

df.loc[df["age"] > 50, ["age", "class"]].head()

df[(df["age"] > 50) & (df["sex"] == "male")]


###### Toplulaştırma ve Gruplama( Aggregation & Grouping)

# -count()
# -first()
# -last()
# - mean()
# -median()
# -min()
# -max()
# -std()
# -var()
# -sum()
# -pivot table

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()
df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})
df.groupby("sex").agg({"age": ["mean", "sum"],
                      "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"],
                                        "survived": "mean"})

#### Pivot Table

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embark_town") #default halde ortalama alır

df.pivot_table("survived", "sex", "embark_town", aggfunc="count") #Agg func sayesinde default değeri değiştirebiliyoruz.

df.pivot_table("survived", ["sex", "class"], ["embark_town"])

df["new age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90]) #Numeric değişkeni karakterik değişkene çevirme

df.pivot_table("survived", "sex", "new age")

#### Apply and Lambda

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")

df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

df[['age', "age2", "age3"]].apply(lambda x: x/10).head()


# Birleştirme(Join) İşlemi

import pandas as pd
import numpy as np

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2]) #Alt alta birleştirme
pd.concat([df1, df2], ignore_index=True) #index sıfırlama

## Merge ile birleştirme

df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "groups": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees") #hangi indexe göre birleştirme yapılacağı belirleme

#Amaç : her çalışanın müdür bilgisine erişmek istiyoruz.

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"groups": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

pd.merge(df3, df4)


##### Veri Görselleştirme : MATPLOTLIB & SEABORN

### MATPLOTLIB

# Veri görselleştirme kütüphanelerin atasıdır.
# Low level görselleştirme aracıdır.

# Kategorik değişken : sütun grafik.
# Sayısal değişken : hist, boxpot

# KATEGORİK DEGİŞKEN GÖRSELLEŞTİRME

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show()

# Sayısal Değişken Görselleştirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

# Matplotlib'in Özellikleri

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

#### plot

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, "o")
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, "o")
plt.show()

## marker

y = np.array([13, 28, 11, 100])

plt.plot(y, marker="o")

#### line

y = np.array([13, 28, 11, 100])
plt.plot(y)
plt.show()

plt.plot(y, linestyle="dashed")
plt.show()

### Multiple Lines

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)
plt.show()

### Labels

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

# Başlık
plt.title("Bu ana başlık")

# X eksenini isimlendirme
plt.xlabel("X eksenini isimlendirme")

# Y eksenini isimlendirme
plt.ylabel("Y eksenini isimlendirme")

plt.grid() #Izgara koyma

# Subplots

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 20, 34, 65, 95])
y = np.array([24, 20, 26, 30, 30, 45, 62, 80, 72, 96])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()

## SEABORN

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show()

sns.histplot(data=df, x=df["total_bill"])
df["total_bill"].hist()
plt.show()