from peewee import Model, SqliteDatabase

db = SqliteDatabase("./data/my.db")

class BaseModel( Model ) :
    class Meta :
        database = db
