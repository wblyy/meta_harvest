#coding=utf-8
import re
s='Toheart(WooHy??un&Ke?y)'
kuohao=re.sub('\(.*?\)|\[.*?]|{.*?}|（.*?）','',s)#去括号
print '(no)',kuohao#s表示需要处理的字符串
#wenhao=re.sub(r'?','',kuohao)
#print  wenhao
