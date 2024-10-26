import pymysql
import mysql.connector 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import warnings 
warnings.filterwarnings("ignore")


connection = pymysql.connect(host= "localhost",
                             user= "root", 
                             password= "tyjkl89",
                             database= "crimedata"
)

print(connection)

qry1 = "select * from crime_data"
qry2 = "select count(*) from crime_data"
qry3 = "select distinct(crm_cd) from crime_data"

df1 = pd.read_sql(qry1, connection)
df2 = pd.read_sql(qry2, connection)
df3 = pd.read_sql(qry3, connection)




pd.set_option("display.max_rows", None)

print(df1)
print(df2)
print(df3)




