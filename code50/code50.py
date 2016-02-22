import socket
import re

s = socket.socket()
s.connect(('188.166.133.53', 11027))

while True:
	line = s.recv(1024)
	if len(line)==0:
		break
	
	print line.strip()
	
	m = re.search(r'Level [0-9]+[.][:] x ([+/*-]) ([0-9-]+?) [=] ([0-9-]+)', line)
	
	if m:
		op = m.group(1)
		x = int(m.group(3))
		y = int(m.group(2))
		
		res = ""
		
		if op=="+":
			print "x = "+str(x-y)
			res = str(x-y)
		elif op=="-":
			print "x = "+str(x+y)
			res = str(x+y)
		elif op=="*":
			print "x = "+str(x/y)
			res = str(x/y)
		else:
			print "x = "+str(x*y)
			res = str(x*y)
	
		s.send(res+"\n")
	
s.close()
