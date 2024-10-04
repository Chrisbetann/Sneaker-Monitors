<p align="center">
  <a href="https://github.com/yasserqureshi1/Sneaker-Monitors/">
    ## Footlocker Monitor Updates (by Christopher Betancourt) 


### New Features:

We have made significant updates to the **Footlocker** monitor, with contributions by Christopher Betancourt. These changes enhance the functionality and adaptability of the monitor:

1. **SMS Notifications**:
    - The Footlocker monitor now has the capability to send SMS notifications for restocks or product releases, as an alternative to using Discord Webhook.
    - Integration with the **Textlocal** API allows SMS alerts to be sent directly to a configured phone number.
    - Configuration of SMS notifications can be managed in the `config.py` file, where you can provide your **Textlocal API Key**, sender name, and target phone number.

2. **CAPTCHA Solving**:
    - Footlocker frequently employs CAPTCHA challenges to block automated access.
    - We've integrated **2Captcha** to solve these CAPTCHA challenges automatically, ensuring the monitor can continue functioning without manual intervention.
    - To enable CAPTCHA solving, provide your **2Captcha API Key** (`TWOCAPTCHA_API_KEY`) in the `config.py` file.

### Configuration Overview:

To use the updated Footlocker monitor:

1. **Configure `config.py`**:
    - Set your region (`LOCATION`) to `US`, `UK`, or `AU`.
    - Enable free proxies or provide your own proxy list for anonymity.
    - Set up **Textlocal** SMS settings (`TEXTLOCAL_API_KEY`, `SENDER`, `TARGET_PHONE_NUMBER`).
    - Provide your **2Captcha API Key** (`TWOCAPTCHA_API_KEY`) for CAPTCHA-solving functionality.

### Running the Monitor:

After configuring `config.py`, you can start the Footlocker monitor by running the `monitor.py` script:

```sh

 Nike Monitor Updates (by Christopher Betancourt)

New Features:

We have implemented new features and improvements to the **Nike** monitor, with significant contributions by Christopher Betancourt. These changes aim to enhance functionality and improve usability.

1. **SMS Notifications**:
    - The Nike monitor has been updated to provide SMS notifications instead of Discord webhook notifications.
    - Integration with **Textlocal** allows the monitor to send SMS alerts directly to your configured phone number.
    - You can configure the SMS settings in the `config.py` file by providing your **Textlocal API Key**, sender name, and target phone number.

2. **CAPTCHA Solving**:
    - Nike’s API can present CAPTCHA challenges to prevent bots.
    - We've integrated **2Captcha** to automatically solve these CAPTCHA challenges, allowing the monitor to proceed seamlessly.
    - To use CAPTCHA-solving functionality, provide your **2Captcha API Key** (`TWOCAPTCHA_API_KEY`) in the `config.py` file.

### Configuration Overview:

To use the updated Nike monitor:

1. **Configure `config.py`**:
    - Set your region (`LOCATION`) to any of the supported countries.
    - Set up **Textlocal** SMS settings (`TEXTLOCAL_API_KEY`, `SENDER`, `TARGET_PHONE_NUMBER`).
    - Provide your **2Captcha API Key** (`TWOCAPTCHA_API_KEY`) to solve CAPTCHA challenges automatically.

### Running the Monitor:

After configuring `config.py`, you can start the Nike monitor by running the `monitor.py` script:

```sh
python monitor.py



ALL CREDIT IS TO BE GIVEN TO THE ORIGNAL CREATOR yasserqureshi1

