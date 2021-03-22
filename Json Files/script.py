import json
from html2text import html2text

final = {}
files = ['account','fd','gold','mutual-funds','stocks']
for file in files:
	with open(file+'.json','r') as f:
		d = json.load(f)
	data = {}
	for key in d:
		values = d[key]
		for item in values:
			question = item['questionTitle']
			if item['answerHtml']:
				answer = html2text(item['answerHtml']).strip()
			else:
				answer = item['answerText']
			if question and answer:
				data[question] = answer
	final[file] = data

res = json.dumps(final, indent=4)
with open('final.json','w') as f:
	f.write(res)