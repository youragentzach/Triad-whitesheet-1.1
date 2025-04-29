# Triad Whitesheet 1.1

Gemini File Extractor (Triad Whitesheet) - Flask app for extracting HVAC job information sheets using Gemini AI.

## Features
- Gemini 2.5 Flash model integration
- Strict, professional whitesheet format for HVAC jobs
- Error handling: no sample data fallbacks, always show actual error states
- Designed for Render.com deployment (uses gunicorn, proper port/host config)
- Environment variable for GOOGLE_API_KEY
- Memory optimization for cloud deployment

## Deployment
1. Set `GOOGLE_API_KEY` in your environment (e.g., in Render.com dashboard)
2. Install requirements: `pip install -r requirements.txt`
3. Run locally: `python app.py`
4. For production, use gunicorn: `gunicorn app:app`

## Whitesheet Output Format
The output format is strictly enforced for HVAC job information sheets. See `app.py` for the template details.

---
