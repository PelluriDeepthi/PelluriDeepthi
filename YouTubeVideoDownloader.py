import pytube

link = input("Paste the url here:")

# Using the module to download the video
video = pytube.YouTube(link)
video.streams.first().download()

print("Downloaded Successfully", link)