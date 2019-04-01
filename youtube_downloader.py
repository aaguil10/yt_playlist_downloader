from __future__ import unicode_literals
import youtube_dl
import eyed3
import urllib2
import json
import os
import shutil
import glob

# from track_gui import Mp3InfoWindow
from Mp3Data import Mp3Data


def getNameAndArtist(info, mp3_data):
    try:
        mylist = info['description'].splitlines()
        arry = mylist[2].split("\xb7")
        mp3_data.setTrack(arry[0].strip())
        mp3_data.setArtist(arry[1].strip())
    except:
        print('An error occured getting the description.')
        print(info)


def downloadVideo(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def createFileName(name, artist):
    artist = artist.replace(' ', '_').replace('\'', '')
    name = name.replace(' ', '_').replace('\'', '')
    filename = artist + '_' + name + ".mp3"
    return filename

def findPath(info):
    # title = info['title']
    # id = info['id']
    # print("title: " + title)
    # print("id: " + id)
    # path = title + "-" + id + ".mp3"
    path = glob.glob("*.mp3")[0]
    return path

# See following link for list of tags
# https://eyed3.readthedocs.io/en/latest/plugins/display_plugin.html
def addid3Tag(mp3_data):
    audiofile = eyed3.load(mp3_data.path)
    audiofile.tag.title = mp3_data.track
    audiofile.tag.artist = mp3_data.artist
    audiofile.tag.save()
    print(audiofile.tag.genre)


def downloadPlaylist(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
    for entries in info['entries']:
        data = Mp3Data(entries[u'webpage_url'])
        getNameAndArtist(entries, data)
        description = entries[u'description']
        downloadVideo(data.id)
        filename = createFileName(data.track, data.artist)
        path = findPath(entries)
        try:
            if not os.path.exists('downloaded_tracks/'):
                os.mkdir('downloaded_tracks/')
            shutil.copyfile(path, 'downloaded_tracks/'+filename)
            os.remove(path)
            data.setPath('downloaded_tracks/'+filename)
        except:
            print("File does not exist " + filename)
            print("Or path is wrong " + path)
            continue
        addid3Tag(data)






downloadPlaylist("https://www.youtube.com/playlist?list=PL80f_f6Nuu4bdwS1DWOgS0i5hRGja3IYT")









