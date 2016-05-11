import requests
from lxml import html


class SorryDuckDuckGoResult:
    def __init__(self, text, link):
        self.text = text
        self.link = link


class SorryDuckDuckGo:
    def __init__(self, are_you_sorry=False):
        if not are_you_sorry:
            raise Exception("You need to be explicitly sorry")

    def search(self, keywords, max_results=None):
        url = 'https://duckduckgo.com/html/'
        params = {
            'q': keywords,
            's': '0',
        }

        res = requests.post(url, data=params)
        doc = html.fromstring(res.text)

        yielded = 0
        results = [SorryDuckDuckGoResult(''.join(a.itertext()), a.get('href')) for a in
                   doc.cssselect('#links .web-result .links_main a.result__a')]
        for result in results:
            yield result
            yielded += 1
            if max_results and yielded >= max_results:
                return

