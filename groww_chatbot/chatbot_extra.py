from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import json

data = json.loads(open("C:\\Users\\Pranjal\\Desktop\\Crio_Last\\GROWW-T8\\groww_chatbot\\chatbot\\mutualfund.json","r").read())
train = []
"""
Part5(mutualfund.json)
"""
for i in ["External Funds","Groww Funds"]:
    for row in data[i]:
        if row['answerHtml'] == None or row['answerHtml'] == "":
            print(row['questionTitle'])    
            print(row['answerText'])
            train.append(str(row['questionTitle']))
            train.append(str(row['answerText']))
        else:
            print(row['questionTitle'])    
            print(row["answerHtml"])
            train.append(str(row['questionTitle']))
            train.append(str(row['answerText']))

"""
Part4(Stock)
for i in ["Holdings","Intraday Positions","Delivery Positions"]:
    for row in data[i]:
        if row['answerHtml'] == None or row['answerHtml'] == "":
            print(row['questionTitle'])    
            print(row['answerText'])
        else:
            print(row['questionTitle'])    
            print(row["answerHtml"])
    
"""
"""
Part-3
GOld

for i in ["Buy Order","Getting Started"]:
    for row in data[i]:
        if row['answerHtml'] == None or row['answerHtml'] == "":
            print(row['questionTitle'])    
            print(row['answerText'])
        else:
            print(row['questionTitle'])    
            print(row["answerHtml"])
"""
"""
Part-2(account.json)
for row in data["DEFAULT"]:
    if row['answerHtml'] == None or row['answerHtml'] == "":
        print(row['questionTitle'])    
        print(row['answerText'])
    else:
        print(row['questionTitle'])    
        print(row["answerHtml"])

"""
"""
# Part-1(fd.json)
for i in ["Getting Started","About","Eligibility"]:
    for row in data[i]:
        if row['answerHtml'] == None:
            print(row['questionTitle'])    
            print(row['answerText'])
        else:
            print(row['questionTitle'])    
            print(row["answerHtml"])
    # print(row['questionTitle'])
    # print(row['answerText'])
    train.append(row['questionTitle'])
    train.append(row['answerText'])
"""
chatterbot = ChatBot("Groww")
trainer = ListTrainer(chatterbot)
trainer.train(train)
