import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load the dataset and initialize the vectorizer
data = pd.read_csv('normalised_dataset.csv')
# Fill missing values with an empty string
data['description'] = data['description'].fillna('')
database_texts = data['description'].tolist()
database_urls = data['url'].tolist()
vectorizer = TfidfVectorizer()
database_features = vectorizer.fit_transform(database_texts)

@app.route('/', methods=['POST'])
def find_similar_items():
    # Parse the JSON payload
    input_text = request.json['input_text']

    # Transform the input text
    input_feature = vectorizer.transform([input_text])

    # Compute cosine similarity between input text and database texts
    similarity_scores = cosine_similarity(input_feature, database_features)

    # Get the indices of the top-N most similar items
    top_indices = np.argsort(similarity_scores)[0, ::-1][:30]

    # Get the URLs of the top-N most similar items
    top_urls = [database_urls[idx] for idx in top_indices]

    # Create the JSON response
    response = {'similar_items': top_urls}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
