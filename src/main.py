import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
app = App()

app.master.title("Jeux Olympiques")
app.master.minsize(900, 500)

logo_app = tk.PhotoImage(file="images/anneaux_olympiques.png")

logo_label = tk.Label(app, image=logo_app)
logo_label.pack()

app.mainloop()
