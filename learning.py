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
#doc file train (.csv)
df=pd.read_csv("train.csv")
#lam day cac gia tri trong 
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Cabin']=df['Cabin'].fillna(df['Cabin'].mode()[0])
#chuan hoa du lieu so
scaler=MinMaxScaler()
df[['Age','Fare']]=scaler.fit_transform(df[['Age','Fare']])
#encode du lieu dang chu (vi du sex(male,female)=>(0,1))
le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])
#tao cac cot Embarked
df=pd.get_dummies(df,columns=[])
#chia du lieu train test
x=df[['Pclass','Sex','Age','Fare']]
y=df['Survived']
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.2,random_state=43
) # chia 80 train 20 test 
model=LogisticRegression()
model.fit(x_train,y_train)
#du doan va danh gia
y_pred=model.predict(x_test)
print("Do chinh xac:",accuracy_score(y_test,y_pred))
models = [
    ("Logistic Regression", LogisticRegression()),
    ("KNN", KNeighborsClassifier()),
    ("Decision Tree", DecisionTreeClassifier()),
    ("Random Forest", RandomForestClassifier()),
    ("SVM", SVC()),
    ("Naive Bayes", GaussianNB())
]

for name, model in models:
    scores = cross_val_score(model, x, y, cv=5)  # 5-fold cross validation
    print(name, "-> Accuracy trung bình:", scores.mean())
