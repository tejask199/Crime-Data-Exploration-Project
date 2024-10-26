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
    Location, COUNT(DR_NO) AS crimes
FROM
    crime_data
GROUP BY Location
ORDER BY crimes Desc
LIMIT 15"""

df = pd.read_sql(qry, connection)

pd.set_option("display.max_rows", None)

print(df)

connection.close()


plt.figure(figsize=(10, 8))

sns.lineplot(x= df["Location"], y= df["crimes"], color= "red")

plt.xlabel("Location")

plt.ylabel("Crime Rate")

plt.title("Most Crimes Occur Location")

plt.xticks(rotation= 45)

plt.savefig("question4.png")

plt.show()










