from peewee import Model, SqliteDatabase

db = SqliteDatabase(":memory:") # ./data/my.db

class BaseModel( Model ) :
    class Meta :
        database = db
