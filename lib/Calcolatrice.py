from tkinter import *

window = Tk()
window.title("Numeri Naturali")
icon = PhotoImage(file='icon1.png')
window.tk.call('wm', 'iconphoto', window._w, icon)
window.geometry("325x210")

def calcola():
	x = float(e1.get())
	y = float(e3.get())
	z = e2.get()
	if z=="+":
		a = x+y
		t1.configure(text=a)
	elif z=="-":
		a = x-y
		t1.configure(text=a)
	elif z=="x":
		a = x*y
		t1.configure(text=a)
	elif z==":":
		a = x/y
		t1.configure(text=a)
	else:
		return x

def pulisci():
	e1.delete(0, END)
	e2.delete(0, END)
	e3.delete(0, END)
	t4.configure(text="")

e1 = Entry(width=10)
e1.grid(column=0, row=1)

e2 = Entry(width=10)
e2.grid(column=1, row=1)

e3 = Entry(width=10)
e3.grid(column=2, row=1)

b1 = Button(text="Calcola", command=calcola, width=10)
b1.grid(column=0, row=3)

b2 = Button(text="Pulisci", command=pulisci, width=10)
b2.grid(column=1, row=3)

b3 = Button(text="Esci", command=quit, width=10)
b3.grid(column=2, row=3)

t1 = Label(height=2, width=10, bg="orange")
t1.grid(column=1, row=4, pady=5)

t2 = Label(width=10, text="Risultato:")
t2.grid(column=0, row=4, pady=5)

window.mainloop()