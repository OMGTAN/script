
from chatterbot.trainers import ChatterBotCorpusTrainer
from chater import bot

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.chinese",
)



