# import json
# import random

# def getPath(url):
# 	path = []
# 	l = url.split('/')[1:]
# 	if l[0] != '':
# 		path.append(l[1])
# 		if l[2]:
# 			path.append(l[2])
# 	return path

# def getQuestions(url):
# 	json_path = '../Json Files/train.json'
# 	print(url)
# 	path = getPath(url)
# 	print(path)
# 	temp = root
# 	for next in path:
# 		if temp.children:
# 			temp = temp.children[next]
# 		else:
# 			break
# 	questions = []
# 	with open(json_path,'r') as f:
# 		data = json.load(f)
# 		l = list(data.get(temp.category,{}).items())
# 		random.shuffle(l)
# 		for question,answer in l[:4]:
# 			questions.append(question)
# 	print(questions)
# 	return questions
	

# class Node:
# 	def __init__(self,catergory,children):
# 		self.category = catergory
# 		self.children = children
	
# 	def add_children(self,children):
# 		for child in children:
# 			self.children[child] = children[child]

# root = Node('root',{})

# stocks = Node('stocks',{})
# fd = Node('fd',{})
# mutual_funds = Node('mutual-funds',{})
# gold = Node('gold',{})
# profile = Node('profile',{})
# orders = Node('orders',{})

# root.children['stocks'] = stocks
# root.children['fd'] = fd
# root.children['mutual-funds'] = mutual_funds
# root.children['gold'] = gold
# root.children['profile'] = profile
# root.children['orders'] = orders


