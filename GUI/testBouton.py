import tkinter as tk 
 
compteur = 0
 
def unkilometre():
    global compteur
    compteur += 1
    label['text'] = "{} km(s) à pieds...".format(compteur)
 
root = tk.Tk()
root.title("Example")         
root.geometry("140x90") 
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)
label = tk.Label(frame, text="Salut", fg="blue", bg="yellow")
label.place(x=10, y=10, width=120, height=30)
bouton = tk.Button(frame, text="Hit me!", command=unkilometre)
bouton.place(x=10, y=50, width=120, height=30)
 
root.mainloop()


