# Random Debit/Credit Card Generator

A Python GUI application that generates random debit/credit card details for testing or educational purposes. The application creates theoretically valid card numbers (using the Luhn algorithm), fetches random cardholder names and zip codes from APIs, and displays the results in a copiable text area. It can be packaged as a standalone executable (`.exe`) for Windows using PyInstaller.

## Features
- Generates random card details for Visa, Mastercard, American Express, or Discover.
- Includes cardholder name, card number, CVV, expiration date (2025–2027), and zip code.
- Fetches names from Random User API and zip codes from Random Data API, with fallbacks for offline use.
- Displays details in a selectable text area with a "Copy to Clipboard" button.
- Clean, comment-free codebase following PEP 8 standards.
- Can be built as a standalone `.exe` for easy distribution.

## Prerequisites
- Python 3.6 or higher
- Internet connection (optional, for API calls; fallbacks provided)
- Windows operating system (for running the `.exe`)

## Installation
1. Clone or download the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `random_card_generator.py`, `requirements.txt`, and this `README.md` are in the same directory.

## Building the Executable
To create a standalone `.exe` file:
1. Ensure PyInstaller is installed (included in `requirements.txt`).
2. Run the following command in the project directory:
   ```bash
   pyinstaller --onefile --noconsole random_card_generator.py
   ```
3. The executable will be created in the `dist` folder as `random_card_generator.exe`.

**Notes**:
- The `--onefile` flag creates a single `.exe` file.
- The `--noconsole` flag prevents a console window from appearing (suitable for GUI apps).
- The resulting `.exe` is approximately 10–15 MB and includes all dependencies.

## Usage
### Running the Python Script
1. Run the application:
   ```bash
   python random_card_generator.py
   ```
2. Click "Generate Card" to create new card details.
3. Select text to copy manually (Ctrl+C) or click "Copy to Clipboard" to copy all details.
4. Paste the copied text (Ctrl+V) elsewhere as needed.

### Running the Executable
1. Navigate to the `dist` folder.
2. Double-click `random_card_generator.exe` to launch the GUI.
3. Use the application as described above.

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
- The `.exe` is Windows-specific. For other platforms, use the Python script or adapt the PyInstaller command (e.g., remove `--noconsole` for macOS/Linux).

## Dependencies
Listed in `requirements.txt`:
- `requests`: For API calls to fetch names and zip codes.
- `pyinstaller`: For building the standalone executable.

## License
This project is for educational purposes only. No license is provided for production use.

## Disclaimer
Use this tool responsibly. The author is not liable for misuse of generated data.