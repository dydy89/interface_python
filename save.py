from tkinter import *

fenetre = Tk()
fenetre.geometry('400x400')
fenetre.title('nouveau projet')
fenetre['bg'] = 'blue'

fenetre.resizable(height=True,width=True)

label = Label(fenetre, text="Trapil simulation")
label.pack( padx=50)

fenetre.mainloop()

