import sys
import spotipy
import spotipy.util as util


def searchFor(token, name, artist):
    sp = spotipy.Spotify(auth=token)
    results = sp.search(q=artist, type='artist')
    artist_items = results[u'artists'][u'items']
    print(artist_items)
    # albums = sp.artist_albums(artist_id)
    # print(results)
    mytrack = "";
    # for track in results[u'tracks'][u'items']:
    #     if(mytrack != ""):
    #         break
    #     for artist_item in track[u'artists']:
    #         print(artist_item[u'name'])
    #         if(artist_item[u'name'] == artist):
    #             mytrack = track
    #             break



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