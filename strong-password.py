 #!/usr/bin/python3
        import random
        import tkinter as tk
        from tkinter import *
        
        cara  =[chr(i) for i in range(32,127)]
        charlist=[]
        class MyWindow(Tk):
            def __init__(self):
                Tk.__init__(self)
            
            
                for x in range(0,18):
                    t=random.randrange(0,94)
                    charlist.extend(cara[t])       
                self.__name = StringVar()
                self.__lenpass = IntVar()
                xyz=''.join(charlist)
                text = tk.StringVar()
                text.set('')
                
                    
            
                label = Label( self, text="your password")
                label.pack()
                name = Entry(self, textvariable=self.__name )
                name.focus_set()
                name.pack()
            
                label = Label( self, text="password lenght")
                label.pack()
                lenpass = Entry(self, textvariable=self.__lenpass )
                lenpass.focus_set()
                lenpass.pack()
                
                button = Button( self, text="generate", command=self.doSomething)
                button.pack()
        
                self.geometry( "300x150" )
                self.title( "password generator" )
        
                
            def doSomething(self):
                charlist=[]
        
                try : 
                    numberpass=self.__lenpass.get()
                    print(str(numberpass))
                    type(numberpass) is int
                    print("is integer")
                    print(type(numberpass))
                    
        
                    if type(numberpass) is int:
                        
                        for x in range(0,numberpass):
                        
                            t=random.randrange(0,94)
                            charlist.extend(cara[t])       
                        #self.__name = StringVar()
                        xyz=''.join(charlist)
                        text = tk.StringVar()
                        text.set(xyz)
                        self.__name.set(xyz)
                        #print(xyz)    
        
                    else : 
                        print("NAN")
        
                except : 
                    print("NAN")
                    print('The variable is not a number')
                    win = NaNumber()
                    win.mainloop()
                    return False 
                
                
                    
        
        class NaNumber(Tk):
            def __init__(self):
                Tk.__init__(self)
                
                label = Label( self, text="password length must be a number")
                label.pack()      
        
                self.geometry( "300x80" )
                self.title( "NotANumber" )
        
        window = MyWindow()
        window.mainloop()