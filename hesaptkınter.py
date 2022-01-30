import tkinter as tk
def topla():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1+s2))
def cikar():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1-s2))
def carp():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1*s2))
def bolme():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1=float(sayi1.get())
        s2=float(sayi2.get())
        sonuc.configure(text=str(s1/s2))
pencere = tk.Tk()
pencere.title("hesap makinesi")
ekrangenis=pencere.winfo_screenwidth()//2
ekranyuksek=pencere.winfo_screenheight()//2
pencere.geometry("320x300+{}+{}".format(ekrangenis,ekranyuksek))

sonuc=tk.Label(pencere,text="Sonuc",font="Courier 16 bold",width="30",justify="center")
sonuc.place(x=-50, y=20)
sayi1=tk.Entry(pencere, font="Courier 14 bold", width=15, justify="left")
sayi1.place(x=70, y=50)
sayi2=tk.Entry(pencere, font="Courier 14 bold", width=15, justify="left")
sayi2.place(x=70, y=80)
#tusları olusturacagız bunun için button nesnesini kullanacagız.
tus1=tk.Button(pencere,text="+",font="Courier 14 bold",width=5,command=topla )
tus1.place(x=170,y=110)
tus1=tk.Button(pencere,text="-",font="Courier 14 bold",width=5,command=cikar )
tus1.place(x=170,y=140)
tus1=tk.Button(pencere,text="*",font="Courier 14 bold",width=5,command=carp )
tus1.place(x=170,y=170)
tus1=tk.Button(pencere,text="/",font="Courier 14 bold",width=5,command=bolme )
tus1.place(x=170,y=200)

sayi1.focus()

pencere.mainloop()


