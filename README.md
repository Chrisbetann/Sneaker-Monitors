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
python monitor.py
  
  <h3 align="center">Sneaker Monitors</h3>

  <p align="center">
    A collection of web monitors that notify of restocks or releases on sneaker related sites through Discord Webhook or SMS
    <br />
    <a href="https://github.com/yasserqureshi1/Sneaker-Monitors/">Report Bug</a>
    ·
    <a href="https://github.com/yasserqureshi1/Sneaker-Monitors/">Request Feature</a>
  </p>

  <p align="center">
    <a href="https://www.paypal.com/donate?hosted_button_id=SKRAD2YFGZC5C">
    <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="Logo" width="auto" height="50" >
  </a>
  </p> 
</p>
<br />

Please **star** this repository to increase the awareness of the project for others to use or add to. 

Join my Discord Server for code, sneakers and everything in-between! Join here: [discord.gg/YasCommunity](https://discord.gg/YasCommunity)


## About the Project
This project is aimed at providing web-monitors for various sites to the sneaker community for free. 
A monitor is a tool that tracks and alerts about changes on website.
These monitors currently notify if a restock or release occurs via Discord Webhook or SMS on popular sneaker related websites.

Today, competition to purchase sneakers is getting increasingly difficult with resellers using paid automated tools to give them a massive advantage over everyone else.
As such, I have and will continue to develop monitors that will help those members that struggle to finally get the sneakers they want.

This project is continually expanding, and I would greatly appreciate any contributions. 
When contributing please fork the project and open a Pull Request.

However, due to popular demand, I am developing a paid (but competitively priced) set of hosted monitors. These will be released on my Discord Server that you can join in [#Contact](#Contact).

*Below is a screenshot of the SNKRS monitor in action...*

<p align="center">
  <img width="300" src="https://github.com/yasserqureshi1/Sneaker-Monitors/blob/master/static/SNKRS_example.png?raw=true">
</p>

## Contents
* [About the Project](#about-the-project)
* [Monitors](#monitors)
* [Set Up](#set-up)
* [Footlocker Monitor Updates](#footlocker-monitor-updates)
* [Issues](#issues)
* [License](#license)
* [Contact](#contact)

## Monitors 

Currently the sites that have monitors are:
- All Shopify sites (e.g. Palace Skateboards, Hanon Shop, OVO, shopnicekicks.com, BDGA Store, Noir Fonce, Travis Scott, etc.)
- Supreme
- Nike SNKRS (Supports 42 countries - see the associated README file)
- Nike
- Footsites (Footlocker UK, US, and AU)
- Ssense
- Zalando (UK)
- Off-Spring (UK)
- Snipes
- Sivasdescalzo

ALL CREDIT IS TO BE GIVEN TO THE ORIGNAL CREATOR yasserqureshi1

