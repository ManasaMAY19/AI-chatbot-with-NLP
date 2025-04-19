import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"what is your name",
        ["I'm a chatbot created with NLTK.", "You can call me NLTKBot!"]
    ],
    [
        r"how are you",
        ["I'm doing well, thank you!", "I'm good, how about you?"]
    ],
    [
        r"what can you do",
        ["I can answer simple questions, have a conversation, or help with basic information."]
    ],
    [
        r"(.*) weather (.*)",
        ["I'm sorry, I don't have access to real-time weather data."]
    ],
    [
        r"(.*) (help|assist) (.*)",
        ["I'll do my best to help you. What do you need assistance with?"]
    ],
    [
        r"quit|exit|bye",
        ["Goodbye!", "It was nice talking to you. Bye!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?", 
         "Interesting. Tell me more.",
         "I see. Can you elaborate on that?"]
    ]
]

# Create the chatbot
def create_chatbot():
    print("Hello! I'm your NLTK chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = chat.respond(user_input)
        print("Chatbot:", response)

# Function to preprocess text (for more advanced implementations)
def preprocess(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    
    # Remove punctuation
    tokens = [word for word in tokens if word not in string.punctuation]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

# Run the chatbot
if __name__ == "__main__":
    create_chatbot()
