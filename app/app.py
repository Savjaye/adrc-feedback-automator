from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)
FDBK_LETTER_FOLDER = os.path.abspath('../data/feedback_letters')
I_C_FOLDER = os.path.abspath('../data/int_and_conclusions')

@app.route('upload', methods=['POST'])
def 