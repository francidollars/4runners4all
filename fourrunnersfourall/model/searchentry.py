from datetime import datetime
from datetime import date
from enum import Enum

from furl import furl
from peewee import Field, AutoField, CharField, DateField, DateTimeField, ForeignKeyField, IntegerField
from playhouse import hybrid
import tldextract

from .model import BaseModel

class ValidUrl( Enum ) :
    BRINGATRAILER = furl(url="https://www.bringatrailer.com/"),
    CRAIGSLIST = furl(url="https://www.craigslist.org/", path="search/sites/"),
    FACEBOOK = furl(url="https://www.facebook.com/", path="marketplace/"),
    PICKNPULL = furl(url="https://www.picknpull.com/", path="check-inventory/")

class Url( ) :
    def __init__( self,
                  url: str ) :
        _fUrl = furl(url)

    def subDomain( self ) -> str :

        return _extractResult

class SearchEntry( BaseModel ) :
    searchentry_id = AutoField()
    _emailAddress = CharField()
    _yearRange = DateField()
    _make = CharField()
    _model = CharField()
    _dateTimePosted = DateTimeField()
    _zipcode = IntegerField()   # zipcodes
    _radius = IntegerField()
    _url = CharField()

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
              make: str ) :
        self._make = make

    @hybrid.hybrid_property
    def model( self ) -> str :

        return self._model

    @model.setter
    def model( self,
               model: str ) :
        self._model = model

    @hybrid.hybrid_property
    def dateTimePosted( self ) -> None :

        return self._dateTimePosted

    @dateTimePosted.setter
    def dateTimePosted( self,
              dateTimePosted: datetime ) :
        self._dateTimePosted = dateTimePosted

    @hybrid.hybrid_property
    def zipcode( self ) -> int :

        return self._zipcode

    @zipcode.setter
    def zipcode( self,
                 zipcode: int ) :
        self._zipcode = zipcode

    @hybrid.hybrid_property
    def radius( self ) -> int :

        return self._radius

    @radius.setter
    def radius( self,
                radius: int) :
        self._radius = radius

    @hybrid.hybrid_property
    def url( self ) -> str :

        return self._url

    @url.setter
    def url( self,
             url: str ) :

        self._url = url

SearchEntry._meta.database.create_tables([SearchEntry])
