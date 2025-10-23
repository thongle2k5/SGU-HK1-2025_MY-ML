import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
df=pd.read_csv("train.csv")
has_null = df.isnull().sum().any()
has_nan  = df.isna().sum().any()
n_duplicated = df.duplicated().sum()
print(f'Tính toàn vẹn dữ liệu:')
print(f'+ Có giá trị Null: {has_null}')
if has_null:
    df['Age']=df['Age'].fillna(df['Age'].mean())
    df['Cabin']=df['Cabin'].fillna(df['Cabin'].mode()[0])  
print(f'+ Có giá trị Nan: {has_nan}')
if has_nan:
    df = df.dropna()   
print(f'+ Số dòng trùng: {n_duplicated}')
if n_duplicated>0:
    df = df.drop_duplicates()
scaler=MinMaxScaler()
df[['Age','Fare']]=scaler.fit_transform(df[['Age','Fare']])
le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])
df=pd.get_dummies(df,columns=[])
x=df[['Pclass','Sex','Age','Fare']]

y=df['Survived']
selected_features = importances[importances > 0.05].index
x_new = x[selected_features]
x_train,x_test,y_train,y_test=train_test_split(
    x_new,y,test_size=0.2,random_state=43
) # chia 80 train 20 test 
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Do chinh xac:",accuracy_score(y_test,y_pred))