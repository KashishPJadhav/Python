import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv('loan_data.csv')

label_encoders = {}
for column in ['Gender', 'Married']:  # Add all categorical columns here
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le
    
x=data.drop(columns=['Loan_Status'])
y=data['Loan_Status']

xtr,xte,ytr,yte=train_test_split(x,y,test_size=0.2,random_state=42)

knn=KNeighborsClassifier(n_neighbors=3)

knn.fit(xtr,ytr)
try:
    print("Please provide the following inputs:")
    
    # Take individual inputs
    gender = input("Gender (Male/Female): ")
    married = input("Married (Yes/No): ")
    applicant_income = int(input("ApplicantIncome (e.g., 5000): "))
    loan_amount = int(input("LoanAmount (e.g., 120): "))
    
    # Process inputs
    gender_encoded = label_encoders['Gender'].transform([gender])[0]  # Encode Gender
    married_encoded = label_encoders['Married'].transform([married])[0]  # Encode Married
    
    # Prepare the input for prediction
    user_input = [[gender_encoded, married_encoded, applicant_income, loan_amount]]
    prediction = knn.predict(user_input)
    
    print(f"\nPrediction for the entered features: {prediction[0]} (e.g., Y/N)")
except KeyError:
    print("Invalid categorical input. Please use valid categories (e.g., Male/Female, Yes/No).")
except ValueError:
    print("Invalid input. Ensure numeric fields are numbers.")