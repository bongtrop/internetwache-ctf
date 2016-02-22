import socket
import math
import re

s = socket.socket()
s.connect(('188.166.133.53', 11059))

def isprime(count):
	for x in range(2, int(math.sqrt(count) + 1)):
		if count % x == 0: 
			return False
			
	return True
			

while True:
	line = s.recv(1024)
	if len(line)==0:
		break
	
	print line.strip()
	
	m = re.search(r'Find the next prime number after ([0-9]+)[:]', line)
	
	if m:
		n = int(m.group(1))
		
		if n==1:
			print "2"
			s.send(str(2)+"\n")
			continue
		
		if n % 2 == 0:
			n+=1
		else:
			n+=2
			
		
		while True:
			if isprime(n):
				print n
				s.send(str(n)+"\n")
				break
			
			n+=2
		
		
	
s.close()
