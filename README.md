# Small_Functions

Some interesting code fragments to please

1. PC monitor record
  
  the code will record  the mouse's position and the keyboard words when the victim click the mouse or press the keyboard. What's more, the recorder can give you the window info which the victim visit now and the exact time of the monitor trace.

2. Baidu_Map_API
  
  give somewhere ,  and the code will give you an exact position of it.

3. face_detect

  use C++ with OpenCV to detect the face in a picture, and cut out of it.
  myFace: open the PC's camera, and then get lots of your pictures. the program then detect your face exactly
  otherFace: use other person's picture to detect
  
4. Auto_Login_with_Visidate

  Some website's login page has the identify code, and it's difficult to use auto login script(like requests, urlib2 and so on). We use selenium to simulate the broswer and recognize the identify code. What's more, we get the alert result info, and you can use the script to brute force some website login page with identify code.

5. wechat_boom

  Select your friends and the words u want to tell them, then boom their wechat program!! The version is the gui, it's convinient to process the attack.
  
6. Fb_leak_via_CSS

  Use the the CSS function of mix-blend-mode and the vulnerability of the Chrome(v49 -- v63) or Firefox(v49 -- v50), the script can read the name, head sculpture and website you like on your Facebook. More about it, see [details](https://www.bleepingcomputer.com/news/security/css-is-so-overpowered-it-can-deanonymize-facebook-users/)
  To test the result, I provide a website to test the attack. [my poc](http://www.lovebear.top/fb_leak_general_poc.html)

7. Github_auoto_star

  Gitstar is a website where pepople can star each other conviniently. If we want to star a lot of repetories, we need a lot of time. The tool is used to automatelly get the list of the repos and star them in a very fast way.

8. CrackOffice

  CrackOffice is a tool to get the password of the Encrypted Office files(word, excel and so on) with the method of violent crack. You can use the default password dictionary. Or you can customize your own dictionary. It's amazing!
  
9. iuka.cn

  Some vunerable websites' Poc experience. That's cool! This is for www.iuka.cn, i have got all of the database of it.

10. instant

  Make your site’s pages instant in 1 minute and improve your conversion rate by 1%.
  
11. HuaweiAttack

  Poc of Huawei Talent Summit URL Password Attack Vulnerability.
  
12. IPv6 Config

  Automatelly config IPv6 on Windows. Use the Administrator previledge to run the bat file.

13. ip2pref

  Give 2 ip, calc the min prefix of them

14. ssh_rproxy

  create reverse proxy via ssh

15. Controll_ZK

  controll all slaves on master, start/stop/status