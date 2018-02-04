# -*- coding: utf-8 -*- 
import socket
import commands
import struct
import os
import threading

flag=True
def getFile():
		fileinfo_size=struct.calcsize('=12sl')
		fhead=conn.recv(fileinfo_size)
		if(fhead):
			cfilename,cfilesize=struct.unpack('=12sl',fhead)
			cfilename=cfilename.strip('\00')
			if(not cfilename.startswith('hook')):
				flag=False
				return
			if(not os.path.exists(file_name+str(addr)+'\\')):
				os.makedirs(file_name+str(addr)+'\\')
			logf=open(file_name+str(addr)+'\\'+str(addr)+'_head_log.txt','ab')
			logf.write(cfilename+' '+str(cfilesize)+'\n\r')
			logf.close()
			
			recv_size=0
			f=open(file_name+str(addr)+'\\'+str(addr)+'_data_log.txt','ab')
			while(not recv_size==cfilesize):
				if cfilesize-recv_size>1024:
					data=conn.recv(1024)
					recv_size+=len(data)
				else:
					data=conn.recv(cfilesize-recv_size)
					recv_size=cfilesize
				f.write(data)
			f.close()
			flag=True

HOST='192.168.1.105'
PORT=8090
file_name='D:\\getdata\\'
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(5)
while 1:
	try:
		conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
		print'Connected by',addr    #输出客户端的IP地址
		thread = threading.Thread(target=getFile)  #多线程
		thread.setDaemon(True)   #守护进程
		thread.start()
		if(not flag):
			conn.close()
	except socket.timeout:
		conn.close()