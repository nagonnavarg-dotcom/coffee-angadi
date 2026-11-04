# COFFEE ಅಂಗಡಿ

A one-page café website built with Python and Flask.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. (Optional but recommended) Create and activate a virtual environment:

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:
   ```powershell
   py -m pip install -r requirements.txt
   ```

5. Start the website:
   ```powershell
   py app.py
   ```

6. Open http://127.0.0.1:5000 in your browser.

## Before publishing

Replace these sample placeholders in `templates/index.html`:
- `[Owner Name]`
- `[Your café address]`
- `[Your phone number]`
- `[Your opening hours]`
- `[Instagram URL]`

Update the WhatsApp link (`https://wa.me/`) with your full country code and number, digits only. Confirm the sample menu prices and image choices. The photos and Google Fonts are loaded from external services, so an internet connection is required for them to appear.

## Project structure

```text
coffee-angadi/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```
