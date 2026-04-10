# Algorytmy - projekt 2

## Implementacja 
- [x] Algorytm First Come First Served konstruowania drzewa Binary Search Tree (BST)
    - [x] Wyszukiwanie w drzewie elemntu o najmniejszej i najwięszkej wartości i wypisanie ścieżki 
    - [x] podanie poziomu drzewa gdzie znajduje się węzeł o kluczu wskazanym prez użytkownika oraz wypisanie wszystkich elementów znajdujących się na tym samym poziomie 
    - [x] Wypisanie wszystkich elementów drzewa w porządku malejącym z wykorzystaniem metody trawersowania drzewa binarnego
    - [x] Wypisanie w porządku pre-order poddrzewa, którego korzeń podaje użytkownik, podanie wysokości i usunięcie poddrzewa metodą post-order

- [ ] Algorytm konstruowania drzewa AVL wykorzystujący bisekcję i jeden z algorytmów sortowania o złożoności logarytmicznej
    - [ ] Wyszukiwanie w drzewie elemntu o najmniejszej i najwięszkej wartości i wypisanie ścieżki 
    - [ ] podanie poziomu drzewa gdzie znajduje się węzeł o kluczu wskazanym prez użytkownika oraz wypisanie wszystkich elementów znajdujących się na tym samym poziomie 
    - [ ] Wypisanie wszystkich elementów drzewa w porządku malejącym z wykorzystaniem metody trawersowania drzewa binarnego
    - [ ] Wypisanie w porządku pre-order poddrzewa, którego korzeń podaje użytkownik, podanie wysokości i usunięcie poddrzewa metodą post-order

- [ ] Algorytm konstruowania kopca minimalnego HMIN 
    - [ ] Wyszukiwanie w drzewie elemntu o najmniejszej i najwięszkej wartości i wypisanie ścieżki 
    - [ ] podanie poziomu drzewa gdzie znajduje się węzeł o kluczu wskazanym prez użytkownika oraz wypisanie wszystkich elementów znajdujących się na tym samym poziomie 
    - [ ] Wypisanie wszystkich elementów drzewa w porządku malejącym
    - [ ] Wypisanie w porządku pre-order poddrzewa, którego korzeń podaje użytkownik, podanie wysokości i usunięcie poddrzewa metodą post-order

 

## Menu 
- [ ] Menu, które pozwoli użytkownikowi na wybór stosownej funkcjonalności i po wykonaniu procedury powróci do menu, gdzie można wybrać inną funkcjonalność lub zamknąć program

## Równoważenie drzewa BST za pomocą jednej z poniższych metod 
- [ ] przez rotację za pomocą algorytmu DSW (Day-Stout-Warren)
- [ ] przez usuwanie korzenia 

## Dane wejściowe 
- n-elementowy różnowartościowy ciąg liczb naturalnych wczytywany z pliku tekstowego (liczby w pliku oddzielone spacją) generowany przez generator danych

## Dane wejściowe
- Czas działania programu dla funkcjonalności
    - wyszukiwania min/max 
    wypisania elemntów 
    równoważenia drzewa 


## Testy 
- Wygenerowanie 5 n-elementowych ciągów liczb naturalnych 
- Wygenerowanie 5 n-elementowych ciągów liczb naturalnych posortowanych rosnąco
- n z przedziału <10, k>, k dobierane eksperymentalnie, możliwie duże
- Zmierzyć czas wykonania pracy:
    - Tworzenie drzewa
    - Wyszkuiwanie elementu o maksymlanej wartości
    - Równoważenia drzewa BST
- Czas tworzenia AVL powinien obejmować sortowanie ciągu przez bisekcję

## Raport
- Przedstawić dane wejściowe oraz wyniki testów dla każdej z operacji
    - pierwsze i ostatnie sześć cyfr testowanego ciągu wejściowego oraz jego wartość n, uwaga: w celu zachowania zwięzłości dokumentu, proszę nie wpisywać całych ciągów wejściowych i wynikowych,
    - czas wykonania operacji,
    - informacje z podpunktów zdefiniowanych w sekcji Implementacja:
    - najmniejsza i największa wartość wraz ze ścieżką przeszukiwania dla operacji wyszukiwania,
    - poziom drzewa, na którym znajduje się węzeł o założonym kluczu wraz z wszystkimi elementami znajdującymi się na tym samym poziomie,
    - pierwsze i ostatnie sześć elementów poddrzewa, w porządku pre-order, dla założonego korzenia (klucza), wraz z wysokością tego poddrzewa, pierwsze i ostatnie sześć elementów drzewa w porządku malejącym.
- dwa wykresy: jeden dla struktury, drugi dla wyszukiwania maksimum t=f(n) zależności czasu obliczeń t od liczby n elementów w drzewie zbudowanym z ciągu losowego. Na każdym wykresie proszę przedstawić trzy krzywe – po jednej krzywej dla każdej struktury drzewiastej.
- dwa wykresy (jeden wykres dla tworzenia struktury, drugi dla wyszukania maksimum) t=f(n) zależności czasu obliczeń t od liczby n elementów w drzewie zbudowanym z ciągu posortowanego rosnąco. Na każdym wykresie proszę przedstawić trzy krzywe – po jednej krzywej dla każdej struktury drzewiastej.
- wykres t=f(n) zależności czasu równoważenia t od liczby n elementów w drzewie BST. Na wykresie proszę przedstawić dwie krzywe – jedną dla drzewa zbudowanego z ciąg losowego, a drugą dla drzewa zbudowanego z ciągu rosnącego.
- Wskazać zalety i wady kązdej z trzech analizowanych struktur drzewiastych
