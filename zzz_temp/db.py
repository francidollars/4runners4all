from peewee import *
import datetime

db = SqliteDatabase('my_db.db')

class BaseModel(Model) :
    class Meta :
        database = db

class User :
    def __init__( self,
                  userId,
                  emailAddress ) :
        self.userId = userId
        self.emailAddress = emailAddress

    def __str__( self ) -> str:

        return f"{self.userId}: {self.emailAddress}"

class UserRepository(BaseModel, User) :
