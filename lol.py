import wikipedia as wiki
import random
wiki.set_lang("pl")

def character( name):
    page = wiki.search( name)
    character_page = wiki.page(page[0])
    content = character_page.content


    return content

name = "Bruce Lee"
print(character( name))