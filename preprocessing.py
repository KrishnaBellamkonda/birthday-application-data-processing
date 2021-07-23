# Imports 
import os 
import json 
import pandas as pd
import numpy as np

# Entire DF Source
source =  "./dataset/birthday_data.csv"

# Remember list 
remember_list_source = "./dataset/remember_data.csv"

# Read the file 
df = pd.read_csv(source)

#df.info()

# Birthday still not entered 
birthday_not_entered = df["Birthday"].isna()
df.loc[birthday_not_entered, "Birthday"] = ""

# Date parsing function 
def date_parse(date):
    if (date != ""):
        return date.replace("-", "/")
    else:
        return ""

# Converting the dates into a regularized format 
df["Birthday"] = df["Birthday"].apply(date_parse)

# df 
#df.head()

## Converting the dataframe into JSON

# Create a folder for JSON data
folder_name = "json_data"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    print("Exists")
else:
    os.mkdir(folder_path)

# Convert the dataframe to a dict 
name_column = df["Name"].values
birthday_column = df["Birthday"].values
name_birthday_dict = { name:day for (name, day) in zip(name_column, birthday_column) }

# JSON source 
df_json_source = os.path.join(folder_path, "birthday_data.json")
with open(df_json_source, "w") as fp:
    json.dump(name_birthday_dict, fp)

### Quiz list :)

# List 
remember_list = pd.read_csv(remember_list_source)
names = remember_list["Name"].values

# Set Index df 
df = df.set_index("Name")

# Get the Quiz list 
df_remember_list = df.loc[names, ["Birthday"]]

# Converting to a JSON 
remember_list_dict = { name: day for name, day in zip(df_remember_list.index, df_remember_list["Birthday"]) }
remember_list_dict

# Save as JSON
remember_list_path = os.path.join(folder_path, "remember_data.json")
with open(remember_list_path, "w") as fp:
    json.dump(remember_list_dict, fp)