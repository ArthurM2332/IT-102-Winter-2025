import tkinter as tk


root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("300x200")

label = tk.Label(root, text="Click the button below!", font=("Arial", 14))
label.pack(pady=20)

def on_click():
    label.config(text="Button Clicked!", fg="red")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

root.mainloop()
