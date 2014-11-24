#coding=utf-8
import re
s='我的老故事 (？？ ？？？？？)'
s=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',s)#去括号
print '(no)',s.decode('utf-8')#s表示需要处理的字符串
#wenhao=re.sub(r'?','',kuohao)
#print  wenhao
