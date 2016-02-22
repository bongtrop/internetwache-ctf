import socket
import re

class Node:
	def __init__(self, val):
		self.l = None
		self.r = None
		self.v = val

class Tree:
	def __init__(self):
		self.root = None
		
	def getRoot(self):
		return self.root
		
	def _add(self, val, node):
		if(val <= node.v):
			if(node.l != None):
				self._add(val, node.l)
			else:
				node.l = Node(val)
		else:
			if(node.r != None):
				self._add(val, node.r)
			else:
				node.r = Node(val)

	def add(self, val):
		if(self.root == None):
			self.root = Node(val)
		else:
			self._add(val, self.root)
			
	def preorder(self, node, path):
		path.append(node.v)
		
		if node.r != None:
			self.preorder(node.r, path)

		if node.l != None:
			self.preorder(node.l, path)
			


s = socket.socket()
s.connect(('188.166.133.53', 11491))

while True:
	line = s.recv(1024)
	if len(line)==0:
		break
	
	print line.strip()
	
	m = re.search(r'Level [0-9]+[.][:] \[([0-9, ]+?)\]', line)
	
	if m:
		inp = m.group(1)

		tree = Tree()
		words = inp.split(", ")
		for word in words:
			tree.add(int(word))

		path = []
		tree.preorder(tree.getRoot(), path)
		print path
		s.send(str(path)+"\n")
		

s.close()

     
