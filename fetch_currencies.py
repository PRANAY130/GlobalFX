import requests
from datetime import datetime, timezone
import os

# Replace this with your actual API key
API_KEY = '0c4c3b79cfbe0c999078173780092644'

# API endpoint to fetch exchange rates (with the access key)
API_URL = f"http://api.exchangerate.host/live?access_key={API_KEY}&base=INR"

# Mapping of currency codes to country names
CURRENCY_TO_COUNTRY = {
    "AED": "United Arab Emirates",
    "AFN": "Afghanistan",
    "ALL": "Albania",
    "AMD": "Armenia",
    "ANG": "Netherlands Antilles",
    "AOA": "Angola",
    "ARS": "Argentina",
    "AUD": "Australia",
    "AWG": "Aruba",
    "AZN": "Azerbaijan",
    "BAM": "Bosnia and Herzegovina",
    "BBD": "Barbados",
    "BDT": "Bangladesh",
    "BGN": "Bulgaria",
    "BHD": "Bahrain",
    "BIF": "Burundi",
    "BMD": "Bermuda",
    "BND": "Brunei",
    "BOB": "Bolivia",
    "BRL": "Brazil",
    "BSD": "Bahamas",
    "BTC": "Bitcoin",
    "BTN": "Bhutan",
    "BWP": "Botswana",
    "BYN": "Belarus",
    "BYR": "Belarus (Old Currency)",
    "BZD": "Belize",
    "CAD": "Canada",
    "CDF": "Democratic Republic of the Congo",
    "CHF": "Switzerland",
    "CLF": "Chile",
    "CLP": "Chile",
    "CNH": "China (Offshore Yuan)",
    "CNY": "China",
    "COP": "Colombia",
    "CRC": "Costa Rica",
    "CUC": "Cuba (Convertible Peso)",
    "CUP": "Cuba",
    "CVE": "Cape Verde",
    "CZK": "Czech Republic",
    "DJF": "Djibouti",
    "DKK": "Denmark",
    "DOP": "Dominican Republic",
    "DZD": "Algeria",
    "EGP": "Egypt",
    "ERN": "Eritrea",
    "ETB": "Ethiopia",
    "EUR": "European Union",
    "FJD": "Fiji",
    "FKP": "Falkland Islands",
    "GBP": "United Kingdom",
    "GEL": "Georgia",
    "GGP": "Guernsey",
    "GHS": "Ghana",
    "GIP": "Gibraltar",
    "GMD": "Gambia",
    "GNF": "Guinea",
    "GTQ": "Guatemala",
    "GYD": "Guyana",
    "HKD": "Hong Kong",
    "HNL": "Honduras",
    "HRK": "Croatia",
    "HTG": "Haiti",
    "HUF": "Hungary",
    "IDR": "Indonesia",
    "ILS": "Israel",
    "IMP": "Isle of Man",
    "INR": "India",
    "IQD": "Iraq",
    "IRR": "Iran",
    "ISK": "Iceland",
    "JEP": "Jersey",
    "JMD": "Jamaica",
    "JOD": "Jordan",
    "JPY": "Japan",
    "KES": "Kenya",
    "KGS": "Kyrgyzstan",
    "KHR": "Cambodia",
    "KMF": "Comoros",
    "KPW": "North Korea",
    "KRW": "South Korea",
    "KWD": "Kuwait",
    "KYD": "Cayman Islands",
    "KZT": "Kazakhstan",
    "LAK": "Laos",
    "LBP": "Lebanon",
    "LKR": "Sri Lanka",
    "LRD": "Liberia",
    "LSL": "Lesotho",
    "LTL": "Lithuania",
    "LVL": "Latvia",
    "LYD": "Libya",
    "MAD": "Morocco",
    "MDL": "Moldova",
    "MGA": "Madagascar",
    "MKD": "North Macedonia",
    "MMK": "Myanmar (Burma)",
    "MNT": "Mongolia",
    "MOP": "Macau",
    "MRU": "Mauritania",
    "MUR": "Mauritius",
    "MVR": "Maldives",
    "MWK": "Malawi",
    "MXN": "Mexico",
    "MYR": "Malaysia",
    "MZN": "Mozambique",
    "NAD": "Namibia",
    "NGN": "Nigeria",
    "NIO": "Nicaragua",
    "NOK": "Norway",
    "NPR": "Nepal",
    "NZD": "New Zealand",
    "OMR": "Oman",
    "PAB": "Panama",
    "PEN": "Peru",
    "PGK": "Papua New Guinea",
    "PHP": "Philippines",
    "PKR": "Pakistan",
    "PLN": "Poland",
    "PYG": "Paraguay",
    "QAR": "Qatar",
    "RON": "Romania",
    "RSD": "Serbia",
    "RUB": "Russia",
    "RWF": "Rwanda",
    "SAR": "Saudi Arabia",
    "SBD": "Solomon Islands",
    "SCR": "Seychelles",
    "SDG": "Sudan",
    "SEK": "Sweden",
    "SGD": "Singapore",
    "SHP": "Saint Helena",
    "SLE": "Sierra Leone",
    "SLL": "Sierra Leone (Old Currency)",
    "SOS": "Somalia",
    "SRD": "Suriname",
    "STD": "São Tomé and Príncipe",
    "SVC": "El Salvador",
    "SYP": "Syria",
    "SZL": "Swaziland",
    "THB": "Thailand",
    "TJS": "Tajikistan",
    "TMT": "Turkmenistan",
    "TND": "Tunisia",
    "TOP": "Tonga",
    "TRY": "Turkey",
    "TTD": "Trinidad and Tobago",
    "TWD": "Taiwan",
    "TZS": "Tanzania",
    "UAH": "Ukraine",
    "UGX": "Uganda",
    "USD": "United States",
    "UYU": "Uruguay",
    "UZS": "Uzbekistan",
    "VEF": "Venezuela",
    "VND": "Vietnam",
    "VUV": "Vanuatu",
    "WST": "Samoa",
    "XOF": "West African CFA Franc (XOF)",
    "XPF": "CFP Franc",
    "YER": "Yemen",
    "ZAR": "South Africa",
    "ZMK": "Zambia (Old Currency)",
    "ZMW": "Zambia",
    "ZWL": "Zimbabwe",
}

def fetch_exchange_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes

        data = response.json()
        if 'quotes' in data:  # Check if 'quotes' key exists in the response
            return data['quotes'], data['timestamp']
        else:
            raise ValueError("API response does not contain 'quotes' field.")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Request failed: {e}")
    except ValueError as e:
        raise SystemExit(f"Data error: {e}")
    except Exception as e:
        raise SystemExit(f"Unexpected error: {e}")

def update_data_file(rates, timestamp):
    # Convert timestamp to human-readable format using timezone-aware datetime
    time_stamp_date = datetime.fromtimestamp(timestamp, timezone.utc)
    formatted_date = time_stamp_date.strftime("%Y-%m-%d %H:%M:%S UTC")

    # Prepare data.ts content
    data_content = f"""// Generated on {formatted_date}
// This file contains exchange rates for various currencies relative to INR, along with their corresponding countries.

export interface CurrencyData {{
  code: string;
  country: string;
  rate: number;
}}

export const exchangeRates: CurrencyData[] = [
"""

    for currency, rate in sorted(rates.items()):
        if rate != 0:  # Avoid division by zero
            currency_code = currency[3:]  # Extract 3-letter currency code from quotes like USDINR
            rate_in_inr = rate / 100  # Adjust the rate value
            country = CURRENCY_TO_COUNTRY.get(currency_code, "Unknown Country")
            data_content += f'  {{ code: "{currency_code}", country: "{country}", rate: {rate_in_inr:.4f} }},\n'

    data_content += f"""];

export const lastUpdated = "{formatted_date}";
"""

    # Ensure the directory structure exists
    file_path = os.path.join("src", "data", "currencyData.ts")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write to src\data\currencyData.ts with UTF-8 encoding
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data_content)


def update_json(rates):
    # Convert the rates dictionary to a JSON object
    content = f"""[
"""

    for currency, rate in sorted(rates.items()):
        if rate != 0:  # Avoid division by zero
            currency_code = currency[3:]  # Extract 3-letter currency code from quotes like USDINR
            rate_in_inr = rate / 100  # Adjust the rate value
            country = CURRENCY_TO_COUNTRY.get(currency_code, "Unknown Country")
            content += f'  {{\n\t"code": "{currency_code}",\n\t"country": "{country}",\n\t"rate": {rate_in_inr:.4f}\n}},\n'

    content += f"]"

    file_path = os.path.join("public","currencyData.json")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write to src\data\currencyData.ts with UTF-8 encoding
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    try:
        rates, timestamp = fetch_exchange_rates()
        update_data_file(rates, timestamp)
        update_json(rates)
    except Exception as e:
        print(f"Error: {e}")
