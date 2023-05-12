
############ KURAL TABANLI SINIFLANDIRMA İLE POTANSİYEL MÜŞTERİ GETİRİSİ HESAPLAMA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

# 1. Dosyayı okutunuz ve veri seti ile igili genel bilgileri gösteriniz.

df = pd.read_excel("datasets/miuul_gezinomi.xlsx")
df.head()
df.tail()
df.shape
df.info()
df.index

# 2. Kaç unique şehir vardır ? Frekansları nedir ?

print(df["SaleCityName"].unique()) #Şehirlerin neler olduğunu gösterir.
print(df["SaleCityName"].nunique()) #Kaç tane şehir olduğunu gösterir.
print(df["SaleCityName"].value_counts()) # Veri setinde bulunan şehirlerin kaç kere kullanıldığını gösterir.

# Kaç tane Concept vardır ?

print(df["ConceptName"].unique())
print(df["ConceptName"].nunique())

# Hangi Concepten kaç tane satış gerçekleşmiş ?

print(df["ConceptName"].value_counts())

# Şehirlere göre satışlardan toplamda ne kadar kazanılmış ?

print(df.groupby("SaleCityName")["Price"].sum())
print(df.groupby("SaleCityName").agg({"Price" : "sum"}))

# Concept türlerine göre ne kadar kazanılmış ?

print(df.groupby("ConceptName").agg({"Price": "sum"}))

# Şehirlere göre Prıce ortalamaları nedir ?

print(df.groupby("SaleCityName").agg({"Price": "mean"}))

# Conceptlere göre Prıce ortalamaları nedir ?
print(df.groupby("ConceptName").agg({"Price": "mean"}))

# Şehir - Concept kırılımında Price ortalamaları nedir ?

print(df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"}))

# satis_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz.

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index=False)

# Şehir, Concept, [EB_Score, Sezon, CInday] kırılımında ücret ortalamaarına ve frekanslarına bakınız.

# - Şehir -Concept - EB Score kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]})
# - Şehir -Concept - Sezon kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})
# - Şehir -Concept - CInday kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})


# City - Concept - Seasons kırılımının çıktısını Prıce' a göre sıralayınız. Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)
agg_df.head(20)

# Indexte yer alan isimleri değişken ismine çeviriniz.

agg_df.reset_index(inplace=True)

agg_df.head()

# Yeni seviye tabanlı satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# • Yeni eklenecek değişkenin adı: sales_level_based
# • Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek sales_level_based değişkenini oluşturmanız gerekmektedir.

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: "_".join(x).upper(), axis=1)

# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
# • Yeni personaları PRICE’a göre 4 segmente ayırınız.
# • Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# • Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# • Antalya’da herşey dahil ve yüksek sezonda tatil yapmak isteyen bir kişinin ortalama ne kadar gelir kazandırması beklenir?
# • Girne’de yarım pansiyon bir otele düşük sezonda giden bir tatilci hangi segmentte yer alacaktır?

new_user ="ANTALYA_HERŞEY DAHIL_HIGH"
new_user2 = "GIRNE_YARIM PANSIYON_LOW"

agg_df[agg_df["sales_level_based"]== new_user]
agg_df[agg_df["sales_level_based"]== new_user2]
