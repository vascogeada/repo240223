# app.py - the Flask app
from google.cloud import storage
import os

from flask import Flask, request, jsonify, render_template

# v03 - no longer using the private key, because it is sensitive info being uploaded to the GAE
# Set up the path to your service account credentials file
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./mine-prj-240307-97dbe2e68b14.json"


# Create an instance of the Google Cloud Storage client
storage_client = storage.Client()

# Your Google Cloud Storage bucket name
BUCKET_NAME = 'your-bucket-name-here'

app = Flask(__name__)

VALUE_OF_THE_NAME_ATTRIBUTE_OF_THE_INPUT_FILE_ELEMENT_IN_THE_HTML = "post_file" # corresponds to the name of the file input, in the HTML

@app.route("/", methods=['POST', 'GET'])
def serve_root():
    return render_template("gui_for_file_uploading.html")
# serve_root

# upload_file means to receive the file, server side
@app.route('/upload', methods=['POST'])
def upload_file():
    b_check:bool = request and request.files and VALUE_OF_THE_NAME_ATTRIBUTE_OF_THE_INPUT_FILE_ELEMENT_IN_THE_HTML in request.files.keys()
    # file is of type FileStorage and has attributes: content_length, content_type, filename, mimetype, name, etc.
    if(b_check):
        file = request.files[VALUE_OF_THE_NAME_ATTRIBUTE_OF_THE_INPUT_FILE_ELEMENT_IN_THE_HTML]
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

        if file:
            # Prepare the file for upload
            the_blob = storage_client.bucket(BUCKET_NAME).blob(file.filename)

            # Upload the file to Google Cloud Storage
            the_blob.upload_from_string(
                file.read(),
                content_type=file.content_type
            )

            dict_response = {
                'message': 'File uploaded successfully',
                'filename': file.filename
            }
            return jsonify(dict_response), 200
    # if
# def upload_file

if __name__ == '__main__':
    app.run(debug=True)

# app.py ends