import sys
import spotipy
import spotipy.util as util


def searchFor(token, name, artist):
    sp = spotipy.Spotify(auth=token)
    results = sp.search(q=artist, type='artist')
    artist_items = results[u'artists'][u'items']
    art_id = ""
    for artist_item in artist_items:
        if artist_item[u'name'] == artist:
            art_id = artist_item[u'id']

    if art_id == "":
        print("Could not find artist. Which is it?")
        print("0. None")
        count = 0
        for artist_item in artist_items:
            count += 1
            statement = str(count) + ". " + artist_item[u'name']
            print(statement)
        answer = raw_input("Type the number: ")
        type(answer)
        print("You typed " + answer)
        if answer == 0:
            return
        else:
            art_id = artist_items[int(answer)-1][u'id']
    final_track = ""
    albums = sp.artist_albums(art_id)
    for alb in albums[u'items']:
        if final_track != "":
            break
        tracks = sp.album_tracks(alb[u'id'])
        for track in tracks[u'items']:
            print(track[u'name'])
            n = track[u'name'].upper().lower()
            if n == name.upper().lower():
                final_track = track
                break
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
    else:
        print "Can't get token for", username






add_missing_mp3_data("downloaded_tracks/6ix9ine_KIKA_(feat._Tory_Lanez).mp3")