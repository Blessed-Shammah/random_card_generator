# Random Debit/Credit Card Generator

A Python GUI application that generates random debit/credit card details for testing or educational purposes. The application creates theoretically valid card numbers (using the Luhn algorithm), fetches random cardholder names and zip codes from APIs, and displays the results in a copiable text area.

## Features
- Generates random card details for Visa, Mastercard, American Express, or Discover.
- Includes cardholder name, card number, CVV, expiration date (2025–2027), and zip code.
- Fetches names from Random User API and zip codes from Random Data API, with fallbacks for offline use.
- Displays details in a selectable text area with a "Copy to Clipboard" button.
- Clean, comment-free codebase following PEP 8 standards.

## Prerequisites
- Python 3.6 or higher
- Internet connection (optional, for API calls; fallbacks provided)

## Installation
1. Clone or download the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `random_card_generator.py`, `requirements.txt`, and this `README.md` are in the same directory.

## Usage
1. Run the application:
   ```bash
   python random_card_generator.py
   ```
2. Click "Generate Card" to create new card details.
3. Select text to copy manually (Ctrl+C) or click "Copy to Clipboard" to copy all details.
4. Paste the copied text (Ctrl+V) elsewhere as needed.

## Example Output
```
Name: Jane Smith
Visa
1234 5678 9012 3456
CVV: 123
Exp: 06/2026
Zip: 90210
```

## Notes
- **For Testing Only**: Generated card numbers are not real and must not be used for actual transactions. Doing so is illegal and unethical.
- APIs (Random User, Random Data) may have rate limits or downtime; fallback names and zip codes ensure functionality.
- The application uses `tkinter` for the GUI, which is included in standard Python installations.

## Dependencies
Listed in `requirements.txt`:
- `requests`: For API calls to fetch names and zip codes.

## License
This project is for educational purposes only. No license is provided for production use.

## Disclaimer
Use this tool responsibly. The author is not liable for misuse of generated data.