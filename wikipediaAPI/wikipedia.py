import wikipediaapi


# Get wikipedia data


class WikipediaData:
    wiki = wikipediaapi.Wikipedia('en')

    def __init__(self, word):
        self.word = word


    def get(self):
        page = self.wiki.page(self.word)
        return page


    def url(self):
        page = self.get()
        return page.fullurl


    def summary(self):
        page = self.get()
        return page.summary[0:]
    

    def all(self):
        data = self.get()
        return {
            'summary': data.summary[0:],
            'url': data.fullurl
        }

	
    