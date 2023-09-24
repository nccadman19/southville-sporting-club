from geopy.geocoders import Nominatim
import requests

# Create a Geolocator instance (requires internet connection)
geolocator = Nominatim(user_agent="bag")

def determine_country_from_postcode(postcode):
    try:
        location = geolocator.geocode(postcode)
        if location:
            # Extract country code (e.g., 'GB' for United Kingdom)
            country_code = location.raw.get("address", {}).get("country_code")
            return country_code
    except Exception as e:
        pass
    return None

country_to_currency = {
    'AF': 'AFN',  # Afghanistan
    'AL': 'ALL',  # Albania
    'DZ': 'DZD',  # Algeria
    'AD': 'EUR',  # Andorra
    'AO': 'AOA',  # Angola
    'AR': 'ARS',  # Argentina
    'AM': 'AMD',  # Armenia
    'AU': 'AUD',  # Australia
    'AT': 'EUR',  # Austria
    'AZ': 'AZN',  # Azerbaijan
    'BS': 'BSD',  # Bahamas
    'BH': 'BHD',  # Bahrain
    'BD': 'BDT',  # Bangladesh
    'BY': 'BYN',  # Belarus
    'BE': 'EUR',  # Belgium
    'BZ': 'BZD',  # Belize
    'BJ': 'XOF',  # Benin
    'BT': 'BTN',  # Bhutan
    'BO': 'BOB',  # Bolivia
    'BA': 'BAM',  # Bosnia and Herzegovina
    'BW': 'BWP',  # Botswana
    'BR': 'BRL',  # Brazil
    'BN': 'BND',  # Brunei
    'BG': 'BGN',  # Bulgaria
    'BF': 'XOF',  # Burkina Faso
    'BI': 'BIF',  # Burundi
    'KH': 'KHR',  # Cambodia
    'CM': 'XAF',  # Cameroon
    'CA': 'CAD',  # Canada
    'CV': 'CVE',  # Cape Verde
    'CF': 'XAF',  # Central African Republic
    'TD': 'XAF',  # Chad
    'CL': 'CLP',  # Chile
    'CN': 'CNY',  # China
    'CO': 'COP',  # Colombia
    'KM': 'KMF',  # Comoros
    'CG': 'XAF',  # Congo (Brazzaville)
    'CD': 'CDF',  # Congo (Kinshasa)
    'CR': 'CRC',  # Costa Rica
    'HR': 'HRK',  # Croatia
    'CU': 'CUP',  # Cuba
    'CY': 'EUR',  # Cyprus
    'CZ': 'CZK',  # Czech Republic
    'DK': 'DKK',  # Denmark
    'DJ': 'DJF',  # Djibouti
    'DO': 'DOP',  # Dominican Republic
    'EC': 'USD',  # Ecuador
    'EG': 'EGP',  # Egypt
    'SV': 'USD',  # El Salvador
    'GQ': 'XAF',  # Equatorial Guinea
    'ER': 'ERN',  # Eritrea
    'EE': 'EUR',  # Estonia
    'ET': 'ETB',  # Ethiopia
    'FJ': 'FJD',  # Fiji
    'FI': 'EUR',  # Finland
    'FR': 'EUR',  # France
    'GA': 'XAF',  # Gabon
    'GM': 'GMD',  # Gambia
    'GE': 'GEL',  # Georgia
    'DE': 'EUR',  # Germany
    'GH': 'GHS',  # Ghana
    'GR': 'EUR',  # Greece
    'GT': 'GTQ',  # Guatemala
    'GN': 'GNF',  # Guinea
    'GW': 'XOF',  # Guinea-Bissau
    'GY': 'GYD',  # Guyana
    'HT': 'HTG',  # Haiti
    'HN': 'HNL',  # Honduras
    'HK': 'HKD',  # Hong Kong SAR
    'HU': 'HUF',  # Hungary
    'IS': 'ISK',  # Iceland
    'IN': 'INR',  # India
    'ID': 'IDR',  # Indonesia
    'IR': 'IRR',  # Iran
    'IQ': 'IQD',  # Iraq
    'IE': 'EUR',  # Ireland
    'IL': 'ILS',  # Israel
    'IT': 'EUR',  # Italy
    'JM': 'JMD',  # Jamaica
    'JP': 'JPY',  # Japan
    'JO': 'JOD',  # Jordan
    'KZ': 'KZT',  # Kazakhstan
    'KE': 'KES',  # Kenya
    'KP': 'KPW',  # North Korea
    'KR': 'KRW',  # South Korea
    'KW': 'KWD',  # Kuwait
    'KG': 'KGS',  # Kyrgyzstan
    'LA': 'LAK',  # Laos
    'LV': 'EUR',  # Latvia
    'LB': 'LBP',  # Lebanon
    'LS': 'LSL',  # Lesotho
    'LR': 'LRD',  # Liberia
    'LY': 'LYD',  # Libya
    'LI': 'CHF',  # Liechtenstein
    'LT': 'EUR',  # Lithuania
    'LU': 'EUR',  # Luxembourg
    'MO': 'MOP',  # Macao SAR
    'MK': 'MKD',  # North Macedonia
    'MG': 'MGA',  # Madagascar
    'MW': 'MWK',  # Malawi
    'MY': 'MYR',  # Malaysia
    'MV': 'MVR',  # Maldives
    'ML': 'XOF',  # Mali
    'MT': 'EUR',  # Malta
    'MH': 'USD',  # Marshall Islands
    'MR': 'MRU',  # Mauritania
    'MU': 'MUR',  # Mauritius
    'MX': 'MXN',  # Mexico
    'MD': 'MDL',  # Moldova
    'MC': 'EUR',  # Monaco
    'MN': 'MNT',  # Mongolia
    'ME': 'EUR',  # Montenegro
    'MA': 'MAD',  # Morocco
    'MZ': 'MZN',  # Mozambique
    'MM': 'MMK',  # Myanmar
    'NA': 'NAD',  # Namibia
    'NP': 'NPR',  # Nepal
    'NL': 'EUR',  # Netherlands
    'NZ': 'NZD',  # New Zealand
    'NI': 'NIO',  # Nicaragua
    'NE': 'XOF',  # Niger
    'NG': 'NGN',  # Nigeria
    'NO': 'NOK',  # Norway
    'OM': 'OMR',  # Oman
    'PK': 'PKR',  # Pakistan
    'PS': 'ILS',  # Palestinian Territories
    'PA': 'PAB',  # Panama
    'PG': 'PGK',  # Papua New Guinea
    'PY': 'PYG',  # Paraguay
    'PE': 'PEN',  # Peru
    'PH': 'PHP',  # Philippines
    'PL': 'PLN',  # Poland
    'PT': 'EUR',  # Portugal
    'QA': 'QAR',  # Qatar
    'RO': 'RON',  # Romania
    'RU': 'RUB',  # Russia
    'RW': 'RWF',  # Rwanda
    'WS': 'WST',  # Samoa
    'SM': 'EUR',  # San Marino
    'SA': 'SAR',  # Saudi Arabia
    'SN': 'XOF',  # Senegal
    'RS': 'RSD',  # Serbia
    'SC': 'SCR',  # Seychelles
    'SL': 'SLL',  # Sierra Leone
    'SG': 'SGD',  # Singapore
    'SK': 'EUR',  # Slovakia
    'SI': 'EUR',  # Slovenia
    'SB': 'SBD',  # Solomon Islands
    'SO': 'SOS',  # Somalia
    'ZA': 'ZAR',  # South Africa
    'ES': 'EUR',  # Spain
    'LK': 'LKR',  # Sri Lanka
    'SD': 'SDG',  # Sudan
    'SR': 'SRD',  # Suriname
    'SE': 'SEK',  # Sweden
    'CH': 'CHF',  # Switzerland
    'SY': 'SYP',  # Syria
    'TW': 'TWD',  # Taiwan
    'TJ': 'TJS',  # Tajikistan
    'TZ': 'TZS',  # Tanzania
    'TH': 'THB',  # Thailand
    'TL': 'USD',  # Timor-Leste
    'TG': 'XOF',  # Togo
    'TO': 'TOP',  # Tonga
    'TT': 'TTD',  # Trinidad and Tobago
    'TN': 'TND',  # Tunisia
    'TR': 'TRY',  # Turkey
    'TM': 'TMT',  # Turkmenistan
    'TV': 'AUD',  # Tuvalu
    'UG': 'UGX',  # Uganda
    'UA': 'UAH',  # Ukraine
    'AE': 'AED',  # United Arab Emirates
    'GB': 'GBP',  # United Kingdom
    'US': 'USD',  # United States
    'UY': 'UYU',  # Uruguay
    'UZ': 'UZS',  # Uzbekistan
    'VU': 'VUV',  # Vanuatu
    'VA': 'EUR',  # Vatican City
    'VE': 'VES',  # Venezuela
    'VN': 'VND',  # Vietnam
    'YE': 'YER',  # Yemen
    'ZM': 'ZMW',  # Zambia
    'ZW': 'ZWL',  # Zimbabwe
}

def determine_country_currency(country_code):
    return country_to_currency.get(country_code, 'Unknown')