
#renommer des fichiers avec tkinter et python



        try:                        # In order to be able to import tkinter for
        import tkinter as tk    # either in python 2 or in python 3
    except ImportError:
        import Tkinter as tk
    
    from tkinter import filedialog
    from tkinter import filedialog as fd    # importing the filedialog module from tkinter  
    
    
    class EntryWithSet(tk.Entry):
        """
        A subclass to Entry that has a set method for setting its text to
        a given string, much like a Variable class.
        """
    
        def __init__(self, master, *args, **kwargs):
            tk.Entry.__init__(self, master, *args, **kwargs)
    
    
        def set(self, text_string):
            """
            Sets the object's text to text_string.
            """
    
            self.delete('0', 'end')
            self.insert('0', text_string)
    
    
    def on_button_click():
        import random, string
        rand_str = ''.join(random.choice(string.ascii_letters) for _ in range(19))
        entry.set(rand_str)
        
    def on_rootfolder():
        root_folder = fd.askdirectory(title = "Select root Folder") 
        rootfolder.set(root_folder)
        
    def on_destfolder():
        dest_folder = fd.askdirectory(title = "Select target Folder") 
        destfolder.set(dest_folder)
    
    if __name__ == '__main__':
        root = tk.Tk()
        tk.Label(root,text="enter the prefix:").pack()
        
        prefix = tk.Entry(root,textvariable="" )
        prefix.focus_set()
        prefix.pack()
        
        tk.Label(root,text="enter the generic name:").pack()
        
        genName = tk.Entry(root,textvariable="" )
        genName.focus_set()
        genName.pack()
        
        tk.Label(root,text="enter the root folder:").pack()
        
        rootfolder = EntryWithSet(root)
        rootfolder.pack()
        
        tk.Button(root, text="choose root folder", command=on_rootfolder).pack()
        
        tk.Label(root,text="enter the destination folder:").pack()
        
        destfolder = EntryWithSet(root)
        destfolder.pack()
        
        
        tk.Button(root, text="choose target folder", command=on_destfolder).pack()
        
        entry = EntryWithSet(root)
        entry.pack()
        tk.Button(root, text="Set", command=on_button_click).pack()
        tk.mainloop()

