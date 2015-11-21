def isSticker(obj):
    if getattr(obj, 'sticker', False)  and obj.sticker != None:
        return True
    return False

def getFileFromSticker(conn, sticker):
    return conn.getFile(sticker.file_id)
