dictionary = {"a": "x", "b": "y", "c": "z", "d": "a", "e": "b", "f": "c", "g": "d", "h": "e", "i": "f", 
           "j": "g", "k": "h", "l": "i", "m": "j", "n": "k", "o": "l", "p": "m", "q": "n", "r": "o",
           "s": "p", "t": "q", "u": "r", "v": "s", "w": "t", "x": "u", "y": "v", "z": "w"} #slownik przypisujący każdej literze odpowiednią wartość zgodnie z szyfrenm cezara

while True: #pętla działająca ciągle
    word = str(input("Podaj slowo do zaszyfrowania: ")) #podanie słowa do zaszyfrowania
    new_word = ""

    for i in range(0, len(word)): #pętla działająca tyle razy ile jest słów w podanym słowie
        letter = word[i] #zmienna przechowująca konkretną literę słowa
        new_word = new_word+dictionary[letter] #dodanie do zmiennej 'nowe_slowo' wartości odpowiedniej litery ze słownika
    print("Zaszyfrowane slowo to: ", nowe_slowo) #wypisanie zaszyfrowanego słowa
