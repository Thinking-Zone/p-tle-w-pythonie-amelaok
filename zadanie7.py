import random

def zapytaj_o_pogode():
   
    czy_pada = random.choice([True, False])
    
    
    while True:
        odpowiedz = input("Czy pada deszcz? (tak/nie): ").strip().lower()
        
        
        if odpowiedz not in ["tak", "nie"]:
            print("Proszę odpowiedzieć 'tak' lub 'nie'.")
            continue
        
       
        if (odpowiedz == "tak" and czy_pada) or (odpowiedz == "nie" and not czy_pada):
            print("BRAWO BRAWO!!")
            break
        else:
            print("Spróbuj ponownie.")


zapytaj_o_pogode()
