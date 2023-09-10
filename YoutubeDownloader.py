import pytube

link = input("Enter Youtube Video URL : ")
yt = pytube.YouTube(link)
filter = yt.streams.filter(progressive=True, file_extension='mp4')
filter.get_highest_resolution().download()

print('downloaded', link)
