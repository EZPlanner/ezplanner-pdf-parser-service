from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
from extract import extract_courses_from_transcript


app = Flask(__name__)
CORS(app)

@app.route('/transcript/courses/<string:userId>', methods=['POST'])
def transcript_courses(userId):
    pdf_file = request.files['file']

    courses = extract_courses_from_transcript(userId, pdf_file)

    return jsonify(courses), 200

if __name__ == '__main__':
    serve(app, port=8080)