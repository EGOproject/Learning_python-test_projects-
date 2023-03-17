from pytube import YouTube
link = str(input("enter your link: "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
 