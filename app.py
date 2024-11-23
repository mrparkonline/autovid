# Using venv
# activate autovid venv
# ./autovid/Scripts/activate.ps1

# External Libraries / Programs
# moviepy python -m pip install moviepy==1.0.3
# Libraries: moviepy, pygame, pyttsx3
# Programs: ffmpeg, ImageMagick


# EXTERNAL IMPORTS
import streamlit as st
import pyttsx3
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

# INTERNAL IMPORTS
import os
import datetime
from random import choice

# os.environ["FFMPEG_BINARY"] = "C:\\ProgramData\\ffmpeg\\bin\\ffmpeg.exe"
# os.environ["FFPLAY_BINARY"] = "C:\\ProgramData\\ffmpeg\\bin\\ffplay.exe"
# os.environ["IMAGEMAGICK_BINARY"] = "C:\\Program Files\\ImageMagick\\magick.exe"

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
custom_vids = list(os.listdir(f"./src/custom"))

video = None
# END OF INITIALIZATIONS

# Helper Functions
def remove_tmp_audio(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied: Unable to delete '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# STREAMLIT APP
st.title("AutoVid Application")

vid_type = st.radio(
    label="Video Type:",
    options=["minecraft", "stock", "hacker","custom"],
    captions=[
        "Minecraft Parkour!",
        "Randoms in the background",
        "Terminal, Hooded man kinda vibe",
        "Choose your own video!"
    ],
    key="vid_type"
)

if vid_type == "custom":
    custom_video = st.selectbox(
        label="Choose a video",
        options=custom_vids
    )
    v_path = f"./src/custom/"+custom_video
# end vid_type == custom

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
    with open(f"./output/reel_script_{formatted_date}.txt", "w") as data_file:
        data_file.write(story)
        print(f"{story}\n written to reel_script_{formatted_date}.txt")
# end of audio_gen

# Video Creation Portion
if audio_made:
    # Streamlit Settings

    # Set audio
    if audio_path:
        audio = AudioFileClip(audio_path)

    # Set Video
    if vid_type != "custom":
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

    #video.write_videofile(f"./output/reel_{formatted_date}.mp4", codec="libx264", audio_codec="aac")
    video.write_videofile(f"./output/reel_{formatted_date}.mp4", codec="mpeg4", audio_codec="aac")
    remove_tmp_audio(audio_path) # Removes the tmp audio after video is created
# END OF PROGRAM
