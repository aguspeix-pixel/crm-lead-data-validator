# Automated CRM & B2B Lead Data Validator

Automated Python & SQLite data hygiene pipeline that cleans, standardizes, deduplicates, and validates B2B lead lists before CRM ingestion (HubSpot, Salesforce, Mailchimp).

## Business Problem Solved
Sales and marketing teams waste budget and hurt email deliverability when importing messy spreadsheets containing invalid emails, malformed phone numbers, and duplicate contacts. This tool automates data validation, isolates bad records for review, and exports a clean CRM-ready workbook.

## Key Features
* **Regex Email & Phone Validation:** Filters out malformed email addresses and normalizes phone numbers to clean numeric strings.
* **Smart Deduplication (`pandas`):** Standardizes casing/whitespace and removes duplicate contacts based on unique email addresses.
* **Audit Trail Separation:** Splits records into `Leads_Validos` (CRM-ready) and `Registros_Rechazados` (for manual review).
* **SQL Storage & Analytics (`SQLite3`):** Stores qualified leads in a relational database and aggregates lead volume by acquisition channel.

## Tech Stack
* **Python 3**
* **pandas** (Data cleaning, deduplication & transformation)
* **Regular Expressions (`re`)** (Email syntax & phone digit validation)
* **SQLite3** (Relational database & SQL reporting)
* **openpyxl** (Automated multi-sheet Excel export)

## How to Run
1. Install dependencies: `pip install pandas openpyxl`
2. Generate sample dirty leads: `python generar_leads_prueba.py`
3. Run the validator: `python validador_leads.py`