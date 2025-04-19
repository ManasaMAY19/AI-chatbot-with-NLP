# AI-chatbot-with-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MANASA.S

*INTERN ID*: CT04WT288

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

# Description of the AI chatbot with NLP 

# Building a Chatbot using NLTK

Build a simple chatbot using the Natural Language Processing Toolkit (NLTK). This chatbot will be capable of answering user queries based on pattern matching and predefined responses.

## Step-by-Step Approach

Here's a complete implementation of a basic chatbot using NLTK:

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

## How This Chatbot Works

1. **Pattern Matching**: The chatbot uses regular expressions to match user input against predefined patterns.
 
3. **Response Generation**: When a pattern matches, the chatbot randomly selects a response from the corresponding list.
   
5. **Text Preprocessing**: The code includes a `preprocess` function that demonstrates how to:

   - Tokenize text into words
     
   - Remove punctuation
     
   - Remove stopwords (common words like "the", "is")
   
   - Lemmatize words (reduce words to their base form)

## Extending the Chatbot

To make this chatbot more advanced, you could:

1. **Add more patterns and responses** to handle a wider range of queries
   
2. **Implement intent classification** using NLTK's classification tools
   
3. **Use the preprocessing function** to better understand user queries
    
4. **Add a knowledge base** for the chatbot to retrieve information from

5. **Implement context tracking** to maintain conversation state

## Suggested Python Packages for Advanced Chatbots

If you want to build more sophisticated chatbots, consider these packages:

- **spaCy**: For more advanced NLP capabilities
  
- **TensorFlow** or **PyTorch**: For implementing neural network-based chatbots
  
- **Rasa**: An open-source framework specifically for building conversational AI

- **ChatterBot**: A machine learning conversational dialog engine
  
- **Transformers**: For implementing state-of-the-art language models like BERT or GPT

This implementation provides a solid foundation that you can build upon to create a more sophisticated chatbot tailored to your specific needs.

*OUTPUT*

![Image](https://github.com/user-attachments/assets/c465a725-0657-4ed1-9ff2-4cc007e33b4a)



