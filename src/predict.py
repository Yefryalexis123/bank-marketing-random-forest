import joblib

model = joblib.load("models/bank_marketing_pipeline.joblib")

def predict(data):
    prediction = model.predict(data)
    probability = model.predict_proba(data)

    return prediction, probability