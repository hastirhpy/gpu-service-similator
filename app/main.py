from fastapi import FastAPI

app = FastAPI(title="GPU Service Simulator")

@app.get("/")
def root():
    return {"message": "GPU Service API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}