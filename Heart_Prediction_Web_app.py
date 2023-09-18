import numpy as np
import pickle
import streamlit as st

#loading the saved model 
loaded_model = pickle.load(open('Heart_Disease_Prediction_Model/trained_model.sav','rb'))

def Heart_prediction(input_data):
    array = np.asarray(input_data)
    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==0):
      return 'The person does not have a heart disease'
    else:
      return 'The person has heart disease'
    
def main():
    
    html_temp = '''
    <div style="background-color: green; padding: 10px;">
        <h2 style="color: white; text-align: center;">
            <strong>Heart Disease Prediction Web App</strong>
        </h2>
      </div>
    '''

    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('''      
                        *       Your Heart, Our Priority!   ''')
    
    # Getting the input data from the user
    age = st.text_input('Enter your age ')
    sex = st.selectbox('Select your sex', ['Male', 'Female'])
    chest_pain_type = st.selectbox('Select your chest_pain_type', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptotic'])
    resting_blood_pressure = st.text_input('Enter your resting_blood_pressure')
    cholesterol = st.text_input('Enter your cholesterol')
    fasting_blood_sugar = st.selectbox('Select your fasting_blood_sugar', ['> 120mg/dl', '<= 120mg/dl'])
    rest_ecg = st.selectbox('Select your rest_ecg', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
    max_heart_rate_achieved = st.text_input('Enter your max_heart_rate_achieved')
    exercise_induced_angina = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    st_depression = st.text_input('Enter the st_depression value which is an integer or float.')
    st_slope = st.selectbox('Select your st_slope', ['Upsloping', 'Flat', 'Downsloping'])
    num_major_vessels = st.selectbox('Number of major vessels (0–3) colored by fluoroscopy', [0, 1, 2, 3])
    thalassemia = st.selectbox('Select your thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    diagnosis = ''

    if st.button('Heart Test Result'):
        # Convert input values to appropriate data types
        age = float(age)
        sex = 1 if sex == 'Male' else 0
        chest_pain_type = ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptotic'].index(chest_pain_type)  # Convert to index
        resting_blood_pressure = float(resting_blood_pressure)
        cholesterol = float(cholesterol)
        fasting_blood_sugar = 1 if fasting_blood_sugar == '> 120mg/dl' else 0
        rest_ecg = ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'].index(rest_ecg)
        max_heart_rate_achieved = float(max_heart_rate_achieved)
        exercise_induced_angina = 1 if exercise_induced_angina == 'Yes' else 0
        st_depression = float(st_depression)
        st_slope = ['Upsloping', 'Flat', 'Downsloping'].index(st_slope)
        num_major_vessels = int(num_major_vessels)
        thalassemia = ['Normal', 'Fixed Defect', 'Reversible Defect'].index(thalassemia)

        diagnosis = Heart_prediction([age, sex, chest_pain_type, resting_blood_pressure, cholesterol, fasting_blood_sugar, rest_ecg, max_heart_rate_achieved, exercise_induced_angina, st_depression, st_slope, num_major_vessels, thalassemia])

    st.success(diagnosis)
    if st.button('About'):
       st.text('Lets Learn')
       st.text('Heart disease is a pervasive and life-threatening health condition that affects \nmillions of people worldwide. To address this pressing public health concern, we\nhave developed an advanced Heart Disease Prediction Model, leveraging the power \nof artificial intelligence and machine learning. Our model is designed to assist \nhealthcare professionals, researchers, and individuals in making informed decisions\nabout heart disease risk assessment and prevention.')

    if st.button('Founder'):
       st.text('Sayeum Mahajan')

if __name__== '__main__':
   main()
  


