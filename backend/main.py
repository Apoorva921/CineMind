from fastapi import FastAPI

app = FastAPI(
    title="CineMind API",
    description="Backend for CineMind — Multimodal AI for Movie Intelligence",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to CineMind API "}

@app.post("/predict")
def predict():
    return {"result": "Coming soon... AI magic in progress!"}
