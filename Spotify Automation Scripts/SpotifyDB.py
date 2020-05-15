import sqlite3

'''
# This class acts as an encapsulation tool for database code Defines the getSpotifyToken() method which is very handy
# when interacting with the Spotify WEB API Defines insertPlaylist which is an automation pipeline for creating and 
# inserting Spotify playlists based on database Values 

This will allow for the following object/call tree
--> db = SpotifyDB()
--> spotifyToken = db.getSpotifyToken()
--> db.insertPlaylist(newPlaylistId, playlistName)
 
'''


class SpotifyDB:
    def __init__(self):
        self.conn = sqlite3.connect('script.db')

    def getSpotifyToken(self):
        c = self.conn.cursor()
        c.execute("SELECT value FROM tokens WHERE token_type = 'access_token'")
        return c.fetchone()[0]

    def insertPlaylist(self, newPlaylistId, playlistName):
        c = self.conn.cursor()
        c.execute("INSERT INTO playlists_created (spotify_playlist_id, playlist_name) VALUES (?, ?)",
                  (newPlaylistId, playlistName))
        self.conn.commit()
