# -*- coding:utf-8 -*-
import requests
from Tkinter import *

def on_click():
	mv_url = mv_url_text.get()
	requests.adapters.DEFAULT_RETRIES = 5
	s = requests.session()
	s.keep_alive = False
	url = 'http://www.weibodang.cn/dang.php'
	headers = {'Cookie':'csrftoken=fDgkPCPjhuwlPx5tRPO4SzOdNoybQHuv; _ga=GA1.2.1333615370.1525947715; lang=chs; _gid=GA1.2.2104045124.1527408500; Hm_lvt_9918e92916590d12525d5fc1be3d1d5f=1525947715,1527409793; Hm_lpvt_9918e92916590d12525d5fc1be3d1d5f=1527412641'}
	data = {'csrfmiddlewaretoken':'fDgkPCPjhuwlPx5tRPO4SzOdNoybQHuv','q':mv_url,'check':'%C2%A0%C2%A0%C2%A0%E8%8E%B7%E5%8F%96%E8%A7%86%E9%A2%91%C2%A0%C2%A0%C2%A0'}
	r=requests.post(url, headers = headers, data = data)
	res = str(r.text.encode('utf8'))
	start = res.find('<video src=')
	end = res.find(' controls="controls"')
	file_url = res[start+13:end-1]
	print file_url

	r = requests.get(file_url, stream=True)
	with open('C:/Users/lovebear96/Desktop/1.mp4', 'wb') as pdf:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				pdf.write(chunk)



#mv_url = 'http://v.yinyuetai.com/video/3219893'

root = Tk(className='Mv Download')

mv_url_label = Label(root, text='mv_url')
mv_url_label.grid(row=0, column=1)
mv_url_text = StringVar()
mv_url_text.set('http://...')
mv_url_entry = Entry(root)
mv_url_entry['textvariable'] = mv_url_text
mv_url_entry.grid(row=0, column=2)

start_btn = Button(root)
start_btn['text'] = 'Download'
start_btn['command'] = on_click
start_btn.grid(row=1, column=2)

root.mainloop()