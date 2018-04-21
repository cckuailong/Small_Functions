# -*- coding: utf-8 -*-
import itchat
import time
import os
from Tkinter import *

# kill the process by pid
def stop():
	cmd = 'taskkill.exe /F /pid:'+str(pid)
	os.system(cmd)


def on_click():  
	name = name_text.get()
	msg = msg_text.get()
	t = t_text.get()
	try:
		# login
		itchat.auto_login(hotReload=True)
		info_label['text'] = '轰炸ing。。。'
		# search friends
		users = itchat.search_friends(name=name)
		userName = users[0]['UserName']
		# loop to send message 
		while True:
			itchat.send(msg, toUserName = userName)
			time.sleep(t)
	except:
		info_label['text'] = '请检查你的好友昵称和网络连接情况'

pid = os.getpid()
# create gui
root = Tk(className='微信轰炸程序')  
root.geometry('300x200')
# name input
name_label = Label(root, text='好友微信昵称')
name_label.pack()  

name_text = StringVar()  
name_text.set('李强')  

name_entry = Entry(root)  
name_entry['textvariable'] = name_text  
name_entry.pack()
# message input
msg_label = Label(root, text='轰炸信息内容')
msg_label.pack()  

msg_text = StringVar()  
msg_text.set('哈哈哈')  

msg_entry = Entry(root)  
msg_entry['textvariable'] = msg_text  
msg_entry.pack()
# time input
t_label = Label(root, text='轰炸时间间隔')
t_label.pack()  

t_text = StringVar()  
t_text.set('3')  

t_entry = Entry(root)  
t_entry['textvariable'] = t_text  
t_entry.pack()
# hint info
info_label = Label(root, text='输入昵称和消息，点击按钮享受轰炸的快感吧', fg='red')
info_label.pack()
# attack button
attack_btn = Button(root)  
attack_btn['text'] = 'Attack!!'  
attack_btn['command'] = on_click  
attack_btn.pack(side=LEFT, padx=50)
# stop button
stop_btn = Button(root)  
stop_btn['text'] = 'Stop!!'
stop_btn['command'] = stop  
stop_btn.pack(side=RIGHT, padx=50)

root.mainloop()
