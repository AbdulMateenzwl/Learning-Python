import pandas as pd

df = pd.read_csv('data.csv')

# print(df.head(100))

df["Is_Adult"] = df["value"] >= 18

df.to_csv("new_data.csv", index=False)
