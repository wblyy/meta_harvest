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
        company_info=mydb.get_album_company(album)
        if company:
            company=company_info[0]
            print '处理后：',album,company            
            meta.update_album_company(album,company)
            index_full=index_full+1

    except Exception, e:
        index_error=index_error+1
        print e,index_error
        

