from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PyPDF2 import PdfMerger
from PIL import Image
import os

app = Flask(__name__, static_folder='frontend/static')  # Serve static files from 'frontend/static'
CORS(app)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'frontend/static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400

    files = request.files.getlist('files')
    if not files:
        return jsonify({'error': 'No files uploaded'}), 400

    saved_files = []
    pdf_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            saved_files.append(filename)

            if filename.lower().endswith(('jpg', 'jpeg', 'png')):
                image = Image.open(file_path)
                pdf_path = file_path.rsplit('.', 1)[0] + '.pdf'
                image.convert('RGB').save(pdf_path)
                pdf_files.append(pdf_path)
            elif filename.lower().endswith('pdf'):
                pdf_files.append(file_path)
        else:
            return jsonify({'error': f'File type not allowed: {file.filename}'}), 400

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merged_pdf_path = os.path.join(STATIC_FOLDER, 'merged_output.pdf')
    merger.write(merged_pdf_path)
    merger.close()

    print(f"Merged PDF saved at: {merged_pdf_path}")  # Debugging log

    download_url = url_for('static', filename='merged_output.pdf', _external=True)
    print(f"Download URL: {download_url}")  # Debugging log

    return jsonify({'message': 'Files uploaded and merged successfully', 'download_url': download_url}), 200

if __name__ == '__main__':
    app.run(debug=True)