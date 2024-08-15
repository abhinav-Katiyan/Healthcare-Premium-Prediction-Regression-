<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insurance Premium Prediction ML Web App</title>
</head>
<body>

<h1>Insurance Premium Prediction ML Web App</h1>

<p>Welcome to the Insurance Premium Prediction ML Web App repository! This project demonstrates a complete end-to-end machine learning pipeline, from data preprocessing and model training to deployment. The app predicts insurance premiums based on user inputs and provides insights and tips to potentially reduce premiums.</p>

<h2>Project Highlights</h2>
<ul>
    <li><strong>Dataset:</strong> Utilizes a dataset of over 50,000 records to train the model.</li>
    <li><strong>Model Accuracy:</strong> Achieves a remarkable accuracy of 97% using XGBoost and Scikit-Learn.</li>
    <li><strong>Deployment:</strong> Deployed on Streamlit to provide a user-friendly web interface.</li>
    <li><strong>Features:</strong> Includes data cleaning, feature engineering, model training, and real-time predictions.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<p>Before running the application, ensure you have the following installed:</p>
<ul>
    <li>Python 3.7+</li>
    <li>Streamlit</li>
    <li>Joblib</li>
    <li>Pandas</li>
    <li>Scikit-learn</li>
    <li>XGBoost</li>
</ul>
<p>You can install the required packages using pip:</p>
<pre><code>pip install streamlit joblib pandas scikit-learn xgboost</code></pre>

<h3>Project Structure</h3>
<ul>
    <li><strong>app.py:</strong> Main Streamlit application script.</li>
    <li><strong>prediction_helper.py:</strong> Contains helper functions for preprocessing data and making predictions.</li>
    <li><strong>Artifacts/:</strong> Directory containing pre-trained models and scalers.</li>
</ul>

<h3>How to Run</h3>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/your-username/insurance-premium-prediction.git
cd insurance-premium-prediction</code></pre>
    </li>
    <li><strong>Run the Streamlit App:</strong>
        <pre><code>streamlit run app.py</code></pre>
        <p>This will start the Streamlit server and open the application in your default web browser.</p>
    </li>
</ol>

<h2>Code Explanation</h2>

<h3>app.py</h3>
<ul>
    <li><strong>Title and Intro:</strong> Sets up the Streamlit app with a title and an introductory message.</li>
    <li><strong>Input Fields:</strong> Creates a grid layout with dropdowns and number inputs for various user inputs (e.g., Age, Gender, BMI Category).</li>
    <li><strong>Validation:</strong> Checks if all required fields are filled and displays a warning if not.</li>
    <li><strong>Processing and Prediction:</strong> Processes user inputs, simulates a progress bar, and makes predictions using the <code>predict_premium</code> function from <code>prediction_helper.py</code>.</li>
    <li><strong>Tips:</strong> Provides personalized tips based on user inputs.</li>
</ul>

<h3>prediction_helper.py</h3>
<ul>
    <li><strong>calculate_normalized_risk(medical_history):</strong> Calculates a normalized risk score based on the user's medical history.</li>
    <li><strong>preprocess_input_data(input_dict):</strong> Converts user inputs into a format suitable for the model, including encoding categorical variables and scaling numerical features.</li>
    <li><strong>handle_scaling(age, df):</strong> Applies different scalers based on the user's age.</li>
    <li><strong>predict_premium(input_dict):</strong> Uses pre-trained models (<code>model_young</code> and <code>model_rest</code>) to predict the insurance premium based on the preprocessed data.</li>
</ul>

<h3>Models and Scalability</h3>
<ul>
    <li><strong>Models:</strong> Trained models (<code>model_young</code> and <code>model_rest</code>) are loaded from the <code>Artifacts/</code> directory. These models handle different age groups for better prediction accuracy.</li>
    <li><strong>Scaling:</strong> The app uses different scalers for different age groups to normalize features effectively.</li>
</ul>

<h2>Additional Information</h2>
<ul>
    <li><strong>LinkedIn Profile:</strong> <a href="https://www.linkedin.com/in/abhinav-sharma-work21/" target="_blank">Connect with me on LinkedIn</a></li>
    <li><strong>App Link:</strong> <a href="https://insurewise-by-abhinav-katiyan.streamlit.app/" target="_blank">Insurance Premium Prediction App</a></li>
</ul>

<h2>Contribution</h2>
<p>Feel free to contribute to this project by submitting issues, feature requests, or pull requests.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
