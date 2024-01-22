from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

video = askopenfilename()
clip = VideoFileClip(video)
gifname = input("Enter the GIF name to be saved:")
clip.write_gif(gifname, fps=10)     #used imageio to create gifs