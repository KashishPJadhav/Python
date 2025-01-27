from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load and preprocess the data
try:
    data = pd.read_csv('Loan_Data.csv')
    data = data.drop(columns=['Loan_ID'])
    data.fillna({
        'Gender': 'Unknown', 'Married': 'Unknown', 'Education': 'Unknown',
        'Self_Employed': 'Unknown', 'Property_Area': 'Unknown',
        'Dependents': 0, 'LoanAmount': 0, 'Credit_History': 0
    }, inplace=True)

    # Encode categorical columns
    label_encoders = {}
    categorical_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    for column in categorical_columns:
        data[column] = data[column].astype(str)
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

    # Convert Loan_Status to binary
    data=data.drop(columns=['Loan_Amount_Term'])
    data['Loan_Status'] = data['Loan_Status'].map({'Y': 1, 'N': 0})
    x = data.drop(columns=['Loan_Status'])
    y = data['Loan_Status']

    # Train the KNN model
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(x, y)
except Exception as e:
    print(f"Error during initialization: {e}")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Collect data from form
            gender = request.form["gender"]
            married = request.form["married"]
            dependents = int(request.form["dependents"])
            education = request.form["education"]
            self_employed = request.form["self_employed"]
            applicant_income = int(request.form["applicant_income"])
            loan_amount = int(request.form["loan_amount"])
            credit_history = int(request.form["credit_history"])
            property_area = request.form["property_area"]

            # Encode inputs
            gender_encoded = label_encoders["Gender"].transform([gender])[0]
            married_encoded = label_encoders["Married"].transform([married])[0]
            education_encoded = label_encoders["Education"].transform([education])[0]
            self_employed_encoded = label_encoders["Self_Employed"].transform([self_employed])[0]
            property_area_encoded = label_encoders["Property_Area"].transform([property_area])[0]
            coapplicant_income = int(request.form["coapplicant_income"])

            user_input = [[gender_encoded, married_encoded, dependents, education_encoded,
               self_employed_encoded, applicant_income, coapplicant_income,
               loan_amount, credit_history, property_area_encoded]]


            # Predict using KNN
            prediction = knn.predict(user_input)

            # Return result
            result = "Approved" if prediction[0] == 1 else "Not Approved"
            return render_template("index.html", result=result)
        except Exception as e:
            return render_template("index.html", result=f"Error: {e}")

    return render_template("index.html", result=None)


if __name__ == '__main__':
    app.run(debug=True)
