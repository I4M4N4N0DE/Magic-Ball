import tkinter as tk 
from tkinter import ttk
import urllib.request
from PIL import ImageTk
from io import BytesIO
import random
import time

# toto jsou mé komentáře pro lepší porozumění 
        
def randomizer(): # tato funkce má na svědomí veškerou magii
    
    phrases = ["Ano.", "Ne.", "Možná.", "Pravděpodobně.", "Na to bych nespoléhal."
                   ,"Jistě."]
    
    while True:
        
        entry = str(input("Jaký dotaz se ti honí hlavou? "))
        
        if entry.endswith("?"): # tato podmínka kontroluje, zda je vložený text opravdu otázka, či ne
            output = random.choice(phrases) # pokud je, spustí tuto sekvenci
            out = str(output)
            
            print("Magická koule je připravena ti odpovědět...") 
            time.sleep(3)
            print("Odpověď přijde za ")
            time.sleep(2)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(2)
            print(out)
        else: # pokud není, zresetuje magickou kouli
            print("Myslím, že to nebyla otázka...")
           
    
def Gui(): # grafická kontrola pro uživatele
        
    print("Klikni na kouli pro zahájení.")
        
    # tato část kódu vytvoří samostatné okno
    mball = tk.Tk()
    mball.geometry("740x425")
    mball.title("Magic Ball")
        
    # zde je nejzajímavější část kódu - načtení obrázku z URL
    image = "https://i.ibb.co/VmKrNkC/ball.png" # tento řádek pouze uloží URL do paměti pod proměnnou "image"
    takeimage = urllib.request.urlopen(image) # tento řádek otevře URL a tato data uloží pod proměnnou "takeimage"
    imgdata = takeimage.read() # tento řádek přečte data samostatného obrázku a ta uloží pod proměnnou "imgdata"
    takeimage.close() # tento řádek ukončí čtení URL adresy
        
    ballim = ImageTk.PhotoImage(data=imgdata) # tento řádek načte binární data obrázku a pomocí Tkinteru z nich sestaví obrázek

    # tato část pojmenuje obrázek 
    baller = tk.Label(image=ballim) 
    baller.image = ballim
        
    # tato část vytvoří a umístí dvě funkční tlačítka do okna (jedno do obrázku)
    but = tk.Button(mball, image=ballim, command=randomizer)
    but2 = tk.Button(mball, text="Zavřít", command=mball.destroy).place(x=340, y=385)
    but.pack()
        
    # bez tohoto zápisu by se okno nezobrazilo
    mball.mainloop()
        
Gui()
