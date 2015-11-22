from flask import Flask, render_template
from os import getenv

import telegram

from collector import getStickers, getFilepathStickers
from db.mongo import Telegram

app = Flask(__name__)
stickersDB = Telegram(app)

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
