# activate autovid venv
# ./autovid/Scripts/activate.ps1

# Libraries: moviepy, pygame, pyttsx3
# Programs: ImageMagick

# EXTERNAL IMPORTS
import streamlit as st
import pyttsx3
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

# INTERNAL IMPORTS
import datetime
import os
from random import choice

# END OF IMPORTS

# Initialization
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d-%H-%M")
engine = pyttsx3.init()

audio = None
audio_made = False
audio_path = None

m_vids = list(os.listdir(f"./src/minecraft"))
h_vids = list(os.listdir(f"./src/hacker"))
s_vids = list(os.listdir(f"./src/stock"))

video = None
# END OF INITIALIZATIONS

# STREAMLIT APP
st.title("AutoVid Application")

vid_type = genre = st.radio(
    label="Video Type:",
    options=["minecraft", "stock", "hacker"],
    captions=[
        "Minecraft Parkour!",
        "Randoms in the background",
        "Terminal, Hooded man kinda vibe"
    ],
    key="vid_type"
)

story = st.text_area(
    label="Enter the text here.",
    height=136,
    key="story"
)

audio_gen = st.button(
    label="Generate Reel",
    key="audio_btn",
    disabled=True if not story else False
)

if audio_gen:
    audio_path = f"./tmp/story_{formatted_date}.mp3"
    engine.save_to_file(story, audio_path)
    engine.runAndWait()
    audio_made = True
# end of audio_gen

# Video Creation Portion
if audio_made:
    # Streamlit Settings

    # Set audio
    if audio_path:
        audio = AudioFileClip(audio_path)

    # Set Video
    v_path = f"./src/{vid_type}/"
    video = VideoFileClip("./tmp/vid1.mp4")

    if vid_type == "minecraft":
        v_path += choice(m_vids)
    elif vid_type == "stock":
        v_path += choice(s_vids)
    elif vid_type == "hacker":
        v_path += choice(h_vids)

    video = VideoFileClip(v_path)

    # Set Dimensions
    video = video.resize(newsize=(1080, 1920))

    # Loop the video to match the duration of the audio
    video = video.loop(duration=audio.duration)

    # Set the audio to the video
    video = video.set_audio(audio)

    video.write_videofile(f"./output/reel_{formatted_date}.mp4", codec="libx264", audio_codec="aac")
# END OF PROGRAM
