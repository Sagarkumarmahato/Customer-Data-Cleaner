# -*- coding: utf-8 -*-
"""HCL_Guvi_Project1.ipynb
Original file is located at
    https://colab.research.google.com/drive/1Pd8wYujJuor8twFqmihTTBehyxoGbMku
"""

# Commented out IPython magic to ensure Python compatibility.
# Import libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

#import dataset
df = pd.read_csv('/content/drive/MyDrive/Customer sale Data.csv', encoding='latin1')
df.shape

df.head(10)

#data Cleaning information
df.info()

#drop unrelated/blank columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)

df.info()

pd.isnull(df)

# check for null values
pd.isnull(df).sum()

#drop the null values
df.dropna(inplace=True)

pd.isnull(df).sum() #checking after removing the null value

#change the data type
df['Amount']=df['Amount'].astype('int')

df['Amount'].dtypes

df.info()

df.columns

#method returns description for the dataFrame(i.e .count , mean,std ,etc)
df.describe()

# use describe() for specific columns
df[['Age','Orders','Amount']].describe()

df.duplicated()

df.to_csv('/content/drive/MyDrive/Customer_sale_clean Data.csv',index=False)
