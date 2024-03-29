from peewee import AutoField, CharField
from playhouse import hybrid

from .model import BaseModel

class User( BaseModel ) :
    user_id = AutoField()
    _emailAddress = CharField(unique=True)

    def __str__( self ) -> str :

        return f"UserID:{self.user_id}, EmailAddress:{self.emailAddress}"

    @hybrid.hybrid_property
    def emailAddress( self ) -> str :

        return self._emailAddress

    @emailAddress.setter
    def emailAddress( self,
                      emailAddress: str ) :
        self._emailAddress = emailAddress

User._meta.database.create_tables([User])
