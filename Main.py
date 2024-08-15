import streamlit as st
import time
from prediction_helper import preprocess_input_data, predict_premium



# Title of the app
st.title('🏥 Insurance Premium Prediction')

# Display the heads-up as a temporary message
heads_up = st.warning(
    "**Heads up!** This app is for a project and should not be taken seriously. For real insurance-related queries or decisions, please consult a professional.")
st.markdown("[Connect with me on LinkedIn](https://www.linkedin.com/in/abhinav-sharma-work21/)")

# Keep the message visible for 5 seconds
time.sleep(5)

# Clear the heads-up message
heads_up.empty()

# Create three rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)

# Dropdowns with animations arranged in a 3x3 grid
with st.spinner('Loading options...'):
    time.sleep(1)
    with row1[0]:
        age = st.selectbox('Age', ['None'] + list(range(18, 111)))
    with row1[1]:
        genetical_risk = st.selectbox('Genetical Risk', ['None'] + list(range(1, 6)))
    with row1[2]:
        number_of_dependants = st.selectbox('Number of Dependants', ['None'] + list(range(1, 8)))

    with row2[0]:
        gender = st.selectbox('Gender', ['None', '👨 Male', '👩 Female'])
    with row2[1]:
        region = st.selectbox('Region', ['None', '🌲 Northwest', '🌴 Southeast', '🏙️ Northeast', '🏜️ Southwest'])
    with row2[2]:
        marital_status = st.selectbox('Marital Status', ['None', '💍 Married', '💔 Unmarried'])

    with row3[0]:
        bmi_category = st.selectbox('BMI Category', ['None', '✅ Normal', '⚖️ Obesity', '📈 Overweight', '📉 Underweight'])
    with row3[1]:
        smoking_status = st.selectbox('Smoking Status', ['None', '🚭 No Smoking', '🚬 Regular', '💨 Occasional'])
    with row3[2]:
        employment_status = st.selectbox('Employment Status', ['None', '👔 Salaried', '📈 Self-Employed', '💻 Freelancer'])

    with row3[0]:
        income = st.number_input('Income (in Lakhs)', min_value=0, max_value=200, step=1)
    with row3[1]:
        medical_history = st.selectbox('Medical History', [
            'None', '🩺 No Disease', '💉 Diabetes', '💊 High blood pressure', '🩸 Diabetes & High blood pressure',
            '🦠 Thyroid', '❤️ Heart disease', '🫀 High blood pressure & Heart disease',
            '🧬 Diabetes & Thyroid', '🫁 Diabetes & Heart disease'
        ])
    with row3[2]:
        insurance_plan = st.selectbox('Insurance Plan', ['None', '🥉 Bronze', '🥈 Silver', '🥇 Gold'])

# Check if all necessary fields are filled
missing_fields = []

for key, value in {
    'Age': age,
    'Genetical Risk': genetical_risk,
    'Number of Dependants': number_of_dependants,
    'Gender': gender,
    'Region': region,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Employment Status': employment_status,
    'Income': income,  # Assuming income is required and cannot be None
    'Medical History': medical_history,
    'Insurance Plan': insurance_plan
}.items():
    if value == 'None':
        missing_fields.append(key)

if missing_fields:
    st.warning(f"Please fill in all the required fields: {', '.join(missing_fields)}")

# Map the selected options to values without emojis if no fields are missing
if not missing_fields:
    input_dict = {
        'Age': age,
        'Genetical Risk': genetical_risk,
        'Number of Dependants': number_of_dependants,
        'Gender': gender.split(' ')[1],
        'Region': region.split(' ')[1],
        'Marital Status': marital_status.split(' ')[1],
        'BMI Category': bmi_category.split(' ')[1],
        'Smoking Status': smoking_status.split(' ')[1],
        'Employment Status': employment_status.split(' ')[1],
        'Income': income,  # Directly use the income value
        'Medical History': medical_history.split(' ', 1)[1],  # Only split at the first space
        'Insurance Plan': insurance_plan.split(' ')[1]
    }

    # Simulate a progress bar after selections
    st.write("Processing your selections...")
    progress_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)

    st.success("Selections processed successfully!")

    # Add a "Predict" button
    if st.button('🔮 Predict'):
        # Predict the insurance premium
        prediction = predict_premium(input_dict)

        # Provide tips based on user selections
        tips = []
        if input_dict['Smoking Status'] in ['Regular', 'Occasional']:
            tips.append('Consider quitting smoking for a healthier life!')
        if input_dict['BMI Category'] in ['Obesity', 'Overweight']:
            tips.append('Maintaining a healthy BMI can lower your premium.')
        if input_dict['Genetical Risk'] > 3:
            tips.append('Genetic risk is high! Stay proactive with regular checkups.')
        if input_dict['Income'] < 10:
            tips.append('Saving more might help in reducing the premium.')
        if input_dict['Marital Status'] == 'Unmarried':
            tips.append('Getting married? Some insurers offer discounts for married couples.')

        # Display the prediction and tips
        st.success(f'Predicted Premium is: ₹{prediction}')
        if tips:
            st.info(" ".join(tips))
