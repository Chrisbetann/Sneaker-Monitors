# locations.py

import requests
import json
import time
import random
import logging
from config import (
    send_sms_via_textlocal, TWOCAPTCHA_API_KEY, TEXTLOCAL_API_KEY,
    LOCATION, LANGUAGE
)

___standard_api___ = [
    'GB', 'US', 'AU', 'AT', 'BE', 'BG', 'CA', 'CN', 'HR', 'CZ', 'DK', 'EG',
    'FI', 'FR', 'DE', 'HU', 'IN', 'ID', 'IE', 'IT', 'MY', 'MX', 'MA', 'NL',
    'NZ', 'NO', 'PH', 'PL', 'PT', 'PR', 'RO', 'RU', 'SA', 'SG', 'SI', 'ZA',
    'ES', 'SE', 'CH', 'TR', 'AE', 'VN', 'JP'
]

def solve_captcha(captcha_url, sitekey):
    api_key = TWOCAPTCHA_API_KEY

    # Send CAPTCHA solving request to 2Captcha with the correct sitekey
    response = requests.post(
        f'http://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={sitekey}&url={captcha_url}'
    )
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

def standard_api(ITEMS, LOCATION, LANGUAGE, user_agent, proxy, KEYWORDS, start):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': LANGUAGE,
        'dnt': '1',
        'origin': f'https://www.nike.com/{LOCATION.lower()}/',
        'referer': f'https://www.nike.com/{LOCATION.lower()}/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user_agent,
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'
    }

    anchor = 0
    while anchor < 181:
        print('-- scrape --')
        url = f'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=3BCF9783E5B8CEB165B9DB2C449B7F26&country={LOCATION}&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace({LOCATION})%26filter%3Dlanguage({LANGUAGE})%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c)%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D60%26sort%3DeffectiveStartViewDateDesc&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D'
        response = requests.get(url=url, timeout=20, headers=headers, proxies=proxy)

        try:
            response_json = json.loads(response.text)

            # Handle CAPTCHA
            if 'captcha' in response_json.get('message', '').lower():
                print('CAPTCHA detected, solving it...')
                captcha_url = response.url
                sitekey = 'your_sitekey_here'  # You need to find the correct sitekey

                solved_captcha = solve_captcha(captcha_url, sitekey)

                if not solved_captcha:
                    print("Failed to solve CAPTCHA")
                    return []

                # Retry the request with the solved CAPTCHA
                headers['x-captcha-token'] = solved_captcha
                response = requests.get(url=url, timeout=20, headers=headers, proxies=proxy)
                response_json = json.loads(response.text)

            if 'data' not in response_json or 'products' not in response_json['data']:
                print(f"Error or no products found. Response: {response_json}")
                return []

            output = response_json['data']['products']['products']

        except json.JSONDecodeError:
            print('Error decoding JSON. Response content:', response.text)
            return []

        for item in output:
            for variant in item['colorways']:
                if variant['inStock'] and variant['pid'] not in ITEMS:
                    ITEMS.append(variant['pid'])
                    if start == 0:
                        if not KEYWORDS or any(key.lower() in item['title'].lower() for key in KEYWORDS):
                            message = f"New Product Alert:\nTitle: {item['title']}\nColour: {variant['colorDescription']}\nPrice: {variant['price']['currentPrice']}\nStyle Code: {variant['pdpUrl'].split('/')[-1]}\nURL: https://www.nike.com/{LOCATION.lower()}/{variant['pdpUrl'].replace('{countryLang}', LANGUAGE)}"
                            send_sms_via_textlocal(message)
                            print(f"Sent SMS for {item['title']}")

                elif not variant['inStock'] and variant['pid'] in ITEMS:
                    ITEMS.remove(variant['pid'])

        anchor += 60
        time.sleep(random.uniform(1, 3))  # Random delay to mimic human behavior

    return []
