from datetime import datetime
from datetime import date
from furl import furl
from peewee import Field, AutoField, CharField, DateField, DateTimeField, IntegerField
from playhouse import hybrid

from .model import BaseModel

class UrlField( Field ) :
    field_type = 'UrlList'

    def db_value( self,
                  value ) -> str :
        if isinstance(value, str):

            return value
        if isinstance(value, furl):

            return value.url
        try:

            return furl(value).url
        except:

            return value


    def python_value( self,
                      value ) :
        if isinstance(value, furl.url):

            return value

        return furl.url(value) if value is not None else None

class SearchEntry( BaseModel ) :
    search_entry_id = AutoField()
    _yearRange = DateField()
    _make = CharField()
    _model = CharField()
    _dateTimePosted = DateTimeField()
    _zipcode = IntegerField()
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
