slownik = {"a": "x", "b": "y", "c": "z", "d": "a", "e": "b", "f": "c", "g": "d", "h": "e", "i": "f", #slownik przypisujący każdej literze odpowiednią wartość zgodnie z szyfrenm cezara
           "j": "g", "k": "h", "l": "i", "m": "j", "n": "k", "o": "l", "p": "m", "q": "n", "r": "o",
           "s": "p", "t": "q", "u": "r", "v": "s", "w": "t", "x": "u", "y": "v", "z": "w"}

while True: #pętla działająca ciągle
    slowo = str(input("Podaj slowo do zaszyfrowania: ")) #podanie słowa do zaszyfrowania
    nowe_slowo = ""

    for i in range(0, len(slowo)): #pętla działająca tyle razy ile jest słów w podanym słowie
        litera = slowo[i] #zmienna przechowująca konkretną literę słowa
        nowe_slowo = nowe_slowo+slownik[litera] #dodanie do zmiennej 'nowe_slowo' wartości odpowiedniej litery ze słownika
    print("Zaszyfrowane slowo to: ", nowe_slowo) #wypisanie zaszyfrowanego słowa
