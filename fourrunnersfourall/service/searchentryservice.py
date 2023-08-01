from ..model.searchentry import SearchEntry

class SearchEntryService( ) :

    def addSearchEntry( SearchEntry: SearchEntry ) :

        return SearchEntry.save(SearchEntry)


    def addSearchEntry( str: str ) :
        sub = str.split(' ')
        min_year = sub[]

        return SearchEntry.save()
