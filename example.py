from sorryduckduckgo import SorryDuckDuckGo


# You need to be sorry to use the searcher
try:
    duck = SorryDuckDuckGo()
    assert False
except Exception:
    pass

# Sample usage
duck = SorryDuckDuckGo(are_you_sorry=True)
for result in duck.search("DuckDuckGo is awesome"):
    print "{} [{}]".format(result.text, result.link)
