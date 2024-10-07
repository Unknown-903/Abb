import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 20478011)) #API ID
API_HASH = environ.get('API_HASH', '0e4dcf39643e83c3c174a0d2370e5b4a') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '7077374297:AAGgxSqJOrJ5GR8E3iiphrAzpL1FT1RW3Fk') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://suryagupta1928:6thfnQ3AxzK6VJUA@cluster0.6ppqasw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 2061656269)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1001930662842))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1002083092778))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', 9)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
