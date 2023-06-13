slownik = {"a": "x", "b": "y", "c": "z", "d": "a", "e": "b", "f": "c", "g": "d", "h": "e", "i": "f", 
           "j": "g", "k": "h", "l": "i", "m": "j", "n": "k", "o": "l", "p": "m", "q": "n", "r": "o",
           "s": "p", "t": "q", "u": "r", "v": "s", "w": "t", "x": "u", "y": "v", "z": "w"} #slownik przypisujący każdej literze odpowiednią wartość zgodnie z szyfrenm cezara

slownik2 = dict((v,k) for k,v in slownik.items())
while True: #pętla działająca ciągle
    wybor = int(input("Zaszyfrowanie: 1; Odszyfrowywanie: 2: "))
    if wybor == 1:
        slowo = str(input("Podaj slowo do zaszyfrowania: ")) #podanie słowa do zaszyfrowania
        nowe_slowo = ""

        for i in range(0, len(slowo)): #pętla działająca tyle razy ile jest słów w podanym słowie
            litera = slowo[i] #zmienna przechowująca konkretną literę słowa
            nowe_slowo = nowe_slowo+slownik[litera] #dodanie do zmiennej 'nowe_slowo' wartości odpowiedniej litery ze słownika
        print("Zaszyfrowane slowo to: ", nowe_slowo) #wypisanie zaszyfrowanego słowa
    elif wybor == 2:
        slowo = str(input("Podaj slowo do odszyfrowania: ")) #podanie słowa do odszyfrowania
        nowe_slowo = ""

        for i in range(0, len(slowo)): #pętla działająca tyle razy ile jest słów w podanym słowie
            litera = slowo[i] #zmienna przechowująca konkretną literę słowa
            nowe_slowo = nowe_slowo+slownik2[litera] #dodanie do zmiennej 'nowe_slowo' wartości odpowiedniej litery ze słownika
        print("Odszyfrowane slowo to: ", nowe_slowo) #wypisanie odszyfrowanego słowa
    else:
        print("niepoprawny wybor")
