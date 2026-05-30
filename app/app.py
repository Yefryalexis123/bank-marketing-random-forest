import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st

from src.preprocessing import create_input_dataframe
from src.predict import predict

st.set_page_config(
    page_title="Bank Marketing Predictor",
    page_icon="🏦"
)

st.title("🏦 Predicción de Aceptación de Depósito")

st.write(
    "Ingrese los datos del cliente para estimar la probabilidad de aceptar una oferta de depósito."
)

age = st.number_input(
    "Edad",
    min_value=18,
    max_value=100,
    value=35
)

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
    [
        "married",
        "single",
        "divorced"
    ]
)

education = st.selectbox(
    "Nivel educativo",
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
    "¿Tiene crédito hipotecario?",
    ["yes", "no"]
)

loan = st.selectbox(
    "¿Tiene préstamo personal?",
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
    "Número de contactos previos",
    min_value=0,
    value=0
)

poutcome = st.selectbox(
    "Resultado de campaña anterior",
    ["unknown", "failure", "success", "other"]
)

if st.button("Predecir"):

    input_data = create_input_dataframe(
        age,
        job,
        marital,
        education,
        balance,
        housing,
        loan,
        contact,
        campaign,
        previous,
        poutcome
    )

    prediction, probability = predict(input_data)

    prediction = prediction[0]

    prob_yes = probability[0][1] * 100

    if prediction == "yes":

        st.success(
            f"✅ El cliente probablemente aceptará la oferta.\n\n"
            f"Probabilidad estimada: {prob_yes:.2f}%"
        )

    else:

        st.error(
            f"❌ El cliente probablemente NO aceptará la oferta.\n\n"
            f"Probabilidad estimada de aceptación: {prob_yes:.2f}%"
        )