const fileInput = document.getElementById('fileInput');
const fileList = document.getElementById('fileList');
const uploadButton = document.getElementById('uploadButton');
let selectedFiles = [];

// Handle file selection
fileInput.addEventListener('change', () => {
    const files = Array.from(fileInput.files);
    selectedFiles = [...selectedFiles, ...files];
    updateFileList();
});

// Update the file list displayed on the page
function updateFileList() {
    fileList.innerHTML = '';
    selectedFiles.forEach((file, index) => {
        const li = document.createElement('li');

        const fileName = document.createElement('span');
        fileName.textContent = file.name;

        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.addEventListener('click', () => {
            selectedFiles.splice(index, 1);
            updateFileList();
        });

        li.appendChild(fileName);
        li.appendChild(removeButton);
        fileList.appendChild(li);
    });
}

// Handle file upload and display the download link for the merged PDF
uploadButton.addEventListener('click', async () => {
    if (selectedFiles.length === 0) {
        alert('Please select at least one file.');
        return;
    }

    const formData = new FormData();
    selectedFiles.forEach(file => {
        formData.append('files', file);
    });

    try {
        const response = await fetch('http://127.0.0.1:5000/api/upload', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();
            const downloadUrl = result.download_url;

            // Display the download link
            const downloadLink = document.createElement('a');
            downloadLink.href = downloadUrl;
            downloadLink.textContent = 'Download Merged PDF';
            downloadLink.target = '_blank';
            downloadLink.classList.add('download-button'); // Add a class for styling
            document.body.appendChild(downloadLink);

            // alert('Files uploaded and merged successfully!');
            selectedFiles = [];
            updateFileList();
        } else {
            const error = await response.json();
            // alert(`Failed to upload files: ${error.error}`);
        }
    } catch (error) {
        console.error('Error uploading files:', error);
        alert('An error occurred while uploading files.');
    }
});