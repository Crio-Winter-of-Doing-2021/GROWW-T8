# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
# import json

# data = json.loads(open("fd.json","r").read())
# train = []
# for row in data["Getting Started"]:
#     print(row['questionTitle'])
#     print(row['answerText'])
#     train.append(row['questionTitle'])
#     train.append(row['answerText'])

# chatbot = ChatBot("QA")
# trainer = ListTrainer(chatbot)
# trainer.train(train)

# while True:
#     request = input("You: ")
#     response = chatbot.get_response(request)
#     print("Bot: ", response)

