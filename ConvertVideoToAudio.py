import moviepy.editor

s = input("Enter the video name:")
#video can be any format like mp4... 
video = moviepy.editor.VideoFileClip(s)
audio = video.audio
a = input("Enter the audio file name:")
#audio file will be in mp3 format...
audio.write_audiofile(a)
