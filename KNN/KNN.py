import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
from sklearn.preprocessing import StandardScaler

# Create the dataset
data = pd.DataFrame({
    'Age': [35, 22, 63, 25, 59],
    'income': [35000, 50000, 200000, 4500, 17500],
    'no. of cards': [3, 2, 1, 2, 1],
    'Loan': ['N', 'Y', 'N', 'Y', 'N']
})

# Encode the 'Loan' column (target variable)
label_encoder = LabelEncoder()
data['Loan'] = label_encoder.fit_transform(data['Loan'])  # 'Y' -> 1, 'N' -> 0

# Define features (X) and target (y)
X = data.drop(columns=['Loan'])
y = data['Loan']

# Normalize the features (optional but can improve performance for KNN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the KNeighborsClassifier model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Save the model and label encoder to pickle files
with open('knn_model.pkl', 'wb') as model_file:
    pickle.dump(knn, model_file)

with open('label_encoder.pkl', 'wb') as encoder_file:
    pickle.dump(label_encoder, encoder_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Test prediction with user input
try:
    print("Please provide the following inputs:")

    # Take individual inputs
    age = int(input("Age: "))
    income = int(input("Income: "))
    no_of_cards = int(input("Number of Credit Cards: "))

    # Prepare the input data
    user_input = [[age, income, no_of_cards]]

    # Scale the input data
    user_input_scaled = scaler.transform(user_input)

    # Make the prediction
    prediction = knn.predict(user_input_scaled)
    
    # Decode the prediction back to 'Y'/'N'
    loan_status = label_encoder.inverse_transform(prediction)

    print(f"\nPrediction for the entered features: {loan_status[0]} (e.g., Y/N)")

except ValueError:
    print("Invalid input. Ensure numeric fields are entered correctly.")
