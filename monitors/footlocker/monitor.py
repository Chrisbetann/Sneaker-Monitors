from random_user_agent.user_agent import UserAgent
import requests
from fp.fp import FreeProxy
from datetime import datetime
import time
import logging
import traceback
from locations import US, UK, AU  # Importing regional product scraping functions
from config import LOCATION, ENABLE_FREE_PROXY, FREE_PROXY_LOCATION, DELAY, PROXY, KEYWORDS, software_names, hardware_type

# Initialize logging
logging.basicConfig(filename='footlocker-monitor.log', filemode='a', format='%(asctime)s - %(name)s - %(message)s', level=logging.DEBUG)

# Setting up Random User Agent
user_agent_rotator = UserAgent(software_names=software_names, hardware_type=hardware_type)

# Initialize Free Proxy if enabled
if ENABLE_FREE_PROXY:
    proxy_obj = FreeProxy(country_id=FREE_PROXY_LOCATION, rand=True)

INSTOCK = []

def monitor():
    """
    Starts the Foot Locker monitoring.
    """
    print('''\n--------------------------------------
--- FOOTLOCKER MONITOR HAS STARTED ---
--------------------------------------\n''')
    logging.info('Successfully started monitor')

    # Ensures that the first scrape does not notify all products
    start = 1

    # Initialize proxy and headers
    if ENABLE_FREE_PROXY:
        proxy = {'http': proxy_obj.get()}
    elif PROXY:
        proxy_no = 0
        proxy = {"http": PROXY[proxy_no], "https": PROXY[proxy_no]}
    else:
        proxy = {}

    user_agent = user_agent_rotator.get_random_user_agent()

    while True:
        try:
            # Make request to site based on location and get products
            if LOCATION == 'US':
                US(INSTOCK, user_agent, proxy, KEYWORDS, start)

            elif LOCATION == 'UK':
                UK(INSTOCK, user_agent, proxy, KEYWORDS, start)

            elif LOCATION == 'AU':
                AU(INSTOCK, user_agent, proxy, KEYWORDS, start)

            else:
                print('LOCATION CURRENTLY NOT AVAILABLE.')
                return

            # Allows changes to be notified
            start = 0

        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.info('Rotating headers and proxy')

            if ENABLE_FREE_PROXY:
                proxy = {'http': proxy_obj.get()}

            elif PROXY:
                proxy_no = 0 if proxy_no == (len(PROXY) - 1) else proxy_no + 1
                proxy = {"http": PROXY[proxy_no], "https": PROXY[proxy_no]}

        except Exception as e:
            print(f"Exception found: {traceback.format_exc()}")
            logging.error(e)

        # User-set delay
        time.sleep(float(DELAY))


if __name__ == '__main__':
    monitor()
