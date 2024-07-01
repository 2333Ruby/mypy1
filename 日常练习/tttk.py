import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Tkinter Example")

label = tk.Label(root, text="Hello World!", font=("Arial", 24))
label.pack()

root.mainloop()
