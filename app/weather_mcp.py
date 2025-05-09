from fastapi import FastAPI, Query
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Weather MCP Server")

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.get("/weather")
def get_weather(city: str = Query(...), units: str = "metric"):
    if not OPENWEATHER_API_KEY:
        return {"error": "API key not configured"}
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "City not found or API failed"}
    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"]
    }