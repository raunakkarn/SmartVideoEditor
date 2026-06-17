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
        "Trim"
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
