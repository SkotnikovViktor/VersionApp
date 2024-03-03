import wikipedia
wikipedia.set_lang("ru")
search = wikipedia.summary('Манси это')
print(search)