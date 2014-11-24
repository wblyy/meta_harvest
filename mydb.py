#coding=utf-8
import random
import csv
import MySQLdb
import sys

class Mydb(object):
    def __init__(self, user, passwd, dbname):
        self._id = 0           # use in pop function
        self.user = user
        self.passwd = passwd
        self.dbname = dbname

    @property
    def db(self):
        return MySQLdb.connect("localhost", self.user, self.passwd, self.dbname, charset='utf8')

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def _execute(self, *args, **kwargs):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args, **kwargs)
        conn.commit()

    def _query_row(self, *args):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args)
        rows = cur.fetchone()
        return rows

    def _query_rows(self, *args):
        conn = self.db
        cur = conn.cursor()
        cur.execute(*args)
        rows = cur.fetchall()
        return rows    

class Tiedb(Mydb):
    def __init__(self):
        Mydb.__init__(self, 'root', '654321', 'music_meta')

    def get_album_info(self, album_id):
        return self._query_row('select company,publishDate from album_info where id=%s', (album_id, ))
    def get_song_info_xiami(self,song, artist):
        return self._query_row('select album_id,album,musicUrl,lyricid,song_id from song_info_xiami where title=%s and artist=%s limit 1', (song, artist))
    def get_song_info_qqmusic(self,song, artist):
        return self._query_row('select album_id,album,musicUrl,lyricid,song_id from song_info_qqmusic where title=%s and artist=%s limit 1', (song, artist))
    def get_lyric(self, song_id):
        return self._query_row('select lyric from lyrics where song_id=%s', (song_id, ))
      
class Meta(Mydb):
    def __init__(self):
        Mydb.__init__(self, 'root', '654321', 'metadata')

    def update_album_info(self, album_name,song,artist):
        self._execute("update meta set album_name=%s where song=%s and artist=%s", (album_name,song,artist))

        
if __name__ == "__main__":
    mydb = Tiedb()
    meta = Meta()
    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    #print mydb.get_song_info("青花瓷","周杰伦")[0],mydb.get_song_info("青花瓷","周杰伦")[1],mydb.get_song_info("青花瓷","周杰伦")[2]
    csvfile = file('meta_no_album.csv', 'rb')
    reader = csv.reader(csvfile)
    index=0
    index_error=0
    index_full=0
    for lrow in list(reader):
        index=index+1
        print lrow[0].decode('gbk'),lrow[1].decode('gbk'),'index:',index
        try:
            song_info=mydb.get_song_info_qqmusic(lrow[0].decode('gbk').encode('UTF-8'),lrow[1].decode('gbk').encode('UTF-8'))
            song=lrow[0].decode('gbk').encode('UTF-8')
            artist=lrow[1].decode('gbk').encode('UTF-8')
            album_id=song_info[0]
            album_name=song_info[1]
            download_url=song_info[2]
            lyricid=song_info[3]
            song_id=song_info[4]
            print album_id,album_name,download_url,lyricid,song_id,'index_full:',index_full
            meta.update_album_info(album_name,song,artist)
            #album_info=mydb.get_album_info(album_id)
            #company=album_info[0]
            #publishDate=album_info[1]
            #if company:
            index_full=index_full+1

            #lyric=mydb.get_lyric(song_id)[0]

            #print album_id,album_name,download_url,lyricid,song_id,company,publishDate,'index_full:',index_full
            #print lyric

        except Exception, e:
            index_error=index_error+1
            print e,index_error
        

