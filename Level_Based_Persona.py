#############################################
# LEVEL BASED PERSONA
#############################################
import pandas as pd
users = pd.read_csv('C:\\Users\\LENOVO\\Desktop\\hilal\\users.csv')
purchases = pd.read_csv('C:\\Users\\LENOVO\\Desktop\\hilal\\purchases.csv')
users.head()
purchases.head()
df = purchases.merge(users, how="inner", on="uid")
df.head()

#############################################
df.groupby(["country","device","gender","age"]).agg({"price":"sum"})
#############################################
agg_df = df.groupby(["country","device","gender","age"]).agg({"price":"sum"}).sort_values("price", ascending=False)
agg_df.head()
#############################################
agg_df.reset_index(inplace= True)
agg_df.columns
#############################################
agg_df["age_cat"] = pd.cut(agg_df["age"],
                           bins=[0, 19, 24, 31, 41, agg_df["age"].max()],
                           labels=["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["age"].max())])
agg_df.head()
#############################################
agg_df["customer_level_based"]=[rows[0]+"_"+rows[1].upper()+"_"+rows[2]+"_"+rows[5]  for rows in agg_df.values]

agg_df=agg_df[["customer_level_based","price"]]
agg_df = agg_df.groupby("customer_level_based").agg({"price":"mean"})
agg_df.reset_index(inplace=True)
agg_df.head()
#############################################
agg_df["segment"] = pd.qcut(agg_df["price"], 4, labels=["D", "C", "B", "A"])

agg_df
agg_df.groupby("segment").agg({"price":"mean"})

#############################################

new_user = "TUR_IOS_F_41_75"
new_users = agg_df.loc[agg_df["customer_level_based"] == new_user]
new_users
