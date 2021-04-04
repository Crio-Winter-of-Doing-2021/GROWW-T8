def getPath(url):
	path = []
	l = url.split('/')[1:]
	if l[0] != '':
		path.append(l[1])
		if l[2]:
			path.append(l[2])
	return path

def getQuestions(url):
	print(url)
	path = getPath(url)
	print(path)
	temp = root
	for next in path:
		if temp.children:
			temp = temp.children[next]
		else:
			break
	

class Node:
	def __init__(self,catergory,children):
		self.catergory = catergory
		self.children = children
	
	def add_children(self,children):
		for child in children:
			self.children[child] = children[child]

root = Node('root',{})

stocks = Node('stocks',{})
fd = Node('fd',{})
mutual_funds = Node('mutual-funds',{})
gold = Node('mutual-funds',{})
profile = Node('profile',{})
orders = Node('profile',{})

root.children['stocks'] = stocks
root.children['fd'] = fd
root.children['mutual-funds'] = mutual_funds
root.children['gold'] = gold
root.children['profile'] = profile
root.children['orders'] = orders


