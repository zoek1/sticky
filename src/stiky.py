from os import getenv
import telegram
from collector import getStickers, getFilepathStickers
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    bot = telegram.Bot(token=getenv('TELEGRAM_TOKEN'))

    stickers = getStickers(bot)
    fp_stickers = getFilepathStickers(bot, stickers)

    return render_template('index.html', stickers=fp_stickers)

if __name__ == "__main__":
    app.debug = True
    app.run()
