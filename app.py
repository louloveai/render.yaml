from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'AI Health API is running!'

@app.route('/api/chat', methods=['POST'])
def chat():
    return {"message": "Chat endpoint ready"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
