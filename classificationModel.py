import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model


dataset = pd.read_csv('LoanDataset.csv')

dataset = dataset.drop(['Loan_ID'], axis=1)

dataset = dataset.drop(['Credit_History'], axis=1)

dataset = dataset.dropna()

gender_encoder = LabelEncoder() 
dataset['Gender'] = gender_encoder.fit_transform(dataset['Gender'])

married_encoder = LabelEncoder() 
dataset['Married'] = married_encoder.fit_transform(dataset['Married'])

departments_encoder = LabelEncoder() 
dataset['Dependents'] = departments_encoder.fit_transform(dataset['Dependents'])

education_encoder = LabelEncoder() 
dataset['Education'] = education_encoder.fit_transform(dataset['Education'])

selfEmployed_encoder = LabelEncoder() 
dataset['Self_Employed'] = selfEmployed_encoder.fit_transform(dataset['Self_Employed'])

term_encoder = LabelEncoder() 
dataset['Loan_Amount_Term'] = term_encoder.fit_transform(dataset['Loan_Amount_Term'])

property_encoder = LabelEncoder() 
dataset['Property_Area'] = property_encoder.fit_transform(dataset['Property_Area'])

status_encoder = LabelEncoder() 
dataset['Loan_Status'] = status_encoder.fit_transform(dataset['Loan_Status'])

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

scaler = StandardScaler()
X = scaler.fit_transform(X)


model = linear_model.LogisticRegression()
model.fit(X, y)

data = {
   "model" : model,
   "scaler": scaler,
   "gender_encoder": gender_encoder,
   "married_encoder": married_encoder,
   "departments_encoder": departments_encoder,
   "education_encoder": education_encoder,
   "selfEmployed_encoder": selfEmployed_encoder,
   "term_encoder": term_encoder,
   "property_encoder": property_encoder
   }

with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)