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


qry = """select 
case 
when Vict_Age between 0 and 10 then "0-10"
when Vict_Age between 11 and 20 then "11-20"
when Vict_Age between 21 and 30 then "21-30"
when Vict_Age between 31 and 40 then "31-40"
when Vict_Age between 41 and 50 then "41-50" 
else "Above 50" 
end as "age_dist", count(*) as reported_crime
from crime_data 
group by age_dist"""

df = pd.read_sql(qry, connection)

pd.set_option("display.max_rows", None)

print(df)

connection.close()

plt.figure(dpi= 150)

df['percentage'] = (df['reported_crime'] / df['reported_crime'].sum()) * 100

plt.pie(df["percentage"], labels= df["age_dist"],autopct='%1.1f%%', shadow= True)

plt.title("Distribution of Victim Ages in Reported Crimes")

plt.savefig("question2.png")

plt.show()
