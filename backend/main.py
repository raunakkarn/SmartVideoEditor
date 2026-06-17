from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import subprocess
import uuid
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/trim")
async def trim_video(
    file: UploadFile = File(...),
    start: int = Form(...),
    duration: int = Form(...)
):
    input_path = os.path.join(
        UPLOAD_DIR,
        f"{uuid.uuid4()}_{file.filename}"
    )

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = os.path.join(
        OUTPUT_DIR,
        f"trimmed_{file.filename}"
    )

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-ss",
        str(start),
        "-t",
        str(duration),
        output_path
    ])

    return FileResponse(output_path)

@app.post("/convert")
async def convert_video(
    file: UploadFile = File(...),
    fmt: str = Form(...)
):
    input_path = os.path.join(
        UPLOAD_DIR,
        f"{uuid.uuid4()}_{file.filename}"
    )

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = os.path.join(
        OUTPUT_DIR,
        f"converted.{fmt}"
    )

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        output_path
    ])

    return FileResponse(output_path)

@app.post("/extract-audio")
async def extract_audio(
    file: UploadFile = File(...)
):
    input_path = os.path.join(
        UPLOAD_DIR,
        f"{uuid.uuid4()}_{file.filename}"
    )

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = os.path.join(
        OUTPUT_DIR,
        "audio.mp3"
    )

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-vn",
        output_path
    ])

    return FileResponse(output_path)

@app.post("/extract-audio")
async def extract_audio(
    file: UploadFile = File(...)
):
    input_path = os.path.join(
        UPLOAD_DIR,
        f"{uuid.uuid4()}_{file.filename}"
    )

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = os.path.join(
        OUTPUT_DIR,
        "audio.mp3"
    )

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-vn",
        output_path
    ])

    return FileResponse(output_path)

@app.post("/thumbnail")
async def thumbnail(
    file: UploadFile = File(...)
):
    input_path = os.path.join(
        UPLOAD_DIR,
        f"{uuid.uuid4()}_{file.filename}"
    )

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = os.path.join(
        OUTPUT_DIR,
        "thumbnail.jpg"
    )

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-ss",
        "00:00:01",
        "-vframes",
        "1",
        output_path
    ])

    return FileResponse(output_path)
