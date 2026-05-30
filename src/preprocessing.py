import pandas as pd

def create_input_dataframe(
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
):

    return pd.DataFrame({
        "age": [age],
        "job": [job],
        "marital": [marital],
        "education": [education],
        "default": ["no"],
        "balance": [balance],
        "housing": [housing],
        "loan": [loan],
        "contact": [contact],
        "day": [15],
        "month": ["may"],
        "campaign": [campaign],
        "pdays": [-1],
        "previous": [previous],
        "poutcome": [poutcome]
    })