import tkinter as tk

def display_text():
    label.config(text="Bir Akif Cifci Hikayesi yaziyorum. Figuran olma. Başrol OL.")


root = tk.Tk()
root.title("Click Me")
root.geometry("400x400+400+100")  


label = tk.Label(root, text="Click Me")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=display_text)
button.pack()

root.mainloop()
