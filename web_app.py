import os
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from app.harder_drive import HarderDrive

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
harder_drive = HarderDrive()

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def store_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        with open(file_path, 'rb') as f:
            content = f.read()
        os.remove(file_path)  # Remove the file after reading
        message, success = harder_drive.store_file(filename, content)
        return jsonify({'message': message, 'success': success})

@app.route('/retrieve', methods=['POST'])
def retrieve_file():
    filename = request.form['filename']
    message, content = harder_drive.retrieve_file(filename)
    if content is None:  # File not found
        return jsonify({'message': message}), 404
    # Create a temporary file to send
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(temp_path, 'wb') as f:
        f.write(content)
    return send_file(temp_path, as_attachment=True, download_name=filename), 200, {
        'X-Harder-Drive-Message': message
    }

@app.route('/converse', methods=['GET'])
def converse():
    message = harder_drive.initiate_conversation()
    return jsonify({'message': message})

@app.route('/list_files', methods=['GET'])
def list_files():
    files = harder_drive.file_handler.list_files()
    return jsonify({'files': files})

if __name__ == '__main__':
    app.run(debug=True)