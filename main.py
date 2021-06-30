from telegram.ext import Updater , CommandHandler , CallbackContext
import datetime
import pytz
from tradingview_ta import TA_Handler, Interval

print('Bot started running at ' + str(datetime.datetime.today()))

#Emojis
raising_hands = u'\U0001F64C' #raising hands
robot = u'\U0001F916' #robot
check_mark_button = u'\U00002705' #check mark button
e_mail = u'\U0001F4E7' #e-mail
alien_monster = u'\U0001F47E' #alien_monster
satellite_antenna = u'\U0001F4E1' #satellite antenna
gear = u'\U00002699' #gear
cross_mark = u'\U0000274C' #cross_mark
coffee = u'\U00002615' #coffee
open_book = u'\U0001F4D6' #open book
dove_of_peace = u'\U0001F54A' #drove of peace
rocket = u'\U0001F680' #rocket
rising_chart = u'\U0001F4C8' #Chart with Upwards Trend
falling_chart = u'\U0001F4C9' #Chart with Downwards Trend


#Place your TelegramBot-API Here:
apikey = ''
updater = Updater(token=apikey)
dispatcher = updater.dispatcher
#Also, on line 234, You need to place your own channel's user_id

btc_price = {}
eth_price = {}
ada_price = {}

btc_last = list()
eth_last = list()
ada_last = list()

def btc():
    binance =  TA_Handler(symbol="BTCUSD", screener="crypto", exchange="BINANCE", interval=Interval.INTERVAL_1_DAY)
    binance_price = binance.get_analysis().indicators["close"]
    binance_price = format(binance_price, '.2f')
    btc_price['Binance'] = binance_price

    coinbase =  TA_Handler(symbol="BTCUSD", screener="crypto", exchange="COINBASE", interval=Interval.INTERVAL_1_DAY)
    coinbase_price = coinbase.get_analysis().indicators["close"]
    coinbase_price = format(coinbase_price, '.2f')
    btc_price['Coinbase'] = coinbase_price

    bitfinex =  TA_Handler(symbol="BTCUSD", screener="crypto", exchange="BITFINEX", interval=Interval.INTERVAL_1_DAY)
    bitfinex_price = bitfinex.get_analysis().indicators["close"]
    bitfinex_price = format(bitfinex_price, '.2f')
    btc_price['Bitfinex'] = bitfinex_price

    bittrex =  TA_Handler(symbol="BTCUSD", screener="crypto", exchange="BITTREX", interval=Interval.INTERVAL_1_DAY)
    bittrex_price = bittrex.get_analysis().indicators["close"]
    bittrex_price = format(bittrex_price, '.2f')
    btc_price['Bittrex'] = bittrex_price

    capitalcom =  TA_Handler(symbol="BTCUSD", screener="crypto", exchange="CAPITALCOM", interval=Interval.INTERVAL_1_DAY)
    capitalcom_price = capitalcom.get_analysis().indicators["close"]
    capitalcom_price = format(capitalcom_price, '.2f')
    btc_price['Capitalcom'] = capitalcom_price

def eth():
    binance = TA_Handler(symbol="ETHUSD", screener="crypto", exchange="BINANCE", interval=Interval.INTERVAL_1_DAY)
    binance_price = binance.get_analysis().indicators["close"]
    binance_price = format(binance_price, '.2f')
    eth_price['Binance'] = binance_price

    coinbase = TA_Handler(symbol="ETHUSD", screener="crypto", exchange="COINBASE", interval=Interval.INTERVAL_1_DAY)
    coinbase_price = coinbase.get_analysis().indicators["close"]
    coinbase_price = format(coinbase_price, '.2f')
    eth_price['Coinbase'] = coinbase_price

    bitfinex = TA_Handler(symbol="ETHUSD", screener="crypto", exchange="BITFINEX", interval=Interval.INTERVAL_1_DAY)
    bitfinex_price = bitfinex.get_analysis().indicators["close"]
    bitfinex_price = format(bitfinex_price, '.2f')
    eth_price['Bitfinex'] = bitfinex_price

    bittrex = TA_Handler(symbol="ETHUSD", screener="crypto", exchange="BITTREX", interval=Interval.INTERVAL_1_DAY)
    bittrex_price = bittrex.get_analysis().indicators["close"]
    bittrex_price = format(bittrex_price, '.2f')
    eth_price['Bittrex'] = bittrex_price

    capitalcom = TA_Handler(symbol="ETHUSD", screener="crypto", exchange="CAPITALCOM", interval=Interval.INTERVAL_1_DAY)
    capitalcom_price = capitalcom.get_analysis().indicators["close"]
    capitalcom_price = format(capitalcom_price, '.2f')
    eth_price['Capitalcom'] = capitalcom_price
    
def ada():
    binance = TA_Handler(symbol="ADAUSD", screener="crypto", exchange="BINANCE", interval=Interval.INTERVAL_1_DAY)
    binance_price = binance.get_analysis().indicators["close"]
    binance_price = format(binance_price, '.5f')
    ada_price['Binance'] = binance_price

    coinbase = TA_Handler(symbol="ADAUSD", screener="crypto", exchange="COINBASE", interval=Interval.INTERVAL_1_DAY)
    coinbase_price = coinbase.get_analysis().indicators["close"]
    coinbase_price = format(coinbase_price, '.5f')
    ada_price['Coinbase'] = coinbase_price

    bitfinex = TA_Handler(symbol="ADAUSD", screener="crypto", exchange="BITFINEX", interval=Interval.INTERVAL_1_DAY)
    bitfinex_price = bitfinex.get_analysis().indicators["close"]
    bitfinex_price = format(bitfinex_price, '.5f')
    ada_price['Bitfinex'] = bitfinex_price

    bittrex = TA_Handler(symbol="ADAUSD", screener="crypto", exchange="BITTREX", interval=Interval.INTERVAL_1_DAY)
    bittrex_price = bittrex.get_analysis().indicators["close"]
    bittrex_price = format(bittrex_price, '.5f')
    ada_price['Bittrex'] = bittrex_price

    capitalcom = TA_Handler(symbol="ADAUSD", screener="crypto", exchange="CAPITALCOM", interval=Interval.INTERVAL_1_DAY)
    capitalcom_price = capitalcom.get_analysis().indicators["close"]
    capitalcom_price = format(capitalcom_price, '.5f')
    ada_price['Capitalcom'] = capitalcom_price

def btc_check():
    global btc_last
    try:
        if btc_price['Binance'] > btc_last[0]:
            first_line =  rising_chart + ' Bitcoin (BTC-USD)'
        elif btc_price['Binance'] < btc_last[0]:
            first_line =  falling_chart + ' Bitcoin (BTC-USD)'
        else:
            first_line = falling_chart + ' Bitcoin (BTC-USD)'
    except:
        first_line = falling_chart + ' Bitcoin (BTC-USD)'

    text_list = [first_line]
    for count, exchange in enumerate(list(btc_price.keys())):
        try:
            item = percent(exchange, btc_price[exchange], btc_last[count])
            text_list.append(item)
        except:
            pass

    btc_last = list(btc_price.values())

    if len(text_list) > 1:
        return ''.join(text_list)
    
def eth_check():
    global eth_last
    try:
        if eth_price['Binance'] > eth_last[0]:
            first_line =  rising_chart + ' Ethereum (ETH-USD)'
        elif eth_price['Binance'] < eth_last[0]:
            first_line =  falling_chart + ' Ethereum (ETH-USD)'
        else:
            first_line = falling_chart + ' Ethereum (ETH-USD)'
    except:
        first_line = falling_chart + ' Ethereum (ETH-USD)'

    text_list = [first_line]
    for count, exchange in enumerate(list(eth_price.keys())):
        try:
            item = percent(exchange, eth_price[exchange], eth_last[count])
            text_list.append(item)
        except:
            pass

    eth_last = list(eth_price.values())

    if len(text_list) > 1:
        return ''.join(text_list)
    
def ada_check():
    global ada_last
    try:
        if ada_price['Binance'] > ada_last[0]:
            first_line =  rising_chart + ' Cardano (ADA-USD)'
        elif ada_price['Binance'] < ada_last[0]:
            first_line =  falling_chart + ' Cardano (ADA-USD)'
        else:
            first_line = falling_chart + ' Cardano (ADA-USD)'
    except:
        first_line = falling_chart + ' Cardano (ADA-USD)'

    text_list = [first_line]
    for count, exchange in enumerate(list(ada_price.keys())):
        try:
            item = percent(exchange, ada_price[exchange], ada_last[count])
            text_list.append(item)
        except:
            pass

    ada_last = list(ada_price.values())

    if len(text_list) > 1:
        return ''.join(text_list)

def percent(exchange, current_price, last_price):
    percent_amount = ((float(current_price) / float(last_price))-1) * 100
    text = '\n' + exchange + ': $' + str(current_price) + ' (' + str(format(percent_amount, '.3f')) + '%)' 
    
    return text

def message():
    btc()
    eth()
    ada()

    try:
        message_content = btc_check() + '\n\n' + eth_check() + '\n\n' + ada_check()
        print(message_content)
        return message_content
    except:
        pass
    
count = 0
while count < 3:
  message()
  count += 1
  if count >= 3:
    break
print('gathering data completed. bot started at ' + str(datetime.datetime.today()))


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=raising_hands + " Hey! What's up! Welcome to CryptoStats. This bot is especially designed for @CryptoStats1 so feel free to join our channel.\n\n" + robot + " If you are interested about the functionality of this bot, use /about to get some help!\n\n" + alien_monster + " Other than that, there's not much this bot can help you do; Obviously because it's just a channel manager for @CryptoStats1.")
dispatcher.add_handler(CommandHandler('start', start))

def about(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=alien_monster + " This bot can help you get access to the latest prices of the most popular cryptocurrency stocks.\nWe will send @CryptoStats1 a message each 5 minutes containing the information.\n\n" + robot + " Remember this bot is an open-source bot, So you can always access the source files and instruction from Github.Com; Link in the bot description\n\n" + satellite_antenna + " Early Version - Under Development\n" + gear + " Beta V1.00\n\n" + robot + " Developed By:\n@JoiFoi & @mac_mr\n\n" + e_mail + " cryptostatssupport@solarunited.net")
dispatcher.add_handler(CommandHandler('about', about))

hourlist = []
minlist = []

for hour in range(0 , 24):
    hourlist.append(hour)
for min in range(0 , 60):
    if min%5 == 0:
        minlist.append(min)

#Remeber to put your channel chat_id in this section:
def cryptostats(context: CallbackContext):
    btc()
    eth()
    ada()
    try:
        context.bot.send_message(chat_id=, text=message())
    except:
        pass

j = updater.job_queue

for hours in hourlist:
    for mins in minlist:
        job_daily = j.run_daily(cryptostats, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=hours, minute=mins, tzinfo=pytz.timezone('Asia/Tehran')))

updater.start_polling()
