from tkinter import *
import base

class Interface():
    def __init__(self):
        self.root = Tk()
        self.root.title('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< BASE-CONVERTER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        self.root.geometry('941x529+180+80')
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.iconbitmap("icon.png")

    def corps(self):
        self.image = PhotoImage(file='main.interphace.PNG')
        self.background = Label(self.root, image=self.image).place(relx=0, rely=0)

        self.nbr_init = StringVar()
        self.nbr_init_input = Entry(self.root, textvariable=self.nbr_init, bg='white',font=18, borderwidth='0c',fg='blue').place(relx=0.053, rely=0.450, width=193.5, height=50.5)

        self.nbr_final = StringVar()
        self.nbr_final_input = Label(self.root, text='', bg='white', font=18, borderwidth='0c',fg="blue")
        self.nbr_final_input.place(relx=0.351, rely=0.443, width=194.2, height=54)

        self.search_psd = PhotoImage(file='convert.png')
        self.search_btn = Button(self.root, image=self.search_psd, bg='black', overrelief="flat", borderwidth='0c',activebackground='black', highlightthickness=0, command=self.conversion).place(relx=0.27, rely=0.460)

        self.base_init = IntVar()
        self.base_final = IntVar()

        self.base_list = (2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16)
        self.base_init_list = OptionMenu(self.root, self.base_init, *self.base_list,).place(relx = 0.13, rely = 0.386)
        self.base_final_list = OptionMenu(self.root, self.base_final, *self.base_list ).place(relx = 0.425, rely = 0.380)

    def finale(self):
        self.root.mainloop()
    
    def conversion(self):
        self.nbr_final = base.turn_in_base(self.nbr_init.get(), self.base_init.get(), self.base_final.get())
        self.nbr_final_input.config(text = self.nbr_final)
        self.nbr_final_input.update()

if __name__ == "__main__":
    fen = Interface()
    fen.corps()
    fen.finale()
