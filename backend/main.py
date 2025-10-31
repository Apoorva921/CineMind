from fastapi import FastAPI
from routes.predict import router as predict_router

app = FastAPI(
    title="CineMind API",
    description="Backend for CineMind – Multimodal AI for Movie Intelligence",
    version="1.1.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to CineMind API"}

# Register routes
app.include_router(predict_router, prefix="/api")
