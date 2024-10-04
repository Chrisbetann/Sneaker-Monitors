# monitor.py

import requests as rq
import urllib3
from fp.fp import FreeProxy
from random_user_agent.user_agent import UserAgent

from datetime import datetime
import time
import json
import logging
import traceback

import locations
from config import (
    LOCATION, LANGUAGE, ENABLE_FREE_PROXY, FREE_PROXY_LOCATION, DELAY, PROXY,
    KEYWORDS, software_names, hardware_type, send_sms_via_textlocal
)

# Initialize logging
logging.basicConfig(
    filename='nike-monitor.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(message)s',
    level=logging.DEBUG
)

# Setting up Random User Agent
user_agent_rotator = UserAgent(software_names=software_names, hardware_types=hardware_type)

# Initialize Free Proxy if enabled
if ENABLE_FREE_PROXY:
    proxy_obj = FreeProxy(country_id=FREE_PROXY_LOCATION, rand=True)

INSTOCK = []
___standard_api___ = [
    'GB', 'US', 'AU', 'AT', 'BE', 'BG', 'CA', 'CN', 'HR', 'CZ', 'DK', 'EG',
    'FI', 'FR', 'DE', 'HU', 'IN', 'ID', 'IE', 'IT', 'MY', 'MX', 'MA', 'NL',
    'NZ', 'NO', 'PH', 'PL', 'PT', 'PR', 'RO', 'RU', 'SA', 'SG', 'SI', 'ZA',
    'ES', 'SE', 'CH', 'TR', 'AE', 'VN', 'JP'
]

def monitor():
    """
    Initiates the monitor
    """
    print('''\n---------------------------------
--- NIKE MONITOR HAS STARTED ---
---------------------------------\n''')
    logging.info(msg='Successfully started monitor')

    # Ensures that first scrape does not notify all products
    start = 1

    # Initialize proxy and headers
    if ENABLE_FREE_PROXY:
        proxy = {'http': proxy_obj.get()}
    elif PROXY != []:
        proxy_no = 0
        proxy = {"http": PROXY[proxy_no], "https": PROXY[proxy_no]}
    else:
        proxy = {}
    user_agent = user_agent_rotator.get_random_user_agent()

    while True:
        # Makes request to site and stores products
        try:
            if LOCATION in ___standard_api___:
                locations.standard_api(INSTOCK, LOCATION, LANGUAGE, user_agent, proxy, KEYWORDS, start)
            else:
                print(f'LOCATION "{LOCATION}" CURRENTLY NOT AVAILABLE. IF YOU BELIEVE THIS IS A MISTAKE PLEASE CREATE AN ISSUE ON GITHUB OR MESSAGE THE #issues CHANNEL IN DISCORD.')
                return

            # Allows changes to be notified
            start = 0

        except rq.exceptions.RequestException as e:
            logging.error(e)
            logging.info('Rotating headers and proxy')

            # Rotates headers
            user_agent = user_agent_rotator.get_random_user_agent()

            if ENABLE_FREE_PROXY:
                proxy = {'http': proxy_obj.get()}

            elif PROXY != []:
                proxy_no = 0 if proxy_no == (len(PROXY)-1) else proxy_no + 1
                proxy = {"http": PROXY[proxy_no], "https": PROXY[proxy_no]}

        except Exception as e:
            print(f"Exception found: {traceback.format_exc()}")
            logging.error(e)

        # User set delay
        time.sleep(float(DELAY))

if __name__ == '__main__':
    urllib3.disable_warnings()
    monitor()
