import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def create_buttons(root):
    """
    Button Widget
    """

    # 1. Basic button
    btn1 = tk.Button(
        root,
        text="Click Me",    
    )
    btn1.pack(pady=10)

    # 2. Button with colors
    btn2 = tk.Button(
        root,
        text="Colored Button",
        fg="white",         
        bg="#2c3e50",        
        activeforeground="yellow",  # text color when pressed/hovered
        activebackground="green"    # background color when pressed/hovered
    )
    btn2.pack(pady=10)

    # 3. Custom font
    btn3 = tk.Button(
        root,
        text="Custom Font",
        font=("Arial", 12, "bold italic")  # (family, size, style)
        # family = "Arial"
        # size   = 12px
        # style  = bold + italic
    )
    btn3.pack(pady=10)

    # 4. Button with border styles
    btn4 = tk.Button(
        root,
        text="Border Styles",
        relief="ridge",  # border style: flat, groove, raised, ridge, solid, sunken
        bd=5             # border thickness (pixels)
    )
    btn4.pack(pady=10)

    # 5. Disabled button (unclickable, grayed out)
    btn5 = tk.Button(
        root,
        text="Disabled",
        state="disabled"  # states: normal (default), disabled
    )
    btn5.pack(pady=10)

    # 6. Button with fixed size
    btn6 = tk.Button(
        root,
        text="Fixed Size",
        width=20,     # width in text characters
        height=2      # height in text lines
    )
    btn6.pack(pady=10)

    # 7. Button with image
    img = Image.open("assets/images/py.png")
    img = img.resize((20, 20))  
    photo = ImageTk.PhotoImage(img)

    btn = tk.Button(
        root,
        text="With Image",
        image=photo,
        compound="left"
    )
    btn.image = photo 
    btn.pack(pady=10)


    # 8. Button with cursor change on hover
    btn8 = tk.Button(
        root,
        text="Hover Me",
        cursor="hand2"  # mouse cursor style (arrow, hand2, cross, xterm, etc.)
    )
    btn8.pack(pady=10)

    # 9. Button with underline 
    btn9 = tk.Button(
        root,
        text="Underlined",
        underline=0   # index of character to underline (0 = first char)
    )
    btn9.pack(pady=10)

    #10, Underline all text button
    underline_font = font.Font(underline=True)
    btn10 = tk.Button(
        root,
        text="All Underlined",
        font=underline_font
    )
    btn10.pack(pady=10)