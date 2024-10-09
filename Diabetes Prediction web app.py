import numpy as np
import altair as alt
import pickle
import streamlit as st
import pickle


# loading the saved model
loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):

    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    loaded_model = pickle.load(open('diabetes_model.sav', 'rb'))

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
    


def main():
   

    # giving a title
    st.title('Diabetes Prediction Web app')


    # getting the input data from the user
    

    Pregnancies = st.number_input('Number Of Pregnancies')
    Glucose = st.number_input('Glucose Level')
    BloodPressure = st.number_input('Blood Pressure Value')
    SkinThickness = st.number_input('Skin Thickness Value')
    Insulin = st.number_input('Insulin Level')
    BMI = st.number_input('BMI Value')
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value ')
    Age = st.number_input('Age Of the Person')


    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction ,Age])


    st.success(diagnosis)





if __name__ == '__main__':
    main()








