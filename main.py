from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Python REST API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}