import clean
try:
	from tkinter import *
except:
	from Tkinter import *

root=Tk()
root.title("Cleanup")
root.geometry("400x200+420+166")
label = Label(root, text ="Enter the path:")
label.place(relx=0.02, rely=0.10)
e= Entry(root)
e.place(relx=0.28, rely=0.10, relheight=0.10
                , relwidth=0.65)
obj=clean.Clean()

def callback(b):
	s=e.get()
	if s:
		if b:
			obj.all(s)
		else:
			try:
				obj.current(s)
			except Exception as err:
				print(err)

b = Button(root, text = "Clean", command = lambda: callback(False))
b.place(relx=0.05, rely=0.7, height=26, width=67)
c = Button(root, text = "Clean_all", command = lambda: callback(True))
c.place(relx=0.73, rely = 0.7, height=26, width=67)

root.mainloop()
