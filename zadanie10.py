#Napisz program, który obliczy sumę wszystkich liczb parzystych w zakresie od 1 do 200. Program powinien wykorzystać pętlę for.
print("rozwiazanie pod spodem!! :))")

def suma_parzystych():
    suma = 0  
    for liczba in range(1, 201):  
        if liczba % 2 == 0:  
            suma += liczba  
    return suma


wynik = suma_parzystych()
print(f"Suma liczb parzystych w zakresie od 1 do 200 wynosi: {wynik}")
