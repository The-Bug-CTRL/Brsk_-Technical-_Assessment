import random
import spacy
import requests

nlp = spacy.load("en_core_web_md")

def download_words_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
        
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not download the word list {e}")
        return None

download_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
downloaded_words = download_words_from_url(download_url)

if downloaded_words:
    print(f"Successfully downloaded all words from the word URL. {len(downloaded_words)} words available.")
else:
    print("Couldn't download for some reason or another!")
    exit()

def validate_words(word):
    return nlp(word.lower()).has_vector

def mix_the_sentence_words(sentence, downloaded_words):
    sentence_list = []
    
    for word in sentence.split():
        new_words_for_sentence = [w for w in downloaded_words if len(w) == len(word) and w[0] == word[0] and w != word]

        if new_words_for_sentence:
            new_word = random.choice(new_words_for_sentence)
            if validate_words(new_word):
                sentence_list.append(new_word)
            else:
                sentence_list.append(word)
        else:
            sentence_list.append(word)
        
    return ' '.join(sentence_list)

menu = True

while menu:
    sentence = input("Please enter your sentence you want to scrabble: ")
    new_sentence = mix_the_sentence_words(sentence, downloaded_words)

    print(f"Your sentence: {sentence}")
    print(f"Your new sentence: {new_sentence}")
    menu = False
