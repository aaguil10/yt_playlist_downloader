from __future__ import unicode_literals
from os import listdir
from os.path import isfile, join


from spotify_expert import add_missing_mp3_data
from youtube_downloader import downloadPlaylist

mypath = "downloaded_tracks"


downloadPlaylist("https://www.youtube.com/playlist?list=PL80f_f6Nuu4ZLnh8RI45TrXne4giazCtX")

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file_item in onlyfiles:
	if "DS_Store" in file_item:
		continue
	print(file_item)
	add_missing_mp3_data(mypath + "/" + file_item)
