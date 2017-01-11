# bot
TOKEN = ''


# botan
BOTAN_TOKEN = ''


# webhook
WEBHOOK_HOST = ''
WEBHOOK_PORT = 443
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_SSL_CERT = './cert/webhook_cert.pem'
WEBHOOK_SSL_PRIV = './cert/webhook_pkey.pem'

WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}"
WEBHOOK_URL_PATH = f"/{TOKEN}/"

# info
VERSION = "2.2.2"
DB_DATE = "07.01.2017"


# database
MYSQL_HOST = ''
MYSQL_DATABASE = ''
MYSQL_USER = ''
MYSQL_PASSWORD = ''


# tor
PROXIES = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}