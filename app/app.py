import streamlit as st
import pandas as pd
import joblib

# Cargar modelo
model = joblib.load("models/bank_marketing_pipeline.joblib")
st.set_page_config(
    page_title="Bank Marketing Predictor",
    page_icon="🏦"
)

st.title("🏦 Predicción de Aceptación de Depósito")
st.write(
    "Ingrese la información del cliente para estimar la probabilidad "
    "de aceptar una oferta de depósito a plazo."
)

# Inputs

age = st.number_input("Edad", min_value=18, max_value=100, value=35)

job = st.selectbox(
    "Trabajo",
    [
        "admin.",
        "blue-collar",
        "entrepreneur",
        "housemaid",
        "management",
        "retired",
        "self-employed",
        "services",
        "student",
        "technician",
        "unemployed",
        "unknown"
    ]
)

marital = st.selectbox(
    "Estado civil",
    ["married", "single", "divorced"]
)

education = st.selectbox(
    "Educación",
    [
        "primary",
        "secondary",
        "tertiary",
        "unknown"
    ]
)

balance = st.number_input(
    "Balance de la cuenta",
    value=1000
)

housing = st.selectbox(
    "Crédito hipotecario",
    ["yes", "no"]
)

loan = st.selectbox(
    "Préstamo personal",
    ["yes", "no"]
)

contact = st.selectbox(
    "Tipo de contacto",
    ["cellular", "telephone", "unknown"]
)

campaign = st.number_input(
    "Número de contactos durante la campaña",
    min_value=1,
    value=1
)

previous = st.number_input(
    "Contactos previos",
    min_value=0,
    value=0
)

poutcome = st.selectbox(
    "Resultado campaña anterior",
    ["unknown", "failure", "success", "other"]
)

# Valores por defecto para variables usadas en entrenamiento
day = 15
month = "may"
default = "no"
pdays = -1

# Predicción

if st.button("Predecir"):

    input_data = pd.DataFrame({
        "age": [age],
        "job": [job],
        "marital": [marital],
        "education": [education],
        "default": [default],
        "balance": [balance],
        "housing": [housing],
        "loan": [loan],
        "contact": [contact],
        "day": [day],
        "month": [month],
        "campaign": [campaign],
        "pdays": [pdays],
        "previous": [previous],
        "poutcome": [poutcome]
    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    prob_yes = probability[list(model.classes_).index("yes")] * 100

    if prediction == "yes":
        st.success(
            f"✅ El cliente probablemente aceptará la oferta.\n\n"
            f"Probabilidad: {prob_yes:.2f}%"
        )
    else:
        st.error(
            f"❌ El cliente probablemente NO aceptará la oferta.\n\n"
            f"Probabilidad de aceptación: {prob_yes:.2f}%"
        )