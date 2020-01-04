def ip2char(ip):
	tmp = ip.split('.')
	return "{0:08b}{1:08b}{2:08b}{3:08b}".format(int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3]))

def char2ip(chars):
	return "{0:d}.{1:d}.{2:d}.{3:d}".format(int(chars[:8],2),int(chars[8:16],2),int(chars[16:24],2),int(chars[24:],2))

def gen_pref(ip1, ip2):
	ip1, ip2 = ip2char(ip1), ip2char(ip2)
	for i in range(32):
		if ip1[i] != ip2[i]:
			break
	res = ip1[:i]+'0'*(32-i)
	return char2ip(res)+'/'+str(i)

print(gen_pref('192.168.0.1', '192.168.255.255'))