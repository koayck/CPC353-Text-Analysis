import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

stop_words = set(stopwords.words('english'))

tokenized_texts = []
file_name = []

for txt_file in os.listdir('./txt'):
    file_name.append(txt_file.split('.')[0])

    # tokenize the text inside the text file
    with open(f'./txt/{txt_file}', 'r', encoding="utf-8") as txt:
        text = txt.read()
        tokenized_texts.append(sent_tokenize(text))

# Process the tokenized texts
for idx, tokenized_text in enumerate(tokenized_texts):
    # Get the corresponding file name (from the first loop)
    current_file_name = file_name[idx]
    
    # Create a new file for each original text file
    with open(f'./pos-tagged-txt/{current_file_name}.txt', 'w', encoding="utf-8") as tagged_file:
        for sentence in tokenized_text:
            # Tokenize sentence into words
            wordsList = word_tokenize(sentence)

            # Remove stop words from the word list
            wordsList = [w for w in wordsList if w.lower() not in stop_words]

            # Apply POS tagging
            tagged = nltk.pos_tag(wordsList)

            # Write the tagged sentence to the file
            tagged_file.write(str(tagged) + '\n')  # Each sentence's POS tags in a new line
