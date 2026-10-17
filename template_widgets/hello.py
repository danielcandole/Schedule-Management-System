import tkinter as tk

def hello(root):
  
    center_frame = tk.Frame(root)
    center_frame.pack(expand=True)  

    label1 = tk.Label(
        center_frame,
        fg="#fff",
        bg="#2c3e50",
        text="Hello World",
        font=("Times New Roman", 12)
    )
    label1.pack()

