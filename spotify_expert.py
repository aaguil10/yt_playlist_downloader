import sys
import spotipy
import spotipy.util as util

PAGINATION_LIMIT = 50

def findArtist(sp, artist):
    index = 0
    results = sp.search(q=artist, limit=PAGINATION_LIMIT, offset=index, type='artist')
    artist_items = results[u'artists'][u'items']
    for artist_item in artist_items:
        if artist_item[u'name'] == artist:
            return artist_item[u'id']
    while len(results[u'artists'][u'items']) > 0:
        index += PAGINATION_LIMIT
        results = sp.search(q=artist, limit=PAGINATION_LIMIT, offset=index, type='artist')
        artist_items = artist_items + results[u'artists'][u'items']
        for artist_item in results[u'artists'][u'items']:
            if artist_item[u'name'] == artist:
                return artist_item[u'id'] 

    print("Could not find artist. Which is it?")
    print("0. None")
    count = 0
    for artist_item in artist_items:
        count += 1
        statement = str(count) + ". " + artist_item[u'name']
        print(statement)
    answer = raw_input("Type the number: ")
    type(answer)
    if answer == 0:
        return 0
    else:
        return artist_items[int(answer)-1][u'id']

def getTrackFromAlbums(sp, artist_id, index, final_tracks, name):
    last_response = sp.artist_albums(artist_id, limit=PAGINATION_LIMIT, offset=index)
    albums = last_response[u'items']
    for alb in albums:
        tracks = sp.album_tracks(alb[u'id'])
        for track in tracks[u'items']:
            n = track[u'name'].upper().lower()
            if n == name:
                track[u"album"] = alb[u'name']
                final_tracks.append(track)
                break;
    return len(albums)

def findTrack(sp, artist_id, name):
    final_tracks = []
    index = 0
    num_albums_returned = getTrackFromAlbums(sp, artist_id, index, final_tracks, name)
    while num_albums_returned > 0:
        index += PAGINATION_LIMIT
        num_albums_returned = getTrackFromAlbums(sp, artist_id, index, final_tracks, name)
    
    if len(final_tracks) == 0:
        return ""
    if len(final_tracks) == 1:
        return final_tracks[0]
    print("Found mutiple albums with the song. Which do you want?")
    index = 0
    for t in final_tracks:
        index += 1
        print(str(index) + ". " + t[u"album"])
    answer = raw_input("Type the number: ")
    type(answer)
    return final_tracks[int(answer) - 1]



def searchFor(token, name, artist):
    name = name.upper().lower()
    artist = artist.upper().lower()
    sp = spotipy.Spotify(auth=token)
    artist_id = findArtist(sp, artist)
    final_track = findTrack(sp, artist_id, name)
    
    print(final_track)




def add_missing_mp3_data(mp3_filepath):
    scope = 'user-library-read'
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print "Usage: %s username" % (sys.argv[0],)
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if token:
        searchFor(token, u'stop', u'jane\'s Addiction')
        # searchFor(token, u'stop', u'john')
    else:
        print "Can't get token for", username






add_missing_mp3_data("downloaded_tracks/6ix9ine_KIKA_(feat._Tory_Lanez).mp3")