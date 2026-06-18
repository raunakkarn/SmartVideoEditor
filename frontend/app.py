import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("Smart Video Editor")

uploaded_file = st.file_uploader(
    "Upload Video",
    type=["mp4", "mkv", "avi", "mov"]
)

operation = st.selectbox(
    "Choose Operation",
    [
        "Thumbnail",
        "Audio Extraction",
        "Trim",
        "Convert",
        "Compress",
        "Resize"
    ]
)

if uploaded_file:

    st.success("Video Uploaded")

    if operation == "Thumbnail":

        if st.button("Generate Thumbnail"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "video/mp4"
                )
            }

            response = requests.post(
                f"{BACKEND_URL}/thumbnail",
                files=files
            )

            if response.status_code == 200:
                st.image(response.content)

            else:
                st.error("Thumbnail generation failed")

    elif operation == "Audio Extraction":

        if st.button("Extract Audio"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "video/mp4"
                )
            }

            response = requests.post(
                f"{BACKEND_URL}/extract-audio",
                files=files
            )

            if response.status_code == 200:

                st.download_button(
                    "Download Audio",
                    response.content,
                    file_name="audio.mp3"
                )

            else:
                st.error("Audio extraction failed")

    elif operation == "Trim":

        start = st.number_input(
            "Start Time (seconds)",
            min_value=0,
            value=0
        )

        duration = st.number_input(
            "Duration (seconds)",
            min_value=1,
            value=5
        )

        if st.button("Trim Video"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "video/mp4"
                )
            }

            data = {
                "start": start,
                "duration": duration
            }

            response = requests.post(
                f"{BACKEND_URL}/trim",
                files=files,
                data=data
            )

            if response.status_code == 200:

                st.download_button(
                    "Download Trimmed Video",
                    response.content,
                    file_name=f"trimmed_{uploaded_file.name}"
                )

            else:
                st.error("Video trimming failed")
    elif operation == "Convert":
    
        fmt = st.selectbox(
            "Output Format",
            ["mp4", "mkv", "avi", "mov"]
        )
    
        if st.button("Convert Video"):
    
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "video/mp4"
                )
            }
    
            data = {
                "fmt": fmt
            }
    
            response = requests.post(
                f"{BACKEND_URL}/convert",
                files=files,
                data=data
            )
    
            if response.status_code == 200:
    
                st.download_button(
                    "Download Converted Video",
                    response.content,
                    file_name=f"converted.{fmt}"
                )
    
            else:
                st.error("Conversion failed")
    
    elif operation == "Compress":
    
        crf = st.slider(
            "Compression Level",
            min_value=18,
            max_value=35,
            value=28
        )
    
        if st.button("Compress Video"):
    
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "video/mp4"
                )
            }
    
            data = {
                "crf": crf
            }
    
            response = requests.post(
                f"{BACKEND_URL}/compress",
                files=files,
                data=data
            )
    
            if response.status_code == 200:
    
                st.download_button(
                    "Download Compressed Video",
                    response.content,
                    file_name=f"compressed_{uploaded_file.name}"
                )
    
            else:
                st.error("Compression failed")

    elif operation == "Resize":
    
        resolution = st.selectbox(
            "Resolution",
            [
                "1920:1080",
                "1280:720",
                "854:480"
            ]
        )
    
        if st.button("Resize Video"):
    
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "video/mp4"
                )
            }
    
            data = {
                "resolution": resolution
            }
    
            response = requests.post(
                f"{BACKEND_URL}/resize",
                files=files,
                data=data
            )
    
            if response.status_code == 200:
    
                st.download_button(
                    "Download Resized Video",
                    response.content,
                    file_name=f"resized_{uploaded_file.name}"
                )
    
            else:
                st.error("Resize failed")
