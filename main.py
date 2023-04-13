from pytube import YouTube

link=input("Enter your link:")
youtube_1=YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos=youtube_1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)

strm=int(input("Enter"))
videos[strm].download()
print('Done ✔')