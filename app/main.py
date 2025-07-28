from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI(title="Task Management API", version="1.0.0")

# Include the authentication routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Management API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
