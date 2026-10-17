import tkinter as tk

def create_labels(root):
    """
    Label Widget
    """

    # 1. label
    label1 = tk.Label(
        root,
        text="hello"
    )
    label1.pack(pady=10)

    # 2. Text with colors
    label2 = tk.Label(
        root,
        text="White text on dark bg",
        fg="white",        # foreground
        bg="#2c3e50"       # background
    )
    label2.pack(pady=10)

    # 3. with font
    label3 = tk.Label(
        root,
        text="Custom Font",
        font=("Arial", 20, "bold") 
        # family = "Arial"
        # size   = 20px
        # style  = "bold" (options: normal, bold, italic, underline, overstrike)
    )
    label3.pack(pady=10)

    # 4. Fixed size label
    label4 = tk.Label(
        root,
        text="Fixed size box",
        width=20,          # number of characters wide (not pixels!)
        height=2,          # number of text lines tall (not pixels!)
        bg="lightgray"  
    )
    label4.pack(pady=10)

    # 5. Multi-line text with justification
    label5 = tk.Label(
        root,
        text="Multi-line\nText Example",  # \n = line break
        justify="left"   # how multiple lines are aligned: LEFT, RIGHT, or CENTER
    )
    label5.pack(pady=10)

    # 6. Anchored text inside fixed-size label
    label6 = tk.Label(
        root,
        text="Anchored text",
        width=20,             # width in characters
        height=3,             # height in lines
        anchor="se",          # where text is placed inside the box (n, s, e, w, ne, se, sw, nw, center)
        bg="lightblue"        # background color
    )
    label6.pack(pady=10)

    # 7. Border styles (relief)
    label7 = tk.Label(
        root,
        text="Relief Styles",
        relief="groove",  # border effect: flat, groove, raised, ridge, solid, sunken
        bd=5              # border thickness (in pixels)
    )
    label7.pack(pady=10)

    # 8. Wrapped text
    label8 = tk.Label(
        root,
        text="This is a very long sentence that will wrap after 150 pixels",
        wraplength=150,   # max width in pixels before wrapping text to new line
        bg="yellow"       # background color
    )
    label8.pack(pady=10)

    # 9. Cursor change on hover
    label9 = tk.Label(
        root,
        text="Hover me",
        cursor="hand2",   # mouse cursor when hovering (e.g., arrow, hand2, cross, xterm, etc.)
        bg="lightgreen"   # background color
    )
    label9.pack(pady=10)
