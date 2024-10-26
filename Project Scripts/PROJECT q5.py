import pymysql
import mysql.connector 
import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
import warnings 
warnings.filterwarnings("ignore")

connection = pymysql.connect(host= "localhost",
                             user= "root", 
                             password= "tyjkl89",
                             database= "crimedata"
)

print(connection)

qry = "select crm_cd, DR_No from crime_data"

df = pd.read_sql(qry, connection)

pd.set_option("display.max_rows", None)

print(df)

# plt.figure(figsize=(15, 10))

plt.figure(figsize=(10, 6))

sns.countplot(data=df, x="crm_cd", order=df["crm_cd"].value_counts().index[:499], palette="viridis", saturation=1)

plt.xlabel("Crime Code")

plt.ylabel("Number of Crimes")

plt.title("Distribution of Reported Crimes by Crime Code")

plt.xticks(rotation=45)  

plt.tight_layout()

plt.savefig("question5.png")

plt.show()














