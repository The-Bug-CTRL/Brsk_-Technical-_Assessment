import requests
import random
import spacy

nlp = spacy.load("en_core_web_md")


def download_word_list(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading word list: {e}")
        return None

word_list_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
word_list = download_word_list(word_list_url)

if word_list:
    print(f"Word list downloaded successfully. Total words: {len(word_list)}")
else:
    print("Failed to download the word list. Exiting.")
    exit()


def replace_words(sentence, word_list):
    replaced_sentence = []

    for word in sentence.split():
        replacement_words = [w for w in word_list if len(w) == len(word) and w[0] == word[0] and w != word]

        if replacement_words:
            replaced_sentence.append(random.choice(replacement_words))
        else:
            replaced_sentence.append(word)

    return ' '.join(replaced_sentence)


def main():
    sentence = input("Enter a sentence: ")

    new_sentence = replace_words(sentence, word_list)

    print("Original Sentence:", sentence)
    print("Modified Sentence:", new_sentence)

if __name__ == "__main__":
    main()