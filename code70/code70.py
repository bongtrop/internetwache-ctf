import socket
import math
import re

def encode(eq):
	out = []
	for c in eq:
		q = bin(ord(c)^32).lstrip("0b")
		q = "0" * (8-len(q)) + q
		out.append(q)
	b = ''.join(out)
	print b
	pr = []
	for x in range(0,len(b),2):
		c = chr(int(b[x:x+2],2)+51)
		pr.append(c)
	s = '.'.join(pr)
	return s

def decode(eq):
	ss = eq.split('.')
	b = ""
	for s in ss:
		sb = bin(ord(s)-51)[2:]
		sb = "0" * (2-len(sb)) + sb
		b+=sb
	
	res = ""
	for i in range(0, len(b), 8):
		res+=chr(int(b[i:i+8], 2)^32)
		
	return res

s = socket.socket()
s.connect(('188.166.133.53', 11071))


while True:
	line = s.recv(1024)
	if len(line)==0:
		break
	
	print line.strip()
	
	m = re.search(r'Level [0-9]+[.][:] ([0-9.]+)', line.replace("\n","").replace("\r", ""))
	
	if m:
		eq = m.group(1)
		question = decode(eq)
		print question
		m = re.search(r'x ([+/*-]) ([0-9-]+?) [=] ([0-9-]+)', question)
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

			s.send(encode(res)+"\n")
		

s.close()


