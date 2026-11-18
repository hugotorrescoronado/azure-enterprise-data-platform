import pandas as pd

df = pd.read_csv("../datasets/customers.csv")

df["name"] = df["name"].str.upper()

df.drop_duplicates(inplace=True)

df.to_csv(
    "../adls/curated/customers.csv",
    index=False
)

print("ETL completed")