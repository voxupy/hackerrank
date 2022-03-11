import requests
import sys

# Pobranie tekstu ze strony (jako tafla tesktu).
orangutan = 'https://zajecia-programowania-xd.pl/flagi'


def polacz_sie_ze_strona( orangutan):
    surowe_info = requests.get( orangutan)
    text = surowe_info.text
    return text


def stworz_liste_flag ( orangutan):
    text_strony_www = polacz_sie_ze_strona( orangutan)
    lista_linii = text_strony_www.split('</p>')
    linki = []

    for linia in lista_linii:
        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link or link == '':
            continue
        linki.append( link)
        #print(linia)
    return linki


#print(stworz_liste_flag(orangutan))


#if __name__ == '__main__':
 #   argument = sys.argv[1]
  #  lista_flag = stworz_liste_flag(argument)
   # print(lista_flag)
