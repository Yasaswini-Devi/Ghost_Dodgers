from flask import Flask, jsonify, render_template
from flask_cors import CORS
import subprocess
import sys

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/run-script', methods = ['POST'])
def run_script():
    try:
        result = subprocess.run([sys.executable, "main.py"], capture_output = True, text = True)
        return jsonify({'output': result.stdout, 'error': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug = True)
