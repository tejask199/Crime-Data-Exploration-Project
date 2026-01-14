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

qry = "select AREA_NAME as area, count(DR_NO) as total_crimes from crime_data group by area"

df = pd.read_sql(qry, connection)


pd.set_option("display.max_rows", None)

print(df)

connection.close()


plt.figure(figsize=(20,8))
plt.barh(df["area"],df["total_crimes"], color= "red")
plt.xlabel("Total Crimes")
plt.ylabel("Area")
plt.title("Geographical Hotspots for Reported Crimes")
plt.savefig("question1.png")
plt.show()

