import pandas as pd

df = pd.read_csv("people.csv")
print(df)

df.to_excel("people.xlsx", index=False)

df2 = pd.read_excel("people.xlsx")
print(df2)
