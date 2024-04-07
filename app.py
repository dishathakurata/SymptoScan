import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title = "SymptoScan",
                   layout = "wide",
                   page_icon = "🧑‍⚕️🔍")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('./saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('./saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('./saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon = 'hospital-fill',
                           icons = ['activity', 'heart', 'person'],
                           default_index = 0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction')

    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder = 'Enter number of pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level', placeholder = 'Enter glucose level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value', placeholder = 'Enter blood pressure value < 100')

    with col4:
        SkinThickness = st.text_input('Skin Thickness value', placeholder = 'Enter skin thickness value < 50')

    with col1:
        Insulin = st.text_input('Insulin Level', placeholder = 'Enter insulin level')

    with col2:
        BMI = st.text_input('BMI value', placeholder = 'Enter BMI value')

    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', placeholder = 'Enter DPF value')

    with col4:
        Age = st.text_input('Age of the Person', placeholder = 'Enter patient age')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is NOT Diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', placeholder = 'Enter patient age')

    with col2:
        sex = st.text_input('Sex', placeholder = 'Enter M for Male or F for Female')

    with col3:
        cp = st.text_input('Chest Pain types', placeholder = 'Enter chest pain intensity (0 to 3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', placeholder = 'Enter resting blood pressure (< 200)')

    with col2:
        chol = st.text_input('Serum Cholestoral', placeholder = 'Enter serum cholestrol in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar', placeholder = 'Enter fasting blood sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', placeholder = 'Enter resting electrocardiographic result (0 or 1)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', placeholder = 'Enter maximum heart rate')

    with col3:
        exang = st.text_input('Exercise Induced Angina', placeholder = 'Enter exercise induced angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', placeholder = 'Enter depression induces by execise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', placeholder = 'Enter slope of peak exercise')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', placeholder = 'Enter major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal', placeholder = '0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does NOT have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo', placeholder = 'Enter MDVP:Fo in Hz')

    with col2:
        fhi = st.text_input('MDVP:Fhi', placeholder = 'Enter MDVP:Fhi in Hz')

    with col3:
        flo = st.text_input('MDVP:Flo', placeholder = 'Enter MDVP:Flo in Hz')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter', placeholder = 'Enter MDVP:Jitter in percentage')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter', placeholder = 'Enter MDVP:Jitter in Abs')

    with col1:
        RAP = st.text_input('MDVP:RAP', placeholder = 'Enter MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ', placeholder = 'Enter MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP', placeholder = 'Enter Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', placeholder = 'Enter MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer', placeholder = 'Enter MDVP:Shimmer in decibel')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', placeholder = 'Enter Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', placeholder = 'Enter Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ', placeholder = 'Enter MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA', placeholder = 'Enter Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR', placeholder = 'Enter NHR')

    with col1:
        HNR = st.text_input('HNR', placeholder = 'Enter HNR')

    with col2:
        RPDE = st.text_input('RPDE', placeholder = 'Enter RPDE')

    with col3:
        DFA = st.text_input('DFA', placeholder = 'Enter DFA')

    with col4:
        spread1 = st.text_input('spread1', placeholder = 'Enter spread1')

    with col5:
        spread2 = st.text_input('spread2', placeholder = 'Enter spread2')

    with col1:
        D2 = st.text_input('D2', placeholder = 'Enter D2')

    with col2:
        PPE = st.text_input('PPE', placeholder = 'Enter PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)