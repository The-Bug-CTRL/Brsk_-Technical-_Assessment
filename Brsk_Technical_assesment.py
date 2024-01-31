# Importing necessary libraries for the program
import random
import spacy
import requests

# Loading the English language model for Natural Language Processing
nlp = spacy.load("en_core_web_md")

# Function to download words from a specified URL
def download_words_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Splitting downloaded words into a list
        return response.text.splitlines()
        
    except requests.exceptions.RequestException as e:
        # Handling download errors
        print(f"Error: Could not download the word list {e}")
        return None

# URL for downloading English words
download_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
# Storing downloaded words from the URL
downloaded_words = download_words_from_url(download_url)

# Checking if word download was successful
if downloaded_words:
    print(f"Successfully downloaded all words from the word URL. {len(downloaded_words)} words available.")
else:
    print("Couldn't download for some reason or another!")
    exit()

# Function to validate if a word is an English word
def validate_words(word):
    # Checking if the word has a vector representation in the language model
    return nlp(word.lower()).has_vector

# Function to rearrange words in a sentence using the downloaded word list
def mix_the_sentence_words(sentence, downloaded_words):
    sentence_list = []
    
    for word in sentence.split():
        # Filtering words of the same length and starting with the same letter
        new_words_for_sentence = [w for w in downloaded_words if len(w) == len(word) and w[0] == word[0] and w != word]

        if new_words_for_sentence:
            # Choosing a random word from the filtered list
            new_word = random.choice(new_words_for_sentence)
            if validate_words(new_word):
                sentence_list.append(new_word)
            else:
                # If the chosen word is not a valid English word, keep the original word
                sentence_list.append(word)
        else:
            # If no valid words found, keep the original word
            sentence_list.append(word)
        
    return ' '.join(sentence_list)

# Displaying the menu
menu = True

# Looping through the menu until a sentence is provided and processed
while menu:
    sentence = input("Please enter your sentence you want to scrabble: ")
    new_sentence = mix_the_sentence_words(sentence, downloaded_words)

    print(f"Your sentence: {sentence}")
    print(f"Your new sentence: {new_sentence}")
    menu = False
