import tkinter as tk

def create_inputs(root):
    """
    Entry (Input) Widget
    """

    # 1. Basic input field
    entry1 = tk.Entry(
        root,
        width=20   # number of characters that can be shown (not pixel width)
    )
    entry1.pack()
    entry1.insert(0, "Default text")  # insert initial text at position 0

    # 2. Input with background and text colors
    entry2 = tk.Entry(
        root,
        fg="white",        
        bg="#2c3e50",      
        insertbackground="yellow"  # color of the blinking cursor (insertion point)
    )
    entry2.pack(pady=10)
    entry2.insert(0, "White text, dark bg")

    # 3. Custom font
    entry3 = tk.Entry(
        root,
        font=("Arial", 11, "italic")  # (family, size, style)
        # family = "Arial"
        # style  = "italic" (options: normal, bold, italic, underline, overstrike)
    )
    entry3.pack(pady=10)
    entry3.insert(0, "Custom Font")

    # 4. Input with border styles
    entry4 = tk.Entry(
        root,
        relief="ridge",  # border style: flat, groove, raised, ridge, solid, sunken
        bd=3              # border thickness (pixels)
    )
    entry4.pack(pady=10)
    entry4.insert(0, "Border style: ridge")

    # 5. Disabled input
    entry5 = tk.Entry(
        root,
        state="disabled"   # states: normal (default), disabled, readonly
    )
    entry5.pack(pady=10)
    entry5.insert(0, "Disabled field")

    # 6. Read-only input
    entry6 = tk.Entry(root)
    entry6.pack(pady=10)
    entry6.insert(0, "Read-only field")
    entry6.config(state="readonly")

    # 7. Password field (mask input with *)
    entry7 = tk.Entry(
        root,
        show="*"   # replaces characters with a symbol (common for passwords)
    )
    entry7.pack(pady=10)
    entry7.insert(0, "mypassword")

    # 8. Justified text inside the entry
    entry8 = tk.Entry(
        root,
        justify="center"  # LEFT, RIGHT, CENTER
    )
    entry8.pack(pady=10)
    entry8.insert(0, "Centered text")

