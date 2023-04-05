from datetime import datetime
from datetime import date

from furl import furl

class SearchEntry:
    def __init__( self,
                  searchId = -1,
                  yearRange = date(1, 1, 1),
                  make = "",
                  model = "",
                  dateTimePosted = datetime(1, 1, 1, 0, 0, 0, 0),
                  zipcode = -1,
                  radius = -1,
                  url = furl() ) :
        self.searchId = searchId
        self.yearRange = yearRange
        self.make = make
        self.model = model
        self.datePosted = dateTimePosted
        self.zipcode = zipcode
        self.radius = radius
        self.url = furl(url)

    def __str__( self ) -> str:

        return f"{self.searchId}: {self.yearRange} {self.make} {self.model} {self.url.url}"
