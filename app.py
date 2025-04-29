import os
import json
import base64
import io
import csv
import tempfile
import time
from datetime import datetime
from dotenv import load_dotenv
import PyPDF2
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Configure Google Generative AI
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    print("WARNING: GOOGLE_API_KEY environment variable is not set")

try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    print(f"Error configuring Google Generative AI: {str(e)}")

# Default model to use throughout the application - use the full name format with version
DEFAULT_MODEL = "gemini-2.5-flash"

# Default prompt to use if none is provided
DEFAULT_PROMPT = """You are creating a \"whitesheet\" for a job based on the source file. 
Extract all relevant information and respond using EXACTLY the following format without any deviations except for making the spacing professional and visually appealing:

JOB INFORMATION SHEET

Sales Engineer:

Date White Sheet turned in:

Plans dated:

Job Name:

GC Name / Phone Number:

Email Address:

Customer Address:

Job Site Address:

Start Date:

Total Number Of Units:

Type of structure:      Garden  or    Wrap

Is this a HUD or OCIP job:       Yes or No

Copy of Estimate Take Off in file:        Yes or No

Copy Of Equipment Price List Used:        Yes or No

VE Options: Boots and grills are stock sizes: 10x4, 10x6, 12x6, 14x6, 16x8.





APARTMENTS EQUIPMENT SCHEDULE


Manufacturer:                  Number of Units:

Heat Pump:                             A/C:

Heat Pump Model #

A/C make & model #:

Apartment AH make & model #:

KW  Model #:

SEER Rating:

Copper Lineset Insulation:    Size:               ETC:

Apts bath fan make and model #:

Wall mount:                Ceiling mount with RD:

Kitchen fan make & model #:

Wall mount:                Ceiling mount with RD:

Fresh air:    Duct Size:            Insulation:

Radiation damper:      Yes or No

Fresh air fan make and model #:

Motorized damper make & model #:

Dryer pipe gauge:    26 gauge

Fire wrap required:

Thermostat make & model #:

Wall cap manufacturer:

Size:            Color White or Brown:

Quick Flash required (Y/N):

Drain: CPVC / PVC:            Insulation:

Supply Register size:    10x4, 10x6, 12x6, 14x6, 16x8.

Return Grille size:    Per drawings

Transfer grille size:    Per drawings

Laundry room transfer grille size:    Per drawings

Conderser on:    Plastic:         Concrete:         Racks:         Cones:

    Vibration pads:             Size:        Hurricane clips:

Roof racks manufacturer:


COMMON AREAS


A/H make & model #:


H/P make & model #:


A/C make & model #:


RTU make & model #:                        Voltage:

100% OAU make & model #:                        Voltage:

Metal:                  Duct board & flex:

Bath fan make & model #:

Smoke Detector:

Fresh air:        Size:            CRD:         Insulation:


Wall Louvers (Y/N):

Common fans:                   Voltage:

Garage fans make & model #:               Voltage:

VFD (Y/N):         Quantity:

CO2/NO2 (Y/N):         Quantity:

Control panels (Y/N):         Quantity:

Strob required (Y/N):         Quantity:

Stairwell pressurization
fans make & model #:              Voltage:

EUH make & model #:

    Phase:            Voltage:                KW:

Wall mounted heaters make & model #:

    Phase:            Voltage:                KW:

Mini Split make & model #:
"""

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Reduce to 5MB max upload size
app.config['UPLOAD_FOLDER'] = '/tmp'  # Use /tmp directory on Render

# Error handling for production
@app.errorhandler(500)
def server_error(e):
    return jsonify({
        'success': False,
        'error': 'Internal Server Error',
        'details': str(e)
    }), 500

# Memory optimization for Render
processing_history = []
MAX_HISTORY_SIZE = 10  # Limit history size to prevent memory growth

def add_to_history(file_name, file_type, prompt, result, success, error):
    global processing_history
    entry = {
        'timestamp': datetime.now().isoformat(),
        'file_name': file_name,
        'file_type': file_type,
        'prompt': prompt,
        'result': result,
        'success': success,
        'error': error
    }
    processing_history.insert(0, entry)
    if len(processing_history) > MAX_HISTORY_SIZE:
        processing_history.pop()

def process_pdf(file_content, prompt):
    # Process a PDF file and extract content using the Gemini API.
    # ... (rest of function unchanged) ...
    pass

def process_csv(file_content, prompt):
    # Process a CSV file and extract content using the Gemini API.
    # ... (rest of function unchanged) ...
    pass

def extract_content_from_file(file):
    # Extract content from a file with memory optimization.
    # ... (rest of function unchanged) ...
    pass

@app.route('/')
def index():
    # Render the main page.
    # ... (rest of function unchanged) ...
    pass

@app.route('/static/<path:path>')
def serve_static(path):
    # Serve static files.
    # ... (rest of function unchanged) ...
    pass

@app.route('/process-file', methods=['POST'])
def process_file():
    # Process the uploaded file using Gemini API.
    # ... (rest of function unchanged) ...
    pass

@app.route('/api-status')
def api_status():
    # Check if the API key is configured and valid.
    # ... (rest of function unchanged) ...
    pass

@app.route('/history')
def get_history():
    """Get the processing history."""
    return jsonify(processing_history)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """Clear the processing history."""
    global processing_history
    processing_history = []
    return jsonify({'success': True})

@app.route('/process-multiple', methods=['POST'])
def process_multiple_files():
    try:
        if 'files[]' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No files provided',
                'details': 'Please upload at least one file'
            }), 400
            
        files = request.files.getlist('files[]')
        
        if not files or len(files) == 0:
            return jsonify({
                'success': False,
                'error': 'No files provided',
                'details': 'Please upload at least one file'
            }), 400
            
        # Process each file
        all_content = ""
        filenames = []
        
        # ... (rest of function unchanged) ...
        pass
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error processing multiple files: {str(e)}'
        }), 500

def diagnostics():
    # Endpoint to check API configuration and available models.
    # ... (rest of function unchanged) ...
    pass

if __name__ == '__main__':
    # Use PORT environment variable if available (for Render deployment)
    port = int(os.environ.get('PORT', 5070))
    app.run(host='0.0.0.0', debug=False, port=port)
