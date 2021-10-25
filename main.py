import asyncio
import time

import requests
import schedule
import telebot

bot = telebot.TeleBot('<bot_token>')


def track_price():
    try:

        ftx = requests.get('https://ftx.com/api/markets/BTC/USDT').json()['result']
        binance = requests.get('https://api1.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT').json()
        ftx_dict = {
            'name': 'FTX',
            'ticker': 'BTC/USDT',
            'ask': ftx['ask'],
            'bid': ftx['bid'],
            'link': 'https://ftx.com/trade/BTC/USDT'
        }

        binance_dict = {
            'name': 'Binance',
            'ticker': 'BTC/USDT',
            'ask': round(float(binance['askPrice']), 1),
            'bid': round(float(binance['bidPrice']), 1),
            'link': 'https://www.binance.com/ru/trade/BTC_USDT'
        }
        if ftx_dict['ask'] < binance_dict['bid']:
            message_text = (f"More profitable - {binance_dict['name']}\n"
                  f"Ticker - {binance_dict['ticker']}\n"
                  f"Ask - {binance_dict['ask']}\n"
                  f"Bid - {binance_dict['bid']}\n"
                  f"Link - {binance_dict['link']}")
            bot.send_message(chat_id='<your_chat_id>', text=message_text)

        elif binance_dict['ask'] < ftx_dict['bid']:
            message_text = (f"More profitable - {ftx_dict['name']}\n"
                  f"Ticker - {ftx_dict['ticker']}\n"
                  f"Ask - {ftx_dict['ask']}\n"
                  f"Bid - {ftx_dict['bid']}\n"
                  f"Link - {ftx_dict['link']}")
            bot.send_message(chat_id='<your_chat_id>', text=message_text)
        else:
            pass
    except Exception as ex:
        print(ex)


schedule.every(10).minutes.do(track_price)

while True:
    schedule.run_pending()
    time.sleep(1)