Insurance Premium Prediction ML Web App
Overview
Welcome to the Insurance Premium Prediction ML Web App repository! This project demonstrates a complete end-to-end machine learning pipeline, from data preprocessing and model training to deployment. The app predicts insurance premiums based on user inputs and provides insights and tips to potentially reduce premiums.

Project Highlights
Dataset: Utilizes a dataset of over 50,000 records to train the model.
Model Accuracy: Achieves a remarkable accuracy of 97% using XGBoost and Scikit-Learn.
Deployment: Deployed on Streamlit to provide a user-friendly web interface.
Features: Includes data cleaning, feature engineering, model training, and real-time predictions.
Getting Started
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.7+
Streamlit
Joblib
Pandas
Scikit-learn
XGBoost
You can install the required packages using pip:

bash
Copy code
pip install streamlit joblib pandas scikit-learn xgboost
Project Structure
app.py: Main Streamlit application script.
prediction_helper.py: Contains helper functions for preprocessing data and making predictions.
Artifacts/: Directory containing pre-trained models and scalers.
How to Run
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/insurance-premium-prediction.git
cd insurance-premium-prediction
Run the Streamlit App:

bash
Copy code
streamlit run app.py
This will start the Streamlit server and open the application in your default web browser.

Code Explanation
app.py
Title and Intro: Sets up the Streamlit app with a title and an introductory message.
Input Fields: Creates a grid layout with dropdowns and number inputs for various user inputs (e.g., Age, Gender, BMI Category).
Validation: Checks if all required fields are filled and displays a warning if not.
Processing and Prediction: Processes user inputs, simulates a progress bar, and makes predictions using the predict_premium function from prediction_helper.py.
Tips: Provides personalized tips based on user inputs.
prediction_helper.py
calculate_normalized_risk(medical_history): Calculates a normalized risk score based on the user's medical history.
preprocess_input_data(input_dict): Converts user inputs into a format suitable for the model, including encoding categorical variables and scaling numerical features.
handle_scaling(age, df): Applies different scalers based on the user's age.
predict_premium(input_dict): Uses pre-trained models (model_young and model_rest) to predict the insurance premium based on the preprocessed data.
Models and Scalability
Models: Trained models (model_young and model_rest) are loaded from the Artifacts/ directory. These models handle different age groups for better prediction accuracy.
Scaling: The app uses different scalers for different age groups to normalize features effectively.
Additional Information
LinkedIn Profile: Connect with me on LinkedIn
App Link: Insurance Premium Prediction App
Contribution
Feel free to contribute to this project by submitting issues, feature requests, or pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.
