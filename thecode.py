from pytube import YouTube

yt = YouTube(input("Enter the URL of the YouTube video you want to download: "))
kind = input("If you want an mp4 download enter \"mp4\" \n If you want a mp3 download enter \"mp3\"").upper()

if kind == "MP4":
    now = yt.streams.get_highest_resolution()
elif kind == "MP3":
    now = yt.streams.get_audio_only()

now.download("/Users/avigranoff/Desktop")