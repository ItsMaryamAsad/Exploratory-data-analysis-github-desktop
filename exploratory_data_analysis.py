# -*- coding: utf-8 -*-
"""Exploratory_Data_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eKFdGGX03-yAkEcNz5YUZAr7ok1AOsvN
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('train.csv')
# print(df.head())
df['Age'].describe()
df['Age'].plot(kind='hist',bins=20)



df['Age'].plot(kind='kde')

df['Age'].skew()

df['Age'].plot(kind='box')

df['Age'].isnull().sum()/len(df['Age'])

# conclusion:
# age is almost normally distributed(0.3)
# 20% of the values are missing
# there are some outliers

df['Fare'].describe()

df['Fare'].plot(kind='kde')

df['Fare'].skew()

df['Fare'].plot(kind='box')

df[df['Fare']>250]

df['Fare'].isnull().sum()

# conclusion:
# the data is highly positively skewed
# fare column contains group fare not individual fare which might an issue
# we need to create a new column named group fare

df['Survived'].value_counts()

df['Survived'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['Survived'].isnull().sum()

df['Pclass'].value_counts()

df['Pclass'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['Sex'].value_counts()

df['Sex'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['Sex'].isnull().sum()

df['SibSp'].value_counts()

df['SibSp'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['SibSp'].isnull().sum()

df['Parch'].value_counts()

df['Parch'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['Parch'].isnull().sum()

df['Embarked'].value_counts()

df['Embarked'].value_counts().plot(kind='pie',autopct='%0.1f%%')

df['Embarked'].isnull().sum()

# bi-variate Analysis
pd.crosstab(df['Survived'],df['Pclass'],normalize='columns')

# Numerical-Numerical
# categorial-numerical
# categorical-categorical

sns.heatmap(pd.crosstab(df['Survived'],df['Pclass'],normalize='columns'))

pd.crosstab(df['Survived'],df['Sex'],normalize='columns')

pd.crosstab(df['Survived'],df['Embarked'],normalize='columns')

pd.crosstab(df['Sex'],df['Embarked'],normalize='columns')

pd.crosstab(df['Pclass'],df['Embarked'],normalize='columns')

df[df['Survived']==1]['Age'].plot(kind='kde',label='Survived')
df[df['Survived']==0]['Age'].plot(kind='kde',label='Survived')
plt.legend()
plt.show()

df[df['SibSp']==8]

df[df['Ticket']=='CA. 2343']

df[df['Name'].str.contains('Sage')]

#the rest of the family members maybe in test.csv as it is showing only 7 out of 11

df1=pd.read_csv('test.csv')
df=pd.concat([df,df1])

df[df['Ticket']=='CA 2144']

df['individ_fare']=df['Fare']/(df['SibSp']+df['Parch']+1)

df['individ_fare']

df['individ_fare'].plot(kind='box')

df['individ_fare'].describe()

df['family_size']=df['SibSp']+df['Parch']+1
df['family_size']

def family_typ(num):
  if num==1:
    return 'alone'
  if num>1 and num<5:
    return 'small'
  else:
    return 'large'

df['Family_type']=df['family_size'].apply(family_typ)

pd.crosstab(df['Survived'],df['Family_type'],normalize='columns')

df['surname']=df['Name'].str.split(',').str.get(0)

df['surname']

df['title'] = df['Name'].str.split(',').str.get(1).str.strip().str.split(' ').str.get(0)

df['title'].value_counts()

temp_df = df[df['title'].isin(['Mr.','Miss.','Mrs.','Master.','ootherr'])]

pd.crosstab(temp_df['Survived'],temp_df['title'],normalize='columns')*100

df['title'] = df['title'].str.replace('Rev.','other')
df['title'] = df['title'].str.replace('Dr.','other')
df['title'] = df['title'].str.replace('Col.','other')
df['title'] = df['title'].str.replace('Major.','other')
df['title'] = df['title'].str.replace('Capt.','other')
df['title'] = df['title'].str.replace('the','other')
df['title'] = df['title'].str.replace('Jonkheer.','other')
# ,'Dr.','Col.','Major.','Don.','Capt.','the','Jonkheer.']

df['Cabin'].isnull().sum()/len(df['Cabin'])

df['Cabin'].fillna('M',inplace=True)
df['Cabin'].value_counts()

df['deck'] = df['Cabin'].str[0]
df['deck'].value_counts()

pd.crosstab(df['deck'],df['Pclass'])

pd.crosstab(df['deck'],df['Survived'],normalize='index').plot(kind='bar',stacked=True)

sns.heatmap(df.corr())

sns.pairplot(df1)

df.head()