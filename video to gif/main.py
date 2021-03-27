from moviepy.editor import VideoFileClip

clip = VideoFileClip("anyway.mp4")
clip.write_gif("mygif.gif", fps=15)
