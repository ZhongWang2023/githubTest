import nltk
from nltk.chat.util import Chat, reflections

##############################################
## Group Members : Vamshi Reddy & Zhong Wang #
##############################################


# Define patterns and responses for the anime chatbot
patterns = [
    (r'hi|hello|hey|howdy', ['Hello fellow anime enthusiast! What anime are you currently watching?',
                             'Hey there! Ready to talk about some anime?']),
    (r'(.*)(recommend|recommendation|suggest|suggestion)(.*?)',
     ['Sure! What genre or type of anime are you interested in?',
      'Of course! Do you have any specific preferences for the anime you\'re looking for?']),
    (r'(.*)(action|adventure)(.*?)',
     ['You might enjoy "Naruto" or "One piece" or "Demon Slayer" for action-packed adventures!']),
    (r'(.*)(comedy|funny)(.*?)', ['For some laughs, check out "One Punch Man" or "Gintama"!']),
    (r'(.*)(drama|romance)(.*?)',
     ['If you\'re in the mood for romance and drama, "Your Lie in April" or "Clannad" are great choices.']),
    (r'(.*)(thank you|thanks)(.*?)', ['You\'re welcome! Feel free to ask for more recommendations anytime.']),
    (r'(.*)', ['Hmm, I\'m not sure about that. What else would you like to know about anime?'])
]

# Assiging the imported packages to Patterns
## this is the main logic of the chatbot
def anime_chatbot():
    print("Anime Chatbot: Hello! I'm your anime assistant. What anime are you currently watching?")
    chatbot = Chat(patterns, reflections)
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Anime Chatbot: Goodbye! Keep enjoying your anime.")
            break
			
	print("#################################")

#Output part.
        response = chatbot.respond(user_input)
        print("Anime Chatbot:", response)

## this is the main road of the programme
####################
if __name__ == "__main__":
    anime_chatbot()





