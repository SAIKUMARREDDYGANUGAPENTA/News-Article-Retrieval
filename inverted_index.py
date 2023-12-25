import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

# Preprocess data with stemming and stop words removal
stop_words = set(stopwords.words('english'))

def preprocess(text):
    # Check for NaN or float values and replace with an empty string
    if pd.isnull(text) or isinstance(text, float):
        text = ''
    else:
        text = str(text)  # Convert non-string values to string
    
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    return ' '.join(words)

# Create a dictionary to store document IDs for each term
inverted_index = {}

# Iterate through each document and build the inverted index
for i in range(1, 100000):
    file_name = f'{str(i)}.txt'
    
    with open(f'output_folder_1/{file_name}', 'r', encoding='utf-8') as file:
        text = file.read()

    doc_id = f'{i}'  # Define a doc_id for each file
    
    preprocessed_text = preprocess(text)
    
    # Tokenize the preprocessed text
    tokens = preprocessed_text.split()
    
    # Update the inverted index for each token
    for token in set(tokens):  # Use set() to remove duplicates
        if token not in inverted_index:
            inverted_index[token] = [doc_id]
        else:
            inverted_index[token].append(doc_id)
    
    # Display message after every 1000 documents
    if i % 1000 == 0:
        print(f"{i} documents processed.")

# Convert lists to sets to remove duplicates in document IDs
inverted_index = {token: sorted(list(set(doc_ids))) for token, doc_ids in inverted_index.items()}

# Sort the keys (terms) alphabetically
sorted_inverted_index = dict(sorted(inverted_index.items()))

# Save the sorted inverted index to a JSON file
with open('inverted__1.json', 'w') as file:
    json.dump(sorted_inverted_index, file)

print("Inverted index created and saved to 'inverted_1.txt'.")
