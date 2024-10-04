# config.py

# Random User Agent Configuration
from random_user_agent.params import SoftwareName, HardwareType

# Configuration for Random User Agents
software_names = [SoftwareName.CHROME.value]
hardware_type = [HardwareType.MOBILE__PHONE]

# General Monitoring Configuration
LOCATION = 'US'  # Choose between 'US', 'UK', 'AU'
ENABLE_FREE_PROXY = True
FREE_PROXY_LOCATION = 'US'  # Proxy country for free proxy ('US', 'UK', 'AU')
DELAY = 10  # Delay between requests in seconds
PROXY = []  # Add proxies if needed, e.g., ["http://proxy1", "http://proxy2"]
KEYWORDS = ["shoes", "Nike", "Adidas"]  # Keywords to search for products

# Textlocal SMS Configuration
TEXTLOCAL_API_KEY = 'your_textlocal_api_key_here'
SENDER = 'FootMon'  # Replace with a valid sender name (6-11 alphanumeric characters)
TARGET_PHONE_NUMBER = 'target_phone_number_here'

# 2Captcha Configuration for CAPTCHA Solving
TWOCAPTCHA_API_KEY = 'your_2captcha_api_key_here'
