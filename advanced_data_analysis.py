############################################################################

 # GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTİONAL EDA )

###########################################################################

# 1.Genel Resim
# 2.Kategorik Değişken Analizi
# 3.Sayısal Değişken Analizi
# 4.Hedef Değişken Analizi
# 5.Korelasyon Analizi

# Genel Resim

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.info()
df.index
df.shape
df.columns
df.describe().T
df.isnull().values.any()
df.isnull().sum()


def check_df(dataframe, head=5):
    print("############################### Shape ################")
    print(dataframe.shape)
    print("############################### Types ################")
    print(dataframe.dtypes)
    print("############################### Head ################")
    print(dataframe.head(head))
    print("############################### Tail ################")
    print(dataframe.tail(head))


check_df(df)

## 2.Katagorik Değişken Analizi

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")
df.head()

df["embarked"].value_counts()
df["sex"].unique()
df["class"].nunique()

cat_col = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["float64", "int64"]]

cat_col = cat_col + num_but_cat

df[cat_col].nunique()

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))


for col in df.columns:
    cat_summary(df, col)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("####################################################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


cat_summary(df, "sex", plot=True)

for col in cat_col:
    if df[col].dtypes == "bool":
        print("adsdsadsdaddsd")
    else:
        cat_summary(df, col, plot=True)

for col in cat_col:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)


#### SAYISAL DEĞİŞKEN ANALİZİ

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")
df.head()


df[["age", "fare"]].describe().T

num_col =[col for col in df.columns if df[col].dtypes in ['int64', 'float64']]

num_col = [col for col in num_col if col not in cat_col]

def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df,"age")


for col in num_col:
    num_summary(df, col)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


num_summary(df, num_col, plot=True)

#################### DEĞİŞKENLERİN YAKALANMASI VE İŞLEMLERİN GENELLEŞTİRİLMESİ


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")
df.head()
df.info()

def glob_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Parameters
    ----------
    dataframe : dataframe
        değişken isimleri alınmak istenen dataframe dir.
    cat_th : int , float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th : int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
        cat_cols : list
            Kategorik değişken listesi
        num_cols: list
            Numerik değişken listesi
        cat_but_car:
            Kategorik görünümü kardinal değişken listesi

    """
    cat_col = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["float64", "int64"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_col = cat_col + num_but_cat
    #cat_col = [col for col in df.columns if col not in cat_but_car]
    num_col = [col for col in df.columns if df[col].dtypes in ['int64', 'float64']]
    num_col = [col for col in num_col if col not in cat_col]

    print(f"Observation : {dataframe.shape[0]}")
    print(f"Variable : {dataframe.shape[1]}")
    print(f"cat_col : {len(cat_col)}")
    print(f"num_col : {len(num_col)}")
    print(f"cat_but_car :{len(cat_but_car)}")
    print(f"num_but_car :{len(num_but_cat)}")

    return cat_col,num_col, cat_but_car

glob_col_names(df)

######################## Hedef Değişken Analizi

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = sns.load_dataset("titanic")

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def glob_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Parameters
    ----------
    dataframe : dataframe
        değişken isimleri alınmak istenen dataframe dir.
    cat_th : int , float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th : int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
        cat_cols : list
            Kategorik değişken listesi
        num_cols: list
            Numerik değişken listesi
        cat_but_car:
            Kategorik görünümü kardinal değişken listesi

    """
    cat_col = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["float64", "int64", "int32"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_col = cat_col + num_but_cat
    #cat_col = [col for col in df.columns if col not in cat_but_car]
    num_col = [col for col in df.columns if df[col].dtypes in ['int64', 'float64']]
    num_col = [col for col in num_col if col not in cat_col]

    print(f"Observation : {dataframe.shape[0]}")
    print(f"Variable : {dataframe.shape[1]}")
    print(f"cat_col : {len(cat_col)}")
    print(f"num_col : {len(num_col)}")
    print(f"cat_but_car :{len(cat_but_car)}")
    print(f"num_but_car :{len(num_but_cat)}")

    return cat_col,num_col, cat_but_car

cat_col,num_col, cat_but_car = glob_col_names(df)

## Hedef Değişkenin Kategorik Değişkenlerle Analizi

df.groupby("sex")["survived"].mean()

def target_summary_wit_cat(dataframe, target, categorical_col):

    print(pd.DataFrame({"Target mean ": dataframe.groupby(categorical_col)[target].mean()}))

target_summary_wit_cat(df,"survived","alone")

for col in cat_col:
    target_summary_wit_cat(df, "survived", col)

# Hedef Değişkenin Sayısal Değişkenlerle Analizi

df.groupby("survived")["age"].mean()

df.groupby("survived").agg({"age": "mean"})

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}))

target_summary_with_num(df,"survived", "age")

# Korelasyon Analizi

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

df = pd.read_csv("datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]

df.head()
num_col = [col for col in df.columns if df[col].dtype in [int, float]]

corr = df[num_col].corr()

sns.set(rc={"figure.figsize":(12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

#### Yüksek korelasyonlu değişkenlerin silinmesi

cor_matrix = df.corr().abs

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
