# Imports
import requests
import time
from scheduled_notifications import email_notification
import schedule

# base url
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    
def get_crypto_prices():
    # Get Prices
    headers = {
        'X-CMC_PRO_API_KEY': 'cf1ee749-0f7a-492a-8a75-fbb96cc07cbc',
        'Accepts': 'application/json'
        }
    params = {
        'start': '1',
        'limit': '2',
        'convert': 'CAD'
        }
    response = requests.get(url, params = params, headers = headers)
    
    # if response success
    if response.status_code == 200:
        crypto_info = response.json()
        coins = crypto_info['data']
        
        # email prices
        subject = 'Daily BTC & ETH Price'
        body = ''
        for value in coins:
            symbol = value['symbol']
            price = value['quote']['CAD']['price']
            body += f"{symbol}: ${price:.2f} CAD\n"
        email_notification(subject, body, 'benj.kimmy03@gmail.com')
    
    # if response fails
    else:
        email_notification("Failed", "Failed to Retrieve data", "benj.kimmy03@gmail.com")
        

def get_percent_change():
    # Get Prices
    headers = {
        'X-CMC_PRO_API_KEY': 'cf1ee749-0f7a-492a-8a75-fbb96cc07cbc',
        'Accepts': 'application/json'
        }
    params = {
        'start': '1',
        'limit': '2',
        'convert': 'CAD'
        }
    response = requests.get(url, params = params, headers = headers)
    
    # if response success
    if response.status_code == 200:
        crypto_info = response.json()
        coins = crypto_info['data']
        
        # variables
        BTC_7d_percent_change = coins[0]['quote']['CAD']['percent_change_7d']
        ETH_7d_percent_change = coins[1]['quote']['CAD']['percent_change_7d']
        BTC_price = coins[0]['quote']['CAD']['price']
        ETH_price = coins[1]['quote']['CAD']['price']
        
        # outcomes & email drops or gains
        if BTC_7d_percent_change > 15:
            subject = 'Emergency BTC Gain'
            body = f"BTC: ${BTC_price:.2f} CAD\nBTC Percent Change 7d: {BTC_7d_percent_change:.2f}%"
            email_notification(subject, body, 'benj.kimmy03@gmail.com')
        elif BTC_7d_percent_change < -15:
            subject = 'Emergency BTC Drop'
            body = f"BTC: ${BTC_price:.2f} CAD\nBTC Percent Change 7d: {BTC_7d_percent_change:.2f}%"
            email_notification(subject, body, 'benj.kimmy03@gmail.com')
        if ETH_7d_percent_change > 15:
            subject = 'Emergency ETH Gain'
            body = f"ETH: ${ETH_price:.2f} CAD\nETH Percent Change 7d: {ETH_7d_percent_change:.2f}%"
            email_notification(subject, body, 'benj.kimmy03@gmail.com')
        elif ETH_7d_percent_change < -15:
            subject = 'Emergency ETH Drop'
            body = f"ETH: ${ETH_price:.2f} CAD\nETH Percent Change 7d: {ETH_7d_percent_change:.2f}%"
            email_notification(subject, body, 'benj.kimmy03@gmail.com') 
    
    # if response fails
    else:
        email_notification("Failed", "Failed to Retrieve data", "benj.kimmy03@gmail.com")
        
# perform task every...
schedule.every().day.at('16:48').do(get_crypto_prices)
schedule.every().sunday.at('16:43').do(get_percent_change)
while True:
    schedule.run_pending()
    time.sleep(2)
    
    
    
    