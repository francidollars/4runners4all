from furl import furl
from enum import Enum

from model.model import db
from model.user import User
# from model.searchentry import SearchEntry

class ValidUrl( Enum ) :
    CRAIGSLIST = furl(url="https://www.craigslist.org/", path="search/sites/"),
    FACEBOOK = furl(url="https://www.facebook.com/", path="marketplace/"),
    PICKNPULL = furl(url="https://www.picknpull.com/", path="check-inventory/")

    def __repr__( self ) ->furl :

        return self

    def __str__( self ) ->str :

        return str(self.value)

def main( argv = None ) -> None :
    urls = []
    urls.append(ValidUrl.CRAIGSLIST)

    print(urls)

    return 0

if __name__ == "__main__":
    main()
