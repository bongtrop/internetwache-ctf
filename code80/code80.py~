import socket
import re
import hashlib
import time
from datetime import datetime
import pytz

tz = pytz.timezone('CET')

s = socket.socket()
s.connect(('188.166.133.53', 11117))

word = ""
for i in range(0,256):
	word+=chr(i)

res = ""
while True:
	line = s.recv(1024)
	if len(line)==0:
		break
	
	print line.strip()
	
	m = re.search(r'Char [0-9]+[:] Time is (.+?)and the hash is: ([0-9a-f]+)', line)
	
	if m:
		t = m.group(1)[:8]
		nxt = m.group(1)[8:-1]
		h = m.group(2)

		dt_with_tz = tz.localize(datetime(2016, 2, 21, int(t[0:2]), int(t[3:5]), int(t[6:8])), is_dst=None)
		ts = int((dt_with_tz - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds())
		
		done = False
		for i in range(-30,31):
			t = str(ts + i)
			for w in word:
				crack=t+":"+w
				
				m = hashlib.sha1()
				m.update(crack)
				
				if h==m.hexdigest():
					res+=w
					print res
					s.send(crack+"\n")
					done = True
					break
					
			if done:
				break

							

s.close()


