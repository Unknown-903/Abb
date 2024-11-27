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

API_ID = int(environ.get('API_ID', 29776284)) #API ID
API_HASH = environ.get('API_HASH', 'aa9d8ca9cf83f30aa897effa6296493a') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '7598218790:AAGxZbAT1bwvuYTScRc9spPPdvl1HK9-8EA') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://Toonpro12:animebash@cluster0.e6hpn8l.mongodb.net/?retryWrites=true&w=majority') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 6866798543)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1002336740271))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1002424834393))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', 9)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
