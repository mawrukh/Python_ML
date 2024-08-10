from flask import Flask, request, jsonify
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn import __version__ as sklearn_version
from collections import Counter
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the saved model, vectorizer, and MultiLabelBinarizer
try:
    with open(r'*link to the model file generated using pickle*', 'rb') as f:
        model_data = pickle.load(f)
        nearest_neighbors = model_data['nearest_neighbors']
        vectorizer = model_data['vectorizer']
        mlb = model_data['mlb']
        index_to_moods = model_data['index_to_moods']
        saved_sklearn_version = model_data['sklearn_version']

    # # Check if the loaded scikit-learn version matches the current version
    # if sklearn_version != saved_sklearn_version:
    #     raise ValueError(f"The saved model was created with scikit-learn version {saved_sklearn_version}, but the current version is {sklearn_version}. This may cause compatibility issues.")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise

@app.route('/predict', methods=['POST'])
def predict_mood():
    try:
        if 'lyrics' not in request.json:
            return jsonify({'error': 'No lyrics provided'}), 400
        
        lyrics = request.json['lyrics']
        lyrics_vectorized = vectorizer.transform([lyrics])
        distances, indices = nearest_neighbors.kneighbors(lyrics_vectorized)
        
        # Get the moods of the 10 nearest neighbors
        neighbor_moods = [index_to_moods[index] for index in indices[0]]
        
        # Count the frequency of each mood
        mood_counts = Counter(sum(neighbor_moods, []))
        
        # Select the top 3 most common moods
        predicted_moods = [mood for mood, count in mood_counts.most_common(3)]
        
        # Return the moods as a list
        return jsonify({'predictedMoods': predicted_moods})
    except Exception as e:
        logger.error(f"Error in predict_mood: {str(e)}")
        return jsonify({'error': 'An error occurred during mood prediction.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
