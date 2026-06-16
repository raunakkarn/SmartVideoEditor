
from fastapi import FastAPI, UploadFile, File
app = FastAPI()

@app.get("/health")
def health():
    return {"status":"ok"}
