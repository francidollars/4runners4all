from peewee import AutoField, CharField
from playhouse import hybrid

from .model import BaseModel

class User( BaseModel ) :
    user_id = AutoField()
    _emailAddress = CharField()

    def __str__( self ) -> str :

        return f"UserID:{self.user_id}, EmailAddress:{self.emailAddress}"

    @hybrid.hybrid_property
    def emailAddress( self ) -> str :

        return self._emailAddress

    @emailAddress.setter
    def emailAddress( self,
                      emailAddress ) :
        self._emailAddress = emailAddress
