# Parse OLX
## Description
A project that parses data from olx and writes to Google sheet.

## Setup
```
git clone https://github.com/AVyha/parse_olx.git
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Then you need to create a service account, upload your credentials, and create your sheet.
```
python write_to_sheet.py
python parse.py
```
