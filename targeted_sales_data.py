from pathlib import Path  
import pandas as pd  

# Only do this method if all csvs in data are wanted
data_folder = Path("data")
files = list(data_folder.glob("*.csv"))


# Empty list that will hold all of our new data
df_list = []


for file in files:
    df = pd.read_csv(file)
    df = df[df["product"] == "pink morsel"] 
    df["price"] = (
        df["price"]
        .replace(r"[\$,]", "", regex=True)
        .astype(float)
    ) 
    df["sales"] = df["quantity"] * df["price"]  
    df = df[["sales", "date", "region"]]  
    df_list.append(df)  


final_df = pd.concat(df_list, ignore_index=True) 
final_df.to_csv("final_data.csv", index=False) 

