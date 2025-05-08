import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'MrSSKBot')
API_ID = int(environ.get('API_ID', '26339634'))
API_HASH = environ.get('API_HASH', 'e0318ca1a4652f9348844203de8f491b')
BOT_TOKEN = environ.get('BOT_TOKEN', "7361998653:AAHsfQxiOxEpvf7B9ClRCA97tFJs9RecMto")

# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://ynvmovies.koyeb.app/")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002290275432'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6306607988').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://harishkumargorinta:P6ak9kZKvx33Jx3@movies24.ng58m.mongodb.net/?retryWrites=true&w=majority&appName=Movies24")
DATABASE_NAME = environ.get('DATABASE_NAME', "Movies24")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'api.shareus.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'hRPS5vvZc0OGOEUQJMJzPiojoVK2')
