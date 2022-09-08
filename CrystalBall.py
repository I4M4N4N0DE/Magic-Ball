import tkinter as tk 
from tkinter import ttk
import urllib.request
from PIL import ImageTk
from io import BytesIO
import random
import time

# these are my comments for your better understanding

class Magic:
    
    phrases = ["Yes.", "No.", "Maybe.", "Probably.", "I won't rely on that."
                   ,"Sure."]
        
    def randomizer(): # this function does all the Magic
        
        entry = str(input("What question is on your mind? "))
        
        if entry.endswith("?"): # this statement checks if the inputted text is really a question, or not
            output = random.choice(Magic.phrases) # if it is, then it starts to do this job
            out = str(output)
            
            print("The magic ball is ready to answer your question...") 
            time.sleep(3)
            print("The answer comes in ")
            time.sleep(2)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(2)
            print(out)
        else: # if it isn't, then it's gonna reset the magic ball
            print("I guess that wasn't a question...")
            Magic.randomizer()
            
class Ball: # the GUI control for the user
    
    def Gui():
        
        print("Click the ball to start.")
        
        #this part of the code creates the window
        mball = tk.Tk()
        mball.geometry("740x425")
        mball.title("Magic Ball")
        
        #there is the most interesting part of this code - the URL image load
        image = "https://i.ibb.co/VmKrNkC/ball.png" # this line just stores the URL into the "image" variable
        takeimage = urllib.request.urlopen(image) # this line opens the URL and stores that job into the "takeimage" variable
        imgdata = takeimage.read() # this line reads the URL's data and stores it as an "imgdata" variable
        takeimage.close() # this line closes the URL
        
        ballim = ImageTk.PhotoImage(data=imgdata) # this line takes the binary data and makes an image from it 

        # this part sets a label for the taken image
        baller = tk.Label(image=ballim) 
        baller.image = ballim
        
        # this part creates and allocates the two functional buttons into the window (one is in the ball photo)
        but = tk.Button(mball, image=ballim, command=Magic.randomizer)
        but2 = tk.Button(mball, text="Exit", command=mball.destroy).place(x=340, y=385)
        but.pack()
       
        # without this code the window wouldn't display
        mball.mainloop()
        
     
Ball.Gui()