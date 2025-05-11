import tkinter as tk
import random
import requests
from datetime import datetime

CARD_TYPES = {
    "Visa": ["4"],
    "Mastercard": ["51", "52", "53", "54", "55"],
    "American Express": ["34", "37"],
    "Discover": ["6011"]
}

CARD_LENGTHS = {
    "Visa": 16,
    "Mastercard": 16,
    "American Express": 15,
    "Discover": 16
}

FALLBACK_NAMES = [
    "John Doe", "Jane Smith", "Alex Johnson", "Emily Brown", "Michael Chen"
]

FALLBACK_ZIP_CODES = [
    "90210", "10001", "60601", "94105", "33101"
]

def luhn_checksum(card_number):
    digits = [int(d) for d in card_number]
    checksum = 0
    is_even = False
    for digit in digits[::-1]:
        if is_even:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
        is_even = not is_even
    return checksum % 10 == 0

def generate_card_number(card_type):
    length = CARD_LENGTHS[card_type]
    prefix = random.choice(CARD_TYPES[card_type])
    card_number = list(prefix)
    while len(card_number) < length - 1:
        card_number.append(str(random.randint(0, 9)))
    temp_number = card_number + ['0']
    while not luhn_checksum(''.join(temp_number)):
        check_digit = random.randint(0, 9)
        temp_number[-1] = str(check_digit)
    return ''.join(temp_number)

def get_random_name():
    try:
        response = requests.get('https://randomuser.me/api/', timeout=5)
        response.raise_for_status()
        data = response.json()
        name = data['results'][0]['name']
        return f"{name['first']} {name['last']}"
    except Exception:
        return random.choice(FALLBACK_NAMES)

def get_random_zip():
    try:
        response = requests.get('https://random-data-api.com/api/address/random_address', timeout=5)
        response.raise_for_status()
        return response.json()['zip_code']
    except Exception:
        return random.choice(FALLBACK_ZIP_CODES)

def generate_card():
    card_type = random.choice(list(CARD_TYPES.keys()))
    card_number = generate_card_number(card_type)
    cvv = str(random.randint(100, 999)) if card_type != "American Express" else str(random.randint(1000, 9999))
    expiry_month = str(random.randint(1, 12)).zfill(2)
    expiry_year = str(random.choice([2025, 2026, 2027]))
    cardholder_name = get_random_name()
    zip_code = get_random_zip()
    if card_type == "American Express":
        formatted_number = f"{card_number[:4]} {card_number[4:10]} {card_number[10:]}"
    else:
        formatted_number = ' '.join(card_number[i:i+4] for i in range(0, len(card_number), 4))
    card_text.delete("1.0", tk.END)
    card_details = f"Name: {cardholder_name}\n{card_type}\n{formatted_number}\nCVV: {cvv}\nExp: {expiry_month}/{expiry_year}\nZip: {zip_code}"
    card_text.insert(tk.END, card_details)
    copy_button.config(command=lambda: root.clipboard_clear() or root.clipboard_append(card_text.get("1.0", tk.END).strip()))

root = tk.Tk()
root.title("Random Debit/Credit Card Generator")
root.geometry("400x380")

generate_button = tk.Button(root, text="Generate Card", command=generate_card, font=("Arial", 12))
generate_button.pack(pady=10)

card_text = tk.Text(root, height=6, width=30, font=("Arial", 14), wrap=tk.WORD)
card_text.insert(tk.END, "Click the button to generate a card!")
card_text.config(state=tk.NORMAL)
card_text.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: None, font=("Arial", 12))
copy_button.pack(pady=10)

root.mainloop()