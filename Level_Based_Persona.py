#############################################
# LEVEL BASED PERSONA
#############################################
# 1. users ve purchases veri setlerini okutunuz ve veri setlerini "uid" değişkenine göre inner join ile merge ediniz.
import pandas as pd
users = pd.read_csv('C:\\Users\\LENOVO\\Desktop\\hilal\\users.csv')
purchases = pd.read_csv('C:\\Users\\LENOVO\\Desktop\\hilal\\purchases.csv')
users.head()
purchases.head()
df = purchases.merge(users, how="inner", on="uid")
df.head()

# 2. country, device, gender, age kırılımında toplam kazançlar nedir?
df.groupby(["country","device","gender","age"]).agg({"price":"sum"})

# 3. Çıktıyı daha iyi görebilmek için kod'a sort_values metodunu azalan olacak şekilde price'a göre uygulayınız.
agg_df = df.groupby(["country","device","gender","age"]).agg({"price":"sum"}).sort_values("price", ascending=False)
agg_df.head()

# 4. agg_df'in index'lerini değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan price dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.

agg_df.reset_index(inplace= True)
agg_df.columns

# 5. age değişkenini kategorik değişkene çeviriniz ve agg_df'e "age_cat" ismiyle ekleyiniz.
# Aralıkları istediğiniz şekilde çevirebilirsiniz fakat ikna edici olmalı.

agg_df["age_cat"] = pd.cut(agg_df["age"],
                           bins=[0, 19, 24, 31, 41, agg_df["age"].max()],
                           labels=["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["age"].max())])
agg_df.head()
# 6. Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Önceki soruda elde ettiğiniz çıktıya göre veri setinde yer alan kategorik kırılımları
# müşteri grupları olarak düşününüz ve bu grupları birleştirerek yeni müşterileri tanımlayınız.
agg_df["customer_level_based"]=[rows[0]+"_"+rows[1].upper()+"_"+rows[2]+"_"+rows[5]  for rows in agg_df.values]

agg_df=agg_df[["customer_level_based","price"]]
agg_df = agg_df.groupby("customer_level_based").agg({"price":"mean"})
agg_df.reset_index(inplace=True)
agg_df.head()

# 7. Yeni müşterileri price'a göre segmentlere ayırınız, "segment" isimlendirmesi ile agg_df'e ekleyiniz.
# Segmentleri betimleyiniz.

agg_df["segment"] = pd.qcut(agg_df["price"], 4, labels=["D", "C", "B", "A"])

agg_df
agg_df.groupby("segment").agg({"price":"mean"})

# 8. 42 yaşında IOS kullanan bir Türk kadını hangi segmenttedir?
# agg_df tablosuna göre bu kişinin segmentini (grubunu) ifade ediniz.

new_user = "TUR_IOS_F_41_75"
new_users = agg_df.loc[agg_df["customer_level_based"] == new_user]
new_users
