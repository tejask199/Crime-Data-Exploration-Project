# Victim Demographics:

# Is there a significant difference in crime rates between male and female victims?

import pymysql
import mysql.connector 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
import geopandas as gpd
import warnings 
warnings.filterwarnings("ignore")

connection = pymysql.connect(host= "localhost",
                             user= "root", 
                             password= "tyjkl89",
                             database= "crimedata"
)

print(connection)


qry = """ SELECT 
    Vict_Sex, COUNT(*) AS total_crime
FROM
    crime_data
GROUP BY Vict_Sex"""

df = pd.read_sql(qry, connection)

pd.set_option("display.max_rows", None)

print(df)

connection.close()

plt.figure(figsize=(10,8))

plt.bar(df["Vict_Sex"], df["total_crime"])

plt.xlabel("Victim Genders")

plt.ylabel("Crime Rate")

plt.title("Count of Male and Female Victims")

plt.xticks(df["Vict_Sex"], ["Female", "Male", "X", "Not Defined"])

plt.savefig("question3.png")

plt.show()










