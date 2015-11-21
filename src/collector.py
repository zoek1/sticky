import telegram
from utils import isSticker, getFileFromSticker


def getStickers(conn):
        updates = [msg.message for msg in conn.getUpdates()]
        stickers = map(lambda s: s.sticker, filter(isSticker, updates))
        return stickers

def getFilepathStickers(conn, stickers):
    return [getFileFromSticker(conn, sticker) for sticker in stickers]
