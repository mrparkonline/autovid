# activate autovid venv
# ./autovid/Scripts/activate.ps1

# Libraries: moviepy python -m pip install moviepy==1.0.3 , pygame, pyttsx3
# Programs: ImageMagick

# Movie Creator
from moviepy.editor import VideoFileClip, AudioFileClip

# Text to Audio
import pyttsx3

engine = pyttsx3.init()

story = """
Story Time!
My family poops big. Maybe it's genetic, maybe it's our diet, but everyone births giant logs of crap. If anyone has laid a mega-poop, you know that sometimes it won't flush. It lays across the hole in the bottom of the bowl and the vortex of draining water merely gives it a spin as it mocks you. Growing up, this was a common enough occurrence that our family had a poop knife. It was an old rusty kitchen knife that hung on a nail in the laundry room, only to be used for that purpose. It was normal to walk through the hallway and have someone call out "hey, can you get me the poop knife"? I thought it was standard kit. You have your plunger, your toilet brush, and your poop knife. Fast forward to 22. It's been a day or two between poops and I'm over at my friend's house. My friend was the local dealer and always had 'guests' over, because you can't buy weed without sitting on your ass and sampling it for an hour. I excuse myself and lay a gigantic turd. I look down and see that it's a sideways one, so I crack the door and call out for my friend. He arrives and I ask him for his poop knife. "My what?" Your poop knife, I say. I need to use it. Please. "Wtf is a poop knife?" Obviously he has one, but maybe he calls it by a more delicate name. A fecal cleaver? A Dung divider? A guano glaive? I explain what it is I want and why I want it. He starts giggling. Then laughing. Then lots of people start laughing. It turns out, the music stopped and everyone heard my pleas through the door. It also turns out that none of them had poop knives, it was just my fucked up family with their fucked up bowels. FML. I told this to my wife last night, who was amused and horrified at the same time. It turns out that she did not know what a poop knife was and had been using the old rusty knife hanging in the utility closet as a basic utility knife. Thankfully she didn't cook with it, but used it to open Amazon boxes. She will be getting her own utility knife now.
"""

engine.save_to_file(story, './tmp/story.mp3')
engine.runAndWait()

# Load the video and audio files
video = VideoFileClip("./tmp/vid1.mp4")
audio = AudioFileClip("./tmp/story.mp3")

# Set Dimensions
video = video.resize(newsize=(1080, 1920))

# Loop the video to match the duration of the audio
video = video.loop(duration=audio.duration)

# Set the audio to the video
video = video.set_audio(audio)

# Save the final video
video.write_videofile("reel.mp4", codec="libx264", audio_codec="aac")