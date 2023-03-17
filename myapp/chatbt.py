from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
#chatbot = ChatBot('codeaj')
#replace with blow

chatbt = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 
conversation={
    'hi':'hello',
    'how are you':'i am good',
}

# Training with Personal Ques & Ans 
trainer = ListTrainer(chatbt)
trainer.train(conversation)


#replace this with this below
# training_data_quesans = open('../training_data/ques_ans.txt', encoding="utf8").read().splitlines()
# training_data_personal = open('../training_data/personal_ques.txt', encoding="utf8").read().splitlines()
# training_data = training_data_quesans + training_data_personal

# trainer = ListTrainer(chatbt)
# trainer.train(training_data)


# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbt)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 

# while True:
#     msgin = input("your message : ")
#     msgout=chatbot.get_response(msgin)
#     print(msgout)
#     if msgin == "0":
#         exit()