from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from feature_extraction import extract_features, feature_columns

app = FastAPI()

model = joblib.load("XGB.pkl")

class URLRequest(BaseModel):
    url: str

@app.post("/phish-url-prediction")
async def predict(input_data: URLRequest):
    url = input_data.url

    features = extract_features(url)
    X = pd.DataFrame([features])[feature_columns]

    pred = model.predict(X)[0]
    label = int(pred)
    message = "Phishing URL" if label == 1 else "Legitimate URL"

    return {
        "url": url,
        "label": label,
        "prediction": message
    }
