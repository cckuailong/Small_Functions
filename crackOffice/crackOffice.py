import sys, msoffcrypto, time

base_dir = 'C:\\Users\\lovebear\\Desktop\\'
pwd_file = 'pwd.txt'
encrypt_file = 'test.docx'
f = open(base_dir+encrypt_file, "rb")
file = msoffcrypto.OfficeFile(f)

with open(base_dir+pwd_file, 'r') as f:
	data = f.read().strip()
	pwds = data.split('\n')
for pwd in pwds:
	f1 = open(base_dir+"decrypted.docx", "wb")
	# Use password
	file.load_key(password=pwd)
	try:
		file.decrypt(f1)
		print ('Encrpt Pwd is %s' % pwd)
		break
	except:
		pass
	f1.close()
f.close()