import requests
import json
import time
import random
from config import send_sms_via_textlocal, TWOCAPTCHA_API_KEY, TEXTLOCAL_API_KEY, SENDER, TARGET_PHONE_NUMBER

# Function to solve CAPTCHA using 2Captcha service
def solve_captcha(captcha_url, sitekey):
    api_key = TWOCAPTCHA_API_KEY

    # Send CAPTCHA solving request to 2Captcha with the correct sitekey
    response = requests.post(
        f'http://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={sitekey}&url={captcha_url}')
    print(f"2Captcha Response: {response.text}")  # Debugging line to check response

    # Check for errors in the response
    if 'OK|' not in response.text:
        print(f"Error from 2Captcha: {response.text}")
        return None

    try:
        captcha_id = response.text.split('|')[1]  # Extract the captcha_id
    except IndexError:
        print(f"Failed to parse captcha ID: {response.text}")
        return None

    # Wait for CAPTCHA to be solved
    time.sleep(20)
    captcha_result = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}').text

    while 'CAPCHA_NOT_READY' in captcha_result:
        time.sleep(5)
        captcha_result = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}').text

    if 'OK|' in captcha_result:
        return captcha_result.split('|')[1]
    else:
        print(f"Error solving CAPTCHA: {captcha_result}")
        return None

# Functions to handle Foot Locker products
def get_products(region, ITEMS, user_agent, proxy, KEYWORDS, start):
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user_agent
    }

    # URL setup based on region
    if region == 'US':
        url = 'https://www.footlocker.com/api/products/search?query=men&currentPage=1&sort=newArrivals&pageSize=60'
    elif region == 'UK':
        url = 'https://www.footlocker.co.uk/api/products/search?query=men&currentPage=1&sort=newArrivals&pageSize=60'
        headers['x-api-lang'] = 'en-GB'
    elif region == 'AU':
        url = 'https://www.footlocker.com.au/api/products/search?query=men&currentPage=1&sort=newArrivals&pageSize=60'

    html = requests.get(url=url, headers=headers, proxies=proxy)

    try:
        response_json = json.loads(html.text)

        # Handle CAPTCHA
        if 'geo.captcha-delivery.com' in response_json.get('url', ''):
            print('CAPTCHA detected, solving it...')
            solved_captcha = solve_captcha(response_json['url'], 'replace_with_correct_sitekey')

            if not solved_captcha:
                print("Failed to solve CAPTCHA")
                return []

        if 'products' not in response_json:
            print(f"CAPTCHA or error encountered. Response: {response_json}")
            return []

        output = response_json['products']

    except json.JSONDecodeError:
        print('Error decoding JSON. Response content:', html.text)
        return []

    for product in output:
        try:
            sku = product['sku']
            url = f'{region}/api/products/pdp/{sku}'
            html = requests.get(url=url, headers=headers)
            item = json.loads(html.text)

            time.sleep(random.uniform(5, 15))  # Randomized delay

            sizes = ''
            for size in item['sellableUnits']:
                store = [size['sku'], size['code']]
                if size['stockLevelStatus'] == 'inStock' and store not in ITEMS:
                    ITEMS.append(store)
                    sizes += f"\n{size['size']}"

            if start == 0 and sizes != '':
                message = f"Product: {item['name']}\nPrice: {product['price']['formattedValue']}\nSKU: {product['sku']}\nURL: {region}/product/{item['name'].replace(' ', '-')}/{product['sku']}.html"
                send_sms_via_textlocal(message)

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"Error while processing product SKU {sku}: {e}")
            continue

    return []

# Functions for each region (US, UK, AU)
def US(ITEMS, user_agent, proxy, KEYWORDS, start):
    return get_products('US', ITEMS, user_agent, proxy, KEYWORDS, start)

def UK(ITEMS, user_agent, proxy, KEYWORDS, start):
    return get_products('UK', ITEMS, user_agent, proxy, KEYWORDS, start)

def AU(ITEMS, user_agent, proxy, KEYWORDS, start):
    return get_products('AU', ITEMS, user_agent, proxy, KEYWORDS, start)
