import tkinter as tk
from tkinter import font

def create_text_widgets(root):
    """
    Text widget
    """

    # 1. Basic Text widget
    txt1 = tk.Text(
        root, 
        width=40,      # width in characters
        height=5       # height in lines
    )
    txt1.insert("1.0", "Basic Text widget")
    txt1.pack(pady=10)

    # 2. Text with colors
    txt2 = tk.Text(
        root,
        width=40,
        height=5,
        fg="blue",         # text color
        bg="#f0f0f0",      # background color
        insertbackground="red",  # cursor color
        selectbackground="yellow", # selected text background
        selectforeground="black"  # selected text color
    )
    txt2.insert("1.0", "Colored Text widget")
    txt2.pack(pady=10)

    # 3. Text with font
    txt3 = tk.Text(
        root,
        width=32,
        height=5,
        font=("Arial", 14, "bold italic")  # (family, size, style)
    )
    txt3.insert("1.0", "Custom Font Text widget")
    txt3.pack(pady=10)

    # 4. Text with border and relief
    txt4 = tk.Text(
        root,
        width=40,
        height=5,
        bd=5,               # border thickness
        relief="ridge"      # border style: flat, groove, raised, ridge, solid, sunken
    )
    txt4.insert("1.0", "Text with border")
    txt4.pack(pady=10)

    # 5. Disabled Text (read-only)
    txt5 = tk.Text(
        root,
        width=40,
        height=5,
        state="disabled"  # states: normal (editable), disabled (read-only)
    )
    txt5.pack(pady=10)

    # 6. Text with wrapping options
    txt6 = tk.Text(
        root,
        width=40,
        height=5,
        wrap="word"   # wrap options: none, char, word
    )
    txt6.insert("1.0", "Text with word wrap enabled")
    txt6.pack(pady=10)

    # 7. Text with undo/redo support
    txt7 = tk.Text(
        root,
        width=40,
        height=5,
        undo=True   # enables undo/redo
    )
    txt7.insert("1.0", "Text with undo support")
    txt7.pack(pady=10)

    # 8. Text with highlighting (example)
    txt8 = tk.Text(root, width=40, height=5)
    txt8.insert("1.0", "Highlighted text example")
    txt8.tag_add("highlight", "1.0", "1.9")  # tag range
    txt8.tag_config("highlight", background="yellow", foreground="red")
    txt8.pack(pady=10)
