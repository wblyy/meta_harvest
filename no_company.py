#coding=utf-8
import random
import csv
import MySQLdb
import sys
from mydb import Tiedb
from mydb import Meta
import re


mydb = Tiedb()
meta = Meta()
    # for row in mydb.get_random_rows(100, "%gmail.com"):
        # print row
    # sys.exit(0)
    #print mydb.get_song_info("青花瓷","周杰伦")[0],mydb.get_song_info("青花瓷","周杰伦")[1],mydb.get_song_info("青花瓷","周杰伦")[2]
csvfile = file('meta_no_company.csv', 'rb')
reader = csv.reader(csvfile)
index=0
index_error=0
index_full=0
for lrow in list(reader):
    index=index+1
    print '处理前:',lrow[0].decode('gbk'),index
    album=lrow[0].decode('gbk').encode('UTF-8')
    #album=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',album_raw)#去括号
    try:        
        print '处理后：',album

        if '好声音' in album:
            #梦响强音
            meta.update_album_company(album,'梦响强音')
        elif 'M-net' in album:
            meta.update_album_company(album,'SM')
        elif '好歌曲' in album:
            meta.update_album_company(album,'通力时代')
        elif '雪碧' in album:
            meta.update_album_company(album,'可口可乐')
        elif '最美和声' in album:
            meta.update_album_company(album,'北京卫视')
        elif '我是歌手' in album:
            meta.update_album_company(album,'湖南卫视')
        elif '华语单曲榜' in album:
            meta.update_album_company(album,'KKBOX')
        elif '在线热搜（华语）系列' in album:
            meta.update_album_company(album,'QQ音乐')
        elif '新歌速递' in album:
            meta.update_album_company(album,'QQ音乐')
        elif '最强音' in album:
            meta.update_album_company(album,'湖南卫视')
        elif '直通春晚' in album:
            meta.update_album_company(album,'恒大音乐')






        #company_info=mydb.get_album_company(album)
        if company_info:
            company=company_info[0]
            print '处理后：',album,company            
            
            index_full=index_full+1

    except Exception, e:
        index_error=index_error+1
        print e,index_error
        

