import pandas as pd

df = pd.read_csv("../datasets/customers.csv")

assert df["customer_id"].isnull().sum() == 0

assert df["customer_id"].duplicated().sum() == 0

print("Validation successful")