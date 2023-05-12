import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#  Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

df = pd.read_csv("datasets/persona.csv")

df.head()
df.shape
df.index
df.info()

#Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

print(df["SOURCE"].unique())
print(df["SOURCE"].nunique())

#Soru 3: Kaç unique PRICE vardır?

print(df["PRICE"].nunique())
print(df["PRICE"].unique())

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

print(df["PRICE"].value_counts())

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

print(df.groupby("COUNTRY").agg({"PRICE": "count"}))

#§ Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

print(df.groupby("COUNTRY").agg({"PRICE": "sum"}))

# Soru 7: SOURCE türlerine göre satış sayıları nedir?

print(df.groupby("SOURCE").agg({"PRICE":"count"}))
#§ Soru 8: Ülkelere göre PRICE ortalamaları nedir?

print(df.groupby("COUNTRY").agg({"PRICE": "mean"}))

# § Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

print(df.groupby("SOURCE").agg({"PRICE": "mean"}))

# § Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

print(df.groupby(by=["COUNTRY","SOURCE"]).agg({"PRICE": "mean"}))

# 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

print(df.groupby(by=["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}))

# Görev 3: Çıktıyı PRICE’a göre sıralayınız.
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE",ascending=False)
agg_df.head(50)

# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.

agg_df.reset_index(inplace=True)
agg_df.head()

# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
#Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'

agg_df["AGE_CAT"] = pd.qcut(agg_df["AGE"], 5, labels=["0_18", "19_23", "24_30", "31_40", "41_70"])
agg_df.head(30)

#############################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.


# YÖNTEM 2
agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'AGE_CAT']].agg(lambda x: '_'.join(x).upper(), axis=1)


# YÖNTEM 3
agg_df["customers_level_based"] = ['_'.join(i).upper() for i in agg_df.drop(["AGE", "PRICE"], axis=1).values]


# YÖNTEM 1
# değişken isimleri:
agg_df.columns

# gözlem değerlerine nasıl erişiriz?
for row in agg_df.values:
    print(row)

# COUNTRY, SOURCE, SEX ve age_cat değişkenlerinin DEĞERLERİNİ yan yana koymak ve alt tireyle birleştirmek istiyoruz.
# Bunu list comprehension ile yapabiliriz.
# Yukarıdaki döngüdeki gözlem değerlerinin bize lazım olanlarını seçecek şekilde işlemi gerçekletirelim:
[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]

# Veri setine ekleyelim:
agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
agg_df.head()

# Gereksiz değişkenleri çıkaralım:
agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))


# Amacımıza bir adım daha yaklaştık.
# Burada ufak bir problem var. Birçok aynı segment olacak.
# örneğin USA_ANDROID_MALE_0_18 segmentinden birçok sayıda olabilir.
# kontrol edelim:
agg_df["customers_level_based"].value_counts()

# Bu sebeple segmentlere göre groupby yaptıktan sonra price ortalamalarını almalı ve segmentleri tekilleştirmeliyiz.
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

# customers_level_based index'te yer almaktadır. Bunu değişkene çevirelim.
agg_df = agg_df.reset_index()
agg_df.head()

# kontrol edelim. her bir persona'nın 1 tane olmasını bekleriz:
agg_df["customers_level_based"].value_counts()
agg_df.head()


#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})



#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
