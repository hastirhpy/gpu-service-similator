from fastapi import FastAPI
from app.db.database import Base, engine

app = FastAPI(title="GPU Service Simulator")

# ساخت جدول‌ها (فعلاً خالی است ولی مهم است)
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "GPU Service API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}