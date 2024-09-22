import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!']],
    ['how are you?', ['I am fine, thank you!', 'Doing well!']],
    ['quit', ['Bye!', 'See you!']]
]
chatbot = Chat(pairs, reflections)
chatbot.converse()
