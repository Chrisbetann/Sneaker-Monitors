# config.py

# --------------------- SMS CONFIGURATION ---------------------
TEXTLOCAL_API_KEY = 'your_textlocal_api_key_here'
SENDER = 'NikeMon'  # Replace with a valid sender name (6-11 alphanumeric characters)
TARGET_PHONE_NUMBER = 'target_phone_number_here'

# --------------------- 2CAPTCHA CONFIGURATION ---------------------
TWOCAPTCHA_API_KEY = 'your_2captcha_api_key_here'

# --------------------- NIKE MONITOR DETAILS ---------------------
LOCATION = "GB"
LANGUAGE = "en-GB"

# --------------------- FREE PROXY ---------------------
# A single or multiple locations can be added in the array (e.g. ["GB"] or ["GB", "US"])
ENABLE_FREE_PROXY = False
FREE_PROXY_LOCATION = ["GB"]

# --------------------- DELAY ---------------------
# Delay between site requests (in seconds)
DELAY = 5

# --------------------- OPTIONAL PROXY ---------------------
# Proxies must follow this format: "<proxy>:<port>" OR "<proxy_username>:<proxy_password>@<proxy_domain>:<port>")
# If you want to use multiple proxies, please create an array
# E.G. PROXY = ["proxy1:proxy1port", "proxy2:proxy2port"]
PROXY = []

# --------------------- OPTIONAL KEYWORDS ---------------------
# E.G. KEYWORDS = ["box", "logo"]
KEYWORDS = []

# --------------------- RANDOM USER AGENT CONFIGURATION ---------------------
from random_user_agent.params import SoftwareName, HardwareType

software_names = [SoftwareName.CHROME.value]
hardware_type = [HardwareType.MOBILE__PHONE]

# Function to send SMS via Textlocal
def send_sms_via_textlocal(message):
    import requests
    data = {
        'apikey': TEXTLOCAL_API_KEY,
        'numbers': TARGET_PHONE_NUMBER,
        'message': message,
        'sender': SENDER
    }
    response = requests.post('https://api.txtlocal.com/send/', data=data)
    print(f"SMS sent. Response: {response.text}")
