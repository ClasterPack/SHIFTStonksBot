from pathlib import Path

from .bot_token import token

BOT_TOKEN = token
# BASE_URL = 'https://example.com'  # Webhook domain
# WEBHOOK_PATH = f'/tg/webhooks/bot/{BOT_TOKEN}'
# WEBHOOK_URL = f'{BASE_URL}{WEBHOOK_PATH}'

LOGS_BASE_PATH = str(Path(__file__).parent.parent / 'logs')

admins = []

# ip = {
#     'db':    '',
#     'redis': '',
# }

# mysql_info = {
#     'host':     ip['db'],
#     'user':     '',
#     'password': '',
#     'db':       '',
#     'maxsize':  5,
#     'port':     3306,
# }
#
# redis = {
#     'host':     ip['redis'],
#     'password': ''
# }
