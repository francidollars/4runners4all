from furl import furl

from model.user import User
from model.model import db

class UrlList( furl ) :

    def __init__( self,
                  furl

def main( argv = None ) -> None :
    db.connect()
    db.create_tables([User])

    u = User.create(emailAddress="mfdoyle17@gmail.com")

    db.close()

if __name__ == "__main__":
    main()
