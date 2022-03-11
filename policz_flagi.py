from lista_flag import stworz_liste_flag, orangutan

def policz_domeny_pl(lista):
    #Liczenie ilości domen .pl
    wynik = 0
    import re
    for link in lista:
        match = re.search("^[^.]+\.pl$", link)
        if match:
            wynik += 1

    return wynik

#wynik = policz_domeny_pl(stworz_liste_flag(orangutan))
#print( wynik)


def dlugosc_domen(lista):
    domain_length = []
    for link in lista:
        domain_length.append(len(link))

    longest_domain = max(domain_length)
    shortest_domain = min(domain_length)

    #print(dlugosc)
    return f"Najdłuższa domena: {longest_domain} \nNajkrótsza domena: {shortest_domain}"


print(dlugosc_domen(stworz_liste_flag(orangutan)))



def pl(lista):
    count = 0
    for list in lista:
        if '.pl' in list:
            count += 1
    
    return "Domeny .pl:", count


print(pl(stworz_liste_flag(orangutan)))


def count_domain_com(lista):
    #Liczenie ilości domen .com
    count = 0
    import re
    for link in lista:
        match = re.search("^[^.]+\.com$", link)
        if match:
            count += 1

    return "Domeny .com:", count


print(count_domain_com(stworz_liste_flag(orangutan)))


def count_a(lista):
    letters = []
    count = 0
    for link in lista:
        for l in link:
            if l == 'a':
                count += 1
            #letters.append(l)

    return "Wszystkie litery 'a' w domenach", count


print(count_a(stworz_liste_flag(orangutan)))
