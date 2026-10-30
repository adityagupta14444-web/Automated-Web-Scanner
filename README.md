# Automated Web Scanner

## Project overview
A beginner-friendly Python tool that observes basic HTTPS and HTTP response security-header configuration for a website you own or have explicit permission to assess.

## Features
- Shows HTTP response status and final URL
- Reports whether the final URL uses HTTPS
- Observes selected security headers
- Shows a limited CORS header observation
- Displays basic notes and limitations

## Technology
- Python
- Requests library

## Setup (Windows)
1. Install Python 3.
2. Open Command Prompt in this project folder.
3. Install dependencies:
   `py -m pip install -r requirements.txt`
4. Run:
   `py Automated_Web_Scanner.py`
5. Enter a URL for a site you own or have permission to assess.
6. Confirm authorization when prompted.

## Files
- `Automated_Web_Scanner.py` — source code
- `requirements.txt` — dependency list
- `Project_Report.docx` — project report

## Important limitations and responsible use
This is a lightweight configuration checker, not a full security audit or penetration-testing tool. It makes an ordinary web request and checks visible response headers. A missing header or CORS observation does not automatically prove a vulnerability. It does not test authentication, hidden endpoints, or exploit weaknesses. Use only on websites you own or have explicit permission to assess.
