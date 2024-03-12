from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot(
    "FoodBot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand your question. Please select your option from previous list',
            'maximum_similarity_threshold': 0.90
        }
    ]
)


a = open('training_data/biriyani.txt').read().splitlines()
b = open('training_data/personal_ques.txt').read().splitlines()
c = open('training_data/burger.txt').read().splitlines()
d = open('training_data/icecream.txt').read().splitlines()
e = open('training_data/juice.txt').read().splitlines()
f = open('training_data/menu.txt').read().splitlines()
g = open('training_data/shakes.txt').read().splitlines()
h = open('training_data/table.txt').read().splitlines()
training_data = a + b + c + d + e + f + g + h

trainer = ListTrainer(chatbot)
trainer.train(training_data)
