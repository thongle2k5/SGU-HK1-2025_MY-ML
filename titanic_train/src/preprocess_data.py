import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
def load_and_preprocess_data(train_path="../data/processed/train_processed.csv"):
    train=pd.read_csv(train_path)
    features=['Pclass','Sex','Age','Fare','Embarked','FamilySize']
    X=train[features]
    y=train['Survived']
    X_train,X_val,y_train,y_val=train_test_split(X,y,test_size=0.2,random_state=42)
    return X_train,X_val,y_train,y_val
