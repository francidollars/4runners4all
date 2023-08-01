from datetime import datetime

from redbox import EmailBox, outlook

from model.model import db
from model.user import User
from model.searchentry import furl, SearchEntry, ValidUrl

def main( argv = None ) -> None :
    outlook.username = "fourrunnersfourall@outlook.com"
    outlook.password = "4run4all"

    box = outlook["Inbox"]
    body = box.search(subject="SUBSCRIBE")[0].text_body

    entry = []
    for str in body.split('\n') :
        for sub in str.split(' ') :
            entry.append(sub)

    u = User(outlook.username)

    u_url = ValidUrl.CRAIGSLIST
    print(u_url)

    # SearchEntry(u.user_id,
    #             yearRange=entry[0],
    #             make=entry[1],
    #             model=entry[2],
    #             dateTimePosted=datetime.now(),
    #             zipcode=entry[3],
    #             radius=entry[4],
    #             url=ValidUrl.CRAIGSLIST.url).save()

    # print(list(SearchEntry.select()))

if __name__ == "__main__":
    main()
