import requests

url = 'https://zajecia-programowania-xd.pl/flagi'

surowe_info = requests.get(url)
text = surowe_info.text
lista_linii = text.split('</p>')

linki = []


for i in lista_linii:
    link = i.replace('<p>','')
    link = link.replace('-','')
    link = link.strip()
    if ' ' in link or '<' in link:
        continue
    linki.append( link)

#Wyświetlanie elementów listy
max_length = []
for i in linki:
    max_length.append(len(i))

print("max",max(max_length))
print("min",min(max_length))
#Długość Listy
print(len(linki))
#for i, l in enumerate(linki)
 #   print(i,l )


LICZNIK = 0
LICZNIK_POZOSTALE = 0
LICZNIK_RESZTA = 0

for i,l in enumerate(linki):
    if ('.pl' in l) and ('.com' in l):
         LICZNIK_RESZTA += 1
    elif '.pl' in l:
        LICZNIK += 1
    else:
        LICZNIK_POZOSTALE += 1

print('licznik com.pl', LICZNIK_RESZTA)
print('licznik pl', LICZNIK)
print('pozostale', LICZNIK_POZOSTALE)

def policz_domeny(lista):
    liczba_domen = 0
    
    for i, l in enumerate(lista):
        if '.pl' in l:
            liczba_domen += 1

    return liczba_domen


print('Domeny co maja w nazwie .pl = ', policz_domeny(linki) )


com_pl = 0
wszystkie_domeny = len(linki)


for number, x in enumerate(linki):
    if ('.pl' in x) and ('.com' in x):
        com_pl += 1
    elif not ('.pl' in x):
        com_pl += 1



print(com_pl)
print(wszystkie_domeny - com_pl)


#Wyrażenia reguralne
# ^ - początek stringu co ma zawierac czyli litery a-z, A-Z, 0-9, oraz "-"
# + łączenie znaków
# \. oznacza jako kropke i koncowka pl

def policz_domeny(links):
    import re
    d_pl = 0

    for link in links:
        match = re.search("^[a-zA-Z0-9]+\.pl$",link)
        if match:
            d_pl += 1
            
    return d_pl

print(policz_domeny(linki))


import re


def liczenie(linki):
    pl_domains = 0
    for link in linki:
        match = re.search("^[a-zA-Z0-9]+\.pl$", link)
        if match:
            pl_domains += 1
    return pl_domains


print(liczenie(linki))