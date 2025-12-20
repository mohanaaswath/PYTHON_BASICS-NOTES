import  pandas as pd

df = pd.read_csv("data.csv")
#print(df)

#selecting column
#print(df["Name"])
#print(df[["Name" , "Height" , "Weight"]])

#selecting row 

#print(df.loc["Charizard" , ["Height" , "Weight"]])


#filtering
tall_Pokiman = df[df["Height"] >= 2]
print(tall_Pokiman)

heavy_pokiman = df[df["Weight"] >= 100]
print(heavy_pokiman)


#aggregate

print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count(numeric_only=True))

print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Height"].count())

group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())