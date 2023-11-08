import tkinter as tk

def display_text():
    label.config(text="We create what we want")

# Create the main window
root = tk.Tk()
root.title("Text Display Interface")

# Create a label widget to display text
label = tk.Label(root, text="Click the button to display text")
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click Me", command=display_text)
button.pack()

# Start the main event loop
root.mainloop()
