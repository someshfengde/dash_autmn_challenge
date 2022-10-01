import numpy as np
import pandas as pd

data = pd.read_csv("./data/liquor_iowa_2021.csv")
data["county"] = data["county"].str.title()
data["store_location"] = data.groupby("store_name")["store_location"].transform(
    lambda g: g.ffill().bfill()
)
data["day"] = data["date"].apply(lambda x: pd.to_datetime(x).day_name())
data["week"] = data["date"].apply(lambda x: pd.to_datetime(x).week)
data["lon"] = data["store_location"].str.split(" ").str[1]
data["lon"] = data["lon"].str.split("(").str[1]
data["lon"].fillna(0, inplace=True)
data["lat"] = data["store_location"].str.split(" ").str[2]
data["lat"] = data["lat"].str.split(")").str[0]
data["lat"].fillna(0, inplace=True)
data["lat"] = data["lat"].astype(float)
data["lon"] = data["lon"].astype(float)
df2 = pd.read_csv("./data/uscities.csv")
