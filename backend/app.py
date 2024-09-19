from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key here (or use environment variables)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return "Welcome to Hassan's World"

@app.route('/api/query', methods=['POST'])
def query_openai():
    data = request.json
    user_query = data.get('query')

    try:
        response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ],
        max_tokens=1000,
        temperature=0.7
    )
        return jsonify({'response': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)