from flask import Flask, request, jsonify
import os

app = Flask(__name__)
import os

app.config['UPLOAD_FOLDER'] = 'uploads/'  # Ensure this folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):

    os.makedirs(app.config['UPLOAD_FOLDER'])  # Create the uploads directory if it doesn't exist
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Ensure this folder exists

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit to 16 MB

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'profile-photo' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['profile-photo']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return jsonify({'success': 'File uploaded successfully'}), 200
    return jsonify({'error': 'File upload failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
