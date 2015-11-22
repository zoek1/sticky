from flask.ext.mongoengine import MongoEngine
from mongoengine import NotUniqueError

class Telegram:
    def __getSticker(self):
        class Sticker(self.db.Document):
            file_id = self.db.StringField(required=True, unique=True)
            file_path = self.db.StringField(required=True)
        return Sticker

    def __init__(self, app):
        self.db = MongoEngine(app)
        self.Sticker = self.__getSticker()

    def saveSticker(self, sticker):
        print self.Sticker.objects(file_id=sticker.file_id).count()
        if self.Sticker.objects(file_id=sticker.file_id).count() == 0:
            self.Sticker(file_id=sticker.file_id, file_path=sticker.file_path).save()
