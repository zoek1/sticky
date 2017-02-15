from flask import Flask, render_template
from os import getenv
import os

import telegram
from telegram.ext.dispatcher import Dispatcher
from telegram.ext.updater import Updater
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from collector import getStickers, getFilepathStickers
from db.mongo import Telegram

app = Flask(__name__)
stickersDB = Telegram(app)

TELEGRAM_TOKEN=getenv('TELEGRAM_TOKEN')
PORT=int(os.environ.get('PORT', '5000'))
APP_NAME=getenv('APPNAME')

updater = Updater(TELEGRAM_TOKEN)
dispatcher = Dispatcher.get_instance()


def register_sticker(bot, update):
    """Handler when some sticker is sended"""
    print("Validando recepcion de sticker")
    message = update.message
    stickers = getStickers(bot)
    fp_stickers = getFilepathStickers(bot, stickers)
    map(stickersDB.saveSticker, fp_stickers)


sticker_handler = MessageHandler(Filters.sticker, register_sticker)
dispatcher.add_handler(sticker_handler)

updater.start_polling(3)
# updater.idle()

@app.route('/')
def index():
    stickers = stickersDB.Sticker.objects()
    return render_template('index.html', stickers=stickers)

@app.route('/update', methods=["POST"])
def update():
    bot = telegram.Bot(token=getenv('TELEGRAM_TOKEN'))
    stickers = getStickers(bot)
    fp_stickers = getFilepathStickers(bot, stickers)
    map(stickersDB.saveSticker, fp_stickers)
    return 'Updated successfully'

if __name__ == "__main__":
    app.debug = True
    app.run()
