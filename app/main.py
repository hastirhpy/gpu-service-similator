from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, Base, engine
from app.models import user, job
from app.schemas import user as user_schema, job as job_schema

app = FastAPI(title="GPU Service Simulator")

Base.metadata.create_all(bind=engine)

# Dependency برای گرفتن session دیتابیس
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route ایجاد Job
@app.post("/jobs/", response_model=job_schema.JobRead)
def create_job(job_in: job_schema.JobCreate, db: Session = Depends(get_db)):
    db_job = job.Job(name=job_in.name, owner_id=job_in.owner_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job