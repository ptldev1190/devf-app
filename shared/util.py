import config
import githubimport
from ptldev1190.pylib.Telegram import Telegram


def notify(message=''):
    to = config._Telegram_Chat_Id['Dhaval']
    token = config._Telegram_Bot_Token
    res = Telegram.sendMessage(message, to, token)
    return res

