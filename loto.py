import random
import tkinter as tk

tirage=[]

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.bouton = tk.Button(self, width=30, text="nouveau tirage", command=self.creer_widgets)
        self.bouton2 = tk.Button(self, width=30,text="Quitter", command=self.quit)
        self.creer_widgets()
               
    def creer_widgets(self):
        self.label = tk.Label(self, text=tirage)
        
        
        self.bouton.pack()
        self.bouton2.pack()
        
        self.label.pack()
        
        
        del tirage[0 : 6]
        self.tirageLoto()
    
    def tirageLoto(self):
        
        self.separator = tk.Label(self, text="*******************")
        self.separator.pack()
    
        for i in range(6):

            x=random.randint(1,49)

            if x not in tirage:
                
                tirage.append(x)
                
            else:
                print("exist ="+ str(x))
                x=random.randint(1,49)
                tirage.append(x)
                        
        print (tirage)
        print ("***********************")


if __name__ == "__main__":
    app = Application()
    app.title("tirage du loto :-)")
    canv = tk.Canvas(app, height=50, width=300)
    canv.pack()
    app.mainloop()