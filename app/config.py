from decouple import config
class Config:
    SQLALCHEMY_DATABASE_URI=config('MYSQL_ADDON_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY='QWERTY123'