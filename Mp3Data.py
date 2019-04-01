import json

class Mp3Data:

    def __init__(self, id):
        self.id = id
        self.track = ''
        self.artist = ''
        self.album = ''
        self.albumart_url = ''
        self.path = ''

    def buildFromJson(json_obj):
        obj = Mp3Data(json_obj.get(u'id'))
        obj.setTrack(json_obj.get(u'track'))
        obj.setArtist(json_obj.get(u'artist'))
        obj.setAlbum(json_obj.get(u'album'))
        obj.setAlbumartUrl(json_obj.get(u'albumart_url'))
        obj.setPath(json_obj.get(u'path'))
        return obj

    buildFromJson = staticmethod(buildFromJson)

    def toJson(self):
        j = json.dumps(self, default=lambda o: o.__dict__)
        return j

    def setTrack(self, track_):
        self.track = track_

    def setArtist(self, artist_):
        self.artist = artist_

    def setAlbum(self, album_):
        self.album = album_

    def setAlbumartUrl(self, albumart_url_):
        self.albumart_url = albumart_url_

    def setPath(self, path):
        self.path = path


    def isComplete(self):
        if self.id == '':
            print("no id")
            return False
        if self.track == '':
            print("no track")
            return False
        if self.artist == '':
            print("no artist")
            return False
        if self.album == '':
            print("no album")
            return False
        if self.albumart_url == '':
            print("no albumart_url")
            return False
        return True
