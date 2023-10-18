import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


session_state = st.session_state

if 'logged_in' not in session_state:
    session_state.logged_in = False

st.title("Maternal Health Risk Prediction")

if not session_state.logged_in: 
    st.header("Kindly Login to Continue")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "Ifeoma" and password == "12345":
            session_state.logged_in = True
            st.success("Login Successfully")
        else:
            st.error("Invalid Username or Password")

else:
    st.header("Welcome")
    model = pickle.load(open('model.pkl', 'rb'))

    age = st.text_input("Age", 0)
    systolic_bp = st.text_input("Systolic Blood Pressure")
    diastolic_bp = st.text_input ("Diastolic Blood Pressure")
    bs = st.text_input("Blood Sugar") #bs is the same as blood sugar
    body_temp = st.text_input("Body Temperature")
    heart_rate = st.text_input("Heart Rate")

    button1, button2 = st.columns(2)

    with button1:
        if st.button('Predict'):
            input_details = pd.DataFrame([[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]],
                                        columns=["Age","SystolicBP","DiastolicBP","BS","BodyTemp","HeartRate"])
            
            prediction = model.predict(input_details)
            def map_risk(predict):
                if prediction == 0:
                    return "Low Risk"
                elif prediction == 1:
                    return "Mid Risk"
                else:
                    return "High Risk"
            
            prediction = map_risk(predict=prediction)
            st.write(f"Your Health Risk Level is: {prediction}")

    with button2:
        if st.button("Show Decision Tree"):
            fig, ax = plt.subplots(figsize=(30, 20))
            plot_tree(model, feature_names=["Age","SystolicBP","DiastolicBP","BS","BodyTemp","HeartRate"], class_names=['high risk','mid risk', 'low risk'], filled=True, ax=ax)
            st.pyplot(fig)