#coding=utf-8
import random
import csv
import MySQLdb
import sys
from mydb import Tieba
from mydb import Meta


mydb = Tiedb()
meta = Meta()
    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    #print mydb.get_song_info("青花瓷","周杰伦")[0],mydb.get_song_info("青花瓷","周杰伦")[1],mydb.get_song_info("青花瓷","周杰伦")[2]
csvfile = file('meta_no_artist.csv', 'rb')
reader = csv.reader(csvfile)
index=0
index_error=0
index_full=0
for lrow in list(reader):
    index=index+1
    print '处理前:',lrow[0].decode('gbk'),index
    try:
        song=lrow[0].decode('gbk').encode('UTF-8')
        song==re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',song)#去括号
        song_info=mydb.get_artist_xiami(song)
        print '处理后：',song,artist            
        meta.update_artist_info(song,artist)
        index_full=index_full+1
        
    except Exception, e:
        index_error=index_error+1
        print e,index_error
        

