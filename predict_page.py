import pickle
import numpy as np
import streamlit as st

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
scaler= data["scaler"]
gender_encoder = data["gender_encoder"]
married_encoder = data["married_encoder"]
departments_encoder = data["departments_encoder"]
education_encoder = data["education_encoder"]
selfEmployed_encoder = data["selfEmployed_encoder"]
term_encoder = data["term_encoder"]
property_encoder = data["property_encoder"]

def checker(applicantIncome, coapplicantIncome, loanAmount):
    return applicantIncome == '' or coapplicantIncome == '' or loanAmount == ''

def show_predict_page():
    gender = st.radio(
        "**Gender**",
        ["Male", "Female"],
        horizontal = True
    )

    married = st.radio(
        "**Married**",
        ["No", "Yes"],
        horizontal = True
    )

    dependents = st.radio(
        "**Dependents**",
        ['0', '1', '2', '3+'],
        horizontal = True
    )

    education = st.radio(
        "**Education**",
        ['Graduate', 'Not Graduate'],
        horizontal = True
    )

    self_Employed = st.radio(
        "**Self Employed**",
        ['No', 'Yes'],
        horizontal = True
    )

    applicantIncome = st.text_input('**Applicant Income**', placeholder="Please Enter")

    coapplicantIncome = st.text_input('**Co-Applicant Income**', placeholder="Please Enter (If not applicable type 0)")

    loanAmount = st.text_input('**Loan Amount**', placeholder="Please Enter")

    term = st.selectbox(
        "**Loan Amount Term**",
        (36, 60, 84, 120, 180, 240, 300, 360, 480),
        index = 0,
        placeholder="Please select loan amount term",
        help = "The following number are in months (eg. 360 is 30 years)",
    )

    area = st.radio(
        "**Property Area**",
        ['Urban', 'Rural', 'Semiurban'],
        horizontal = True
    )

    ok = st.button(":blue[Predict]")

    if ok:
        if(checker(applicantIncome, coapplicantIncome, loanAmount)):
            st.error('Please enter all the parameters!', icon="🚨")
        else:
            X = np.array([[gender, married, dependents, education, self_Employed, applicantIncome, coapplicantIncome, loanAmount, term, area]])

            X[:, 0] = gender_encoder.transform(X[:, 0])
            X[:, 1] = married_encoder.transform(X[:, 1])
            X[:, 2] = departments_encoder.transform(X[:, 2])
            X[:, 3] = education_encoder.transform(X[:, 3])
            X[:, 4] = selfEmployed_encoder.transform(X[:, 4])
            X[:, 8] = term_encoder.transform(X[:, 8])
            X[:, 9] = property_encoder.transform(X[:, 9])

            X = scaler.transform(X)

            output = model.predict(X)

            if(output[0] == 1):
                st.subheader("You have high chances of getting loan!")
            else:
                st.subheader("You have less chances of getting loan!")
            
            st.write("""### 👈 :rainbow[To know more about the dataset, go to About page]""")