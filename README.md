# PDF and JPG Merger

PDF and JPG Merger is a web application that allows users to upload multiple PDF and image files (JPG, JPEG, PNG), merge them into a single PDF, and download the merged file. This project is designed to streamline the process of combining PDFs and images for personal or professional use.

Note: This project was primarily generated with the assistance of LLMs and has not been thoroughly reviewed. It is shared on GitHub for further development and contributions."



---

## Features

- Upload multiple PDF and image files.
- Automatically convert image files (JPG, JPEG, PNG) to PDF.
- Merge all uploaded files into a single PDF.
- Download the merged PDF directly from the browser.
- Easy-to-use interface with a responsive design.

---

## Setup

### Using Conda (Recommended)

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/PDF_merger.git
    ```
2. Navigate to the project directory:
    ```bash
    cd PDF_merger
    ```
3. Create a Conda environment:
    ```bash
    conda create -n pdf_merger_env python=3.9 -y
    ```
4. Activate the Conda environment:
    ```bash
    conda activate pdf_merger_env
    ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask server:
    ```bash
    python backend/api.py
    ```

7. Open the `index.html` file in your browser:
    ```bash
    open frontend/index.html  # On Windows: start frontend/index.html
    ```

---

### Using Virtualenv (Alternative)

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/PDF_merger.git
    ```
2. Navigate to the project directory:
    ```bash
    cd PDF_merger
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask server:
    ```bash
    python backend/api.py
    ```

6. Open the `index.html` file in your browser:
    ```bash
    open frontend/index.html  # On Windows: start frontend/index.html
    ```

---

## Usage

1. Select multiple PDF and image files using the "Choose Files" button.
2. Click the "Upload Files" button to upload and merge the files.
3. Once the files are merged, a "Download Merged PDF" button will appear. Click it to download the merged PDF.

---

## Project Structure

```
PDF_merger/
├── backend/
│   ├── api.py               # Flask backend script
│   ├── uploads/             # Folder for uploaded files
│   └── frontend/static/     # Folder for static files (merged PDFs)
├── frontend/
│   ├── index.html           # Main HTML file
│   ├── css/
│   │   └── styles.css       # External CSS file
│   ├── js/
│   │   └── script.js        # External JavaScript file
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

---

## Troubleshooting

### Common Issues

1. **404 Error for Merged PDF**:
   - Ensure the `merged_output.pdf` file is being saved in the `frontend/static` folder.
   - Check the Flask server logs for the file path.

2. **CORS Error**:
   - Ensure `Flask-CORS` is installed and enabled in `api.py`:
     ```python
     from flask_cors import CORS
     CORS(app)
     ```

3. **ModuleNotFoundError**:
   - Install the missing module using `pip`. For example:
     ```bash
     pip install Pillow
     ```

4. **Conda Environment Not Found**:
   - Ensure Conda is installed and properly configured. Use `conda info` to verify your setup.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Thanks to the open-source community for their amazing tools and libraries.