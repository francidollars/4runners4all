from datetime import datetime
from datetime import date
from furl import furl
from peewee import Field, AutoField, CharField, DateField, DateTimeField, ForeignKeyField, IntegerField
from playhouse import hybrid

from .model import BaseModel
from .user import User

class UrlField( CharField ) :
    field_type = 'urllist'

    def db_value( self,
                  value ) -> str :
        if isinstance(value, str):

            return value
        if isinstance(value, furl):

            return value.url
        try: return furl(value).url
        except: return value

    def python_value( self,
                      value ) :
        if isinstance(value, furl.url):

            return value

        return furl.url(value) if value is not None else None

class SearchEntry( BaseModel ) :
    user = ForeignKeyField(User, backref = "searchentry")
    _yearRange = DateField()
    _make = CharField()
    _model = CharField()
    _dateTimePosted = DateTimeField()
    _zipcode = IntegerField()           # See uszipcodes
    _radius = IntegerField()
    _url = UrlField()

    def __str__( self ) -> str :

        return f"{self.id}: {self.yearRange} {self.make} {self.model} {self.url.url}"

    @hybrid.hybrid_property
    def yearRange( self ) -> int :

        return self._yearRange

    @yearRange.setter
    def yearRange( self,
                   yearRange ) :
        self._yearRange = yearRange

    @hybrid.hybrid_property
    def make( self ) -> str :

        return self._make

    @make.setter
    def make( self,
              make ) :
        self._make = make

    @hybrid.hybrid_property
    def model( self ) -> str :

        return self._model

    @model.setter
    def model( self,
               model ) :
        self._model = model

    @hybrid.hybrid_property
    def dateTimePosted( self ) -> None :

        return self._dateTimePosted

    @dateTimePosted.setter
    def dateTimePosted( self,
              dateTimePosted ) :
        self._dateTimePosted = dateTimePosted

    @hybrid.hybrid_property
    def zipcode( self ) -> int :

        return self._zipcode

    @zipcode.setter
    def zipcode( self,
                 zipcode ) :
        self._zipcode = zipcode

    @hybrid.hybrid_property
    def radius( self ) -> int :

        return self._radius

    @radius.setter
    def radius( self,
                radius ) :
        self._radius = radius

SearchEntry._meta.database.create_tables(SearchEntry)
